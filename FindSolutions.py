from PreparePuzzle import *


'''
Containes several initial strategies and methods to update possible candiates for each square. 

Primary methods: 

1. only_option: 



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
            if type(grid[i][j]) is not list: grid[i][j] = [grid[i][j]]
    return grid
            

#Original only option, does not have mini update following finding new clues. Keep for analysis.
def only_option(gamegrid):

    gamegrid = as_list(gamegrid)
    change_count = 0
    oo_dict = dict()
    #loop through grid in each square
    for i in range(9):
        for j in range(9):

            if type(gamegrid[i][j]) is not list: gamegrid[i][j] = [gamegrid[i][j]]
            if len(gamegrid[i][j]) > 1:
                for k in gamegrid[i][j]:
                    
                    #Check if number (k) is not found in any other square of that ROW    
                    if any(k in gamegrid[i][x] for x in range(9) if (i, x) != (i, j)):
                            #if it is keep the square the same.
                            gamegrid[i][j] = gamegrid[i][j]
                    else:
                        # if not, set k to the position in the grid. Solved a new square.
                        gamegrid[i][j] = [k]
                        oo_dict[(i,j)] = k
                        change_count += 1
                        continue
                    #do the same for each col
                    if any(k in gamegrid[x][j] for x in range(9) if (x, j) != (i, j)):
                        gamegrid[i][j] = gamegrid[i][j]

                    else:
                        gamegrid[i][j] = [k]
                        oo_dict[(i,j)] = k
                        change_count += 1
                        continue

                    if any(k in gamegrid[x][y] for x in range(i - i % 3, i - i % 3 + 3) for y in
                        range(j - j % 3, j - j % 3 + 3) if (x, y) != (i, j)):
                        gamegrid[i][j] = gamegrid[i][j]
                            
                    else:
                        gamegrid[i][j] = [k]
                        oo_dict[(i,j)] = k
                        change_count += 1
                            
                        continue


    return change_count, gamegrid



# ANOTHER way to print the grid
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


#Another way to count things.
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


#updates arrays based on new clues found, uses mini_arr_update to update even more if clues found.
def update_array(thisgrid):

    thisgrid = as_list(thisgrid)
    array_update = 0
    count = 0
    UA_dict = dict()
    for i in range(0, len(thisgrid)):
        for j in range(0, len(thisgrid)):

            # if grid is equal to 1 , check to see if it's in any other row/col/box
            if len(thisgrid[i][j]) == 1:   
                for element in thisgrid[i][j]:
                   
                    if any(element in thisgrid[i][x] for x in range(9) if (i, x) != (i, j)):
                        for row_position in range(9):
                            if len(thisgrid[i][row_position]) > 1:
                              
                                for n in thisgrid[i][row_position]:
                                   
                                    if n == element and j != row_position:
                                            if len(thisgrid[i][row_position]) == 2:
                            
                                                thisgrid[i][row_position].remove(element)
                                                if type(thisgrid[i][row_position]) is not list: thisgrid[i][row_position] = [thisgrid[i][row_position]]
                                                thisgrid = mini_arr_update(thisgrid, (i, row_position))
                                                array_update += 1
                                                UA_dict[(i,row_position)] = thisgrid[i][row_position]
                                            else:

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
    

    rem_num = grid[row][col]
    if type(rem_num) is not int: [rem_num] = rem_num
   
                   
    if any(rem_num in grid[row][x] for x in range(9) if (row, x) != (row, col)):
                       
        #print(rem_num, "was found in the ROW", row)

        for row_position in range(9):
            if len(grid[row][row_position]) > 1:
                              
                for n in grid[row][row_position]:
                                   
                    if n == rem_num and col != row_position:
                        if len(grid[row][row_position]) == 2:
                            

                            grid[row][row_position].remove(rem_num)
                            if type(grid[row][row_position]) is not list: grid[row][row_position] = [grid[row][row_position]]
                            MAU_dict[(row,row_position)] = grid[row][row_position]
                            grid = mini_arr_update(grid, (row, row_position))
                            array_update += 1 
                            

                        else:

                            grid[row][row_position].remove(rem_num)
                            array_update += 1 
                            
                                   
    if any(rem_num in grid[x][col] for x in range(9) if (x, col) != (row, col)):
        #print(rem_num, "was found in the COLUMN", col)

        for col_position in range(9):
            if len(grid[col_position][col]) > 1:
                                
                for n in grid[col_position][col]:
                                    
                    if n == rem_num and (row, col) != (col_position, col):
                        if len(grid[col_position][col]) == 2:
                            

                            grid[col_position][col].remove(rem_num)
                            if type(grid[col_position][col]) is not list: grid[col_position][col] = [grid[col_position][col]]
                            MAU_dict[(col_position,col)] = grid[col_position][col]
                            grid = mini_arr_update(grid, (col_position, col))
                            array_update += 1 
                            

                        else:

                            grid[col_position][col].remove(rem_num)
                            array_update += 1 
                                       
                        
                       

    if num_inmini(grid, rem_num, (row, col)):


        box_x = col // 3  # j
        box_y = row // 3  # i
        for y in range(box_y * 3, box_y * 3 + 3):

            for x in range(box_x * 3, box_x * 3 + 3):
                                
                if len(grid[y][x]) > 1:

                    for n in grid[y][x]:
                                    
                                    
                        if n == rem_num and (row, col) != (y, x):
                            if len(grid[y][x]) == 2:

                                grid[y][x].remove(rem_num)
                                MAU_dict[(y,x)] = grid[y][x]
                                grid = mini_arr_update(grid, (y,x))
                                array_update += 1
                                

                            else: 

                                grid[y][x].remove(rem_num)
                                array_update += 1

    return grid
    
    
    
                                        
def only_option2(gamegrid):

    gamegrid = as_list(gamegrid)
    '''Create dictionary of positions and numbers set as clue'''
    oo_dict = dict()
    change_count = 0
    for i in range(9):
        for j in range(9):
            # if the length is greater than 1

            if type(gamegrid[i][j]) is not list: gamegrid[i][j] = [gamegrid[i][j]]
            if len(gamegrid[i][j]) > 1:
              
              
                for k in gamegrid[i][j]:
                   

                    if any(k in gamegrid[i][x] for x in range(9) if (i, x) != (i, j)):
                            gamegrid[i][j] = gamegrid[i][j]
                    else:                        

                        gamegrid[i][j] = [k]
                        oo_dict[(i,j)] = k
                        gamegrid = mini_arr_update(gamegrid, (i,j))
                        change_count += 1 
                        continue

                   

                    if any(k in gamegrid[x][j] for x in range(9) if (x, j) != (i, j)):
                        gamegrid[i][j] = gamegrid[i][j]

                    else:
                        gamegrid[i][j] = [k]
                        oo_dict[(i,j)] = k
                        
                        gamegrid = mini_arr_update(gamegrid, (i,j))
                        change_count += 1 

                        continue

                    if any(k in gamegrid[x][y] for x in range(i - i % 3, i - i % 3 + 3) for y in
                        range(j - j % 3, j - j % 3 + 3) if (x, y) != (i, j)):
                        gamegrid[i][j] = gamegrid[i][j]
                            
                    else:
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
   

# Used throughotu program and in main backsolver to compare grids.
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

