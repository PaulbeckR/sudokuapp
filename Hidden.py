#from BuildPuzzle import *
from PreparePuzzle import *
from FindSolutions import *
from CandidateLines import *


'''
Hidden pairs/triples are if only two/three numbers are available in a box row or col. Finding this can eliminate other options in the arrays of the pair, as well as any options for 

that pair in the associated row/col. 


lonely numbers but set to 2 nums in two squares of the same row/box col/box? 

dictionaries, position / array to map through for

'''

'''
Method to take each box/row /col to "set search parameter" 
    1. Box - take given box start and search each of the 9 squares. 
    2. Row - take given box start and search each of the 3 rows 
    3. Col - take given box start and search each of teh 3 cols. 

'''


def get_iterations(dict):
    iterations_set = set()
    for i in dict:
        for k in dict:
            if i != k:
                iterations_set.add((i,k))
        
        #Create new with no doubles
    iterations2 = set()   
    for it in iterations_set:
        for sec_it in iterations_set:

            if (it != sec_it) and ((sec_it[1], sec_it[0]) not in iterations2):
                iterations2.add(sec_it)

    return iterations2

# Dictionary using numbers (1-9) as Keys, positions as Values.

# Returnes box_dict
def box_dict(grid, box):
    
    # Set starting row / col 
    row_start = box[0] *3
    col_start = box[1] *3 
    
    row_end = row_start + 3
    col_end = col_start + 3

    box_dict = dict()
   
    
    keys = []
    for i in range(9):
        i += 1
        keys.append(i)

    for i in keys:
        #print("KEY CHECKED IS ", i)
        
        bnum_positions = []
        #Search each Square of the BOX
        for row_square in range(row_start, row_end): 
            for col_square in range(col_start, col_end):                
                # if the array is more than 1
                if len(grid[row_square][col_square]) > 1:
                    
                    for number in grid[row_square][col_square]:
                        if number == i:
                            bnum_positions.append((row_square,col_square))        
                            
        #Add that list of positions to the dictionary at the corresponding Key - i
        box_dict[i] = bnum_positions
      
    return box_dict

# returns row_dict
def row_dict (grid, row):
    
    row_dict = dict()

    #keys represent each number 1-9
    keys = []
    for i in range(9):
        i += 1
        keys.append(i)
    
           
    line0 = dict()    
    for k in keys: 
        
        rnum_positions = []  
        #for row in range(row_start, row_end):      
        for col in range(9):
            if len(grid[row][col]) > 1:
                for number in grid[row][col]:
                    if number == k:
                        rnum_positions.append((row,col))

        row_dict[k] = rnum_positions
    return row_dict
        
#returns col_dict
def col_dict(grid, col):
    
    col_dict = dict()
    
    keys = []
    for i in range(9):
        i += 1
        keys.append(i)
    
    #for col in range(col_start, col_end):
   
    for k in keys:         
        cnum_positions = []  
        #for row in range(row_start, row_end):
   
        for row in range(9):
            if len(grid[row][col]) > 1:
                for number in grid[row][col]:
                    if number == k:
                        cnum_positions.append((row,col))

        col_dict[k] = cnum_positions  
    return col_dict



# Reformat Dictionary: Use position as keys, array nums as Values
# NOT USED 
def position_dict(grid, box):
    row_start = box[0] *3
    col_start = box[1] *3 
    
    row_end = row_start + 3
    col_end = col_start + 3

    box_dict = dict()
    row_dict = dict()
    col_dict = dict()
    
    #Search through box.     
    for r_square in range(row_start, row_end):
        for c_square in range(row_start, row_end): 
            # if the square holds more than one num:
            if len(grid[r_square][c_square]) > 1:
                #set position as key
                position = (r_square, c_square)
                numbers_l = []
                
                for number in grid[r_square][c_square]:
                    numbers_l.append(number)
                    
                
                box_dict[position] = numbers_l 
    
    # Search Rows
    for row in range(row_start, row_end):
        row_num = dict()
        for col in range(9):
            if len(grid[row][col]) > 1:
                position = (row,col)
                numbers_list = []
                for number in grid[row][col]:
                    numbers_list.append(number)
                
                row_num[position] = numbers_list
        row_dict[row] = row_num 
        
    for col in range(col_start, col_end):
        col_num = dict()
        for row in range(9):
            if len(grid[row][col]) > 1:
                position = (row,col)
                numbers_list = []
                for number in grid[row][col]:
                    numbers_list.append(number)
                
                col_num[position] = numbers_list
        col_dict[col] = col_num 
        
    
    
    return box_dict, row_dict, col_dict
          

def print_box_dict(dict):
    count = 0
    for item in dict.items():
        count += 1
        if count % 3 == 0 and count != 0:
            print("------------------------------------------")
        print(item)



def print_dict(dict):
    
    for item in dict.items():
        print("--------------------------------------------------------------------------")
        print(item)
        




###### NOT USED 
def hidden_pair(dict):
# For each dict item of length
    pair = dict()
    for key1, value1 in dict.items():
     
    # test all other items in dict to see if match: pair/trip
    
        for key2, value2 in dict.items():
        
        #cant be same ite
            if key1 != key2:
            
                if len(value1) == 2 and len(value2) == 2 and set(value1) == set(value2):
                    #print("matched ", key1, key2)
                    pair[key1] = value1
                    pair[key2] = value2 
    return pair
    


# test_paired = {1: [(0,1), (0,2), (0,3)], 2: [(0,1), (0,2), (0,5)], 3: [(0,7), (0,8)], 4: [(0,7), (0,8)]}

#Returns dictionary of positions with numbers to remove from them.
def hidden_pos_pair(current_dict):
    #search through dict, if any numbers 1-9 only exist two times. get their positions. 
    total_matches = 0
    numbers_list = []
    possible_match = dict()
    
    paired_matches = dict()
    
    for numbers, positions in current_dict.items():
        # if a number only occurs in two positions           
        if len(positions) == 2 :
            #it is a possible match
            possible_match[numbers] = positions

     
    #Must have more than one possible match for a pair. May have two pairs... 
    if len(possible_match) > 1:
        # Check all key value pairs in my matches
        
        for key, value in possible_match.items():
            
            for key1, value1 in possible_match.items():
                if key != key1:
                    
                    if set(value1) == set(value):                        
                        num_list = []
                        
                        num_list.append(key)
                        num_list.append(key1)
                        numbers_list = num_list
                        for item in value:
                            paired_matches[item] = num_list
                            total_matches += 1
                    
                
    return numbers_list, paired_matches



# this will only take the first set of positions from pairedmatches[0]                       
def remove_numbers(num_list, paired_matches):
    pos_not_nums = dict() 
    not_nums = []
   
    matched = dict()
    for k in range(9):
        k += 1
        if k not in num_list:
            not_nums.append(k)
                                         
    for item in paired_matches[0]:
        # adds to dictionary the positions that have numbers to be removed/ if any
        
        pos_not_nums[item] = not_nums
        matched[item] = num_list
     
    return pos_not_nums , matched
                 
    
#hidden_pos_pair(test_hidden). 
test_hidden = {1 : [(0,0),(0,1), (0,2)], 
               2:[(0,0), (0,1)], 
               3:[(0,0), (0,1) ,(0,2)], 
               4: [(0,0), (0,5), (0,6), (0,7) ], 
               5: [], 
               6: [(0,0), (0,3), (0,4),(0,6),(0,8)],
               7 : [(0,4), (0,5), (0,6), (0,8)], 
               8:[(0,4), (0,5), (0,7)], 
               9: [(0,1),(0,4), (0,7)]}

#Takes dict_num (a dictionary) and returns pos_not_nums_dict
def hidden_trip(dict_num):
    
    total_matches = 0
    possible_match = dict()
    for numbers, positions in dict_num.items():
                   
        if len(positions) > 1 and len(positions) < 4:
            possible_match[numbers] = positions
    
    length_matches = len(possible_match)
    iterations2 = get_iterations(possible_match)

    pos_not_nums_dict = dict()

    if length_matches == 3:
        
        num_list = []
        position_set = set()
        
        for value in possible_match.values():
            position_set.update(value)
            
        if len(position_set) == 3:
            #Found a triple! All three nums match in three places only. 
            for key in possible_match.keys():
                num_list.append(key)

            for i in position_set:
                pos_not_nums_dict[i] = num_list
                total_matches += 1     

    elif length_matches > 3:
        # I have ITERATIONS, that control which numbers (keys) are checked from possible_matches. 
        position_set = set()
        triple_dict = dict()
        
        for comb in iterations2:
            key1 = comb[0]
            key2 = comb[1]
            position_set.update(possible_match[key1])
            position_set.update(possible_match[key2])
            num_list = []

            # if the length is less than or equal to three, and WHILE it remains that way. 
            if len(position_set) <= 3:
                
                num_list.append(key1)
                num_list.append(key2)
                for key3, value in possible_match.items():
                    if key3 != key1 and key3!= key2:
                        position_set.update(value)
                        
                        if len(position_set) <= 3:
                            #found a triple!
                            not_nums = []
                            num_list.append(key3)
            
                            for i in position_set:
                                pos_not_nums_dict[i] = num_list
                                total_matches += 1
                                 
    return pos_not_nums_dict, total_matches



# removes any numbers from not nums at the positions in set_positions
def remove_extra (grid, paired_matches):
    count = 0
    remove_hidden_dict = dict()
    #For each position of dict, and numbers to remove;
    for position, paired_numbers in paired_matches.items():
        #look for each number in the given position
        for number in grid[position[0]][position[1]]:
            if number not in paired_numbers:

                grid[position[0]][position[1]].remove(number)
                remove_hidden_dict[position] = number
                count += 1
         
    return grid, count
                

def gen_hidden_loop(grid):
    total_matches = 0
    remove_count = 0 
    grid = grid
    for row in range(3):
        for col in range(3):
            
            # box starting coords 
            box = (row,col)

            dictb = box_dict(grid, box)
            num_list, paired_matches =  hidden_pos_pair(dictb)
            pairs = len(num_list) //2
             
            grid,count = remove_extra(grid, paired_matches) 
            remove_trip_dict, match_count2 = hidden_trip(box_dict(grid,box))
            grid,count2 = remove_extra(grid, remove_trip_dict)
            
            remove_count += count
            total_matches += ( pairs + match_count2)
           
    for row in range(9):

        dictr = row_dict(grid, row)
        num_list, paired_matches = hidden_pos_pair(dictr)
        pairs = len(num_list) //2
        grid, count = remove_extra(grid, paired_matches)
        remove_trip_dict, match_count2 = hidden_trip(row_dict(grid, row))

        grid,count2 = remove_extra(grid, remove_trip_dict)
       
        remove_count += count
        remove_count += count2
        total_matches += ( pairs + match_count2)
        
    for col in range(9):

        dictc = col_dict(grid, col)
        num_list , paired_matches = hidden_pos_pair(dictc)
        pairs = len(num_list) //2
        
        
        
        grid,count = remove_extra(grid, paired_matches)
        remove_trip_dict, match_count2 = hidden_trip(col_dict(grid,col))
        grid,count2 = remove_extra(grid, remove_trip_dict)
            
        remove_count += count
        remove_count += count2
        total_matches += (pairs + match_count2)
        
    return grid , remove_count
           
# This is based off of the pairs being in the same row         
# def find_double_pairs(grid):
    
#     for box_row in range(3):
#         for box_col in range(3):
#             box = (box_row,box_col)
            
#             boxd = box_dict(grid, box)
#             num_list, dict_positions =  hidden_pos_pair(boxd)
#             # dict_positions already returns a pair in a box, (should) not return a single square of len=2
#             print("dict_positions ", dict_positions)
#             for position , numbers in dict_positions.items():
#                 # key = (0,0)
#                 # value = [1,2]
#                 #if type(pos_list) is not list: pos_list = [pos_list]
#                 print("key is ", key)
#                 print("value is ", value)
               
                
#                 row1, col1 = position[0]+box_row, numbers[1]+box_col
#                 row2, col2 = position[1][0]+box_row, numbers[1][1]+box_col

#                 if row1 == row2:
#                     for col in range(9):
#                         if col not in (col1, col2) and (numbers ==  grid[row1][col]):
#                             return True
#                 elif col1 == col2: 
#                     for row in range(9):
#                         if row not in (row1, row2) and (numbers == grid[row][col1]):
#                             return True
#     return False



# def hidden_pairs(unit):
#     """
#     Finds hidden pairs in a row, column, or box of a Sudoku grid.
#     Returns a dictionary of the form {num: [pos_list]} for all hidden pairs found.
#     """
#     # Create a dictionary to keep track of possible positions for each number
#     pos_dict = {num: [] for num in range(1, 10)}
#     for row, cells in enumerate(unit):
#         for col, cell in enumerate(cells):
#             if cell == 0:
#                 for num in range(1, 10):
#                     if num not in unit[row] and num not in [unit[i][col] for i in range(9)] and num not in box_values(unit, row, col):
#                         pos_dict[num].append((row, col))
    
#     # Find hidden pairs in the pos_dict
#     hidden_pairs = {}
#     for num, pos_list in pos_dict.items():
#         if len(pos_list) == 2:
#             if pos_list[0][0] == pos_list[1][0] or pos_list[0][1] == pos_list[1][1]:
#                 hidden_pairs[num] = pos_list
                
#     return hidden_pairs
    



def double_pair (grid):

    double_pair_count = 0
    
    doub_pairs = dict()
    
    #Call function to remove any extra numbers from arrays 

    # Find a double pair in a box 
    for row in range(3):
        for col in range(3):
            
            # box starting coords  
            box = (row,col)      
            #Get dictionary of box items
            box_d = box_dict(grid, box)
           
           
            #list of nums with their positions if there are only two listed positions and numlist whos numbers match
            num_list, paired_matches = hidden_pos_pair(box_d)
            # if the length of  my matches is more than 1:
   
            for box1_pos1, box1_p1vals in paired_matches.items():                
                for box1_pos2, box1_p2vals in paired_matches.items():

                    
                    # if the key's dont match but the values do: (will get only pairs)
                    if (box1_pos1 != box1_pos2) and (set(box1_p1vals) == set(box1_p2vals)):

                        # If keys not in same column, check columns  
                        if box1_pos1[1] != box1_pos2[1]:          
                            # Start with first position
                            col1 = col_dict(grid, box1_pos1[1])
                            
                            # get any hidden pairs of the column. 
                            col_num_list, col_pairs = hidden_pos_pair(col1)  
                            # Check to see if the pairs found are from my initial position.
    
                            for col_position, col_values in col_pairs.items():
                                
                                #Check if match of values. If in same row = same position, and not a match.
                                if (set(col_values) == set(box1_p1vals)) and (col_position[0] != box1_pos1[0]):
                                    # get box of col_position
                                    col_pair1_box = (col_position[0]//3, col_position[1]//3)
                                    
                                    #check col of second square in pair
                                    col2 = col_dict(grid, box1_pos2[1])
                                    col2_list, col_pairs2 = hidden_pos_pair(col2)
                                    
                                    #check if second column hols match for box1_pos2
                                    for col_position2, col_values2 in col_pairs2.items():
                                        if (set(col_values2) == set(box1_p1vals)) and (col_position2[0] != box1_pos2[0]):
                                            doub_pairs[box1_pos1] = box1_p1vals
                                            doub_pairs[box1_pos2] = box1_p2vals
                                            doub_pairs[col_position] = col_values
                                            doub_pairs[col_position2] = col_values2
                                            #if it is a match, check the box. 
                                            col_pair2_box = (col_position2[0]//3, col_position[1]//3)

                                            if col_pair2_box == col_pair1_box:                                       
                                                double_pair_count +=1
                                            
                        # if the box pairs do not share the same ROW, check the rows: 
                        if box1_pos1[0] != box1_pos2[0]:
                                
                            row1 = row_dict(grid, box1_pos1[0])
                            row_num_list, row_pairs = hidden_pos_pair(row1)
                                    #going to check both anyway
                            for row_position, row_value in row_pairs.items():
                                if (set(row_value) == set(box1_p1vals)) and (row_position != box1_pos1):
                                    
                                    # get box of col_position
                                    row_pair1_box = (row_position[0]//3, row_position[1]//3)
                                    
                                    #check ROW of second square in pair
                                    row2 = row_dict(grid, box1_pos2[0])
                                    row2_list, row_pairs2 = hidden_pos_pair(row2)
                                    
                                    #if there is a pair found in the same row of the column match, and same column of the second square pair, found a match
                                    for row_position2, row_values2 in row_pairs2.items():
                                        
                                        if (set(row_values2) == set(box1_p1vals)) and (row_position2[1] != box1_pos2[1]):
                                            doub_pairs[box1_pos1] = box1_p1vals
                                            doub_pairs[box1_pos2] = box1_p2vals
                                            doub_pairs[row_position] = row_value
                                            doub_pairs[row_position2] = row_values2
                                            #if it is a match, check the box. 
                                            row_pair2_box = (row_position2[0]//3, row_position[1]//3)

                                            if row_pair2_box == row_pair1_box:
                                       
                                                double_pair_count +=1
                                          
    return double_pair_count , doub_pairs
    
    

                
                
                
                        
                
            
            
           
            
            
          
                



             
    

        






        
        

    












