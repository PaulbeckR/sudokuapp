from BuildPuzzle import *
from PreparePuzzle import *
from FindSolutions import *
from CandidateLines import *
from Hidden import *

import copy
from TestingDisplay import *
import random


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


def find_array(grid):
   
    position = (0,0)
    
  
    for m in range(2,9):
        for i in range(9):
            for j in range(9):
                if isinstance(grid[i][j], int):
                    pass
                    # for m in range(10):
                    
                    #print("find array location", grid[i][j])
                else:
                    if len(grid[i][j]) == m:
                        position = (i,j)
                        return position
    return None
               
       
      
        
    



# num_row num_col num_inmini (grid, num, pos): Returns TRUE if another int is found.
# is VALID will return FALSE if any are found, and TRUE if none are found (board is valid)

def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_row(row):
            return False
        
    # Check columns
    for col_idx in range(9):
        col = [board[row_idx][col_idx] for row_idx in range(9)]
        if not is_valid_row(col):
            return False
    
    # Check boxes
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
                        


# def valid_board(valid_grid):
#     for i in range(9):
#         for j in range(9):
#             if type(valid_grid[i][j]) is not list: valid_grid[i][j] = [valid_grid[i][j]]
#             if len(valid_grid[i][j]) == 1:
#                 print("checking ", valid_grid[i][j])
#                 num = valid_grid[i][j] 
#                 if num_row(valid_grid, num, (i,j)) :
#                     print("My num", valid_grid[i][j], "was found in a row/col/box")  
#                     return False
#                 if  num_col(valid_grid, num, (i,j)):
#                     print("found in a column")
#                     return False
                    
#                 if num_inmini(valid_grid, num, (i,j)):
#                     print("found in a box")
#                     return False
#     return True




def solved_square(grid):
    count = 0
    for i in range(9):
        for j in range(9):
            if type(grid[i][j]) is not list: grid[i][j] = [grid[i][j]]

            if len(grid[i][j]) == 1:
                count += 1
    return count
        

def runthrough(grid):
    
    total_changes = 10 
    
    while total_changes != 0:
    #run until 0 changes for all
        grida, changes = basic_solve(grid)
        print(" Basic Solve")
        #print_pos_grid(grida)
        total_changes = changes
        print("TOTAL CHANGES " , total_changes)
        

        gridcl, count = check_lonely_nums(grida)
        print(" Candidate lines ")
        #print_pos_grid(gridcl)
        # print("solved squares ", remaining_arrays(grid))
        total_changes += count
        print("TOTAL CHANGES " , total_changes)
    
        gridb, removed = gen_hidden_loop(gridcl) 
        
        total_changes += removed
        print(" Hidden ")
        #print_pos_grid(gridb)
        print("TOTAL CHANGES " , total_changes)
        
        print_pos_grid(gridb)
        
    return gridb, 
    
def check_status(grid):
    status = 0
    doub_pairs2 = dict()
    validb = valid_check(grid)
    #print("valid ??? ", validb)
    double_count, doub_pairs = double_pair(grid)
    doub_pairs2 = doub_pairs
    print("doubp dict", doub_pairs2)
    
    if validb == False:
        print("Board is NOT VALID")
        status = 3 
        return status, doub_pairs2
        
    elif double_count > 0:  
        print("Found double pair, not unique board")
        status = 2
        return status , doub_pairs2
                
    elif solved_square(grid) == 81 and validb == True:    
        print("Board is VALID and is COMPLETE")
        # add orig to check if a match? or keep out and let it be in the final method                 
        status = 1
        return status , doub_pairs2
    return status  , doub_pairs2
           




def solve_grid(main, original, overwrite):
    print("Original")
    print_grid(original)
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    #print("GRID _ o ")
    grid_o = copy.deepcopy(original)
    #print_grid(grid_o)
    #print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    #print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    game_board = copy.deepcopy(overwrite)
    print("OVERWRITE : board to update for final gameboard")
    print_pos_grid(game_board)
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("MAIN GRID to work from")
    grid = copy.deepcopy(main)
    print_pos_grid(grid)
    
        
    random_count = 0
    backup = [] 
    position = set()
    start_over = 0
    
   
    # {1: "Solved and valid", 2: "Not Unique", 3: "Not valid solution"}
    
    print("START SOLVE:::::::::::::::::::")
    print("solved squares ", solved_square(grid))
   

    # Try to solve grid with all methods
    runthrough(grid)
    status , doub_pairs = check_status(grid)
    
    print("Status is ", status)
    print("Doub_pairs is ", doub_pairs)
    
    continue_solve = True
    
    #temp variable for testing
    count = 0
    
    
    backup2 = grid
    
    #list to hold all random positions used 
    rand_list = []
    rand_nums = []
    
    
   
    while continue_solve == True:

        print(rand_list, "rand_list")
 
        # not actually getting solved square if not using arrays
        if solved_square(game_board) >= 35:
            print("Starting over because TOO MANY CLUES")
            main, original, overwrite = create_new()
            random_count = 0 
            rand_nums.clear()
            rand_list.clear()     
            grid_o = copy.deepcopy(original)
            game_board = copy.deepcopy(overwrite)
            grid = copy.deepcopy(main) 
            position = set()
            print("This is the new grid")
            print_pos_grid(grid)
            start_over += 1
                      
            print("SQUARES SOLVED IN NEW OVERWRITE ", solved_square(game_board))
            
            #set status to not get triggered until reset of check status
            status = 5
    
        if status == 0: 
            print("Status 0 - arrays remain, choose random")
           
            grid, backup2, position =  random_guessing(grid)
            
            print(".................. Adding to random list ....................")
            rand_list.append(position)
            rand_nums.append(grid[position[0]][position[1]])
            
            print("rand list ", rand_list)
            backup = [*backup2]
            random_count += 1
            print("random count ", random_count)
            print("Printing POS grid at STATUS 0 (arrays remain) ")
            print_pos_grid(grid)
           
           
    
        elif status == 1:
            print("Status was 1 - completed grid. Does it match??? ")
            #print_grid(original)
            # check if matched to original grid. 
            print_pos_grid(grid)
            if test_if_equal(grid, original) == True: 
                print("Board MATCHES!!!!")
                print("INIT solved squares ", solved_square(main))
                print("SQUARES SOLVED IN FINAL  ", solved_square(game_board))
                print("random count at complete", random_count)
                print("final count - rounds", count)
                print("Start over attempts: ", start_over)
                
                print("Rand list at FINAL ", rand_list)
                print("Rand NUMS at final ", rand_nums)
                continue_solve = False
                print("Actual game board ")
                print_grid(game_board)
                break
 
            else:
                print("Board did not match")
             
                print("random count ", random_count)
                
                #if a random was chosen, backtrack and add as clue, then retry.
                if random_count > 0:
                    
                    
                    print("rand list is ", rand_list, "and first item is ")
                    #rem_pos = rand_list[0]
                    #print(rem_pos, "is first rem_pos from rand_list")                
                    mismatch = find_mismatch(grid, grid_o, rand_list)

                    #if there is a mismatch, what is it, add as clue. 
                    #if mismatch != None:
                        
                    print("using mismatch, ", grid_o[mismatch[0]][mismatch[1]])
                    backtrack_num = grid_o[mismatch[0]][mismatch[1]]
                    game_board[mismatch[0]][mismatch[1]] = [backtrack_num]
                    
                    # else:
                    #     rem_pos = rand_list[0]               
                    #     backtrack_num = grid_o[rem_pos[0]][rem_pos[1]]
                    #     print("backtrack num", backtrack_num)
                    #     game_board[rem_pos[0]][rem_pos[1]] = [backtrack_num]
                
                    #add num as solved square to grid_c, start again with additional clue.
                    
                    print("SQUARES SOLVED IN NEW OVERWRITE ", solved_square(game_board))
              
                
                    tryagain = copy.deepcopy(main)
                    grid = tryagain
                    grid[mismatch[0]][mismatch[1]] = [backtrack_num]
                
                    print("GRID AFTER AT BOARD NOT MATCH")
                    print_pos_grid(grid)
                
                
                    print("grid corrected at STATUS 1", grid[mismatch[0]][mismatch[1]], "at position", mismatch)
                    rand_list.clear()
                    rand_nums.clear()
                    random_count = 0
                    status = 0
                #if no randoms chosen, but board complete and doesn't match, just start over as board had duplicate soluation
                # Could also just add a random clue, find array and add the solution.  
                else:
                    print("STARTING OVER ")
                    main, original, overwrite = create_new()
                    random_count = 0 
                    rand_list.clear()
                    rand_nums.clear()
                    grid_o = copy.deepcopy(original)
                    game_board = copy.deepcopy(overwrite)
                    grid = copy.deepcopy(main) 
                    position = set()
                    print("This is the new grid")
                    print_pos_grid(grid)
                    start_over += 1
                    
                    print("SQUARES SOLVED IN NEW OVERWRITE ", solved_square(game_board))
                    status = 0
                
                
        elif status == 2 : 
            print("Status was 2 - found doubles")
            
            # Sets clue at first double pair.
            
            doub_pos = next(iter(doub_pairs.keys()))
            numbers = next(iter(doub_pairs.values()))
            
            r = doub_pos[0]
            c = doub_pos[1]
        
            solution_num = grid_o[r][c]
            
            #set copy to have additional clue            
            game_board[r][c] = [solution_num]
            print("SQUARES SOLVED IN NEW OVERWRITE ", solved_square(game_board))
            tryagain = copy.deepcopy(main)
            
            #reset grid to most recent back up for continued backsolving
            grid = backup2
            #update grid to additional clue
            grid[r][c] = [solution_num]
            
            
            print("updated grid at STATUS 2", grid[r][c])
            
                 
            status = 0 

                
        # Board Not Valid: Try other random  THIS ISN'T BEING USED EVER  
        elif status == 3: 
            print("status was 3 , Board not VALID")
            rem_pos = rand_list[0]
        
            backtrack_num = grid_o[rem_pos[0]][rem_pos[1]]
            print("backtrack num", backtrack_num)
                
       
            game_board[rem_pos[0]][rem_pos[1]] = [backtrack_num]
            print("SQUARES SOLVED IN NEW OVERWRITE ", solved_square(game_board))
                
            tryagain = copy.deepcopy(main)
            grid = tryagain
            grid[rem_pos[0]][rem_pos[1]] = [backtrack_num]
                
            print("grid corrected to ", grid[rem_pos[0]][rem_pos[1]])
            rand_list.clear()
            rand_nums.clear()
            random_count = 0
            status = 0 
            
 
        runthrough(grid)
        status, doub_pairs = check_status(grid)
        print("STATUS IS NOW (at bottom) ", status)
        print_grid(original)
        print_pos_grid(grid)
        count +=1
    print("Start over attempts: ", start_over)

    print("INIT solved squares ", solved_square(main), "SQUARES SOLVED IN FINAL  ", solved_square(game_board) )

    print("rand_nums list is ", rand_nums , "rand_list is ", rand_list, "random_count is ", random_count)
    return grid, rand_nums, rand_list
    
           
        
 
    
# to run if there are remaining Arrays that ar NOT doubles.     
def random_guessing(grid):
    
   
    position = find_array(grid)
    print("position is ", position)

    if position != None:
        
     
        print("Square nums at position : ", grid[position[0]][position[1]])
    
        #create copy to save as backup
        backup = copy.deepcopy(grid)    
    
        #Get nums for random choice. 
        select_nums = grid[position[0]][position[1]]
        print("nums to choose from", select_nums)
    
        grid[position[0]][position[1]] = random.choice(select_nums)

        return grid , backup , position


# Returns position (i,j) of the wrongly choses random item. Used for completed (81) grids.
def find_mismatch(grid,original, rand_list):
    print("START OF FIND MISMATCH")
    print("...............................")
    mismatch = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] != original[i][j]:
                mismatch.append((i,j))
    print("mismatches are ", mismatch)
    print("rand list is ", rand_list)
    #return mismatch that was a random choice, if random_choice list exists            
    if len(rand_list) != 0:
        for k in rand_list:
            for j in mismatch:
                if k == j:
                    print(k, "from rand_list, matches", j, "from mismatch")
                    miss_pos = (k)
                    return miss_pos
    #otherwise just return the first mismatch            
    else: 
        return mismatch[0]
                            
    
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
    gridarr = copy.deepcopy(gridarray)
    
    return gridarray, original, gridarr


# gridarray, original, game_board = create_new()
# # #print_grid(original)

# final = solve_grid(gridarray, original, game_board)

# # #print_grid(original)

# test = get_solutions(final)   


# print_grid(test)


    

    
    
    

        
    
    
    
    
    
    












            
            
            
            
            




        
        
        
        
    
    








