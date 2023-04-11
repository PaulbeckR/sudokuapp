# from BuildPuzzle import *
# from PreparePuzzle import *
# from FindSolutions import *
# from CandidateLines import *
# from TestingDisplay import *


# '''
# Hidden pairs/triples are if only two/three numbers are available in a box row or col. Finding this can eliminate other options in the arrays of the pair, as well as any options for 

# that pair in the associated row/col. 


# lonely numbers but set to 2 nums in two squares of the same row/box col/box? 

# dictionaries, position / array to map through for

# '''

# '''
# Method to take each box/row /col to "set search parameter" 
#     1. Box - take given box start and search each of the 9 squares. 
#     2. Row - take given box start and search each of the 3 rows 
#     3. Col - take given box start and search each of teh 3 cols. 

# '''

# # grid_new = create_grid_fill()  
# # print(grid_new)

# # grid_game = new_game_board(grid_new)
# # arrays = create_arrays(grid_game)


# # basicsolved = basic_solve(arrays)

# # checkedlonlies, total_returned  = check_lonely_nums(basicsolved)




# #print(":::::::::::::::::::: GRID AFTER BASIC SOLVE :::::::::::::::::::::::::")
# #print_pos_grid(grid2)


# def get_iterations(dict):
#     iterations_set = set()
#     for i in dict:
#         for k in dict:
#             if i != k:
#                 iterations_set.add((i,k))
    
#    # print("Set of iters ", iterations_set)
        
#         #Create new with no doubles
#     iterations2 = set()   
#     for it in iterations_set:
#         for sec_it in iterations_set:
#                 #print("second it is ", sec_it)
#                 # print("positions of s it ", (sec_it[0], sec_it[1]))
#             if (it != sec_it) and ((sec_it[1], sec_it[0]) not in iterations2):
#                     #print("First IF not equal statement", it!= sec_it, "at ", it , "and ", sec_it)
#                     #print("Second if statement", ((it[0], it[1]) != (sec_it[1], sec_it[0])), "at ", it , "and ", sec_it)
#                     #iterations2.add(it)
#                 iterations2.add(sec_it)
#                     #print("iterations added ", sec_it, "to ", iterations2)
#         #print("Set of iters ", iterations_set)
#         #print("Iterations are: ", iterations2)
#     return iterations2

# # Dictionary using numbers (1-9) as Keys, positions as Values.

# # Returnes box_dict
# def box_dict(grid, box):
    
#     # Set starting row / col 
#     row_start = box[0] *3
#     col_start = box[1] *3 
    
#     row_end = row_start + 3
#     col_end = col_start + 3

#     box_dict = dict()
   
    
#     keys = []
#     for i in range(9):
#         i += 1
#         keys.append(i)

#     for i in keys:
#         #print("KEY CHECKED IS ", i)
        
#         bnum_positions = []
#         #Search each Square of the BOX
#         for row_square in range(row_start, row_end): 
#             for col_square in range(col_start, col_end):
#                 #print("square position is ", (row_square,col_square))
                
#                 # if the array is more than 1
#                 if len(grid[row_square][col_square]) > 1:
#                     #print("square array more than one")
                    
#                     for number in grid[row_square][col_square]:
#                         #print("number is , ", number)                    

#                         if number == i:
#                             #print("number == i")
#                             bnum_positions.append((row_square,col_square))        
#                             #print("added to dict at , " , i , "for position", (row_square, col_square))
                            
#         #Add that list of positions to the dictionary at the corresponding Key - i
#         box_dict[i] = bnum_positions
      
#     return box_dict

# # returns row_dict
# def row_dict (grid, row):
    
#     row_dict = dict()
   
    
#     #keys represent each number 1-9
#     keys = []
#     for i in range(9):
#         i += 1
#         keys.append(i)
    
           
#     line0 = dict()    
#     for k in keys: 
#         #print(" K IS ::::::::::", k)   
        
#         rnum_positions = []  
#         #for row in range(row_start, row_end):      
#         for col in range(9):
#             #print("ROW CHECK POSITION IS  ", (row,col))
#             if len(grid[row][col]) > 1:
#                 for number in grid[row][col]:
#                     if number == k:
#                         rnum_positions.append((row,col))
#                         #print("added to dict at , " , k , "for position", (row, col))
#         #line0[k] = rnum_positions
#         #print("Line0 is ", line0)
#         row_dict[k] = rnum_positions
#     return row_dict
        
# #returns col_dict
# def col_dict(grid, col):
    
#     col_dict = dict()
    
#     keys = []
#     for i in range(9):
#         i += 1
#         keys.append(i)
    
#     #for col in range(col_start, col_end):
   
#     for k in keys: 
#         #print(" K IS ::::::::::", k)   
        
#         cnum_positions = []  
#         #for row in range(row_start, row_end):
   
#         for row in range(9):
#             #print("ROW CHECK POSITION IS  ", (row,col))
#             if len(grid[row][col]) > 1:
#                 for number in grid[row][col]:
#                     if number == k:
#                         cnum_positions.append((row,col))
#                         #print("added to dict at , " , k , "for position", (row, col))
#         #line0[k] = cnum_positions
#         #print("Line0 is ", line0)
#         col_dict[k] = cnum_positions  
#     return col_dict
          
 
 
# # # TESTING HIDDEN SEARCH           
# # box_test = box_dict(grid, (0,0))
# # row_test = row_dict(grid, 0)
# # col_test = col_dict(grid, 0)


# # Reformat Dictionary: Use position as keys, array nums as Values
# # NOT USED 
# def position_dict(grid, box):
#     row_start = box[0] *3
#     col_start = box[1] *3 
    
#     row_end = row_start + 3
#     col_end = col_start + 3

#     box_dict = dict()
#     row_dict = dict()
#     col_dict = dict()
    
#     #Search through box.     
#     for r_square in range(row_start, row_end):
#         for c_square in range(row_start, row_end): 
#             # if the square holds more than one num:
#             if len(grid[r_square][c_square]) > 1:
#                 #set position as key
#                 position = (r_square, c_square)
#                 numbers_l = []
                
#                 for number in grid[r_square][c_square]:
#                     numbers_l.append(number)
                    
                
#                 box_dict[position] = numbers_l 
    
#     # Search Rows
#     for row in range(row_start, row_end):
#         row_num = dict()
#         for col in range(9):
#             if len(grid[row][col]) > 1:
#                 position = (row,col)
#                 numbers_list = []
#                 for number in grid[row][col]:
#                     numbers_list.append(number)
                
#                 row_num[position] = numbers_list
#                 #print("rownum", row_num)
#         row_dict[row] = row_num 
        
#     for col in range(col_start, col_end):
#         col_num = dict()
#         for row in range(9):
#             if len(grid[row][col]) > 1:
#                 position = (row,col)
#                 numbers_list = []
#                 for number in grid[row][col]:
#                     numbers_list.append(number)
                
#                 col_num[position] = numbers_list
#                 #print("rownum", row_num)
#         col_dict[col] = col_num 
        
    
    
#     return box_dict, row_dict, col_dict
          
# #box_test_pos , row_test_pos , col_test_pos= position_dict(grid, (0,0))   
# #print("box test 2: ", box_test_pos)  

# def print_box_dict(dict):
#     count = 0
#     for item in dict.items():
#         count += 1
#         if count % 3 == 0 and count != 0:
#             print("------------------------------------------")
#         print(item)



# def print_dict(dict):
    
#     for item in dict.items():
#         print("--------------------------------------------------------------------------")
#         print(item)
        




# ###### NOT USED 
# def hidden_pair(dict):
# # For each dict item of length
#     pair = dict()
#     for key1, value1 in dict.items():
     
#     # test all other items in dict to see if match: pair/trip
    
#         for key2, value2 in dict.items():
        
#         #cant be same ite
#             if key1 != key2:
            
#                 if len(value1) == 2 and len(value2) == 2 and set(value1) == set(value2):
#                     #print("matched ", key1, key2)
#                     pair[key1] = value1
#                     pair[key2] = value2 
#     return pair
    


# # test_paired = {1: [(0,1), (0,2), (0,3)], 2: [(0,1), (0,2), (0,5)], 3: [(0,7), (0,8)], 4: [(0,7), (0,8)]}

# #Returns dictionary of positions with numbers to remove from them.
# def hidden_pos_pair(current_dict):
#     #search through dict, if any numbers 1-9 only exist two times. get their positions. 
#     total_matches = 0
#     numbers_list = []
#     possible_match = dict()
    
#     paired_matches = dict()
    
#     for numbers, positions in current_dict.items():
#         # if a number only occurs in two positions           
#         if len(positions) == 2 :
#             #it is a possible match
#             possible_match[numbers] = positions
#            # print("possible_match", possible_match)
#     #print("Number OF Possible Pairs:  ", len(possible_match))
     
#     #Must have more than one possible match for a pair. May have two pairs... 
#     if len(possible_match) > 1:
#         # Check all key value pairs in my matches
        
#         for key, value in possible_match.items():
            
#             for key1, value1 in possible_match.items():
#                 if key != key1:
#                     #print("keys are ", key , key1)
                    
#                     if set(value1) == set(value):                        
#                         num_list = []
                        
#                         num_list.append(key)
#                         num_list.append(key1)
#                         numbers_list = num_list
#                         #print("num list " , num_list)
#                         for item in value:
#                            # print(item, "item")
#                             paired_matches[item] = num_list
#                         #print("Paired matches", paired_matches)
#                             total_matches += 1
                    
                
#     return numbers_list, paired_matches

# # numbers_list, test_p = hidden_pos_pair(test_paired)
# # print(test_p, "Test P")


# # this will only take the first set of positions from pairedmatches[0]                       
# def remove_numbers(num_list, paired_matches):
#     pos_not_nums = dict() 
#     not_nums = []
   
#     matched = dict()
#     for k in range(9):
#         k += 1
#         if k not in num_list:
#             not_nums.append(k)
                                         
#     for item in paired_matches[0]:
#         # adds to dictionary the positions that have numbers to be removed/ if any
        
#         pos_not_nums[item] = not_nums
#         matched[item] = num_list
#         #print("New dictionary with nums to remove by position: " , pos_not_nums)  
     
#     #print("My matched ", matched)
#     return pos_not_nums , matched
                 
    
# #hidden_pos_pair(test_hidden). 
# test_hidden = {1 : [(0,0),(0,1), (0,2)], 
#                2:[(0,0), (0,1)], 
#                3:[(0,0), (0,1) ,(0,2)], 
#                4: [(0,0), (0,5), (0,6), (0,7) ], 
#                5: [], 
#                6: [(0,0), (0,3), (0,4),(0,6),(0,8)],
#                7 : [(0,4), (0,5), (0,6), (0,8)], 
#                8:[(0,4), (0,5), (0,7)], 
#                9: [(0,1),(0,4), (0,7)]}

# #Takes dict_num (a dictionary) and returns pos_not_nums_dict
# def hidden_trip(dict_num):
    
#     total_matches = 0

#     possible_match = dict()
#     for numbers, positions in dict_num.items():
                   
#         if len(positions) > 1 and len(positions) < 4:
#             possible_match[numbers] = positions
    
#    # print("possible match ", possible_match)
    
#     length_matches = len(possible_match)

#     iterations2 = get_iterations(possible_match)
    
#     triples = dict()
#     pos_not_nums_dict = dict()

#     if length_matches == 3:
#         #print(" There are 3 matches ")
        
#         num_list = []
#         position_set = set()
        
#         for value in possible_match.values():
#             position_set.update(value)
            
#         if len(position_set) == 3:
#             #Found a triple! All three nums match in three places only. 
#             for key in possible_match.keys():
#                 num_list.append(key)
            
#             #now create a not numbers list, based on the num_list    
#             #not_nums = []
            
#             # for k in range(9):
#             #     k += 1
#             #     if k not in num_list:
#             #         not_nums.append(k)
                    
#             for i in position_set:
#                 pos_not_nums_dict[i] = num_list
#                 total_matches += 1
#         #print("Triple exists in positions: ", pos_not_nums_dict)
                
          

#     elif length_matches > 3:
#         #print("Possible matches are more than or equal to 3")
#         # I have ITERATIONS, that control which numbers (keys) are checked from possible_matches. 
#         position_set = set()
#         triple_dict = dict()
        
#         for comb in iterations2:
#            # print("Comb is ", comb)
#             key1 = comb[0]
#            # print("Key1 is ", key1)
#             key2 = comb[1]
#            # print("Key2 is ", key2)
#             position_set.update(possible_match[key1])
#             position_set.update(possible_match[key2])
#             num_list = []
#             #print("position_set is ", position_set)
#            # print("position set is ", position_set)
            
#             # if the length is less than or equal to three, and WHILE it remains that way. 
#             if len(position_set) <= 3:
#                 #print("Less thant or equal to three positions")
                
#                 num_list.append(key1)
#                 num_list.append(key2)
#                 for key3, value in possible_match.items():
#                     #print("key 3 is ", key3)
#                     if key3 != key1 and key3!= key2:
#                         position_set.update(value)
#                        # print("Updated position set after key3", position_set)
                        
#                         if len(position_set) <= 3:
#                             #found a triple!
#                             not_nums = []
#                             num_list.append(key3)
#                             #print("NUM list is ", num_list)
            
#                             # for k in range(9):
#                             #     k += 1
#                             #     if k not in num_list:
#                             #         not_nums.append(k)
#                             #print("not nums are ", not_nums)
                    
#                             for i in position_set:
#                                 pos_not_nums_dict[i] = num_list
#                                 total_matches += 1
                                
#         #print("pos_not_nums_dict is ", pos_not_nums_dict)
 
#     return pos_not_nums_dict, total_matches











# #hidden_trip(test_hidden)

# # removes any numbers from not nums at the positions in set_positions
# def remove_extra (grid, paired_matches):
#     count = 0
#     remove_hidden_dict = dict()
#     #For each position of dict, and numbers to remove;
#     for position, paired_numbers in paired_matches.items():
#         #print("position", position)
#         #look for each number in the given position
#         for number in grid[position[0]][position[1]]:
        
#             if number not in paired_numbers:
#                 #remove it
#                 grid[position[0]][position[1]].remove(number)
                
#                 #print(number, "HIDDEN was removed from", (position[0], position[1]), grid[position[0]][position[1]])
#                 remove_hidden_dict[position] = number
                
#                 count += 1
#     #print("removed # of nums ", count)
#     # if len(remove_hidden_dict) > 0 :
#     #     print("HIDDEN Remove Dict: ")
#     #     print(remove_hidden_dict) 
#     #     print("Total removed: ", count)           
#     return grid, count
                

# def gen_hidden_loop(grid):
#     total_matches = 0
#     remove_count = 0 
#     grid = grid
#     for row in range(3):
#         for col in range(3):
            
#             # box starting coords 
#             box = (row,col)
#             #print(":::::::::::::::::: NEW BOX :::::::::::::::::")
#             #print("----------------", box , "-------------------------")
#             dictb = box_dict(grid, box)
#             #print("For BOX ", box, "the dict it ", dict)
#             num_list, paired_matches =  hidden_pos_pair(dictb)
#             pairs = len(num_list) //2
            
            
#              # print("REMOVING PAIRS")           
#             grid,count = remove_extra(grid, paired_matches)
#             # if count > 0:
#             #     print("PAIRS IN BOX: ", num_list, "at", paired_matches)
#             #     print("# removed from PAIR", count)
                
            
#             remove_trip_dict, match_count2 = hidden_trip(box_dict(grid,box))

           
#            # print("REMOVING TRIPS")
#             grid,count2 = remove_extra(grid, remove_trip_dict)
#             # if count2 > 0:
#             #     print(" TRIP Numbers to remove by position:  ", remove_trip_dict)
#             #     print("removed # of nums from doub TRIP", count2)
            
#             remove_count += count
#             total_matches += ( pairs + match_count2)
           
#     for row in range(9):
#         #print(":::::::::::::::::: NEW ROW :::::::::::::::::")
#         #print("----------------", row , "-------------------------")
#         dictr = row_dict(grid, row)
#         #print("For Row ", row, "the dict it ", dict)
#         num_list, paired_matches = hidden_pos_pair(dictr)
#         pairs = len(num_list) //2
       
        
#         grid, count = remove_extra(grid, paired_matches)
#         # if count > 0:
#         #     print("PAIRS IN ROW: ", num_list, "at", paired_matches)
#         #     print("# removed from pair", count)
        
        
#         remove_trip_dict, match_count2 = hidden_trip(row_dict(grid, row))

#         grid,count2 = remove_extra(grid, remove_trip_dict)
#         # if count2 > 0:
#         #     print(" ROW TRIP: DICT  ", remove_trip_dict)
#         #     print("# removed from TRIP", count2)
       
       
#         remove_count += count
#         remove_count += count2
#         total_matches += ( pairs + match_count2)
        
#     for col in range(9):
#         #print(":::::::::::::::::: NEW COL :::::::::::::::::")
#         #print("----------------", col , "-------------------------")
#         dictc = col_dict(grid, col)
#         #print("For COL ", col, "the dict it ", dict)
#         num_list , paired_matches = hidden_pos_pair(dictc)
#         pairs = len(num_list) //2
        
        
        
#         grid,count = remove_extra(grid, paired_matches)
#         # if count > 0:
#         #     print("PAIRS IN COL", num_list, "at", paired_matches)
#         #     print("# removed from pair", count)
       
#         remove_trip_dict, match_count2 = hidden_trip(col_dict(grid,col))
       
#         grid,count2 = remove_extra(grid, remove_trip_dict)
        
#         # if count2 > 0:
#         #     print(" TRIP IN COL: DICT ", remove_trip_dict)
#         #     print("# removed from TRIP ", count2)
            
#         remove_count += count
#         remove_count += count2
#         total_matches += (pairs + match_count2)
    
#     #print("TOTAL REMOVED ", remove_count)
#     #print("Total MATCHES ", total_matches)
        
#     return grid , remove_count
           
# # This is based off of the pairs being in the same row         
# # def find_double_pairs(grid):
    
# #     for box_row in range(3):
# #         for box_col in range(3):
# #             box = (box_row,box_col)
            
# #             boxd = box_dict(grid, box)
# #             num_list, dict_positions =  hidden_pos_pair(boxd)
# #             # dict_positions already returns a pair in a box, (should) not return a single square of len=2
# #             print("dict_positions ", dict_positions)
# #             for position , numbers in dict_positions.items():
# #                 # key = (0,0)
# #                 # value = [1,2]
# #                 #if type(pos_list) is not list: pos_list = [pos_list]
# #                 print("key is ", key)
# #                 print("value is ", value)
               
                
# #                 row1, col1 = position[0]+box_row, numbers[1]+box_col
# #                 row2, col2 = position[1][0]+box_row, numbers[1][1]+box_col

# #                 if row1 == row2:
# #                     for col in range(9):
# #                         if col not in (col1, col2) and (numbers ==  grid[row1][col]):
# #                             return True
# #                 elif col1 == col2: 
# #                     for row in range(9):
# #                         if row not in (row1, row2) and (numbers == grid[row][col1]):
# #                             return True
# #     return False



# # def hidden_pairs(unit):
# #     """
# #     Finds hidden pairs in a row, column, or box of a Sudoku grid.
# #     Returns a dictionary of the form {num: [pos_list]} for all hidden pairs found.
# #     """
# #     # Create a dictionary to keep track of possible positions for each number
# #     pos_dict = {num: [] for num in range(1, 10)}
# #     for row, cells in enumerate(unit):
# #         for col, cell in enumerate(cells):
# #             if cell == 0:
# #                 for num in range(1, 10):
# #                     if num not in unit[row] and num not in [unit[i][col] for i in range(9)] and num not in box_values(unit, row, col):
# #                         pos_dict[num].append((row, col))
    
# #     # Find hidden pairs in the pos_dict
# #     hidden_pairs = {}
# #     for num, pos_list in pos_dict.items():
# #         if len(pos_list) == 2:
# #             if pos_list[0][0] == pos_list[1][0] or pos_list[0][1] == pos_list[1][1]:
# #                 hidden_pairs[num] = pos_list
                
# #     return hidden_pairs
    

# # def box_values(grid, row, col):
# #     """
# #     Returns the set of values in the box containing the given position in the Sudoku grid.
# #     """
# #     row_offset = (row // 3) * 3
# #     col_offset = (col // 3) * 3
# #     values = set()
# #     for i in range(row_offset, row_offset+3):
# #         for j in range(col_offset, col_offset+3):
# #             values.add(grid[i][j])
# #     return values

# #testing = gen_hidden_loop(grid2)


# #print_pos_grid(testing)

# def double_pair (grid):
#     print("::::::::::::::START OF DOUBLE PAIR :::::")
#     double_pair_count = 0
    
#    # print_pos_grid(grid)
#     doub_pairs = dict()
    
#     #Call function to remove any extra numbers from arrays 

#     # Find a double pair in a box 
#     for row in range(3):
#         for col in range(3):
            
#             # box starting coords  
#             box = (row,col)
#             #print("-------------------------------------------------------------------------")
#             #print(" ::::::::::::::::::::::::::: Current Box ", box, ":::::::::::::::::::::::::::")
#             #print("---------------------------------------------------------------------------------:")
          
#             #Get dictionary of box items
#             box_d = box_dict(grid, box)
           
           
#             #list of nums with their positions if there are only two listed positions and numlist whos numbers match
#             num_list, paired_matches = hidden_pos_pair(box_d)
#             #print("Paired matches are ", paired_matches)
#             # if the length of  my matches is more than 1:
   
#             for box1_pos1, box1_p1vals in paired_matches.items():
#                 #print("b1p1: ", box1_pos1, "row: ", box1_pos1[0], "col: ", box1_pos1[1], "VALS: ", box1_p1vals)
                
#                 for box1_pos2, box1_p2vals in paired_matches.items():
#                     #print("b1p2: ", box1_pos2, "row: ", box1_pos2[0], "col: ", box1_pos2[1], "VALS: ", box1_p2vals)
#                     #print("Checking Key and Key1", key, key1, "Same positions?")
                    
#                     # if the key's dont match but the values do: (will get only pairs)
#                     if (box1_pos1 != box1_pos2) and (set(box1_p1vals) == set(box1_p2vals)):
                     
#                        # print("Found 1  pair in a box: " , box)
                        
                                
#                         # If keys not in same column, check columns  
#                         if box1_pos1[1] != box1_pos2[1]:
                            
                          
                                      
#                             # Start with first position
#                             col1 = col_dict(grid, box1_pos1[1])
#                             #print("COL DICT is ", col1)
                            
#                             # get any hidden pairs of the column. 
#                             col_num_list, col_pairs = hidden_pos_pair(col1)  
#                             #print("Col PAIRS are ", col_pairs)  
#                             # Check to see if the pairs found are from my initial position.
    
#                             for col_position, col_values in col_pairs.items():
#                                 #print("col_position: ", col_position, "row: ", col_position[0], "col: ", col_position[1], "VALS: ", col_values)
                                
#                                 #Check if match of values. If in same row = same position, and not a match.
#                                 if (set(col_values) == set(box1_p1vals)) and (col_position[0] != box1_pos1[0]):
                                    
                                    
#                                     #print("found a pair match in one cols", box1_pos1 , col_position)
                                    
#                                     # get box of col_position
#                                     col_pair1_box = (col_position[0]//3, col_position[1]//3)
                                    
#                                     #check col of second square in pair
#                                     col2 = col_dict(grid, box1_pos2[1])
#                                     col2_list, col_pairs2 = hidden_pos_pair(col2)
#                                     #print("Checking col2", col2, "col_pairs2 are", col_pairs2)
                                    
#                                     #check if second column hols match for box1_pos2
#                                     for col_position2, col_values2 in col_pairs2.items():
#                                         if (set(col_values2) == set(box1_p1vals)) and (col_position2[0] != box1_pos2[0]):
#                                             #print("found a match for second col ", col_position2)
#                                             doub_pairs[box1_pos1] = box1_p1vals
#                                             doub_pairs[box1_pos2] = box1_p2vals
#                                             doub_pairs[col_position] = col_values
#                                             doub_pairs[col_position2] = col_values2
#                                             #if it is a match, check the box. 
#                                             col_pair2_box = (col_position2[0]//3, col_position[1]//3)

#                                             if col_pair2_box == col_pair1_box:
                                       
#                                                 #print("found a match for " , col_position2[0], box1_pos1[0] , " and", col_position2[1] , box1_pos2[1] )
#                                                 double_pair_count +=1
#                                             #print("no second match in cols")
#                                 # else:
#                                 #     print("No match found in first col")
#                                 #     break
#                         # if the box pairs do not share the same ROW, check the rows: 
#                         if box1_pos1[0] != box1_pos2[0]:
#                             #print("NOT same row, check boxes in row")
                                
#                             row1 = row_dict(grid, box1_pos1[0])
#                             #print("New Row DICT ", row1)
#                             row_num_list, row_pairs = hidden_pos_pair(row1)
#                             #print("ANY ROW MATCHES", row_pairs)
#                                     #going to check both anyway
#                             for row_position, row_value in row_pairs.items():
                                
#                                 if (set(row_value) == set(box1_p1vals)) and (row_position != box1_pos1):
#                                     #print("found a pair match in one row at value2_row," , row_position, "and value", box1_p1vals)
                                    
#                                     # get box of col_position
#                                     row_pair1_box = (row_position[0]//3, row_position[1]//3)
                                    
#                                     #check ROW of second square in pair
#                                     row2 = row_dict(grid, box1_pos2[0])
#                                     row2_list, row_pairs2 = hidden_pos_pair(row2)
#                                     #print("checking second row ", row2)
                                    
#                                     #if there is a pair found in the same row of the column match, and same column of the second square pair, found a match
#                                     for row_position2, row_values2 in row_pairs2.items():
                                        
#                                         if (set(row_values2) == set(box1_p1vals)) and (row_position2[1] != box1_pos2[1]):
#                                             #print("found a match in second row", row_position2)
#                                             doub_pairs[box1_pos1] = box1_p1vals
#                                             doub_pairs[box1_pos2] = box1_p2vals
#                                             doub_pairs[row_position] = row_value
#                                             doub_pairs[row_position2] = row_values2
#                                             #if it is a match, check the box. 
#                                             row_pair2_box = (row_position2[0]//3, row_position[1]//3)

#                                             if row_pair2_box == row_pair1_box:
#                                                # print("boxes are the same,", row_pair2_box, row_pair1_box)
                                       
#                                                 #print("found a match for " , row_position2[1], box1_pos2[1] , " and", row_position2[1] , box1_pos2[1] )
#                                                 double_pair_count +=1
#                                                # print("count is ", double_pair_count)
#                                            # print("no second match")
#                                 # else:
#                                 #     print("No match for first key check, stop checking")
#                                 #     break
                                            
#                         # else:
#                         #   #  print("Not in same row/col, continue")
#                         #     continue
                          
#                     #print("SET VALUES DID NOT MATCH")
#    # print("FINAL Count of Double PAIRS ", double_pair_count)  
#     return double_pair_count , doub_pairs
    
    
  
    
# # If double pair is not 0 , the board is not unique
                            
# # hiddenchecked = gen_hidden_loop(checkedlonlies)
# # test2 = basic_solve(hiddenchecked)
# # # count, test3 = check_lonely_nums(test2)
# # # test4 = basic_solve(test3)

# # print_pos_grid(hiddenchecked)

# # double = double_pair(test2)



# # print(" MY DOUBLE" , double)

# # array_display(hiddenchecked, "Find Doubles")

# #bs2 = basic_solve(hiddenchecked)
# # cl2 , count = check_lonely_nums(bs2)

# # array_display(cl2, "Final")

                
                
                
                        
                
            
            
           
            
            
          
                



             
    

        






        
        

    












