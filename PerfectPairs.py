# import copy
# from FindSolutions import *
# from TestingDisplay import *

# ''''
# Script to support advanced solve solutions. From https://www.sudokuoftheday.com/techniques/hidden-pairs-triples

# Candidate Lines: 

# Finding any numbers 0-9 that occur only on a single 3x3 row or column. Where 4 may only occur (exist in array) in 
# in positions (7,8) and (8,8). for the last 3x3 box. Any other 4s listed in arrays of column 7 would be ineligible.
# This is because of a natural limit set by the 4 being required in column 7 AND in the last box.


# Double Pairs: 


# Multiple Lines: 
# When searching across entire columns or rows of 3x3 sections, if a number is only available for 2/3 cols/rows 
# for two boxes, and the third box contains the number in multiple rows. The third box may eliminate any of that number
# from spaces that occupy the two rows/cols that are limited by the initial two boxxes. 

# Naked Pairs (easiest to program)

# If in any given 3x3, row , or column; if two numbers are listed as the only options for two boxes (1,5) (1,5).
# any other array in the 3x3, row or col that is SHARED by the matching pair can remove the associated numbers as
# options. The same can be done for triples (2,4) (4,7) (2,7)

# Hidden pair / triple

# if you have a pair (1,3) (1,2,3) in any 3x3, row,col and the 1 and 3 are not available elsewhere. The two can be 
# removed , as well as the 1,3 from the subsequent row/col/3x3 positions.


# '''


# # take a given grid that contains arrays for unsolved positions. Search for any pairs. Where in a single
# # row/ col / 3x3 grid two arrays contain two digits that are NOT in

# # also want to update any arrays as I go


# # only perfect pairs (1,5) (1,5)


# # - in most recent test: It found the perfect pair in the BOX first, rather than col. and it removed a number from
# # the second paired element. It didnt continue down the col, as it had skipped to box, and so missed removing two elements
# # from two seperate squares.
# def perfect_pairs(grid):
#     # start comparisons with first element.
#     #print(":::::::::::::::::::::::::::::::::::")
#     #print("STARTING PERFECT PAIRS TEST")
#     #print(":::::::::::::::::::::::::::::::::::")
#     for i in range(9):
#         for j in range(9):

#             if len(grid[i][j]) == 2: 
                
#                 #print("::::::::::::CURRENT ARRAY IS ", grid[i][j], "at location ", (i,j))
              

#                 first_array = grid[i][j]
                
#                 # check all of row for other pairs: 
#                 for col_ofrowcheck in range(9):
                    
#                     # only if the row array is a length of 2
#                     if len(grid[i][col_ofrowcheck]) == 2:  
#                         #print("Comparing first_arr to ", grid[i][col_ofrowcheck], "at ROW location ", (i,col_ofrowcheck))
                        
#                         pair_row = grid[i][col_ofrowcheck]
#                         # if the first arr and the position being searched are a match (and not the same location)
#                         if set(first_array) == set(pair_row) and (i, j) != (i, col_ofrowcheck):
#                             #print("PERFECT PAIR IS IN THE ROW")
                            
#                             # create array based on shared numbers.
           
#                             numbers_to_remove = first_array
                            
#                             #loop through ROW and check if any other arrays contain numbers from PAIR. 
#                             for r in range(9):
#                                 # Array to remove must be greater than 1 (not a solved square) and not either pair location. and STATEMENT.
#                                 if (i, r) != (i, j) and (i,r) != (i, col_ofrowcheck):
#                                     # for number in square array
#                                     for value in numbers_to_remove:
#                                         # print("checking" , n ,"in ", grid[i][r], "at ROW location ", (i,r))
#                                         if value in grid[i][r]:
#                                             #print(value, " needs to BE removed from  ", grid[i][r], "at ROW location ", (i,r))

#                                             grid[i][r].remove(value)
#                                             #print(value, "was removed from ", grid[i][r], "at ROW location ", (i,r))

#                 for row_ofcolcheck in range(9):
#                     #for each row of the current column: check only arrays of a length of two.
#                     pair_col = grid[row_ofcolcheck][j]
                    
#                     if len(pair_col) == 2:  
                        
                                                
#                         #print("comparing first_arr to ", pair_col, "at COL location ", (row_ofcolcheck,j))
#                         #if the search array matches the compared square array location is not the same as my current square:
#                         if set(first_array) == set(pair_col) and  (i,j) != (row_ofcolcheck,j):
                            
#                             #print("PERFECT PAIR in the COLUMN", pair_col, "at COL location", (row_ofcolcheck,j))
                            
#                             numbers_to_remove = first_array
                            
#                             # because there is a perfect pair, I will loop again to check all squares of the same COLUMN                            
#                             for r in range(9):
#                                 # If the length of my new search square is more than 1 (not a solved square), and is not the same location of either pair AND
#                                 if (r,j) != (i,j)  and  (r,j) != (row_ofcolcheck,j):
#                                     #look at each number in my new search array                                    
#                                     for value in first_array: 
                                        
#                                         #print("checking", value, " in ", grid[r][j], "at COL location ", (r,j))
                                        
#                                         if value in grid[r][j]:
#                                             #print(value, " needs to be removed from  ", grid[r][j], "at COL location ", (r,j))

#                                             grid[r][j].remove(value)
                                            
#                                             #print(value, "was removed from ", grid[r][j], "at COL location ", (r,j))
#                 box_start_row = i // 3
#                 box_start_col = j // 3

#                 for row_pos in range(box_start_row * 3, box_start_row * 3 + 3):
#                     for col_pos in range(box_start_col * 3, box_start_col * 3 + 3):
                        
#                         # for each element of my square, find one that only has two elements.
#                         if len(grid[row_pos][col_pos]) == 2:
                            
#                             # Create compare variable:
#                             pair_box = grid[row_pos][col_pos]
#                             # if compare and first_arr are the same NUMBERS, but NOT the same position:
#                             if first_array == pair_box and ( (i, j) != (row_pos, col_pos)):
                                
#                                # print("fount a perfect pair in the BOX ", pair_box,  "at location ",  (row_pos, col_pos))
                                
#                                 # I found a pair, now I want to search for any other numbers that are in remaining arrays.
#                                 numbers_to_remove = first_array
#                                 #print(numbers_to_remove, " are my numbers to remove that match my first array:", first_array)
                                
#                                 # search through box again.
#                                 for alt_box_row in range(box_start_row * 3, box_start_row * 3 + 3):
#                                     for alt_box_col in range(box_start_col * 3, box_start_col * 3 + 3):
                                        
#                                         box_square_to_remove = grid[alt_box_row][alt_box_col]
                                        
#                                         # look at squares with arrays greater than 1
#                                         if (alt_box_row, alt_box_col) != (i, j) and (alt_box_row, alt_box_col) != (row_pos, col_pos):
#                                             # look inside the array
#                                             for value in box_square_to_remove:
                                                
#                                                 #print("checking each number ", value, "in", box_square_to_remove, "at BOX location" ,(alt_box_row, alt_box_col))
                                                
#                                                 # if the number exists in my numbers to remove AND its NOT in the i,j position AND my second pair position:
#                                                 if value in numbers_to_remove:
                                                    
#                                                     #print(value, "Needs to be removed ", grid[alt_box_row][alt_box_col], "at BOX location", (alt_box_row, alt_box_col))
                                                    
#                                                     box_square_to_remove.remove(value)
                                                    
                                                    
#                                                     #print(value, "was removed from ", grid[alt_box_row][alt_box_col], "at location", (alt_box_row, alt_box_col))
                                                    
#     #basic_solve(grid)
#     return grid


# #print_updated_grid(pos_nums_grid)
# #test_test = basic_solve(pos_nums_grid)
# #original_test_test = copy.deepcopy(test_test)
# #hope  = perfect_pairs(test_test)

# #print("Printing HOPE")




# '''
# Additional Steps:







# '''



