from BuildPuzzle import *
from PreparePuzzle import*
from scratch import *
import copy

import random


'''
Back solver using remove 1 num at time approach:

1. create board
2. remove one num 
3. try to solve: (Runthrough + fill grid)
    - if solved with no rand choice - remove again. 
    - with rand choice: try all valid solutions - count num of valid. 
        - if 2+ solutions:
            - not unique, add back num. 
                - if 17-40: remove other num 
        - if 1 solution: remove another (if 17-40)
        

A. Fillgrid - solver uses smallest array available to select random. (shorter processing)
B. shuffle_positions - removes number at a position determined by random position list: (prevents removing same square?)
    - may not matter, would just retry again / odds low for dupes.
    
    
Two grids - one to remove/solve, and a copy of available arrays for removed nums. 


Main methods: 

Fillgrid: fills grid using backtracking for valid solutions + runthrough added. 

Unique: holds count for solve attempts; using most recent random as pivot point. 

Board Loop - primary method calling fill/unique methods. Maintains loop until unique board found with 17-40 clues.      
        

'''

def num_frequency(grid):
    num_freq = dict()
    num_list = [1,2,3,4,5,6,7,8,9]
    num_set = set()
    
 
    for i in range(9):
        
        for j in range(9):
            if grid[i][j] in num_list:
                num_set.add(grid[i][j])
    
    if len(num_set) == 9:

        return True
    return False
            
                



   

def run_all_strategies(rungrid):
    
    gcope = copy.deepcopy(rungrid)
    
    for i in range(9):
        for j in range(9):
            if type(gcope[i][j]) is not int: [gcope[i][j]] = gcope[i][j]
    
    
    grid = create_arrays(gcope)
    
    total_changes = 1
    
   
    basic = 0
    candidate_lines = 0
    hidden = 0
    xwings = 0
    
    # run until no changes found. 
    while total_changes != 0:
    
        #Find_Solutions.py : Only option and update arrays.
        # Also runs on a loop until no changes.
        grida, changes = basic_solve2(grid)
        basic  = basic + changes

        # Hidden.py : Hidden and Naked pairs and triples
        gridb, removed = gen_hidden_loop(grida) 
        hidden = hidden + removed
    
        # CandidateLines.py : candidate lines
        gridcl, count = check_lonely_nums(gridb)
        
        candidate_lines = candidate_lines + count
        
        gridx, xwingcount = xwing(gridcl)
        xwings = xwingcount + xwings

        
        update_changes, gridx = update_array(gridx)
        
        basic = update_changes + basic
        
        total_changes = (changes + count + removed + xwingcount)
    
    solved_after_run = solved_square(gridx)
    difficulty_dictionary = {"Basic": basic, "Hidden": hidden, "Candidates": candidate_lines, "Xwing": xwings, "Solved": solved_after_run}
   
    
    check = copy.deepcopy(gridx)
    checkas = back_to_board(check)    
            
    return gridx , difficulty_dictionary




def get_difficulty_level2(mydict):
    # Easy = 0 
    # Medium = 1
    # hard = 2 
    
    level = 0

    if  (mydict["Basic"] <= 10) and (mydict["Hidden"] >=4) or (mydict["Candidates"] >=4):
        level = 1 
    elif (mydict["Xwing"] >= 1 ):
        level =2
        
    #global difficulty_level
    return level



def is_valid_fill(grid):
    for i in range(9):
        for j in range(9):
            
            num = grid[i][j]
            pos = (i,j)
            if is_valid(grid, pos, num) == False:
                return False
    return True
    

def shuffle_positions():
    
    all_positions = []
    for i in range(9):
        for j in range(9):
            all_positions.append((i,j))
            
    random.shuffle(all_positions)
    
    return all_positions


def fill_withsolve(gridarry, gridzero):

    empty = find_empty(gridzero)
    if not empty:
        return True
    
    row, col = empty
   
   
    '''could use gridarray, just never update the arrays, '''
   
    nums = gridarry[row][col]    
    num_valid = 0
                
    for num in nums:
        if is_valid(gridzero, (row, col), num):
            num_valid +=1
            gridzero[row][col]= num
            if fill_withsolve(gridarry, gridzero):
                return True
         
            gridzero[row][col] = 0
    return False



def get_random_num(grid):

    
    rows = [0,1,2,3,4,5,6,7,8]
    cols = [0,1,2,3,4,5,6,7,8]
    
    random_num = 0
    while random_num == 0:
  
        ran_row = random.choice(rows)
        ran_col = random.choice(cols)
    
        random_num = grid[ran_row][ran_col]
        position = (ran_row, ran_col)
    
    if random_num != 0:
        return ran_row, ran_col
    


glob_difflevel = 9

my_dict = dict()

''' Takes filled board and removes one num at a time'''
def create_unique( orig_board, difficulty): 
    arrayboard = copy.deepcopy(orig_board)
    zerosboard = copy.deepcopy(orig_board)
    count = 0
    clue_max = 35
   
    
    
    
  
    while comp_sq(zerosboard) > 17:
    
        rand_row = 0
        rand_col = 0
      
        rand_row, rand_col = get_random_num(zerosboard)
        remove_backup = zerosboard[rand_row][rand_col]
        zerosboard[rand_row][rand_col] = 0
        arrayboard[rand_row][rand_col] = 0
       

        solution_count = try_to_solve2(arrayboard,  orig_board)
        count  += 1

        if count == 100:
            count = 0
            print("Reset" )
            complete_grid2 = create_grid_fill()
            arrayboard = copy.deepcopy(complete_grid2)
            zerosboard = copy.deepcopy(complete_grid2)
            orig_board = complete_grid2
            continue
  
        if solution_count == True:
            if (comp_sq(zerosboard) < clue_max):
          
                if (glob_difflevel == difficulty) and (num_frequency(zerosboard) == True):  
                    print(my_dict)
                    return orig_board, zerosboard
        elif (solution_count == False) or (num_frequency(zerosboard) == False) :
            arrayboard[rand_row][rand_col] = remove_backup
            zerosboard[rand_row][rand_col] = remove_backup
    print("BAD BOARD")
    return orig_board, zerosboard
   
# Think this is in SCRATCH
def back_to_board(grid):

    for i in range(9):
        for j in range(9):
            if type(grid[i][j]) is int: grid[i][j] = [grid[i][j]]
            
            if len(grid[i][j]) > 1: 
                grid[i][j] = 0
            
            if type(grid[i][j]) is list: [grid[i][j]] = grid[i][j]
    return grid
   
    
def try_to_solve2 (array2, orig):

    arrayrun, diff_dict= run_all_strategies(array2)
    
    diff_level = get_difficulty_level2(diff_dict)
    global my_dict
    my_dict = diff_dict
    
    global glob_difflevel
    glob_difflevel = diff_level

    Aa = copy.deepcopy(arrayrun)
    Zz = back_to_board(arrayrun)
    
    Bb = copy.deepcopy(Aa)
    Zz = back_to_board(Bb)
    
 
    mult= 0
    sol = 0 

    if (comp_sq(Zz) == 81):
        return True
    
    solutions, multiple_solutions = solve_loop(Aa, Zz, orig, sol, mult)
    
    
    if (solutions >0) and (multiple_solutions == 0):
        return True
   
    return False
    

def solve_loop (arrayb, zeros, og_board, solutions, multiple_solutions):

    valid_boards = 0
    count_loop = 0
    arrays_checked = dict()
    arrays_total = 0
    array_len = 0
    second_solution = dict()
    key = 0
  
    backup_zeros = copy.deepcopy(zeros)
    backup_zeros = back_to_board(backup_zeros)

    
    trysolve = copy.deepcopy(arrayb)
    
    
    tryzero = copy.deepcopy(arrayb)
    tryzero = back_to_board(tryzero)
    # while there are still arrays after a runthgouh (should skip for most clue removals.)
    if find_array(arrayb) != None:   
    
        
        for i in range(9):
            for j in range(9):
                if tryzero[i][j] == 0:
                    backup_sol = trysolve[i][j]

                    trynums = arrayb[i][j]
                    arrays_total += 1
                    array_len = array_len + len(trynums)
                    arrays_checked[(i,j)] = trynums
                    
                    
                    for num in trynums:
                        count_loop += 1
                        if is_valid(tryzero, (i, j), num):
                            solve_attempt = copy.deepcopy(trysolve)
                            
                            solve_attempt[i][j] = [num]
                            mini_arr_update(solve_attempt, (i,j))

                            solve_zeros = copy.deepcopy(solve_attempt)
                            solve_zeros = back_to_board(solve_zeros)
                        
                            if fill_withsolve(solve_attempt, solve_zeros) == True: 
                                solved_squares = comp_sq(solve_zeros)
                                if solved_squares == 81:
                                    
                         
                                
                                    if is_valid_fill(solve_zeros) == True:
                                        valid_boards += 1
                                
                                        if test_if_equal(solve_zeros, og_board) == False:
                                            key += 1                                        
                                            second_solution[key] = solve_zeros
                                  
                                            multiple_solutions += 1
                                   
                                            
                                            return solutions, multiple_solutions
                                        elif test_if_equal(solve_zeros, og_board) == True:
                                        
                           
                                            solutions += 1
                                         
                                        

                        trysolve[i][j] = backup_sol
                        solve_attempt = trysolve

                        solve_zeros[i][j] = 0
                        solve_zeros = tryzero
            
    return solutions, multiple_solutions



def new_sudoku_board(difficulty):
    
    
    complete_grid = create_grid_fill()

    orig, zeros = create_unique(complete_grid, difficulty)
    
    return zeros, orig



    
    