# tsp_edge_select
A python based game for generating tour based on edge selection
======
This code graphically verifies the algorithm to build TSP tour based on edge selection
As the edges are selected by user progressively
   The algorithm, block edges which are invalid for selection
   The algorithms always results in VALID TOUR SELECTION
======
#   Brief on algorithm:
   	All edges are available initially for selection
     	If no of cities = n; then n edges are to be selected
    	On each selection of edge:
        	All edges in the row of edge are blocked
        	All edges in the column of edge are blocked
        	Edges which can create SUB TOUR are blocked - routine "sub_tour_check"
 
 NOTE: WHEN NO OF PENDING SELECTIONS + NO OF AVAILABLE OPTIONS
        	ALGORITHM AUTO SELECTS ALL REMAINING EDGES
======
# How to use:
   1. Download the file "tsp_edge_select.py"
   2. Install python dependencies "pygame"
   3  Run: python3 tsp_edge_select.py
   
   === OR ===
   
   1. Simply download excutable "tsp_edge_select"
   2. Run: ./tsp_edge_select
   (Tested on ubuntu / linux only)
   
   === OR ===
   Simplest
   try on "https://codehs.com/sandbox/id/pygame-6RucFM"
   
