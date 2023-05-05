from itertools import combinations
from BuildPuzzle import *
from PreparePuzzle import *
from TestingDisplay import *
from FindSolutions import *
from Hidden import *



''' 
Creates dictionary of whole grid



'''

def grid_dictionary(grid):
    
    grid_dict = dict()
    
    for i in range(9):
        line_dict = dict()
        for j in range(9):
            grid_dict[(i,j)] = grid[i][j] 
            #print(line_dict)
        grid_dict.update( line_dict)
        
            
    return grid_dict




def lines_dict(grid):
    
    allrows = dict()
    allcols = dict()
    
    for line in range(9):
        rdict = row_dict(grid, line)
        cdict = col_dict(grid, line)
        
        allrows[line] = rdict
        allcols[line] = cdict
    return allrows , allcols

#r_dict, c_dict = lines_dict(col_sample)



'''
x - wing 

- Example: Two numbers available in two locations on a single line.
- another line has those same two numbers aviable, and they share the
same adj row/col. 

- four boxes, three numbers. One number occurs 4 times, 2 nums occur 2 times. 

1. for each line - find a pair  


'''




def xwing_id(line_dict,  grid ,line_type = True):
    total_removed = 0
 
    # Start with big row dictionary. Check one row at a time. 
    for grid_row in line_dict.keys():
       
        # Hold any double numbers found in a dictionary num:positions 
        row_items = dict()
        
        # Look inside each number 1:9 of the row, and their associated positions.
        for number , positions in line_dict[grid_row].items():
           
            # if a number occurs only in two positions. (ARRAY MUST BE PERFECT)
            if len(positions) == 2:
               
                # If found, add to dictionary. (may not need, could just use number/position.)
                col1 = positions[0][1]
                col2 = positions[1][1]
                
                row1 = positions[0][0]
                row2 = positions[1][0]
                
                position_list = positions
                # does number exist in any other row at the two columns?

                for grid_row2 in line_dict.keys():
                    
                    if grid_row2 != grid_row:
                    
                        if len(line_dict[grid_row2][number]) == 2:
                                
                            second_positions = line_dict[grid_row2][number]
                   
                            col3 = second_positions[0][1]
                            col4 = second_positions[1][1]
                            
                            row3 = second_positions[0][0]
                            row4 = second_positions[1][0]
                            
                            
                            if line_type == True:
                            
                                if (col1, col2) == (col3, col4):

                                    for x in second_positions:
                                        position_list.append(x)   
                                    
                                    row_items[number] = position_list
                                    grid, count = remove_xwings(grid, row_items, line_type)
                                    total_removed += count
                                    
                            elif line_type == False:
                                if (row1, row2) == (row3, row4):
   
                                    for x in second_positions:
                                        position_list.append(x)   

                                    row_items[number] = position_list
                                    grid, count = remove_xwings(grid, row_items, line_type)
                                    total_removed += count
    
    
    return grid , total_removed
                                

def get_box(position):

    box_start_row = position[0] // 3
    box_start_col = position[1] // 3

    box = (box_start_row, box_start_col)
    
    return box
            





def remove_xwings(grid,  row_items, line_type):
    
    #print(row_items)
    
    for number, positions in row_items.items():
        count = 0 
        number = number
        rows = set()
        cols = set()
        for pos in positions:
            rows.add(pos[0])
            cols.add(pos[1])
            
        for i in range(9):
            if line_type == True:   
                for c in cols:
                    if len(grid[i][c]) > 1:                
                        if (number in grid[i][c]) and (i not in rows):
                            grid[i][c].remove(number)
                            count += 1
              
            elif line_type == False:
                for r in rows:
                    if len(grid[r][i]) > 1:
                        if (number in grid[r][i]) and (i not in cols):
                            grid[r][i].remove(number)
                            count += 1

        for p in positions:
            box1 = get_box(p)
            for next_p in positions:
                if p != next_p:
                    box2 = get_box(next_p)
                    if box1 == box2:
                        for i in range(box1[0] *3, box1[0]*3 + 3):
                            for j in range(box1[1] *3, box1[1]*3 + 3):
                                if (i,j) not in positions:
                                    if (number in grid[i][j]) and (len(grid[i][j]) > 1):
                                        grid[i][j].remove(number)
                    
    
    return grid, count
            
     
    
def xwing(grid):
    
    r_dict, c_dict = lines_dict(grid) 
                   
    test_rows ,total_removed = xwing_id(r_dict,  grid, True)
    test_cols, total_removed2 = xwing_id(c_dict, test_rows, False)
    
    total = total_removed + total_removed2
    
    return test_cols, total 
                    
                        

'''
XY Wing strategy: 

Three cells in the grid, each with a pair of candidates that share
at least one digit. Use these three pairs to draw a rect. 

If any number is identified in the lines of the rect, or there 
is a number in the intersection that is in both corners...

they can be removed.



'''

# def xy_wing_dict(grid_dict, grid):
    
    
#     # start with dict :
    
#     for grid_line in grid_dict.keys():
#         print("gridline is " , grid_line)
        
#         wing = dict()
#         tail = dict()
        
#         for position, numbers in grid_dict[grid_line].items():
#             if len(numbers) == 2:
#                 wing[position] = numbers 
        
#         for pos ,nums in wing.items():
            
#             sq1_pos = pos
#             sq1_nums = nums
#             print("found first at ", sq1_pos, sq1_nums)
            
#             #check for a partial matched second square:
#             for pos2, nums2 in wing.items():
#                 if pos2 != pos:
                    
#                     part_set = set(nums, nums2)
#                     if len(part_set) == 3:
#                         # found a partial match
#                         sq2_pos = pos2
#                         sq2_nums2 = nums2 
                        
#                         print("found a second at ", (pos2, nums2))
                        
#                         for n in nums2:
#                             if n in sq1_nums:
#                                 sq2_nums2.remove(n)
                                
#                         tail[pos2] = sq2_nums2

#         # Now that I have a pair in a row , find a pair in the wing - column.
#         for grid_line2 in grid_dict.keys():
            
#             for col_pos, col_nums in grid_line[grid_line2].items():
            
#                 # if it is the col of my tail... 
            
#                 if col_pos[1] == tail[0][1]:
                
#                     for i in range(9):
                        
#                         if (len(grid[i][col_pos[1]]) == 2) and (pos2 != col_pos):
                            
#                             if (sq2_nums2 in col_nums) and any(col_nums in sq1_nums):
                                
#                                 # Found a third
#                                 print("found a third at")

# grid_dict = grid_dictionary(arrays)  

# print(grid_dict)                          

# maybe = xy_wing_dict(grid_dict, arrays)
                                
                                
                            
# def tryagin_dict(grid_dict, grid):
    
#     for position , numbers in grid_dict.items():
        
#         row= position[0]
#         col = position[1]
        
#         for i in range(9):
            
                               
                
                
                
                
            
                
                

            


                
            
            
                        
                        
                            
                        
                      
                        
                        
                        
                        
                    
                    
                
                
    
    
    
    





#do i want to use a dict?

# def xy_wing(grid):
#     square1 = []
#     square2 = []
#     square3 = []
#     square4 = []
    
    
    
#     for i in range(9):
#         for j in range(9):
#             if len(grid[i][j]) == 2:
#                 square1 = grid[i][j]
#                 print("square 1 is ", square1, (i,j))                
#                 #check remaining row/col
#                 for k in range(9):
#                     #check rows for other pair
#                     if len(grid[k][j]) == 2: 
#                         for num in grid[k][j]: 
#                             if ( num in square1 )and (k!= i):
#                                 square2 = grid[k][j]
                                
#                                 for m in range(9):
#                                     if len(grid[k][m]) == 2:
#                                         for num in grid[k][m]:
#                                             #check cols of other pair 
#                                             if (num in square2) and (m!= j) and (()):
#                                                 for num in grid[k][m]:
#                                                     if num in square1:
#                                                         square3 = grid[k][m]
#                                                         print("square3 is ", square3, "at" ,(k,m))
            
#                     #check cols for other pair    
#                     if len(grid[i][k]) == 2:
#                         for num in grid[i][k]:
#                             if (num in square2) and (k != j): 
#                                 square2 = grid[k][j]  
                                                  
#                                 for l in range(9):
#                                     #check rows
#                                     if len(grid[k][l]) == 2:
#                                         for num in grid[k][l]:
#                                             if num in square2:
#                                                 for num in grid[k][l]:
                                                    
#                                                     if num in square1 and (l != j):
#                                                         square3 = grid[k][l]
#                                                         print("square3 is ", square3, "at" ,(l,k))
#     print("square1", square1, "square2", square2, "square3", square3)
    
# test = xy_wing(arrays)

# array_display(arrays, "test")
                                                        
                                                        

                                                        
            
            
    
    
        
                                    
                                
                    
                                
                                
        
        
    





           
           
        
       
    
