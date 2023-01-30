from itertools import combinations
from BuildPuzzle import *
from PreparePuzzle import *
#from TestingDisplay import *


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
# Will search within a box of the grid and return a position that matches 
# num_row num_col and num_inmini will return TRUE if a num is found in a row/col/box

# def in_one_line(box, myint):
    
    # box will be the identified start row/col for a box 3x3 grid.

    #for row_pos in range(box_start_row * 3, box_start_row * 3 + 3):
        #for col_pos in range(box_start_col * 3, box_start_col * 3 + 3):
                        
        # !!!! fix this based on what 
            #for num in grid[row_pos][col_pos]:
        
                #if num == match:    
            # search through box again.
                    #for alt_box_row in range(box_start_row * 3, box_start_row * 3 + 3):
                        #for alt_box_col in range(box_start_col * 3, box_start_col * 3 + 3):
                                        
              
grid_new = create_grid_fill()  
grid_game = new_game_board(grid_new)
grid = create_arrays(grid_game)
                                              

def get_box_dict(grid, pos):
    
    #NEED TO use POS or establish it before making dictionary. 
    x = pos[0]
    y = pos[1]
    
    pos_dic = {}
    num_dic = {}
  
    # create box guides 
 
    for i in range(9):
        pos_dic[i] = (x,y) 
    print("pos dic is ", pos_dic)
    
    box_row = x // 3
    box_col = y // 3
    
    #going three at a time
    count = 0
    list_box_arrays = []
    list_positions = []
    for row in range(box_row * 3, box_row * 3 + 3):
        for col in range(box_col * 3, box_col * 3 + 3):
                        
            list_box_arrays.append(grid[row][col])
            # print("position is ", (row,col))
            list_positions.append((row,col))
            
            # print("list_positions added ", list_positions)
            
            # print("List is ", list_box_arrays)
    for i in list_box_arrays:    
            # create dictionary of all values in box. 
        num_dic[count] = i
        count += 1
    count2 = 0  
    for k in list_positions:
        pos_dic[count2] = k
        count2 += 1
 
    return num_dic, pos_dic
            
test_num, test_pos = get_box_dict(grid, (0,1))

print(test_num)
print(test_pos)


row_0 = set()
row_1 = set()
row_2 = set()

col_0 = set()
col_1 = set()
col_2 = set()

for i, value in enumerate(test_num.values()):
    if i < 3:
        if len(value) > 1:
            row_0.update(value)
    elif i < 6:
        if len(value) > 1:
            row_1.update(value)
    else:
        if len(value) > 1:
            row_2.update(value)

for i, value in enumerate(test_num.values()):
    if (i == 0 or i == 3 or i == 6):
        if len(value) > 1:
            col_0.update(value)
    elif (i == 1 or i == 4 or i == 7):
        if len(value) > 1:
            col_1.update(value)
    else:
        if len(value) > 1:
            col_2.update(value)

print(row_0)
print(row_1)
print(row_2)
print(col_0)
print(col_1)
print(col_2)

# Now find if any number in row_0 is NOT in row_1 or row2. 

for number in row_0:
    if number not in row_1 and number not in row_2:
        lonely_row_int = number
        print("row_0", lonely_row_int)
for number in row_1: 
    if number not in row_0 and number not in row_1:
        lonely_row_1 = number
        print("row_1", lonely_row_1)
for number in row_2:
    if number not in row_0 and number not in row_1:
        lonely_row_2 = number
        print("row_2", lonely_row_2)
for number in col_0:
    if number not in col_1 and number not in col_2:
        lonely_col_0 = number
        print("lonely_col_0", lonely_col_0)
for number in col_1: 
    if number not in col_0 and number not in col_1:
        lonely_col_1 = number
        print("col_1", lonely_col_1)
for number in col_2:
    if number not in col_0 and number not in col_1:
        lonely_col_2 = number
        print("col2", lonely_col_2)


# So now I have two dictionaries with matching keys. Each Key should be associated with 
# the correct position.

# I want to see if in my grid, I have any numbers that share only 1 row or column.

# Rows: 0,1,2 
# Cols: 0,1,2 

# are any numbers ONLY in row 0, row 1, or row2 or col 1 or col 2 or col 3

# I could also create a set of all nums from each row/col. if a set contains 
# a unique number when compared to other rows or columns (separately), then
# I have found a line.



rows_list = []
cols_list = []

#takes from grid
for i in range(1-10):
    for j in range(1-10):
        box_rst = i // 3
        box_cst = j // 3 
        for row in range(box_rst * 3, box_rst * 3 + 3):
            
                    
            for col in range(box_cst * 3, box_cst * 3 + 3): 
                
                for sets in range(3):
                                  
                    if len(grid[row][sets]) > 1:
                        rows = []
                        
                        
                        #update the set for each row 0-2
                        row[sets].append(grid[row][sets])
                        print("rows" , rows)
                        # turn row lsit into a set. 
                        row_set = set(item for sublist in rows for item in sublist)
                        print("rowset" , row_set)
                        
                       
                        for ele in range(3):
                        
                            rows_list.append(row_set[ele])
                            print("rows list ", rows)
                            if i == 4:
                                break
                        
                        
                        
                        print("rows", rows_list)
                        i +=3 
                    
                    if len(grid[sets][col]) > 1:
                        cols = set()
                        cols.update(grid[sets][col])
                        cols_list.append(cols)
                        print("cols", cols_list)
                        j += 3
                    
                    
                     
        
        
            
            

          
            
            
    
    
    
    
    