from BuildPuzzle import *
from collections import defaultdict
from PreparePuzzle import *
from scratch import *
import pandas as pd
import time 
import csv
import copy

'''
Solving time: Measure the average time taken to solve a Sudoku puzzle.
You can compare this against other algorithms or human solving times to 
show the efficiency of your algorithm.

Moves or iterations: Record the number of moves or iterations required to 
solve a puzzle. This can be a measure of your algorithm's search efficiency.

Solution optimality: Analyze the optimality of the solutions produced by 
your algorithm. If your algorithm guarantees the minimum number of steps 
or moves to solve a puzzle, it can be considered optimal.

Difficulty level: Test your algorithm on Sudoku puzzles with varying
difficulty levels (e.g., easy, medium, hard, and expert). Analyze how 
the solving time, number of moves or iterations, and solution optimality
metrics vary across different difficulty levels.

Branching factor: Calculate the average branching factor, which 
represents the average number of possible moves (or branches) your 
algorithm generates at each step. A lower branching factor generally 
means a more efficient search.

Memory usage: Measure the memory usage of your algorithm during its 
execution. This can be useful for comparing the resource efficiency 
of your algorithm with other algorithms.

Scalability: Test your algorithm on larger Sudoku puzzles 
(e.g., 16x16 or 25x25 grids) and analyze its performance. 
This will help demonstrate how well your algorithm scales 
to handle more complex problems.

Robustness: Test your algorithm on a large number of Sudoku puzzles, 
including some edge cases, to demonstrate its ability to solve a wide 
range of problems consistently.

Comparisons with other algorithms: Compare the performance of your 
algorithm with existing Sudoku-solving algorithms using the above 
metrics. This will help demonstrate the advantages and improvements 
your unique algorithm offers over existing methods.

- using numpy for arrays instead of gen python lists. 
- changing loop max (250) for resetting board. 


### I need: 
- tracking of time / time between each run
-trackign of number of steps to solve 
- just the runthrough and solve? - count randoms
-   - choose one random and runthrough again
    - choose another random and runthrough again... 
- use previous scratch???

- try different easy/diff/hard 
    - seperate counts for trips/doubls
    - seperate counts for only opt / single cand
    - seperate counts for cand lines -????



Both creating unique boards and solving them??

'''
grid_starttime = 0
board_startover = 0
total_elapsed = 0 
runthrough_count = 0
#dict of list of run through times for each board.
analitems_dict = dict()
runthrough_times = dict()


# Test: get 10 unique boards to solve,  save to file. CSV of list of lists?


def is_valid_fill(grid):
    for i in range(9):
        for j in range(9):
            
            num = grid[i][j]
            pos = (i,j)
            if is_valid(grid, pos, num) == False:
               # print("NOT VALID ", pos, num)
                return False
    return True
    

def shuffle_positions():
    
    all_positions = []
    for i in range(9):
        for j in range(9):
            all_positions.append((i,j))
            
    random.shuffle(all_positions)
    
    return all_positions



def get_random_num(grid):
    #print("Grid inside get_random")
    #print_grid(grid)
    
    rows = [0,1,2,3,4,5,6,7,8]
    cols = [0,1,2,3,4,5,6,7,8]
    
    random_num = 0
    while random_num == 0:
  
        ran_row = random.choice(rows)
        #print("ran_row is ", ran_row)
        ran_col = random.choice(cols)
        #print("ran_col is ", ran_col)
    
        random_num = grid[ran_row][ran_col]

    
        position = (ran_row, ran_col)
    
    if random_num != 0:
        
    
    
    
        return ran_row, ran_col


# Think this is in SCRATCH
def back_to_board(grid):

    for i in range(9):
        for j in range(9):
            if type(grid[i][j]) is int: grid[i][j] = [grid[i][j]]
            
            if len(grid[i][j]) > 1: 
                grid[i][j] = 0
            
            if type(grid[i][j]) is list: [grid[i][j]] = grid[i][j]
    return grid
   
        

           
           


# BACKSOLVER 
def num_frequency(grid):
    num_freq = dict()
    num_list = [1,2,3,4,5,6,7,8,9]
    num_set = set()
    
 
    for i in range(9):
        
        for j in range(9):
            if grid[i][j] in num_list:
                num_set.add(grid[i][j])
    
   # print("num set is ", num_set)
   
    if len(num_set) == 9:

        return True
    return False
            

solved_after_run = 0
def anal_run(rungrid):
#print("STARTING RUNTHROUGH ")
    global runthrough_count
    runthrough_count += 1
    gcope = copy.deepcopy(rungrid)
    
    #to reduce time - set a count variable?
    for i in range(9):
        for j in range(9):
            if type(gcope[i][j]) is not int: [gcope[i][j]] = gcope[i][j]
    
    grid = create_arrays(gcope)

    total_changes = 1
    loop_count = 0
    basic = 0
    candidate_lines = 0
    hidden = 0
    xwings = 0
    starting_clues = solved_square(grid)
    
    while total_changes != 0:
    #run until 0 changes for all
        loop_count += 1
        grida, changes = basic_solve2(grid)
        basic  = basic + changes
        clues_basic = solved_square(grida)
        basic_solved = clues_basic - starting_clues
        
        gridb, removed = gen_hidden_loop(grida) 
        hidden = hidden + removed
        
        gridcl, count = check_lonely_nums(gridb)
        candidate_lines = candidate_lines + count

        gridx, xwingcount = xwing(gridcl)
        xwings = xwingcount + xwings

        
        update_changes, gridx = update_array(gridx)
        basic = update_changes + basic
        total_changes = (changes + count + removed + xwingcount)
    
    global solved_after_run
    solved_after_run = solved_square(gridx)
    #print("solved after run ", solved_after_run)
    difficulty_dictionary = {"Starting_clues": starting_clues, "Basic": basic, 
                             "Basic_solved": basic_solved,  "Hidden": hidden, 
                             "Candidates": candidate_lines, "Xwing": xwings, 
                             "Solved": solved_after_run}
   
    
    # check = copy.deepcopy(gridx)
    # checkas = back_to_board(check)    
    
    #print(solved_square(gridx), "AFTER!!!! full runthrough", comp_sq(checkas))
    loop_count = 0
    return gridx , difficulty_dictionary




def anal_diff(mydict):
    # Easy = 0 
    # Medium = 1
    # hard = 2 
    
    level = 0
    
   
    # if  (mydict["Basic"] <= 20) and (mydict["Xwing"] == 0) or ((mydict["Hidden"] >=4) and (mydict['Hidden'] <=12)) or ((mydict["Candidates"] >=4) and (mydict["Candidates"] <=12))or (mydict["Solved"] <=75):
    #     level = 1 
    # elif (mydict["Xwing"] >= 1 ) or (mydict["Hidden"] >=8) or (mydict["Candidates"] >=8) or (mydict["Solved"] <= 60):
    #     level =2
    
    
    
    if  (mydict["Xwing"] == 0) and ((mydict["Hidden"] >=1) and (mydict['Hidden'] >=1)):
        level = 1
    
    elif (mydict["Xwing"] >= 1 ) or (mydict["Solved"] < 81):
        level = 2
        
    #global difficulty_level
    return level




def fill_withsolve(gridarry, gridzero):
    empty = find_empty(gridzero)

    if not empty:
        return True
    
    row, col = empty
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



    


glob_difflevel = 9


''' Takes filled board and removes one num at a time'''
def create_unique( orig_board, difficulty, max_count, clue_max): 
    arrayboard = copy.deepcopy(orig_board)

    zerosboard = copy.deepcopy(orig_board)

    count = 0
  
    while comp_sq(zerosboard) > 15:
    #while count < 60:
    
        rand_row = 0
        rand_col = 0
      
        rand_row, rand_col = get_random_num(zerosboard)
    
       
        remove_backup = zerosboard[rand_row][rand_col]
        
       # print("REMOVING NEXT CLUE FROM CREATE_UNIQUE>>>>>>>>>>>>>>>>>>>>", (rand_row, rand_col) ,"CLUE COUNT IS", comp_sq(zerosboard))
        
        zerosboard[rand_row][rand_col] = 0
        arrayboard[rand_row][rand_col] = 0
       

        isit_solved = try_to_solve2(arrayboard,  orig_board, difficulty)

        count  += 1

        if count == max_count:

            
            count = 0
            
            global board_startover 
            board_startover += 1
            

            complete_grid2 = create_grid_fill()
            arrayboard = copy.deepcopy(complete_grid2)
    
            zerosboard = copy.deepcopy(complete_grid2)
            
            orig_board = complete_grid2

            continue
  
        if isit_solved == True:
            count = 0
            if (comp_sq(zerosboard) < clue_max):
          
                if (glob_difflevel == difficulty) and (num_frequency(zerosboard) == True):  
                    global solved_after_run
                    
                    return orig_board, zerosboard, 
                    
                
         
        elif (isit_solved == False) or (num_frequency(zerosboard) == False) :
            arrayboard[rand_row][rand_col] = remove_backup
            zerosboard[rand_row][rand_col] = remove_backup

   
   
    return orig_board, zerosboard, 
   


diff_level = 9
def try_to_solve2 (array2, orig, difficulty):

    arrayrun, diff_dict= anal_run(array2)
    
    global diff_level
    diff_level = anal_diff(diff_dict)
    global analitems_dict
    analitems_dict = diff_dict
    
    # only update global difficulty if looking for specific difficulty level. Otherwise, keep all unique boards.
    if difficulty != 9:
        
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

    total_filled_boards = 0
    valid_boards = 0
    invalid_boards = 0
    count_loop = 0
    arrays_checked = dict()
    invalid_boards = 0
    arrays_total = 0
    array_len = 0
    something_else = 0
    second_solution = dict()
    key = 0
    
    backup_zeros = copy.deepcopy(zeros)
    backup_zeros = back_to_board(backup_zeros)

    trysolve = copy.deepcopy(arrayb)
    tryzero = copy.deepcopy(arrayb)


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
                                if solved_squares != 81:

                                    invalid_boards += 1
                                    continue
                         
                                else:
                                    if is_valid_fill(solve_zeros) == True:
                                        valid_boards += 1

                                
                                        if test_if_equal(solve_zeros, og_board) == False:
                                            key += 1
                                 
                                            second_solution[key] = solve_zeros
                                  
                                            multiple_solutions += 1

                                        if multiple_solutions >= 1:

                                            return solutions, multiple_solutions
                                        elif test_if_equal(solve_zeros, og_board) == True:

                                            solutions += 1

                                        else: 

                                            something_else += 1

                                    else:
                                        invalid_boards += 1

                            else: 
                                ''' When fill with solve is FALSE - it means it retraced all steps and tried all pathes, no solutions found!!'''
  
                                invalid_boards += 1

                        solve_attempt = trysolve

                        solve_zeros[i][j] = 0
                        solve_zeros = tryzero
                        
   

    
    return solutions, multiple_solutions



def new_sudoku_board(difficulty, maxc, clue_max):
    
    complete_grid = create_grid_fill()

    orig, zeros = create_unique(complete_grid, difficulty, maxc, clue_max)
    
    return zeros, orig

#count is how many of each type of configuration
def board_loop(count, diffs, max_rounds, clue_max):
    
    all_grids = dict()
    all_dicts = dict()
    num = 1
   
    #max_rounds = [50,100,150, 200, 300]
    total_count = 1
    for i in max_rounds:
        #diff = 2
        #iffs = [9]
        maxc = i
        #print("starting level", diff)
        for k in diffs:
            
        
            while num <= count:
                global grid_starttime
                grid_starttime += time.time()
        
        
                game_board, solution = new_sudoku_board(k, maxc, clue_max)
        
                global total_elapsed
                total_elapsed += time.time() - grid_starttime
                #print("elapsed time is ", total_elapsed)

        
                all_grids[num] = game_board
        
                global analitems_dict, board_startover, diff_level
            
                analitems_dict["Start_overs"] = board_startover
                analitems_dict["Elapsed_time"] = total_elapsed
                analitems_dict["Max_count"] = maxc
                analitems_dict["Difficulty_Level"] = k
                analitems_dict["Actual_difficulty"] = diff_level
                analitems_dict["Board"] = game_board
                analitems_dict["Solution"] = solution
                all_dicts[total_count] = analitems_dict
                total_count += 1
                #print("total count ", total_count)
                # add diff_dict to file or larger list of whatever 
                grid_starttime = 0
                total_elapsed = 0
                board_startover = 0
                num +=1
            
            
            num = 0
        
    
    return all_grids, all_dicts
        

# zeros , orig = new_sudoku_board(2, 150)
# print_grid(zeros)
# print(".................")
# print_grid(orig)

diffs = [0,1,2]
max_rounds = [50,100,150,200,300,400,500,750,1000]
board_count = 100
clue_max = 35


#ten_grids, ten_dicts = board_loop(board_count, diffs, max_rounds, clue_max)   
#print(len(ten_grids))
# for i in ten_grids:
#     print("          ")
#     print("Grid ", i)
#     print_grid(ten_grids[i])
    
# for i in ten_dicts:
#     print("          ")
#     print("Grid ", i)
#     print(ten_dicts[i])

# diff_list = []    
# for key, value in ten_dicts.items():
#     if key == "Actual_difficulty":
#         diff_list.append(value)

# print(diff_list)
        

import csv


def write_nested_dict_to_file(nested_dict, filename):
    with open(filename, 'w', newline='') as f:
        # Write header line (keys)
        header = nested_dict[list(nested_dict.keys())[0]].keys()
        writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()

        # Write the values for each dictionary
        for key, inner_dict in nested_dict.items():
            # Convert the "Board" value to a string and escape commas
            inner_dict["Board"] = str(inner_dict["Board"]).replace(",", "|")
            inner_dict["Solution"] = str(inner_dict["Solution"]).replace(",", "|")

            writer.writerow(inner_dict)


output_filename = 'MultRounds_AllLev.csv'
# write_nested_dict_to_file(ten_dicts, output_filename)

             
                       


df = pd.read_csv(output_filename, usecols = ["Start_overs", "Elapsed_time", "Max_count" , "Difficulty_Level"])
print(df.head())


# #, columns = [ ])
# print(df)
# print(df.columns)
# print(df['Max_count'].min())
# print("time mean", df['Elapsed_time'].mean())


# # 
print(df.describe())

# meansdf = df.groupby(['Max_count']).mean()

# print(meansdf)

            
            
### File not actually getting all max countes.....