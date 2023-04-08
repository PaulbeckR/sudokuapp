from PreparePuzzle import *

# Now that I have a game board, I have started a solution with finding all single nums.

# I have my possible_numbers_grid and game_board that I want to populate. and grid that is the orig.


# functions for general check / num in row / col / square

# Check if num in row/ column or grid - will be the num of length of 1
# called to update the array list for
'''
Starting with pos_nums_grid. Begins finding total solution. First three functions are gen-use functions for determining
if the number provided (myint) also exists in the same row / col / 3x3 grid as either a 
'''


def num_row(grid, myint, pos):
    # pos is the potition myint is at. also provides row location
    for row_i in range(0, len(grid)):
        for col_j in range(0, len(grid)):
           
            for each_position_row in range(9):
                if isinstance(grid[pos[0]][each_position_row], list):
                    #print("Checking array list ", grid[pos[0]][each_position_row])
                    
                    for element in grid[pos[0]][each_position_row]:

                        if myint == element and (row_i, col_j) != pos:
                            return True
                else:
                    if myint== grid[pos[0]][each_position_row] and (row_i, col_j) != pos:
                        return True


def num_col(grid, myint, pos):
    # if the search int is in any  col o
    # found a match.
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):

           
            for k in range(9):
                if isinstance(grid[k][pos[1]], list):
                    for element in grid[k][pos[1]]:
                        if myint == element and (i, j) != pos:
                            return True
                else:
                    if myint == grid[k][pos[1]] and (i,j) != pos:
                        return True


def num_inmini(gridagain, myint, pos):
    # returns TRUE if it finds a match. I want

    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if isinstance(gridagain[i][j], list):
                for element in gridagain[i][j]:
                    if element == myint and (i, j) != pos:
                        return True
            else:
                if element == myint and (i, j) != pos:
                        return True
                    
def as_list(grid):
    for i in range(9):
        for j in range(9):
            #print("here I am", grid[i][j])
            if type(grid[i][j]) is not list: grid[i][j] = [grid[i][j]]
    return grid
            


def only_option(gamegrid):
   # print("-------------------------------")
  #  print("START OF ONLY OPTION")
   # print("--------------------------------")
    gamegrid = as_list(gamegrid)
    change_count = 0
    oo_dict = dict()
    for i in range(9):
        for j in range(9):
            

        
            if type(gamegrid[i][j]) is not list: gamegrid[i][j] = [gamegrid[i][j]]
            if len(gamegrid[i][j]) > 1:
              
              
                for k in gamegrid[i][j]:
                    

                    if any(k in gamegrid[i][x] for x in range(9) if (i, x) != (i, j)):
                            gamegrid[i][j] = gamegrid[i][j]
                            #print(k, "was found to be in one or more ROWS")
                    else:
                        #print("OO: ROWS ", (i,j), "removed ",  k, "array: " , gamegrid[i][j])

                        gamegrid[i][j] = [k]
                        oo_dict[(i,j)] = k
                        change_count += 1
                        continue

                   

                    if any(k in gamegrid[x][j] for x in range(9) if (x, j) != (i, j)):
                      
                        gamegrid[i][j] = gamegrid[i][j]

                    else:
                        #print("OO: ROWS ", (i,j), "removed ",  k, "array: " , gamegrid[i][j])
                        gamegrid[i][j] = [k]
                        oo_dict[(i,j)] = k
                        change_count += 1
                        
                        continue

                    if any(k in gamegrid[x][y] for x in range(i - i % 3, i - i % 3 + 3) for y in
                        range(j - j % 3, j - j % 3 + 3) if (x, y) != (i, j)):
                       # print(k, "was found to be in one or more BOXES")
                        gamegrid[i][j] = gamegrid[i][j]
                            
                    else:
                        #print("OO: ROWS ", (i,j), "removed ",  k, "array: " , gamegrid[i][j])

                        gamegrid[i][j] = [k]
                        oo_dict[(i,j)] = k
                        change_count += 1
                        #print( "Position is now: ", gamegrid[i][j])
                            
                        continue
    # if change_count > 0:
    #     print("change count is ", change_count)
    #     print("DICT OF new clues: only_option")
    #     print(oo_dict)

    return change_count, gamegrid




def print_updated_grid(thisgrid):
    # print("printing updated grid")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("--------------+-----------------+-------------------")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("||", end=" ")

            print(*thisgrid[i][j], end=" : ")
        print()



def print_count(grid):
    count = 0
    solved = 0
    for i in range(9):
        for j in range(9):
            count = 0
            for k in grid[i][j]:
                count += 1
            # print("count at ", grid[i][j], "is" , count)
            if count == 1:
                solved += 1

    return solved



def update_array(thisgrid):
   # print(":::::::::::::::::::::::::::::::::::")
    #print("UPDATING ARRAY :::: UPDATING ARRAY")
   # print(":::::::::::::::::::::::::::::::::::")
    thisgrid = as_list(thisgrid)
    array_update = 0
    count = 0
    UA_dict = dict()
    for i in range(0, len(thisgrid)):
        for j in range(0, len(thisgrid)):

            # if grid is equal to 1 do nothing
            if len(thisgrid[i][j]) == 1:
                #print("Checking this array" , thisgrid[i][j])

               
                for element in thisgrid[i][j]:
                   
                    if any(element in thisgrid[i][x] for x in range(9) if (i, x) != (i, j)):
                       

                        for row_position in range(9):
                            if len(thisgrid[i][row_position]) > 1:
                              
                                for n in thisgrid[i][row_position]:
                                   
                                    if n == element and j != row_position:
                                            if len(thisgrid[i][row_position]) == 2:
                            
                                                #print("UA ROW : ", (i,row_position), "removed ", element, "array: ", thisgrid[i][row_position])

                                                thisgrid[i][row_position].remove(element)
                                                if type(thisgrid[i][row_position]) is not list: thisgrid[i][row_position] = [thisgrid[i][row_position]]
                                                thisgrid = mini_arr_update(thisgrid, (i, row_position))
                                                array_update += 1
                                                UA_dict[(i,row_position)] = thisgrid[i][row_position]
                                            else:
                                                #print("UA ROW : ", (i,row_position), "removed ", element, "array: ", thisgrid[i][row_position])

                                                thisgrid[i][row_position].remove(element)
                                                array_update += 1 
                                        
                                        
                        
                                    
                                       
                    if any(element in thisgrid[x][j] for x in range(9) if (x, j) != (i, j)):
                        #print(element, "was found in the COLUMN", j)

                        for col_position in range(9):
                            if len(thisgrid[col_position][j]) > 1:
                                
                                for n in thisgrid[col_position][j]:
                                    
                                    if n == element and (i, j) != (col_position, j):
                                        if len(thisgrid[col_position][j]) == 2:
                                       
                                            #print("UA COL : ", (col_position,j), "removed ", element, "array: ", thisgrid[col_position][j])
                                            thisgrid[col_position][j].remove(element)
                                            thisgrid = mini_arr_update(thisgrid, (col_position, j))
                                            array_update += 1
                                            UA_dict[(col_position,j)] = thisgrid[col_position][j]

                                        else:
                                            #print("UA COL : ", (col_position,j), "removed ", element, "array: ", thisgrid[col_position][j])
                                            thisgrid[col_position][j].remove(element)
                                            
                                            array_update += 1
                       

                    if num_inmini(thisgrid, element, (i, j)):

                        #print(element, "it was found in one of the BOXES", (i,j))

                        box_x = j // 3  # j
                        box_y = i // 3  # i
                        for y in range(box_y * 3, box_y * 3 + 3):

                            for x in range(box_x * 3, box_x * 3 + 3):
                                
                                if len(thisgrid[y][x]) > 1:

                                    for n in thisgrid[y][x]:
                                    
                                    
                                        if n == element and (i, j) != (y, x):
                                            if len(thisgrid[y][x]) == 2:
                                                #print("UA BOX: ",(y,x), "removed ",  element, " array: ", thisgrid[y][x])
                                                thisgrid[y][x].remove(element)
                                                thisgrid = mini_arr_update(thisgrid, (y,x))
                                                array_update += 1
                                                UA_dict[(y,x)] = thisgrid[y][x]

                                            else:
                                                #print("UA BOX: ",(y,x), "removed ",  element, " array: ", thisgrid[y][x])

                                                thisgrid[y][x].remove(element)
                                                array_update += 1
    # if array_update > 0:
    #     print("Total removed in update_array", array_update)
    #     print("UA DICT ")
    #     print(UA_dict)
    return array_update, thisgrid

def mini_arr_update(grid, position):
    
    row = position[0]
    col = position[1]
    array_update = 0
    MAU_dict = dict()
    
    
    #if len(grid[row][col]) == 1:
                #print("Checking this array" , thisgrid[i][j])
    rem_num = grid[row][col]
    if type(rem_num) is not int: [rem_num] = rem_num
 
    #print("mini arr updating ", rem_num)

               
        
                   
    if any(rem_num in grid[row][x] for x in range(9) if (row, x) != (row, col)):
                       
        #print(rem_num, "was found in the ROW", row)

        for row_position in range(9):
            if len(grid[row][row_position]) > 1:
                              
                for n in grid[row][row_position]:
                                   
                    if n == rem_num and col != row_position:
                        if len(grid[row][row_position]) == 2:
                            
                           # print("Mini_arr ROW : ", (row,row_position), "removed ", rem_num, "array: ", grid[row][row_position])

                            grid[row][row_position].remove(rem_num)
                            if type(grid[row][row_position]) is not list: grid[row][row_position] = [grid[row][row_position]]
                            MAU_dict[(row,row_position)] = grid[row][row_position]
                            grid = mini_arr_update(grid, (row, row_position))
                            array_update += 1 
                            

                        else:
                           # print("Mini_arr ROW : ", (row,row_position), "removed ", rem_num, "array: ", grid[row][row_position])

                            grid[row][row_position].remove(rem_num)
                            array_update += 1 
                            
                        
                                    
                                       
    if any(rem_num in grid[x][col] for x in range(9) if (x, col) != (row, col)):
        #print(rem_num, "was found in the COLUMN", col)

        for col_position in range(9):
            if len(grid[col_position][col]) > 1:
                                
                for n in grid[col_position][col]:
                                    
                    if n == rem_num and (row, col) != (col_position, col):
                        if len(grid[col_position][col]) == 2:
                            
                           # print("Mini_arr COL : ", (col_position,col), "removed ", rem_num, "array: ", grid[col_position][col])

                            grid[col_position][col].remove(rem_num)
                            if type(grid[col_position][col]) is not list: grid[col_position][col] = [grid[col_position][col]]
                            MAU_dict[(col_position,col)] = grid[col_position][col]
                            grid = mini_arr_update(grid, (col_position, col))
                            array_update += 1 
                            

                        else:
                           # print("Mini_arr COL : ", (col_position,col), "removed ", rem_num, "array: ", grid[col_position][col])

                            grid[col_position][col].remove(rem_num)
                            array_update += 1 
                                       
                        
                       

    if num_inmini(grid, rem_num, (row, col)):

        #print(rem_num, "it was found in one of the BOXES", (row,col))

        box_x = col // 3  # j
        box_y = row // 3  # i
        for y in range(box_y * 3, box_y * 3 + 3):

            for x in range(box_x * 3, box_x * 3 + 3):
                                
                if len(grid[y][x]) > 1:

                    for n in grid[y][x]:
                                    
                                    
                        if n == rem_num and (row, col) != (y, x):
                            if len(grid[y][x]) == 2:
                               # print("MINI ARR BOX: " ,(y,x), "removed", rem_num, "array: ", grid[y][x])

                                grid[y][x].remove(rem_num)
                                MAU_dict[(y,x)] = grid[y][x]
                                grid = mini_arr_update(grid, (y,x))
                                array_update += 1
                                

                            else: 
                               # print("MINI ARR BOX: " ,(y,x), "removed", rem_num, "array: ", grid[y][x])

                                grid[y][x].remove(rem_num)
                                array_update += 1
    # if len(MAU_dict) != 0:
    #     print("mini array update removed", array_update)
    
        # print("DICT IN Mini ARR update")
        # print(MAU_dict)
    return grid
    
    
    
                                        
def only_option2(gamegrid):
     # print("-------------------------------")
  #  print("START OF ONLY OPTION")
   # print("--------------------------------")
    gamegrid = as_list(gamegrid)
    '''Create dictionary of positions and numbers set as clue'''
    oo_dict = dict()
    change_count = 0
    for i in range(9):
        for j in range(9):
            # if the length is greater than 1
            array = gamegrid[i][j]

        
            if type(gamegrid[i][j]) is not list: gamegrid[i][j] = [gamegrid[i][j]]
            if len(gamegrid[i][j]) > 1:
              
              
                for k in gamegrid[i][j]:
                   

                    if any(k in gamegrid[i][x] for x in range(9) if (i, x) != (i, j)):
                            gamegrid[i][j] = gamegrid[i][j]
                            #print(k, "was found to be in one or more ROWS")
                    else:
                        #print("OO ROWS: ", (i,j), "is now ",k,  gamegrid[i][j])
                        

                        gamegrid[i][j] = [k]
                        
                        oo_dict[(i,j)] = k
                        
                        gamegrid = mini_arr_update(gamegrid, (i,j))
                        change_count += 1 
                        continue

                   

                    if any(k in gamegrid[x][j] for x in range(9) if (x, j) != (i, j)):
                      
                        gamegrid[i][j] = gamegrid[i][j]

                    else:
                        #print("OO COLS: ", (i,j), "is now ",k,  gamegrid[i][j])
                        gamegrid[i][j] = [k]
                        oo_dict[(i,j)] = k
                        
                        gamegrid = mini_arr_update(gamegrid, (i,j))
                        change_count += 1 

                        continue

                    if any(k in gamegrid[x][y] for x in range(i - i % 3, i - i % 3 + 3) for y in
                        range(j - j % 3, j - j % 3 + 3) if (x, y) != (i, j)):
                        #print(k, "was found to be in one or more BOXES")
                        gamegrid[i][j] = gamegrid[i][j]
                            
                    else:
                        #print("OO BOXES: ", (i,j), "is now ",k,  gamegrid[i][j])

                        gamegrid[i][j] = [k]
                        oo_dict[(i,j)] = k
                        gamegrid = mini_arr_update(gamegrid, (i,j))

                        change_count += 1 
                        
                            
                        continue
    # if change_count > 0:       
                
        # print("Total changed in only option 2 ")   
        # print("New Clues from only option")
        # print(oo_dict)

    return change_count, gamegrid
   


def test_if_equal(game_grid, original):
    orig = []
    test = []
    
    for i in range(9):
        for j in range(9):
            
            o = original[i][j]
            t = game_grid[i][j]
            #print(t , "is t ")
            if type(t) is not int: [t] = t
            if o != t:
               # print("Doesnt match at original/ test ", (i,j) , o , t )
                return False
    return True
                
            
def basic_solve2(grid):
    change_count = 1
    # array_update = 1
    oo_rem = 0
    array_up = 0

    while change_count > 0:
        oo_count, grid = only_option2(grid)
        oo_rem += oo_count
        array_up += array_up
        array_update, grid = update_array(grid)
        
        
                
        
        #print(print_count(grid))
        #print("array_update ", (array_update + oo_count))
       
        change_count = oo_count + array_update
        
        # add solved_squares valid 

    total_removed = oo_rem + array_up


    return grid , total_removed
         
            
            

    






def basic_solve(grid):
   # print(":::::::::::::::::::::::::::::::::::")
    #print("STARTING BASIC SOLVE")
   # print(":::::::::::::::::::::::::::::::::::")
    change_count = 1
    # array_update = 1

    while change_count != 0:
        oo_count, grid = only_option(grid)
                
        array_update, grid = update_array(grid)
        #print(print_count(grid))
       # print("change_count ", change_count)
       # print("array_update ", array_update)
        change_count = oo_count + array_update
        
        # add solved_squares valid 

        
        
    changes = change_count + array_update

    return grid , change_count

# change_count = 0
# array_update = 0


 