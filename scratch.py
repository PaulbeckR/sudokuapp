from BuildPuzzle import *
from PreparePuzzle import *
from FindSolutions import *
from CandidateLines import *
from Hidden import *

import copy
from TestingDisplay import *
import random
from GridDict import*


'''
Will establish a solver function that walks a given grid through each 
back solver , returning an updated grid.

uses double pair function to find any double pairs, if found board is not 
unique


'''

# grid_game = new_game_board(grid_new)
# arrays = create_arrays(grid_game)
#array_display(arrays, "Creating Arrays ")
#print(completed_count(grid))
#print_pos_grid(grid)

#basicsolved = basic_solve(arrays)
#array_display(basicsolved, "Basic Solve")
#checkedlonlies, total_returned  = check_lonely_nums(basicsolved)

# array_display(arrays, "Create Arrays")


def remaining_arrays(gridcount):
    count = 0
    for i in range(9):
        for j in range(9):
            if type(gridcount[i][j]) is not list: gridcount[i][j] = [ gridcount[i][j] ]

            if len(gridcount) == 1:
                count += 1            
                
                    
    return count



'''
Returns a position (i,j) on the grid wiht the smallest array (unsolved square with candidates) available
'''
def find_array(grid):
   
    for m in range(2,9):
        for i in range(9):
            for j in range(9):
                if type(grid[i][j]) is int:
                    grid[i][j] = [grid[i][j]]
                    pass
                    # for m in range(10):

                elif isinstance(grid[i][j], list):
                    if len(grid[i][j]) == m:
                        position = (i,j)
                        return position
    return None


# num_row num_col num_inmini (grid, num, pos): Returns TRUE if another int is found.
# is VALID will return FALSE if any are found, and TRUE if none are found (board is valid)

def is_valid_sudoku(board):
    # Check rows
    print("checking rows")
    for row in board:
        if not is_valid_row(row):
            return False
        
    # Check columns
    print("checking columsn")
    for col_idx in range(9):
        col = [board[row_idx][col_idx] for row_idx in range(9)]
        if not is_valid_row(col):
            return False
    
    # Check boxes
    print("checking boxes")
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [board[row_idx][col_idx] for row_idx in range(box_row, box_row+3) for col_idx in range(box_col, box_col+3)]
            if not is_valid_row(box):
                return False
    
    # All checks passed
    return True

def is_valid_row(row):
    seen = set()
    for num in row:
        if num == '.':
            continue
        if isinstance(num, int):
            if num in seen:
                return False
            seen.add(num)
        else:
            continue
    print("set is ", seen, "for row ", row)
    return True

def valid_check(grid):
    for i in range(9):
        for j in range(9):
            
            if isinstance(grid[i][j], int):
                for k in range(9):
                    if isinstance(grid[i][k], int):
                        if (grid[i][j] == grid[i][k]) and ((i,k) != (i,j)):
                            return False
                    if isinstance(grid[k][j], int):
                        if (grid[i][j] == grid[k][j]) and ((k,j) != (i,j)):
                            return False
                box_x = i // 3
                box_y = j // 3
                for l in range(box_y*3, box_y*3 + 3):
                    for m in range(box_x*3, box_x*3 + 3):
                        if isinstance(grid[l][m], int):
                            if grid[i][j] == grid[l][m] and (i, j) != (l,m):
                                return False
    return True



'''Counts how many single digit squares are in board'''
def solved_square(grid):
    count = 0
    for i in range(9):
        for j in range(9):
            if type(grid[i][j]) is not list: grid[i][j] = [grid[i][j]]

            if len(grid[i][j]) == 1:
                count += 1
    return count
        
''' Applies all strategies to board with available arrays'''
def runthrough(grid):
    
    total_changes = 10 
    
    while total_changes != 0:
    #run until 0 changes for all
        grida, changes = basic_solve(grid)
        print(" Basic Solve")
        print_pos_grid(grida)
        total_changes = changes
        print("TOTAL CHANGES " , total_changes)
        

        gridcl, count = check_lonely_nums(grida)
        print(" Candidate lines ")
        print_pos_grid(gridcl)
        total_changes += count
        print("TOTAL CHANGES " , total_changes)
    
        gridb, removed = gen_hidden_loop(gridcl) 
        
        total_changes += removed
        print(" Hidden ")
        print_pos_grid(gridb)
        print("TOTAL CHANGES " , total_changes)
        
        gridb2, count2 = basic_solve(gridb)
        gridc, xwingcount = xwing(gridb2)
        print("total removed from xwing", xwingcount )
        print_pos_grid(gridc)
        total_changes += xwingcount + count2
        
        print("TOTAL CHANGES IN RUNTHROUGH ", total_changes)
       # print("------------------------------------------")
        
    return gridc 



'''
Checks status of grid; if not valid (numbers do not align with original ), any doubles found, or 
if complete, is it valid - (aligns with original)

- May want to refine first valid check ("if validb == False"), as some solutiosn are removing all nums,
may have invalid board (two 9's). The solved and valid check should be good enough for checking against original

    - However... may have ' if not valid but complete... redo clues


'''    
def check_status(grid):
    status = 0
    doub_pairs2 = dict()
    validb = valid_check(grid)
    double_count, doub_pairs = double_pair(grid)
    doub_pairs2 = doub_pairs
    
    if validb == False:
        status = 3 
        return status, doub_pairs2
        
    elif double_count > 0:  
        status = 2
        return status , doub_pairs2
                
    elif solved_square(grid) == 81 and validb == True:    
        # add orig to check if a match? or keep out and let it be in the final method                 
        status = 1
        return status , doub_pairs2
    return status  , doub_pairs2
           


'''
Main solution method: Takes main (with arrays), original (completed board), overwrite (0's instead of arrays)

1. Attempts to solve, will check for "status", continue to solve unless a double is found, or invalid board. 

2. Will select random choice for solution. 

3. If any double found (add as clue and continue), alt. solution (start over), too many clues (start over)

##### May want to just add the "double check" method from BoardAnalysis for the matched board. 

'''

def solve_grid(main, original, overwrite):

    grid_o = copy.deepcopy(original)

    game_board = copy.deepcopy(overwrite)

    grid = copy.deepcopy(main)

    
        
    random_count = 0
    backup = [] 
    position = set()
    start_over = 0
    

    runthrough(grid)
    status , doub_pairs = check_status(grid)

    continue_solve = True
    
    #temp variable for testing
    count = 0
    
    
    backup2 = grid
    
    #list to hold all random positions used 
    rand_list = []
    rand_nums = []
    
    
   
    while continue_solve == True:
 
        # not actually getting solved square if not using arrays
        if solved_square(game_board) >= 40:
            #print("Starting over because TOO MANY CLUES")
            main, original, overwrite = create_new()
            random_count = 0 
            rand_nums.clear()
            rand_list.clear()     
            grid_o = copy.deepcopy(original)
            game_board = copy.deepcopy(overwrite)
            grid = copy.deepcopy(main) 
            position = set()

            start_over += 1

            
            #set status to not get triggered until reset of check status
            status = 5
    
        if status == 0: 
            print("Status 0 - arrays remain, choose random")
           
            grid, backup2, position =  random_guessing(grid)
            
            print("position after random method is ", position)
            if position != (10,10):  
                rand_list.append(position)
                rand_nums.append(grid[position[0]][position[1]])
            
            print("rand list ", rand_list)
            backup = [*backup2]
            random_count += 1

        elif status == 1:

            if test_if_equal(grid, original) == True: 

                continue_solve = False

                break
 
            else:
                
                #if a random was chosen, backtrack and add as clue, then retry.
                if random_count > 0:
                
                    mismatch = find_mismatch(grid, grid_o, rand_list)

                    #if there is a mismatch, what is it, add as clue. 
                    #if mismatch != None:
                        
                    backtrack_num = grid_o[mismatch[0]][mismatch[1]]
                    game_board[mismatch[0]][mismatch[1]] = [backtrack_num]

                
                    #add num as solved square to grid_c, start again with additional clue.              
                
                    tryagain = copy.deepcopy(main)
                    grid = tryagain
                    grid[mismatch[0]][mismatch[1]] = [backtrack_num]
                
                    rand_list.clear()
                    rand_nums.clear()
                    random_count = 0
                    status = 0
                #if no randoms chosen, but board complete and doesn't match, just start over as board had duplicate soluation
                # Could also just add a random clue, find array and add the solution.  
                else:

                    main, original, overwrite = create_new()
                    random_count = 0 
                    rand_list.clear()
                    rand_nums.clear()
                    grid_o = copy.deepcopy(original)
                    game_board = copy.deepcopy(overwrite)
                    grid = copy.deepcopy(main) 
                    position = set()

                    start_over += 1                    
                    status = 0
                
                
        elif status == 2 : 
            print("Status was 2 - found doubles")
            
            # Sets clue at first double pair.
            
            doub_pos = next(iter(doub_pairs.keys()))
            print("doub_pos is ", doub_pos)
            numbers = next(iter(doub_pairs.values()))
            
            r = doub_pos[0]
            c = doub_pos[1]
            solution_num = grid_o[r][c]
            
            #set copy to have additional clue            
            game_board[r][c] = [solution_num]
            tryagain = copy.deepcopy(main)
            
            #reset grid to most recent back up for continued backsolving
            grid = backup2
            #update grid to additional clue
            grid[r][c] = [solution_num]
            status = 0 

                
        # Board Not Valid: Try other random  THIS ISN'T BEING USED EVER  
        elif status == 3: 
           # print("status was 3 , Board not VALID")
            rem_pos = rand_list[0]
        
            backtrack_num = grid_o[rem_pos[0]][rem_pos[1]]
           # print("backtrack num", backtrack_num)
                
       
            game_board[rem_pos[0]][rem_pos[1]] = [backtrack_num]
           # print("SQUARES SOLVED IN NEW OVERWRITE ", solved_square(game_board))
                
            tryagain = copy.deepcopy(main)
            grid = tryagain
            grid[rem_pos[0]][rem_pos[1]] = [backtrack_num]
                
           # print("grid corrected to ", grid[rem_pos[0]][rem_pos[1]])
            rand_list.clear()
            rand_nums.clear()
            random_count = 0
            status = 0 
            
 
        runthrough(grid)
        status, doub_pairs = check_status(grid)
       # print("STATUS IS NOW (at bottom) ", status)
        #print_grid(original)
        #print_pos_grid(grid)
        count +=1
    #print("Start over attempts: ", start_over)

    print("INIT solved squares ", solved_square(main), "SQUARES SOLVED IN FINAL  ", solved_square(game_board) )

    #print("rand_nums list is ", rand_nums , "rand_list is ", rand_list, "random_count is ", random_count)
    
  
    
    return game_board, rand_nums, rand_list, grid_o
    

    
'''
Finds first and smallest array and selects random number to add as solution to continue solving. 

'''     
def random_guessing(grid):
    
   
    position = find_array(grid)
    print("position after fine_array is ", position)

    if position != None:
        # only if position is REAL
     
        print("Square nums at position : ", grid[position[0]][position[1]])
    
        #create copy to save as backup
        backup = copy.deepcopy(grid)    
    
        #Get nums for random choice. 
        select_nums = grid[position[0]][position[1]]
        #print("nums to choose from", select_nums)
    
        grid[position[0]][position[1]] = random.choice(select_nums)

        return grid , backup , position 
    
    else: 
        position = (10,10)
        return grid , grid , position


# Returns position (i,j) of the wrongly choses random item. Used for completed (81) grids.
def find_mismatch(grid,original, rand_list):
    #print("START OF FIND MISMATCH")
    #print("...............................")
    mismatch = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] != original[i][j]:
                mismatch.append((i,j))
        
    if len(rand_list) != 0:
        for k in rand_list:
            for j in mismatch:
                if k == j:
                    #print(k, "from rand_list, matches", j, "from mismatch")
                    miss_pos = (k)
                    return miss_pos
    #otherwise just return the first mismatch            
    else: 
        return mismatch[0]
                            



'''
Creates series of new boards: original (completed board), arraycopy (deep copy of arrays)
and grid_array (arrays for possible candidates added)

'''    
def create_new():

    grid_new = create_grid_fill()  
    #print_grid(grid_new)
    original = copy.deepcopy(grid_new)

  #  print("................................")
    game_board = new_game_board(grid_new)
    #print_grid(game_board)
    gridarray = create_arrays(game_board)
   # print(".................................")
   # print_pos_grid(gridarray)
    arraycopy = copy.deepcopy(gridarray)
    
    return gridarray, original, arraycopy




    

    
    
    

        
    
    
    
    
    
    












            
            
            
            
            




        
        
        
        
    
    








