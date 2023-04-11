# from itertools import combinations
# from BuildPuzzle import *
# from PreparePuzzle import *
# from TestingDisplay import *
# from FindSolutions import *


# '''
# Candidate Lines: 


# Function will remove ineligible candidates in remaining arrays: 

# First look in a BOX:
#     - if Any number 1-9 only exists as a candidate in a given row or column
#         then it has to be on that LINE within that BOX. 
#     - Therefore: any other numbers listed on that line OUTSIDE of the box, 
#         can be removed.
        
# In any given 3x3 grid with [i][j] determining the position of a number. If that number is only found in a single row or single column, 
# then it will only have locations that share the same I or J, but not both. 

# So if 4's are only available in column 0 for box 1, then we would remove all OTHER 4's from column 0


# '''

              
# # grid_new = create_grid_fill()  
# # grid_game = new_game_board(grid_new)
# # gridc = create_arrays(grid_game)
# # grid, count = basic_solve(gridc)
# # print_pos_grid(grid)

# # print("END OF INTRO::::::::::::::::::::::::::")
                                              
     
# # Function: Takes a grid and position in the grid, and returns a list  of the available numbers for that grid (numbers that have not been solved. )        
# def available_nums(grid, i,j ):
#     #Sets position (i,j) to the appropriate 3x3 box.
#     box_rst = i // 3 
#     box_cst = j // 3 
        
#     # For the row in range (Whatever the starting row is for my current box) (Row 0 at init) up to three rows (ENDING AT ROW 2 )
#     for row in range(box_rst * 3, box_rst * 3 + 3):
#         # for the col in range (Starting Col (0) to three additional (col 2))        
#         for col in range(box_cst * 3, box_cst * 3 + 3):              
#             # First, set list of available nums. I will use these as what nums to LOOK FOR in my LINES(row/col)
#             available_nums = [1,2,3,4,5,6,7,8,9]
#             # check all squares to determine if it is a solved square: And remove from the available nums list. 
#             for nums in grid[row][col]:
#                 if len(grid[row][col]) == 1:
#                     available_nums.remove(grid[row][col])
#     return available_nums
    
                   
# # Takes grid and position in grid, returns a list of sets: list_cols and list_rows, that are the possible numbers left remaining for the three rows / cols in a box.         
# def box_lists(grid, box):        
    
#     # count variable to adjust which box we are iterating over.                 
#     count = 0                     
                    
        
#     #start new iteration through each square of box
    
#     box_rst = box[0]
#     box_cst = box[1]
    
#     box_cols = []
#     box_rows = []
        
#     # for the row in range (Starting row (0) to three additional (row 2)) 
#     # start at 0, start at 3, start at 9 up to 3, up to 6 up to 9
    
#     for line in range(box_rst * 3, box_rst * 3 + 3):  
        
        
#         single_row = set()

#        # print("box row start is ", (box_rst *3 , box_rst *3 +3))
#         # for the col in range (Starting Col (0) to three additional (col 2))  
              
#         for item in range(box_cst * 3, box_cst * 3 + 3):  
#            # print("box col start is ", (box_cst *3 , box_cst *3 +3))
#             # Iterate in one row at a time through the three columns. 
#             #print(":::::::::::::::::::::::::::")
#             #print("THIS IS THE CURRENT BOX : ", (box_rst, box_cst))
#             #print(":::::::::::::::::::::::::::::::::::::::::")
  
#             if len(grid[line][item]) == 1 :
#                 # For each column in my row: add 0 as holder if the square is 0 
#               #  print("adding to single_ROW set ", 0, "from", (line, item))
#                 single_row.add(0)
#             else:
#               #  print("adding to single_row", grid[line][item] , "at ", (line, item))
                
#                 # CONSIDER ADDING REMOVE: statement if number in position is not in available nums
                
#                 single_row.update(grid[line][item])
        
#         box_rows.append(single_row)
        
#     for item in range(box_cst * 3, box_cst * 3 + 3):
#         single_col = set()
#         for line in range(box_rst * 3, box_rst * 3 + 3):       
          
            
        
    
#             #print("position is COL", (line,item))   
#             if len(grid[line][item]) == 1:
#               #  print("adding to single_row", 0 , "at ", (item,line))
#                 single_col.add(0)

#             else:
#               #  print("adding to single_row", grid[line][item] , "at ", (line, item))
#                 #print("adding to single_COL set ", grid[line][item], "from", (item, line))
#                 single_col.update(grid[line][item])
                
#             #put set into list. 
#             #print("row set is ", single_row) 
#            # print("Cols Set is ", single_col)           
        
        
#         box_cols.append(single_col)
#     #print("box_rows ", box_rows)
#     #print("box_cols ", box_cols)
            
#     return box_rows, box_cols     


# def cand_lines(grid, k):
    
#     '''1. For each section (3 line, 3 box), check each number 1-9, determine if num available (not sovled square) for each line and in each box.
#     2. if a num is only availble for 1 box in 1 line, it is a fixed candidate for that line. 
#     3. remove num from any other squares of that box.'''
    
#     numbers = [1,2,3,4,5,6,7,8,9]
#     rnum_dict = dict()
#     cnum_dict = dict()
#     #for each section (3 major)
#     #for k in range(3):
#     sect_st = k * 3 
#         #print("K is ", k )
#         #print("sect_st at init is ", sect_st)
        
#          #create dict of nums
#     for num in numbers:
        
#         row_dict = dict()
#         col_dict = dict()
            
#         #for each line of section (3 row / 3 col)
#         for sect_st in range(3):
#             rboxes = set()
#             cboxes = set()
#             for square in range(9):
#                     #print("looking at square ", (sect_st, square))
#                 box = square // 3 
#                 if type(grid[sect_st][square]) is not list: grid[sect_st][square] = [grid[sect_st][square]]
#                 if len(grid[sect_st][square]) > 1:
#                     if num in grid[sect_st][square]:
#                             #print("num found, adding ", box, "to list of boxes")
#                         rboxes.add(box)
                        
#                 if type(grid[square][sect_st]) is not list: grid[square][sect_st] = [grid[square][sect_st]]
#                 if len(grid[square][sect_st]) > 1:
#                     if num in grid[square][sect_st]:
#                             #print("num found, adding ", box, "to list of boxes")
#                         cboxes.add(box)
                
#                 #wont include numbs already 
#             if len(rboxes) >= 1 :
#                 row_dict[sect_st] = rboxes
#             if len(cboxes) >= 1 :
#                 col_dict[sect_st] = cboxes
#                 #print("newest row_dict ", row_dict)
            
#             #once finished looping for a num, add dict of rows to num dict
#         rnum_dict[num] = row_dict
#         cnum_dict[num] = col_dict    
#         #print(num_dict, "here is my dict of nums")
#     return rnum_dict, cnum_dict
        



# '''Creates nested dictionary of numbers, rows, and boxes, identifying which 
# numbers should be removed from which rows and boxes after identifying fixed_candidates

# returnes a dict'''

# def find_fixed_candidates(nums_dict):
    
#     candidates = dict()
#     for number , rows in nums_dict.items():
#         if len(rows) > 1:
#             num_reset = dict()
#             for row , boxes in nums_dict[number].items():
             
#                 keep = []
#                 if len(boxes) == 1:
                             
#                     candidates[number] = nums_dict[number]
#                    # print("candidates are ", candidates)                
    
#     remove_dict = dict()
#     if len(candidates) > 0:
#         for number in candidates.keys():
#             for row, box in candidates[number].items():
#                 if len(box) == 1:
#                    # print("box is ", box)
#                     row_holder = dict()
#                     for row1, box1 in candidates[number].items():
#                         if row != row1:
#                             place_holder_list = []
#                            # print("place holder list (to hold box values to remove)", place_holder_list)
#                             for i in box1:
#                                 if i in box:
                            
#                                     place_holder_list.append(i)    
       
#                                     row_holder[row1] = place_holder_list
#             remove_dict[number] = row_holder
                            
#     return remove_dict


# # test2 = find_fixed_candidates(test)
# # print(test2)

                
# def remove_nonfixed(nums_dict, grid, k , row = True):
    
#     '''takes dict with nums to remove and where and removes them.'''
#     box_start = 0
#     line_start = k * 3
#    # print("line start is ", line_start)
#     removed_nums = 0
#     CL_nonfixed_dict = dict()
    
#     #get first number in dict. 
#     for number in nums_dict.keys():
        
#         #get first line/box in dict
#         for line, box in nums_dict[number].items():
#            # print("line is ", line)
            
#             #set starting point for grid
#             gridline= line_start + line
#            # print("......................................................")
#            # print("line to access is ", gridline)
            
#             b = 0
#             for i in box:
#                 b = i
#             box_start = b * 3 
              
#            # print("removing from squares starting at ", box_start)
#             #set box start
#             for box_start in range(box_start, box_start + 3):
                
#                 #PUT ROW/COL DEPENDENCY HERE
#                 if row == True: 
#                    # print("looking at position ", (gridline, box_start))
#                     nums_in_square = grid[gridline][box_start]
                
#                     if len(grid[gridline][box_start]) > 1:
                         
                
#                         for j in grid[gridline][box_start]:
#                             if j == number:
#                                 nums_in_square.remove(j)
#                                 removed_nums += 1
#                         grid[gridline][box_start] = nums_in_square
#                         CL_nonfixed_dict[(gridline, box_start)] = j
#                         #print("CL : ", (gridline, box_start), "removed", j )
#                 else:
                  
#                     nums_in_square = grid[box_start][gridline]
#                         # print("looking at position ", (box_start, gridline))
                
#                     if len(grid[box_start][gridline]) > 1:
                       
                
#                         for j in grid[box_start][gridline]:
#                             if j == number:
#                                 nums_in_square.remove(j)
#                                 removed_nums += 1
#                         grid[box_start][gridline] = nums_in_square
#                         CL_nonfixed_dict[(box_start, gridline)] = j
#                         #print("CL : ", (box_start, gridline), "removed", j )
                    
#     '''Print Statements for debugging'''
#     # if len(CL_nonfixed_dict) > 0:
#     #     print("CL NONFIXED REMOVED", removed_nums)
#     #     print(CL_nonfixed_dict)
#     return grid, removed_nums
    
    
    

        
        
# def section_loop(grid):
#     total = 0
#     updatedgrid = grid
#     for k in range(3):
#        # print("k is ", k)
        
#         rdict, cdict = cand_lines(grid,k) 
#         #print("FIRST row DICT ", rdict)
#         #print("...............................................")
#         #print("FIRST col DICT", cdict)
#         fixed_dict = find_fixed_candidates(rdict)
#         #print("FIXED DICT ", fixed_dict)
        
#         if len(fixed_dict) > 0:
#             updatedgrid, count = remove_nonfixed(fixed_dict, grid, k, True)
#             total += count
            
#         fixed_cdict = find_fixed_candidates(cdict)
#         #print("FIXED cDICT ", fixed_cdict)
        
#         if len(fixed_cdict) > 0:
#             updatedgrid, count = remove_nonfixed(fixed_cdict, updatedgrid, k, False)
#             total += count
            
#    # print("final count is ", total)
    
#     return updatedgrid, total
        
        
# # final = section_loop(grid)
# # print("printing final")
# # print_pos_grid(final)      
        
# #array_display(final, "Final")
                

 
# # TEST TEST TEST 
# # print_pos_grid(grid)
# # testing_box_lines = box_lists(grid, (0,1))    
# # box_rows, box_cols = box_lists(grid, (2,2))

# #array_display(grid)
    
# # I don't need the grid I just need the position to know which box to put it in.  
# #function creates a dictionary based on what box is entered and includes the box location, box_row list and box_col list   
# def create_box_dict(i,j, box_rows, box_cols):  
    
#     box_row_start = i // 3 
#     box_col_start = j // 3    
    
#     lonely_rnum = [] 
 
#     for list_check in range(len(box_rows)):
#         for number in box_rows[list_check]: 
#             check_count = 0
    
#             for other_list in range(len(box_rows)):
#                 #continue to next list if other_list is the same as primary list
#                 if list_check == other_list:
#                     continue
                
#                 if check_count <= 1:
#                     #if not in my first list, check the other.
#                     if number in box_rows[other_list]:
#                         continue
#                     else:
#                         break
#                 else:
#                     if number not in box_rows[other_list]:
#                         lonely_rnum.append(number) 
#                     else:
#                         lonely_rnum.append(0)
#                         break

#     lonely_cnum = [] 
#     for list_check in range(len(box_cols)):
#     #starts at 0
#         for number in box_cols[list_check]:
#             check_count = 0
            
#             for other_list in range(len(box_cols)):
                
#                 if list_check == other_list:
#                     #check next other_list
#                     continue
        
#                 if check_count < 1: 
#                     if number not in box_cols[other_list]:
#                         #not in first check but may be in second. Increase count and continue to next list iteration. 
#                         check_count += 1
#                         continue
#                     else:
#                         #it was found! This means we don't need to check the other list, the number isn't lonely.
#                         break
                
#                 else: 
#                     if number not in box_cols[other_list]:
#                         #Wasn't in first check, not in second = lonely column number. 
#                         lonely_cnum.append(number)
#                     else:
#                         lonely_cnum.append(0)
#                         break

#     my_dict = {
#         "box" : (box_row_start, box_col_start),
#         "box_rows" : box_rows,
#         "box_cols" : box_cols,
#         "lonely_rs" : lonely_rnum,
#         "lonely_cs": lonely_cnum
#     }
    
#     return my_dict


# #alternatively: Get all "lonely numbers that are in each row/col of a specific box. Creates a list of numbers that are only in one row or column
# # returns lonely_rnum_list, lonely_cnum_list. 0's included as place holders to keep the position 0,1,2 of the line position in the box.

# def lonely_nums(box_rows,box_cols):
    
#     box_rows = box_rows 
#     box_cols = box_cols
    
#     lonely_rnum_list = []
    
#     #print("::::::::::::: TEST ROWS FOR LONELY ::::::::::")
#     # print(":::::::::::::::::::::::::::::::::::::::::::::::")
    
#     for list_check in range(len(box_rows)):
        
#         #make a set of all lonely nums from each row
#         lonely_rnum = set() 
#         lonely_rnum.add(0)
        
#        # print("Checking row: ", list_check, box_rows[list_check] )
#         for number in box_rows[list_check]: 
#             check_count = 0
#             #print("NUMBER IS ", number)
            
#             if number == 0:
#                 continue
    
#             for other_list in range(len(box_rows)):
                
#                # print("Checking list :  ", other_list, "containing ", box_rows[other_list])                
                
#                 #continue to next list if other_list is the same as primary list
#                 if list_check == other_list:
#                     #print("duplicate, moving on.")
#                     continue
                
#                 if check_count < 1:
#                     #print("Check Count is Less than 1 CHECKING: ", other_list)
#                     #if not in my first list, check the other.
#                     if number not in box_rows[other_list]:
#                         check_count += 1
                        
#                       #  print( number, "WAS NOT IN list, check next list ")
#                         continue
#                     # if in my first list, check next number
#                     else:
#                        # print(number, "IN list, NUMBER ISNT LONELY:  BREAK OUT OF LOOP AND CHECK NEXT NUMBER")
#                         #remove number from other list, no need to check it again and again
#                         box_rows[other_list].remove(number)
                        
                        
#                         break
#                 else:
#                     #print("Check count is 1 or more")
#                     # if not the first list, (count <= 1) indicate second list)
#                     if number not in box_rows[other_list]:
                        
#                         #print(number, "was NOT IN list", other_list, "ADD TO LONELY NUMS")
                        
#                         lonely_rnum.add(number) 
#                     else:
#                         #print(number, "WAS IN", other_list, "adding 0 as place keeper")
#                         box_rows[other_list].remove(number)
                        
                       
#                         break
#         lonely_rnum_list.append(lonely_rnum)

#     lonely_cnum_list = [] 
#     #print("::::::::::::: TEST COLS FOR LONELY ::::::::::")
#     #print("::::::::::::::::::::::::::::::::::::::::::::::")
#     for list_check in range(len(box_cols)):
#        #print("Checking COL list: ", box_cols[list_check], list_check)
#         lonely_cnum = set()
#         lonely_cnum.add(0)
#     #starts at 0
#         for number in box_cols[list_check]:
#             check_count = 0
#             #print("NUMBER IS ", number)
            
            
#             if number == 0:
#                 #dont care about 0's move on.
#                 continue
            
#             for other_list in range(len(box_cols)):
#                 #print("checking list ", list_check, box_cols[list_check])
                
                
#                 if list_check == other_list:
#                     #print("duplicate list, move on")
#                     #check next other_list
#                     continue
        
#                 if check_count < 1: 
#                     #print("Comparing to :", other_list ,box_cols[other_list])
#                    # print("check_count less than 1 : first comparison" )
#                     if number not in box_cols[other_list]:
#                         #not in first check but may be in second. Increase count and continue to next list iteration. 
#                        # print( number, " was NOT there, check NEXT LIST")
#                         check_count += 1
#                         continue
#                     else:
#                        # print(number, "It WAS THERE, BREAK OUT OF LOOP AND CHECK NEXT NUMBER")
#                         box_cols[other_list].remove(number)
#                         lonely_cnum.add(0)
                      
#                         break
                
#                 else: 
#                     if number not in box_cols[other_list]:
                        
#                         #print(number, "was NOT in ", other_list, "ADD TO LONELY NUMS")
#                         #Wasn't in first check, not in second = lonely column number. 
#                         lonely_cnum.add(number)
#                     else:
#                         #print(number, "WAS in ", other_list, " adding 0 as place keeper")
#                         box_cols[other_list].remove(number)
                        
#                         break
        
#         lonely_cnum_list.append(lonely_cnum)               
   
#     #print("lonly rnum list ", lonely_rnum_list)
#     #print("lonely cnum list", lonely_cnum_list)
#     return lonely_rnum_list, lonely_cnum_list

# #Loneyly nums testing: 
# #testing_lonely_nums = lonely_nums(box_rows, box_cols)



 
# # Now I want to check each box, find any lonely numbers, if i find a lonely number, 
 
# def check_lines(lonlies, box, grid, row = True):
#     CL_numsremoved = dict()
#     CL_newclues = dict()
                
#     #get starting row and col
#     row_start = box[0]
#     col_start = box[1]
    
#     #print("lonlies is ", lonlies)
    
#     #print("Box is ", box)
            
#     box_start = 0
#     grid_start = 0
    
#     # sets line to be the specific row or column of the box and grid
#     if  row == True:
    
#         check_start = box[1]*3
#         grid_start = box[0] *3 
#         not_sums = [ check_start, check_start + 1, check_start + 2]
                   
#     else:
#         check_start = box[0]*3
#         grid_start = box[1] *3
#         not_sums = [ check_start, check_start + 1, check_start + 2]
        
   
    
#     check_only = []
    
#     if row == True:
#         for i in range(9):
#             if i in not_sums:
#                 continue
#             else:
#                 check_only.append(i)
            
#     #print("CHECK ONLY::::::::::       ", check_only)
#     removed = 0
    
#     grid_start = grid_start
#     count = 0 
    
    
#     for lonely_list in lonlies: 
#     # for grid_start (row or col)
        
    
#         #print("grid_start at ", grid_start)    
#         #print("lonely list is ", lonely_list)

        
#         for number in lonely_list: 
#             if number == 0:
#                 continue
          
#             #print("number is ", number)
#             #now that I have my grid_start and nums to check, iterate through each square
            
#             # loop through line    
#             for k in range(9):    

#                 if row == True:
#                     #remove_list = []
                    
#                     if k not in not_sums:
#                         #if type(grid[grid_start][k]) is not list: grid[grid_start][k] = [grid[grid_start][k]]
                        
#                         if len(grid[grid_start][k]) > 1:
#                             remove_list = grid[grid_start][k]
#                             #print("my list is ", remove_list)
#                             if number in remove_list:
#                                # list = grid[grid_start][k]
#                               #  print("my list is ", remove_list)
#                                 if len(remove_list) == 2:
#                                     #print(number, " CL: New CLUE was removed from ",(grid_start, k), "nums ",  remove_list)

#                                     remove_list.remove(number)
                                
                                
#                                     grid[grid_start][k] = remove_list
#                                     removed += 1
#                                    # print("length of new array is ", len(remove_list))
#                                     #print(grid[grid_start][k]) 

#                                     CL_newclues[(grid_start,k)] = remove_list
                                    
#                                     if type(grid[grid_start][k]) is not list: grid[grid_start][k] = [grid[grid_start][k]]

#                                     #print(grid)
#                                     num_count, grid = update_array(grid)
#                                     #("printing grid, " , grid)
                                    
                              
#                                 else:
#                                     #print(number, " CL: removed from ",(grid_start, k), "num ", remove_list)

#                                     remove_list.remove(number)
                                
                                
#                                     grid[grid_start][k] = remove_list
                                
#                                     removed += 1
                                    
#                                     CL_numsremoved[(grid_start,k)] = number
                                
                 
#                             else:
#                                 continue
                        
                            
#                 else:
#                     remove_list = []
#                     if k not in not_sums:
#                        # print(k, "is k") 
#                         #print(grid[k][grid_start]) 
#                         #, "is type", type(grid[k][grid_start]))
                        
#                         #if type(grid[k][grid_start]) is not list: grid[k][grid_start] = [grid[k][grid_start]]
#                         #print(grid[k][grid_start]) 
#                         if len(grid[k][grid_start]) > 1:
#                             remove_list = grid[k][grid_start]
#                             #print("my list is ", remove_list)
#                             if number in remove_list:
#                                 if len(remove_list) == 2:
#                                     remove_list.remove(number)
                                
                                
#                                     grid[k][grid_start] = remove_list
#                                     removed += 1
#                                     #print("length of new array is ", len(remove_list)) 
                                    
#                                     #grid, num_count = update_array(grid)
#                                     #print(number, " CL: New CLUE was removed from ",(k, grid_start), "nums ",  remove_list)

#                                     CL_newclues[(k, grid_start)] = remove_list
#                                     if type(grid[k][grid_start]) is not list: grid[k][grid_start] = [grid[k][grid_start]]

                                    
#                                     #print(grid)
#                                     update_count, grid = update_array(grid)
#                                     #print("printing grid", grid)
                                    
                              
#                                 else:
#                                     #print(number, " CL: removed from ",(k, grid_start), "num ", remove_list)

#                                     remove_list.remove(number)
                                
                                
#                                     grid[k][grid_start] = remove_list
                                
#                                     removed += 1
#                                     CL_numsremoved[(k, grid_start)] = number
                                
                             
                        
                                
#                         else:
#                             continue
                           
#         grid_start += 1
#         '''Print Statements for debugging'''
#     # if len(CL_newclues) > 1:
#     #     print("NEW CLUES from CL")
#     #     print(CL_newclues)
        
#     # if len(CL_numsremoved) > 0:
#     #     print("CL REMOVED NUMS")
#     #     print(CL_numsremoved)                  
                   
#     return grid , removed

# #check lines testing: 

# #lonely_rnum_list, lonely_cnum_list
# #param: lonelies , box, grid, row = true

# # lonely_rnum_list, lonel_cnum_list = lonely_nums(box_rows, box_cols)

# # test_check_lines_rows = check_lines(lonely_rnum_list, (0,0), grid, row = True)



# # MAIN FUNCTION that creates updated grid removing any numbers from possible solutions arrays based on candidate lines strategy.
# # returnes grid, total_returned , with total_returned for testing purposes.

# '''Can still add new cand lines function here'''
           
# def check_lonely_nums(grid):
    
#     total_returned = 0
#     #must loop through each box!!!!!!
#     for row in range(3):
#         for col in range(3):
            
#             # box starting coords 
#             box = (row,col)
            
            
            
#             #print("BOX IS ", box)
            
#             box_rows, box_cols = box_lists(grid,box)
            
#             #print("box_rows", box_rows)
#             #print("box_cols", box_cols)
            
             
         
#             lonely_rnum, lonely_cnum = lonely_nums(box_rows,box_cols)
            
#             #print("lonely_cnum",  lonely_cnum)
#            # print("lonely_rnum", lonely_rnum)
            
#             row_check, returned = check_lines(lonely_rnum, box, grid, True)
            
#             col_check, treturned = check_lines(lonely_cnum, box, row_check, False)
            
         
            
#             total_returned += treturned
#     final, secondtotal = section_loop(col_check)
    
#     total_returned += secondtotal
        
        
#     return final , total_returned      
        

            
# # cl_grid , total_returned = check_lonely_nums(grid)


# # print_pos_grid(cl_grid)            
# # print(total_returned,  "total removed from num arrays after candidate lines. ")


# # Testing testingdisplay:

# #array_display(cl_grid)
              
        
                
                

            
            
            
            
            
                            
                
                   


               
                     
        
        
            
            

          
            
            
    
    
    
    
    