from itertools import combinations
from BuildPuzzle import *
from PreparePuzzle import *
from TestingDisplay import *


'''
Candidate Lines: 


Function will remove ineligible candidates in remaining arrays: 

First look in a BOX:
    - if Any number 1-9 only exists as a candidate in a given row or column
        then it has to be on that LINE within that BOX. 
    - Therefore: any other numbers listed on that line OUTSIDE of the box, 
        can be removed.
        
In any given 3x3 grid with [i][j] determining the position of a number. If that number is only found in a single row or single column, 
then it will only have locations that share the same I or J, but not both. 

So if 4's are only available in column 0 for box 1, then we would remove all OTHER 4's from column 0


'''

              
#grid_new = create_grid_fill()  
#grid_game = new_game_board(grid_new)
#grid = create_arrays(grid_game)
                                              



# So now I have two dictionaries with matching keys. Each Key should be associated with 
# the correct position.

# I want to see if in my grid, I have any numbers that share only 1 row or column.

# I could also create a set of all nums from each row/col. if a set contains 
# a unique number when compared to other rows or columns (separately), then
# I have found a line. If a line is found all numbers that are not in the initial box but are in the cooresponding row/col are removed from the arrays.

        
# Function: Takes a grid and position in the grid, and returns a list  of the available numbers for that grid (numbers that have not been solved. )        
def available_nums(grid, i,j ):
    #Sets position (i,j) to the appropriate 3x3 box.
    box_rst = i // 3 
    box_cst = j // 3 
        
    # For the row in range (Whatever the starting row is for my current box) (Row 0 at init) up to three rows (ENDING AT ROW 2 )
    for row in range(box_rst * 3, box_rst * 3 + 3):
        # for the col in range (Starting Col (0) to three additional (col 2))        
        for col in range(box_cst * 3, box_cst * 3 + 3):              
            # First, set list of available nums. I will use these as what nums to LOOK FOR in my LINES(row/col)
            available_nums = [1,2,3,4,5,6,7,8,9]
            # check all squares to determine if it is a solved square: And remove from the available nums list. 
            for nums in grid[row][col]:
                if len(grid[row][col]) == 1:
                    available_nums.remove(grid[row][col])
    return available_nums
    
                   
# Takes grid and position in grid, returns a list of sets: list_cols and list_rows, that are the possible numbers left remaining for the three rows / cols in a box.         
def box_lists(grid, box):        
    
    # count variable to adjust which box we are iterating over.                 
    count = 0                     
                    
        
    #start new iteration through each square of box
    
    box_rst = box[0]
    box_cst = box[1]
    
    box_cols = []
    box_rows = []
        
    # for the row in range (Starting row (0) to three additional (row 2)) 
    # start at 0, start at 3, start at 9 up to 3, up to 6 up to 9
    
    for line in range(box_rst * 3, box_rst * 3 + 3):  
        
        
        single_row = set()

        #print("box row start is ", (box_rst *3 , box_rst *3 +3))
        # for the col in range (Starting Col (0) to three additional (col 2))  
              
        for item in range(box_cst * 3, box_cst * 3 + 3):  
            #print("box col start is ", (box_cst *3 , box_cst *3 +3))
            # Iterate in one row at a time through the three columns. 
            #print(":::::::::::::::::::::::::::")
            #print("THIS IS THE CURRENT BOX : ", (box_rst, box_cst))
            #print(":::::::::::::::::::::::::::::::::::::::::")
  
            if len(grid[line][item]) == 1 :
                # For each column in my row: add 0 as holder if the square is 0 
                #print("adding to single_ROW set ", grid[line][item], "from", (line, item))
                single_row.add(0)
            else:
                #print("adding to single_row", 0 , "at ", (line, item))
                
                # CONSIDER ADDING REMOVE: statement if number in position is not in available nums
                
                single_row.update(grid[line][item])
        
        box_rows.append(single_row)
        
    for item in range(box_cst * 3, box_cst * 3 + 3):
        single_col = set()
        for line in range(box_rst * 3, box_rst * 3 + 3):       
          
            
        
    
            #print("position is COL", (line,item))   
            if len(grid[line][item]) == 1:
                #print("adding to single_row", 0 , "at ", (item,line))
                single_col.add(0)

            else:
                #print("adding to single_row", 0 , "at ", (line, item))
                #print("adding to single_COL set ", grid[line][item], "from", (item, line))
                single_col.update(grid[line][item])
                
            #put set into list. 
            #print("row set is ", single_row) 
            #print("Cols Set is ", single_col)           
        
        
        box_cols.append(single_col)
    #print("box_rows ", box_rows)
   # print("box_cols ", box_cols)
            
    return box_rows, box_cols     

# TEST TEST TEST 
#print_pos_grid(grid)
#testing_box_lines = box_lists(grid, (0,1))    
#box_rows, box_cols = box_lists(grid, (2,2))

#array_display(grid)
    
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


#alternatively: Get all "lonely numbers that are in each row/col of a specific box. Creates a list of numbers that are only in one row or column
# returns lonely_rnum_list, lonely_cnum_list. 0's included as place holders to keep the position 0,1,2 of the line position in the box.

def lonely_nums(box_rows,box_cols):
    
    box_rows = box_rows 
    box_cols = box_cols
    
    lonely_rnum_list = []
    
    #print("::::::::::::: TEST ROWS FOR LONELY ::::::::::")
    # print(":::::::::::::::::::::::::::::::::::::::::::::::")
    
    for list_check in range(len(box_rows)):
        
        #make a set of all lonely nums from each row
        lonely_rnum = set() 
        lonely_rnum.add(0)
        
        #print("Checking row: ", list_check, box_rows[list_check] )
        for number in box_rows[list_check]: 
            check_count = 0
            #print("NUMBER IS ", number)
            
            if number == 0:
                continue
    
            for other_list in range(len(box_rows)):
                
                #print("Checking list :  ", other_list, "containing ", box_rows[other_list])                
                
                #continue to next list if other_list is the same as primary list
                if list_check == other_list:
                    #print("duplicate, moving on.")
                    continue
                
                if check_count < 1:
                    #print("Check Count is Less than 1 CHECKING: ", other_list)
                    #if not in my first list, check the other.
                    if number not in box_rows[other_list]:
                        check_count += 1
                        
                        #print( number, "WAS NOT IN list, check next list ")
                        continue
                    # if in my first list, check next number
                    else:
                        #print(number, "IN list, NUMBER ISNT LONELY:  BREAK OUT OF LOOP AND CHECK NEXT NUMBER")
                        #remove number from other list, no need to check it again and again
                        box_rows[other_list].remove(number)
                        
                        
                        break
                else:
                    #print("Check count is 1 or more")
                    # if not the first list, (count <= 1) indicate second list)
                    if number not in box_rows[other_list]:
                        
                        #print(number, "was NOT IN list", other_list, "ADD TO LONELY NUMS")
                        
                        lonely_rnum.add(number) 
                    else:
                        #print(number, "WAS IN", other_list, "adding 0 as place keeper")
                        box_rows[other_list].remove(number)
                        
                       
                        break
        lonely_rnum_list.append(lonely_rnum)

    lonely_cnum_list = [] 
    #print("::::::::::::: TEST COLS FOR LONELY ::::::::::")
    #print("::::::::::::::::::::::::::::::::::::::::::::::")
    for list_check in range(len(box_cols)):
        #print("Checking COL list: ", box_cols[list_check], list_check)
        lonely_cnum = set()
        lonely_cnum.add(0)
    #starts at 0
        for number in box_cols[list_check]:
            check_count = 0
            #print("NUMBER IS ", number)
            
            
            if number == 0:
                #dont care about 0's move on.
                continue
            
            for other_list in range(len(box_cols)):
                #print("checking list ", list_check, box_cols[list_check])
                
                
                if list_check == other_list:
                    #print("duplicate list, move on")
                    #check next other_list
                    continue
        
                if check_count < 1: 
                    #print("Comparing to :", other_list ,box_cols[other_list])
                    #print("check_count less than 1 : first comparison" )
                    if number not in box_cols[other_list]:
                        #not in first check but may be in second. Increase count and continue to next list iteration. 
                        #print( number, " was NOT there, check NEXT LIST")
                        check_count += 1
                        continue
                    else:
                        #print(number, "It WAS THERE, BREAK OUT OF LOOP AND CHECK NEXT NUMBER")
                        box_cols[other_list].remove(number)
                        lonely_cnum.add(0)
                      
                        break
                
                else: 
                    if number not in box_cols[other_list]:
                        
                        #print(number, "was NOT in ", other_list, "ADD TO LONELY NUMS")
                        #Wasn't in first check, not in second = lonely column number. 
                        lonely_cnum.add(number)
                    else:
                        #print(number, "WAS in ", other_list, " adding 0 as place keeper")
                        box_cols[other_list].remove(number)
                        
                        break
        
        lonely_cnum_list.append(lonely_cnum)               
   
    #print("lonly rnum list ", lonely_rnum_list)
    #print("lonely cnum list", lonely_cnum_list)
    return lonely_rnum_list, lonely_cnum_list

# Loneyly nums testing: 
# testing_lonely_nums = lonely_nums(box_rows, box_cols)



 
# Now I want to check each box, find any lonely numbers, if i find a lonely number, 
 
def check_lines(lonlies, box, grid, row = True):
    # I have a list length 3 that lists lonelies for my current box. 
    # I want to check if any lonelies are in the other two boxs in the same column. 
    # check all squares of the same column that are not = to my column positions
                
    #get starting row and col
    row_start = box[0]
    col_start = box[1]
    
    #print("lonlies is ", lonlies)
    
    #print("Box is ", box)
            
    box_start = 0
    grid_start = 0
    
    # sets line to be the specific row or column of the box and grid
    if  row == True:
    
        check_start = box[1]*3
        grid_start = box[0] *3 
        not_sums = [ check_start, check_start + 1, check_start + 2]
                   
    else:
        check_start = box[0]*3
        grid_start = box[1] *3
        not_sums = [ check_start, check_start + 1, check_start + 2]
        
    # for my line find all index of line to NOT remove
    #not_nums = []
    # for n in range(grid_start, grid_start + 3 ):
    #    not_nums.append(n)
    #   print("Not numbs are ", not_nums)
        
   # not_sums = [ grid_start, grid_start + 1, grid_start + 2]
    #print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::NOT SUMS ARE" , not_sums)
    
    check_only = []
    
    if row == True:
        for i in range(9):
            if i in not_sums:
                continue
        else:
            check_only.append(i)
            
    #print("CHECK ONLY::::::::::       ", check_only)
            
    
    
    
    
    #print(not_sums, "Num_sums as list ")

    # I want to get my lonlies, which is a list of three sets. each set represents a row/col location in the grid based on the box start. 
    # lonelies[0] = first row/col, lonelies[1] - second row/col, lonelies[2] = thirs row/col
 
     
    removed = 0
    
    grid_start = grid_start
    count = 0 
    
    
    for lonely_list in lonlies: 
    # for grid_start (row or col)
    
    
        #print("grid_start at ", grid_start)    
        #print("lonely list is ", lonely_list)

        
        for number in lonely_list: 
          
            #print("number is ", number)
            #now that I have my grid_start and nums to check, iterate through each square
                
            for k in range(9):    

                if row == True:
                    if k not in not_sums:
                    
                    #print(k, "is k") 
                        if len(grid[grid_start][k]) > 1:
                            if number in grid[grid_start][k]:
                                grid[grid_start][k].remove(number)
                                removed += 1
                                #print(number, "was removed from ", grid[grid_start][k], " at position", (grid_start, k))
                            else:
                                continue
                            #print("No K found in line ", grid_start)
                else:
                    if k not in not_sums:
                    #print(k, "is k") 
                        if len(grid[k][grid_start]) > 1:
                            if number in grid[k][grid_start]:
                                grid[k][grid_start].remove(number)
                                removed += 1
                               # print(number, "was removed from ", grid[k][grid_start], " at position", (k, grid_start))
                            else:
                                continue
                                #print("No K found in line ", grid_start)
                
        grid_start += 1
    #print(removed, "was removed during lines check for row = ", row)
        
            
                
           
                          
                            
                    
                   
    return grid , removed

#check lines testing: 

# lonely_rnum_list, lonely_cnum_list
# param: lonelies , box, grid, row = true

# lonely_rnum_list, lonel_cnum_list = lonely_nums(box_rows, box_cols)

# test_check_lines_rows = check_lines(lonely_rnum_list, (0,0), grid, row = True)



# MAIN FUNCTION that creates updated grid removing any numbers from possible solutions arrays based on candidate lines strategy.
# returnes grid, total_returned , with total_returned for testing purposes.
           
def check_lonely_nums(grid):
    
    total_returned = 0
    #must loop through each box!!!!!!
    for row in range(3):
        for col in range(3):
            
            # box starting coords 
            box = (row,col)
            
            
            
            #print("BOX IS ", box)
            
            box_rows, box_cols = box_lists(grid,box)
            
            #print("box_rows", box_rows)
            #print("box_cols", box_cols)
            
             
         
            lonely_rnum, lonely_cnum = lonely_nums(box_rows,box_cols)
            
            #print("lonely_cnum",  lonely_cnum)
            #print("lonely_rnum", lonely_rnum)
            
            row_check, returned = check_lines(lonely_rnum, box, grid, True)
            
            col_check, treturned = check_lines(lonely_cnum, box, row_check, False)
            
            # col_check should be a full box check. 
            # add to i/j to move to next box. 
    
            # mydict = create_box_dict(i,j,box_rows, box_cols)
            
            total_returned += treturned
        
        
    return grid , total_returned      
        

            
# cl_grid , total_returned = check_lonely_nums(grid)


#print_pos_grid(cl_grid)            
#print(total_returned,  "total removed from num arrays after candidate lines. ")


# Testing testingdisplay:

#array_display(cl_grid)
              
        
                
                

            
            
            
            
            
                            
                
                   


               
                     
        
        
            
            

          
            
            
    
    
    
    
    