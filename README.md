A python based game for generating tour based on edge selection

This code graphically verifies the algorithm to build TSP tour based on edge selection
As the edges are selected by user progressively
   The algorithm, block edges which are invalid for selection
   The algorithms always results in VALID TOUR SELECTION

#   Brief algorithm:
```swift
START 
    Number of cities <- 'n' 
    All edges are available during initial selection
    WHILE (selected edges < n) do
       Select one of the non-BLOCKED edges:
          All edges in the row of selected edge are BLOCKED
          All edges in the column of selected edge are BLOCKED
          Edges which can create SUB TOUR are BLOCKED    #Routine "sub_tour_check"
          if (pending edges to be selected == non-BLOCKED edges):
              Select all remaining edges                 #No more options available
    END WHILE
END
```
     
# How to use:
   1. Download the file "tsp_edge_select.py"
   2. Install python dependencies "pygame"
   3. Run: python3 tsp_edge_select.py
   
   === OR ===
   
   1. Simply download excutable "tsp_edge_select"
   2. Run: ./tsp_edge_select
   (Tested on ubuntu / linux only)
   
   === OR (**Simplest**)
   1. Try on "https://codehs.com/sandbox/id/pygame-6RucFM"
   (to view screenshot)
   2. Make sure the output window is maximised and browser is in full creen mode (F11)
# Screenshots   
   ![This is an image](https://raw.githubusercontent.com/arian-code/tsp_edge_select/main/1-init_pic.png)
   ![This is an image](https://raw.githubusercontent.com/arian-code/tsp_edge_select/main/2-build_tour.png)
   


