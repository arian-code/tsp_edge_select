#########################################################################################
# This code graphically verifies the algorithm to build TSP tour based on edge selection
# As the edges are selected by user progressively
#   The algorithm, block edges which are invalid for selection
#   The algorithms always results in VALID TOUR SELECTION
####################################################################
#   Brief on algorithm:
#   	All edges are available initially for selection
#   	If no of cities = n; then n edges are to be selected
#   	On each selection of edge:
#       	All edges in the row of edge are blocked
#       	All edges in the column of edge are blocked
#       	Edges which can create SUB TOUR are blocked - routine "sub_tour_check"
#
# NOTE: WHEN NO OF PENDING SELECTIONS + NO OF AVAILABLE OPTIONS
#        	ALGORITHM AUTO SELECTS ALL REMAINING EDGES
#########################################################################################
# import pygame library
import pygame
pygame.init()
import numpy as np
import random
#from opentsp.objects import Generator as TSPGenerator


#########################################################################################
def master():
    '''This is the main loop'''
#########################################################################################
    def draw_reset ():
        '''This resets graphical window, when user demands'''
#########################################################################################
        thick = 5
        pygame.draw.line(screen, (255, 0, 0), (0, 560), (800, 560), thick)
        pygame.draw.line(screen, (255, 0, 0), (0, 600), (800, 600), thick)     
        pygame.draw.line(screen, (255, 0, 0), (0, 560), (0, 600), thick)
        pygame.draw.line(screen, (255, 0, 0), (800, 560), (800, 600), thick)
        text2 = font3.render("RESET THE GAME", 1, (255, 0, 0))
        screen.blit(text2, (300, 570))
#########################################################################################
    def draw_tsp_points (cities):
        '''Draw right side window showing the tour''' 
#########################################################################################
        thick = 5
        pygame.draw.line(screen, (0, 255, 0), (500, 0), (800, 0), thick)
        pygame.draw.line(screen, (0, 255, 0), (500, 550), (800, 550), thick)     
        pygame.draw.line(screen, (0, 255, 0), (500, 0), (500, 550), thick)
        pygame.draw.line(screen, (0, 255, 0), (800, 0), (800, 550), thick)

#########################################################################################
    def draw_no_city(max_city):
        '''Draw initial window, to slect no of cities'''
#########################################################################################
        # Draw the lines
        for i in range (max_city):
            for j in range (max_city):
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (255, 255, 255), (i * dif, j * dif, dif + 1, dif + 1))
                # Fill grid with default numbers specified
                text1 = font1.render(str(4+i+max_city*j), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
        for i in range(max_city+1):
            thick = 5
            pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
            pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)     

#########################################################################################
    def draw():
        '''Draw the edge selection matrix or grid'''
#########################################################################################
        # Draw the lines
        for i in range (cities):
            for j in range (cities):
                if grid[i][j]== 0:                                                  # 0 not available; black
                     # Fill blue color in already numbered grid
                    pygame.draw.rect(screen, (60, 60, 60), (i * dif, j * dif, dif + 1, dif + 1))
                     # Fill grid with default numbers specified
                    #text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                    text1 = font1.render("N", 1, (255, 255, 255))
                    screen.blit(text1, (i * dif + 15, j * dif + 15))
                elif grid[i][j]== 1:                                                  #SELECTED; GREY
                     # Fill blue color in already numbered grid
                    pygame.draw.rect(screen, (255, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))
     
                    # Fill grid with default numbers specified
                    text1 = font1.render(str(i+1)+"-"+str(j+1), 1, (0, 0, 0))
                    screen.blit(text1, (i * dif + 15, j * dif + 15))
                else:                                                               # -1 avaialble, not selected; WHITE
                     # Fill blue color in already numbered grid
                    pygame.draw.rect(screen, (255, 255, 255), (i * dif, j * dif, dif + 1, dif + 1))
                    # Fill grid with default numbers specified
                    text1 = font1.render(str(i+1)+"-"+str(j+1), 1, (0, 0, 0))
                    screen.blit(text1, (i * dif + 15, j * dif + 15))
    #                text3 = font1.render(str(i+1)+"-"+str(j+1), 1, (0, 0, 0))
    #                screen.blit(text3, (i * dif + 25, j * dif + 25))
        for i in range(cities+1):
            thick = 5
            pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
            pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)     
#########################################################################################
    def draw_box():     #red box around selected grid
#########################################################################################
        for i in range(2):
            pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
            pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)  
#########################################################################################
    def draw_val(val):
#########################################################################################
        text1 = font1.render(str(val), 1, (0, 0, 0))
        screen.blit(text1, (x * dif + 15, y * dif + 15))   
#########################################################################################
    def get_cord(pos):
        '''Get mouse click position'''
#########################################################################################
        x = pos[0]//dif
        y = pos[1]//dif
        return (x, y)
#########################################################################################
    def instruction_cities():
        '''Write short instruction below the grid'''
#########################################################################################
        text1 = font2.render("Please select no of cities from grid above", 1, (0, 0, 0))
        text2 = font2.render("Waiting for selection", 1, (0, 0, 0))
        screen.blit(text1, (20, 520))       
        screen.blit(text2, (20, 540))
#########################################################################################
    def instruction_tsp_points(cities, selected):
#########################################################################################
        if cities > selected:
                text1 = font2.render("Please select " + str (cities - selected) + " more points", 1, (0, 0, 0))    
        else:
                text1 = font2.render("TSP Points selection completed", 1, (0, 0, 0))    
        text2 = font2.render("Please select TSP points in green rectangle on right side", 1, (0, 0, 0))
        screen.blit(text1, (20, 520))       
        screen.blit(text2, (20, 540))
#########################################################################################
    def instruction(grid, city_get_run):
#########################################################################################
        run = 1
        flat_grid = [item for sublist in grid for item in sublist]
        pending_select= cities - flat_grid.count(1)
        available_cities = flat_grid.count(-1)
        if city_get_run == True:
            text1 = font2.render("Please select no of cities from grid above", 1, (0, 0, 0))
            return (run)
        if pending_select == 0:
            text1 = font2.render("Selection successful", 1, (0, 255, 0))
            run = 0
        else:
            if available_cities < 1:
                text1 = font2.render("Invalid selection", 1, (255, 0, 0))        
                run = 0
            else:
                text1 = font2.render("Please select " + str (pending_select) + " more edges to complete the tour", 1, (0, 0, 0))
        text2 = font2.render("Tour can be visualised in other window", 1, (0, 0, 0))
        screen.blit(text1, (20, 520))       
        screen.blit(text2, (20, 540))
        return (run)
#########################################################################################
    def draw_graph (graph_cord):
#########################################################################################
        for city in range (len (graph_cord[0])):
            text1 = font2.render(str (city+1), 1, (255, 0, 0))
            screen.blit(text1, (graph_cord[0][city], graph_cord[1][city]))       
#########################################################################################
    def draw_edges (graph_cord, grid):
#########################################################################################
        thick = 5
        for fr_city in range (len(grid)):
            for to_city in range (len(grid)):
                if grid[fr_city][to_city] == 1:
                    pygame.draw.line(screen, (((fr_city+to_city)*71)%255, (fr_city*31)%255, (to_city*19)%255), (graph_cord[0][fr_city], graph_cord[1][fr_city]), (graph_cord[0][to_city], graph_cord[1][to_city]), thick)
#########################################################################################
    def sub_tour_check(grid, recent_edge):  #CHECK CLOSING EDGE BASED ON RECENT SELECTIION
        '''Chech edge which needs to be blocked for sub tour elimination
        CRITICAL PART OF ALGORITHIM'''
#########################################################################################
        print (grid)
        print (type(grid))
        print (type(recent_edge))
        print (recent_edge)
        (x_org, y_org) = recent_edge        #RECENT EDGE ADDED
        #GETTING TO X END OF PATH CONNECTED TO RECENT EDGE
        x = x_org
        x_dash = -1
        y_dash = y_org
        while (x_dash != x):
            x_dash = x
            for i in range (cities):
                if (grid [x][i]) == 1:
                     if i != y_dash:
                        y_dash = x
                        x = i
                if (grid [i][x]) == 1:
                     if i != y_dash:
                        y_dash = x
                        x = i
        #GETTING TO Y END OF PATH CONNECTED TO RECENT EDGE
        y = y_org
        y_dash = -1
        x_dash = x_org
        while (y_dash != y):
            y_dash = y
            for i in range (cities):
                if (grid [y][i]) == 1:
                     if i != x_dash:
                        x_dash = y
                        y = i
                if (grid [i][y]) == 1:
                     if i != x_dash:
                        x_dash = y
                        y = i
        return (x,y)            #RETURNING END POINTS OF PATH WITH EDGES
#########################################################################################
    '''master() code starts'''
    max_city=3
    cities=0        #default
    dif = 500 / max_city   #for getting cities number
    x = 0
    y = 0
    val = 0
    # Load test fonts for future use
    font1 = pygame.font.SysFont("comicsans", 30)
    font2 = pygame.font.SysFont("comicsans", 20)
    font3 = pygame.font.SysFont("comicsans", 40)
    city_get_run = True
    run = True
    run2 = True      #loop after game is over
    flag1 = 0
    flag2 = 0
    rs = 0
    error = 0
    # GET CITY loop thats keep the window running
    force_exit = True
    ####        SELECT NUMBER OF CITIES         ####
    while city_get_run and force_exit:
        # White color background
        screen.fill((255, 255, 255))
        # Loop through the events stored in event.get()
        for event in pygame.event.get():
            # Quit the game window
            if event.type == pygame.QUIT:
                print ("you exit")
                run = False
                run2 = False
                city_get_run = False
                force_exit = False
            # Get the mouse position to insert number   
            elif event.type == pygame.MOUSEBUTTONDOWN:
                flag1 = 1
                pos = pygame.mouse.get_pos()
                (x, y)=get_cord(pos)
                if pos[1] > 560:                ## MASTER RESET
                    run = False
                    run2 = False
                    city_get_run = False
                    force_exit = False
                    get_points = False
                    return ("R")
                x = int (x)
                y = int (y)
                print (x)
                print (y)
                if x<max_city and y<max_city:
                    cities = x+4 + y*max_city
                    city_get_run = False
        instruction_cities()
        draw_no_city(max_city)
        draw_reset ()
        pygame.display.update() 
    if cities > 9:
        font1 = pygame.font.SysFont("comicsans", 15)
    elif cities > 7:
        font1 = pygame.font.SysFont("comicsans", 20)
    ####        GENERATE GRAPH POINTS        ####
    pre_def_pts = np.matrix('549 44; 745 47; 746 494; 548 497; 513 191; 514 360; 791 214; 791 371; 602 138; 695 141; 595 424; 708 430')
    pts_pick = np.random.permutation(12)
    gr_x=[]
    gr_y=[]
    for i in range (cities):
        gr_x.append (pre_def_pts[pts_pick[i], 0])
        gr_y.append (pre_def_pts[pts_pick[i], 1])
    graph_cord = (gr_x, gr_y)
    draw_tsp_points (cities)
    draw_graph (graph_cord)
    draw_reset ()
    pygame.display.update() 
    if cities > 9:
        font1 = pygame.font.SysFont("comicsans", 15)
    elif cities > 7:
        font1 = pygame.font.SysFont("comicsans", 20)
    ####        EDGE SELECTION STARTS (USER BASED)         ####
    # MAIN GAME loop thats keep the window running
    if force_exit:
        dif = 500 / cities
        # Default Sudoku Board.
        grid_mat=np.zeros((cities, cities), int)
        grid_mat.fill(-1)                               # -1 avaialble, not selected
        np.fill_diagonal(grid_mat, 0)                   # 0 not available
        grid = grid_mat.tolist()
        draw_edges (graph_cord, grid)
        draw_graph (graph_cord)
        draw()
        draw_box()
        #draw_val(val)
        pygame.display.update() 
    while run and force_exit:
        # White color background
        screen.fill((255, 255, 255))
        # Loop through the events stored in event.get()
        for event in pygame.event.get():
            # Quit the game window
            if event.type == pygame.QUIT:
                print ("you exit-here")
                run = False
                run2 = False
                force_exit = False
            # Get the mouse position to insert number   
            elif event.type == pygame.MOUSEBUTTONDOWN:
                flag1 = 1
                pos = pygame.mouse.get_pos()
                (x, y)=get_cord(pos)
                if pos[1] > 560:                ## MASTER RESET
                    run = False
                    run2 = False
                    city_get_run = False
                    force_exit = False
                    get_points = False
                    return ("R")
                x = int (x)
                y = int (y)
                print (x)
                print (y)
                print ("====")
                if x >= cities or y >= cities:
                    print ("Please select in the edge grid")
                elif grid[x][y] == 0:                         # 0 not available
                    print ("This edge is not available, select among available edges")
                elif grid[x][y] == 1:       
                    print ("Edge is already sleceted, select among available edges")
                else:                                       # -1 avaialble, not selected
                    print ("Edge  seleceted")
##########      UPDATING GRID ON SELECTION
                    grid[x][y] = 1                          #selected edge
                    grid[y][x] = 0                          #mirror edge blocked
                    for i in range (cities):
                        if grid [x][i] == -1:               
                            grid [x][i] = 0                 #all edges in row blocked
                        if grid [i][y] == -1:
                            grid [i][y] = 0                 #all edges in colm blocked
##########     BLOCK SUB TOUR
                    block_edge = sub_tour_check(grid, (x, y))  #CHECK CLOSING EDGE BASED ON RECENT SELECTIION
                    #print (block_edge) 
                    (x, y) = block_edge
                    if grid [x][y] == -1:               
                        grid [x][y] = 0                 #BLOCK
                    if grid [y][x] == -1:
                        grid [y][x] = 0                 #BLOCK MIRRIOR
##########     CHECK PENDING SELECTION AND EDGES
                    flat_grid = [item for sublist in grid for item in sublist]
                    pending_slection = cities - flat_grid.count(1)
                    available_edges = flat_grid.count(-1)
                    print ("pending_slection: " + str(pending_slection) +";  available_edges: " + str(available_edges))
                    if pending_slection == available_edges: #GAME ENDED
                        for i in range (cities):
                            for j in range (cities):
                                if grid[i][j] == -1:
                                    grid[i][j] = 1
        # Update window
        instruction(grid, city_get_run)
        draw_box()
        draw()
        draw_graph (graph_cord)
        draw_edges (graph_cord, grid)
    #    draw_val(val)
        draw_reset()
        pygame.display.update() 

    while run2:
        # Loop through the events stored in event.get()
        for event in pygame.event.get():
            # Quit the game window
            if event.type == pygame.QUIT:
                print ("you exit")
                run2 = False
    # Quit pygame window   
    
    ############

# Total window
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("EDGE SELECTION - TOUR BUILDER")
#img = pygame.image.load('icon.png')
#pygame.display.set_icon(img)

# initialise the pygame font
def main():
    reset = 'R'
    while reset == 'R':
        pygame.font.init()
        reset = master()
    pygame.quit()
main()
