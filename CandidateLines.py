from itertools import combinations
#from BuildPuzzle import *
from PreparePuzzle import *
from FindSolutions import *


'''
Candidate Lines: 

Candidate lines strategy that first finds eligible clues to remove. This CAN lead to finding square solutions, but not always. 

If a number (1-9) is found to be eligible for a single row/col or box, while also containing clues in a connecting row/col or box 
(The combination of which differs in type, eg. Row & Box, or Col & Row), then the numbers found in the second location can be removed as candidates for those squares. 


Function will remove ineligible candidates using dictionaries of numbers and their position: 

First look in a BOX:
    - if Any number 1-9 only exists as a candidate in only ONE row or column of that box
        then the number MUST go on that row or column within that box 
    - Therefore: any other numbers listed on that line OUTSIDE of the box, 
        can be removed.
        



'''

# THIS IS NOT IN USE AT ALL

                                        
# Function: Takes a grid and position in the grid, and returns a list  of the available numbers for that grid (numbers that have not been solved. )        
def available_nums(grid, i,j ):
    
    #Sets position (i,j) to the appropriate 3x3 box.
    box_rst = i // 3 
    box_cst = j // 3 
        
    #For each row/col of my current BOX
    for row in range(box_rst * 3, box_rst * 3 + 3):
        for col in range(box_cst * 3, box_cst * 3 + 3):              
            
            available_nums = [1,2,3,4,5,6,7,8,9]
            # check all squares to determine if it is a solved square: And remove from the available nums list. 
            
            for nums in grid[row][col]:
                if len(grid[row][col]) == 1:
                    available_nums.remove(grid[row][col])
    return available_nums
    
'''
The next few methods support finding eligible numbers within a box to remove. 

1. Cand_lines: creates nested dictionary of numbers for each 3xx9 section and stores the box as the inner dictionary value. 
2. find_fixed_candidates: Finds any number in a given row/col that exists once. This number cannot be a clue in any other row/col of 
    the same box.
3. remove_nonfixed: Takes new dictionary of numbers with fixed candidates. Identifies any boxes that contain that number
    outside of the fixed row/col and removes it. 
4. section_loop: Completes loop through grid of the above methods, checking each 3x9 section (rows/cols)

'''   
    

#Checks for candidates to removed within BOXES - as opposed to the rows/cols
def cand_lines(grid, k):
    
    '''1. For each section (3 line, 3 box), check each number 1-9, determine if num available (not sovled square) for each line and in each box.
    2. if a num is only availble for 1 box in 1 line, it is a fixed candidate for that line. 
    3. remove num from any other squares of that box.'''
    
    numbers = [1,2,3,4,5,6,7,8,9]
    rnum_dict = dict()
    cnum_dict = dict()
   
    sect_st = k * 3 
    
        
    #create dict of nums
    for num in numbers:
        
        row_dict = dict()
        col_dict = dict()
            
        #for each line of section (3 row / 3 col) and square of a line
        for sect_st in range(3):
            rboxes = set()
            cboxes = set()
            for square in range(9):
    
                box = square // 3 
                if type(grid[sect_st][square]) is not list: grid[sect_st][square] = [grid[sect_st][square]]
                
                if len(grid[sect_st][square]) > 1:
                    #If num is found wihtin the current square, add box number to set.
                    if num in grid[sect_st][square]:
                        rboxes.add(box)
                        
                if type(grid[square][sect_st]) is not list: grid[square][sect_st] = [grid[square][sect_st]]
                if len(grid[square][sect_st]) > 1:
                    # add box to set 
                    if num in grid[square][sect_st]:
                        cboxes.add(box)
                
            #Add to dictionary: rows and cols of each section, and what boxes contained the number.
            if len(rboxes) >= 1 :
                row_dict[sect_st] = rboxes
            if len(cboxes) >= 1 :
                col_dict[sect_st] = cboxes
                
            
        # For each number, add dictionary of rows/cols and the boxes that contain the number.     
        rnum_dict[num] = row_dict
        cnum_dict[num] = col_dict    
    #Return nested dictionary of numbers and which rows and squares contain it.    
    return rnum_dict, cnum_dict
        




# nums_dict is rows/cols for one section 3 lines by 9 squares.
def find_fixed_candidates(nums_dict):
    
    candidates = dict()
    #Get lines of each number
    for number , rows in nums_dict.items():
        #if a row containes more than one item (A number was found as a candidate in more than one square of a line)
        if len(rows) > 1:
            for row , boxes in nums_dict[number].items():
                #number found on more than one square of that line            
                if len(boxes) == 1:
                    #Save only these numbers, into new dictonary     
                    candidates[number] = nums_dict[number]
                                   
    
    remove_dict = dict()
    if len(candidates) > 0:
        for number in candidates.keys():
            for row, box in candidates[number].items():
                #if a number only exists in one box of a row
                if len(box) == 1: 
                    row_holder = dict()
                    #look at the next row, 
                    for row1, box1 in candidates[number].items():
                        if row != row1:
                            place_holder_list = []
                            #look in boxes of second row for that same number. IF the box is in the same box.
                            for i in box1:
                                if i in box:
                                    #place holder - add the box that is matched to a list
                                    place_holder_list.append(i)    
                                    row_holder[row1] = place_holder_list
            #add row holders to number in dictionary. remove these numbers. 
            remove_dict[number] = row_holder
                            
    return remove_dict




# Takes dictionary of numbers and positions to remove from shared boxs              
def remove_nonfixed(nums_dict, grid, k , row = True):
    
    box_start = 0
    line_start = k * 3
    removed_nums = 0
    CL_nonfixed_dict = dict()
    
    #For each number, get the line and box where that number exists. (Per section)
    for number in nums_dict.keys():
        for line, box in nums_dict[number].items():

            gridline= line_start + line
            b = 0
            for i in box:
                b = i
            
            box_start = b * 3 

            for box_start in range(box_start, box_start + 3):
                #Check rows
                if row == True: 
                    nums_in_square = grid[gridline][box_start]
                    #Check each square, if greater than one.
                    if len(nums_in_square) > 1:
                        #check each num and see if matches number from dictionary to remove
                        for j in nums_in_square:
                            if j == number:
                                nums_in_square.remove(j)
                                removed_nums += 1
                        #reset grid to new array
                        grid[gridline][box_start] = nums_in_square
                        CL_nonfixed_dict[(gridline, box_start)] = j
                #Check cols
                else:
                    nums_in_square = grid[box_start][gridline]
                    if len(nums_in_square) > 1:   
                        for j in nums_in_square:
                            if j == number:
                                nums_in_square.remove(j)
                                removed_nums += 1
                        grid[box_start][gridline] = nums_in_square
                        CL_nonfixed_dict[(box_start, gridline)] = j
                    
    '''Print Statements for debugging'''
    # if len(CL_nonfixed_dict) > 0:
    #     print("CL NONFIXED REMOVED", removed_nums)
    #     print(CL_nonfixed_dict)
    return grid, removed_nums
    
    
# Another way to check for eligible candidates to remove based on lines. Removes numbers in same box if 
# a number in box is only number of ROW/COL eligible.
def section_loop(grid):
    total = 0
    updatedgrid = grid
    for k in range(3):
        #For each number, for each row (of section) get the box position of the number.
        rdict, cdict = cand_lines(grid,k) 
        #Find which numbers only exist for a given row in one box.
        fixed_dict = find_fixed_candidates(rdict)
        #If there are any to remove, remove the numbers from the box(except its fixed row)
        if len(fixed_dict) > 0:
            updatedgrid, count = remove_nonfixed(fixed_dict, grid, k, True)
            total += count
        #do the same for cols    
        fixed_cdict = find_fixed_candidates(cdict)
        
        if len(fixed_cdict) > 0:
            updatedgrid, count = remove_nonfixed(fixed_cdict, updatedgrid, k, False)
            total += count
    
    return updatedgrid, total
        

'''
Next several methods identify eligible candidates to remove wihtin the row/col, if it is the number is found to be only in a 
single row/col for a given box. Slightly different method. Could reduce and use above example adding different search method
to condense code.

1. box_lists: nested list of sets containing all possible numbers for each row/col in a box. 
2. create_box_dict: takes box_lists, turns into dictionary. NOT USED???
3. lonely_nums: Takes box_row and box_col lists, identifies numbers that only exist in a single row/col. 
4. check_lines: Takes lonlies for either row/col, identifies in the same row/col not in the given box and removes them.

'''
# Takes grid and position in grid, returns a list of lists: list_cols and list_rows, 
# that are the possible numbers left remaining for the three rows / cols in a box.         
def box_lists(grid, box):        
    
    # Takes active grid and box: iteration of all boxes 1-9 from final function.
    
    #Set box starting positions
    box_rst = box[0]
    box_cst = box[1]
    
    #initiate empty lists for rows/cols
    box_cols = []
    box_rows = []
    
    # For each row in the box
    
    for box_r in range(box_rst * 3, box_rst * 3 + 3):  
        #Establish empty set for row items
        single_row = set()

        # For each square of the row    
        for row_square in range(box_cst * 3, box_cst * 3 + 3):  

            #check if the square length is 1, 
            if len(grid[box_r][row_square]) == 1 :
                #Add 0 as place holder for maintaining positioning. 

                single_row.add(0)
            else:

                #Update set to include all numbers in position.
                single_row.update(grid[box_r][row_square])
        
        box_rows.append(single_row)
    # Do the same thing for each column in the box.    
    for b_col in range(box_cst * 3, box_cst * 3 + 3):
        single_col = set()
        for col_square in range(box_rst * 3, box_rst * 3 + 3):       
  
            if len(grid[col_square][b_col]) == 1:

                single_col.add(0)

            else:
    
                single_col.update(grid[col_square][b_col])
                
                 
        
        
        box_cols.append(single_col)

    #Returns list of sets of what numbers are found in each row / col of the box.       
    return box_rows, box_cols 
    
# I don't need the grid I just need the position to know which box to put it in.  
#function creates a dictionary based on what box is entered and includes the box location, box_row list and box_col list   
def create_box_dict(i,j, box_rows, box_cols):  
    
    box_row_start = i // 3 
    box_col_start = j // 3    
    
    lonely_rnum = [] 
 
    for list_check in range(len(box_rows)):
        for number in box_rows[list_check]: 
            check_count = 0
    
            for other_list in range(len(box_rows)):
                #continue to next list if other_list is the same as primary list
                if list_check == other_list:
                    continue
                
                if check_count <= 1:
                    #if not in my first list, check the other.
                    if number in box_rows[other_list]:
                        continue
                    else:
                        break
                else:
                    if number not in box_rows[other_list]:
                        lonely_rnum.append(number) 
                    else:
                        lonely_rnum.append(0)
                        break

    lonely_cnum = [] 
    for list_check in range(len(box_cols)):
    #starts at 0
        for number in box_cols[list_check]:
            check_count = 0
            
            for other_list in range(len(box_cols)):
                
                if list_check == other_list:
                    #check next other_list
                    continue
        
                if check_count < 1: 
                    if number not in box_cols[other_list]:
                        #not in first check but may be in second. Increase count and continue to next list iteration. 
                        check_count += 1
                        continue
                    else:
                        #it was found! This means we don't need to check the other list, the number isn't lonely.
                        break
                
                else: 
                    if number not in box_cols[other_list]:
                        #Wasn't in first check, not in second = lonely column number. 
                        lonely_cnum.append(number)
                    else:
                        lonely_cnum.append(0)
                        break

    my_dict = {
        "box" : (box_row_start, box_col_start),
        "box_rows" : box_rows,
        "box_cols" : box_cols,
        "lonely_rs" : lonely_rnum,
        "lonely_cs": lonely_cnum
    }
    
    return my_dict


# Finds any numbers that are "LONELY", that is any number in a given BOXs row or col that only exists in that row/col for the box
def lonely_nums(box_rows,box_cols):
    # 4/28/23: unecessary but not removing right now.
    box_rows = box_rows 
    box_cols = box_cols
    
    lonely_rnum_list = []
    
    #For each row of the box_rows    
    for list_check in range(len(box_rows)):
        
        #make a set of all lonely nums from each row
        lonely_rnum = set() 
        lonely_rnum.add(0)
        
        # For each number in any given  row
        for number in box_rows[list_check]: 
            check_count = 0
           
            # Skip the 0 placeholders.
            if number == 0:
                continue
            # Check against other rows of that same box.
            for other_list in range(len(box_rows)):
                #continue to next list if other_list is the same as primary list
                if list_check == other_list:  
                    continue
                
                if check_count < 1:
                    #Check next list after not finding number.
                    if number not in box_rows[other_list]:
                        check_count += 1
                        continue
                    # if in my first list, check next number
                    else:
                        #remove number from other list, no need to check it again during next row iteration
                        box_rows[other_list].remove(number)

                        break
                #Checking final row, 
                else: 
                    if number not in box_rows[other_list]:
                        #Not in first or second list, add number to lonely number list.
                        lonely_rnum.add(number) 
                    else: 
                        box_rows[other_list].remove(number)
                        break
        #Add lonely numbers of each row to larger list.
        lonely_rnum_list.append(lonely_rnum)
    #Do the same thing for the columns.
    
    lonely_cnum_list = [] 

    for list_check in range(len(box_cols)):

        lonely_cnum = set()
        lonely_cnum.add(0)
        
        for number in box_cols[list_check]:
            check_count = 0
            if number == 0:
                #dont care about 0's move on.
                continue
            
            for other_list in range(len(box_cols)):
                if list_check == other_list: 
                    #check next other_list
                    continue
        
                if check_count < 1:   
                    if number not in box_cols[other_list]:
                        #not in first check but may be in second. Increase count and continue to next list iteration.      
                        check_count += 1
                        continue
                    else:  
                        box_cols[other_list].remove(number)
                        lonely_cnum.add(0)
                        break
                
                else: 
                    if number not in box_cols[other_list]: 
                        #Wasn't in first check, not in second = lonely column number. 
                        lonely_cnum.add(number)
                    else:
                        box_cols[other_list].remove(number)
                        break
        #add lonely col numbers of each col to list
        lonely_cnum_list.append(lonely_cnum)               

    return lonely_rnum_list, lonely_cnum_list


 
# Take the lonelies found, and see if the numbers exist along the same row/col (not including the box they were found in)
 
def check_lines(lonlies, box, grid, row = True):
    CL_numsremoved = dict()
    CL_newclues = dict()
                
    #get starting row and col
    row_start = box[0]
    col_start = box[1]

    box_start = 0
    grid_start = 0
    
    # sets variables based on if checking rows or cols
    if  row == True:
        check_start = box[1]*3
        grid_start = box[0] *3 
        not_sums = [ check_start, check_start + 1, check_start + 2]
                   
    else:
        check_start = box[0]*3
        grid_start = box[1] *3
        not_sums = [ check_start, check_start + 1, check_start + 2]

    check_only = []
    
    if row == True:
        for i in range(9):
            if i in not_sums:
                continue
            else:
                check_only.append(i)

    removed = 0
 
    
    #For each number in each list of lonlies
    for lonely_list in lonlies: 
        for number in lonely_list:
            #skip the 0 placeholders 
            if number == 0:
                continue
            
            # loop through line (Row or COL)   
            for k in range(9):    
                #Check rows
                if row == True:
                    #If square (k) isn't one of the box squares, and has more than one number
                    if k not in not_sums:
                        if len(grid[grid_start][k]) > 1: 
                            remove_list = grid[grid_start][k]
                            # IF my number from my lonely list, is in my remove_list. I can remove it as a candidate!
                            if number in remove_list:
                                # IF my square also happens to be a length of two, that means I will solve this square. 
                                if len(remove_list) == 2:
                                    #remove the number and add it back to the grid at it's position.
                                    remove_list.remove(number)
                                    grid[grid_start][k] = remove_list
                                    removed += 1
 
                                    #add new clues, just for tracking/curiosity
                                    CL_newclues[(grid_start,k)] = remove_list
                                    if type(grid[grid_start][k]) is not list: grid[grid_start][k] = [grid[grid_start][k]]

                                    #update array function to update grid due to new clue - can remove even more possible numbers!
                                    num_count, grid = update_array(grid)
                                else:
                                    remove_list.remove(number)
                                    grid[grid_start][k] = remove_list
                                    removed += 1
                                    CL_numsremoved[(grid_start,k)] = number
                            else:
                                continue
                        
                #Do the same thing, but working with columns.            
                else:
                    remove_list = []
                    if k not in not_sums:
 
                        if len(grid[k][grid_start]) > 1:
                            remove_list = grid[k][grid_start]
                            
                            if number in remove_list:
                                if len(remove_list) == 2:
                                    remove_list.remove(number)
                                                                
                                    grid[k][grid_start] = remove_list
                                    removed += 1

                                    CL_newclues[(k, grid_start)] = remove_list
                                    if type(grid[k][grid_start]) is not list: grid[k][grid_start] = [grid[k][grid_start]]

                                    update_count, grid = update_array(grid)

                                else:
                                    remove_list.remove(number)
                                    grid[k][grid_start] = remove_list
                                    removed += 1
                                    CL_numsremoved[(k, grid_start)] = number
                                         
                        else:
                            continue
                           
        grid_start += 1                
                   
    return grid , removed




'''
Final main function. 
Part 1. Walk through each box, identifies lonely numbers in a row/col of the box and removes extra from that row/col.
Part 2. Walks through each section, idetnifies numbers found only in a row/col that are in a single box, and removes the other
numbers from that box.


'''
           
def check_lonely_nums(grid):
    
    total_returned = 0
    #must loop through each box
    for row in range(3):
        for col in range(3):
        
            box = (row,col)
            #get list of numbers for each row/col of a box
            box_rows, box_cols = box_lists(grid,box)
            # get any lonely numbers from each row/col of a box
            lonely_rnum, lonely_cnum = lonely_nums(box_rows,box_cols)
            
            #check to see if the remaining row/cols have the lonely numbers and remove them
            row_check, returned = check_lines(lonely_rnum, box, grid, True)
            
            col_check, treturned = check_lines(lonely_cnum, box, row_check, False)
      
            total_returned += treturned
           
    final, secondtotal = section_loop(col_check)
    
    total_returned += secondtotal
        
        
    return final , total_returned      
        


                

            
            
            
            
            
                            
                
                   


               
                     
        
        
            
            

          
            
            
    
    
    
    
    