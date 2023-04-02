from BuildPuzzle import *
from PreparePuzzle import*
from scratch import *


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





evil_sudoku = [[0,9,3,0,0,4,5,6,0],
               [0,6,0,0,0,3,1,4,0],
               [0,0,4,6,0,8,3,0,9],
               [9,8,1,3,4,5,0,0,0],
               [3,4,7,2,8,6,9,5,1],
               [6,5,2,0,7,0,4,8,3],
               [4,0,6,0,0,2,8,9,0],
               [0,0,0,4,0,0,0,1,0],
               [0,2,9,8,0,0,0,3,4]]

evil_sudoku2 = [[0,9,3,0,0,0,5,6,0],
               [0,6,0,0,0,3,1,4,0],
               [0,0,4,6,0,8,3,0,9],
               [9,8,1,3,4,5,0,0,0],
               [3,4,7,2,8,6,9,5,1],
               [6,5,2,0,7,0,4,8,3],
               [4,0,0,0,0,2,8,9,0],
               [0,0,0,4,0,0,0,1,0],
               [0,2,9,8,0,0,0,3,4]]

evil_orig = [[2,9,3,7,1,4,5,6,8],
               [7,6,8,5,9,3,1,4,2],
               [5,1,4,6,2,8,3,7,9],
               [9,8,1,3,4,5,7,2,6],
               [3,4,7,2,8,6,9,5,1],
               [6,5,2,9,7,1,4,8,3],
               [4,7,6,1,3,2,8,9,5],
               [8,3,5,4,6,9,2,1,7],
               [1,2,9,8,5,7,6,3,4]]
evil_sudoku_zero = [[0,9,3,0,0,4,5,6,0],
               [0,6,0,0,0,3,1,4,0],
               [0,0,4,6,0,8,3,0,9],
               [9,8,1,3,4,5,0,0,0],
               [3,4,7,2,8,6,9,5,1],
               [6,5,2,0,7,0,4,8,3],
               [4,0,6,0,0,2,8,9,0],
               [0,0,0,4,0,0,0,1,0],
               [0,2,9,8,0,0,0,3,4]]

test_game1 = [[2,0,1,0,3,0,6,0,7],
               [0,0,6,0,9,0,1,0,8],
               [0,0,0,0,6,0,0,0,2],
               [9,1,7,0,5,8,0,2,0],
               [0,5,0,0,0,0,0,0,0],
               [0,2,0,0,7,0,8,0,5],
               [0,6,0,5,0,0,0,0,0],
               [0,8,4,9,0,2,7,6,0],
               [0,3,2,6,8,0,5,0,0]]


test_oggame1 = [[2,9,1,8,3,5,6,4,7],
               [3,7,6,2,9,4,1,5,8],
               [8,4,5,7,6,1,9,3,2],
               [9,1,7,3,5,8,4,2,6],
               [4,5,8,1,2,6,3,7,9],
               [6,2,3,4,7,9,8,1,5],
               [7,6,9,5,4,3,2,8,1],
               [5,8,4,9,1,2,7,6,3],
               [1,3,2,6,8,7,5,9,4]]

test_grid2 = [[0, 6, 2,0, 0, 0, 0, 0, 1],
[0, 5, 9, 0, 0, 0, 6, 0, 7],
[8, 1, 7, 0, 0, 5, 2, 0, 0],
[7, 0, 6, 0, 2, 9, 0, 0, 8],
[0, 0, 0, 4, 6, 0, 9,0, 0],
[1, 0, 4, 8, 0, 0,5, 0, 6],

[0, 0, 8,0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 9, 0, 1, 8, 5],
[5, 0, 0, 0, 0, 0, 0, 0, 0]]

og_grid2 = [[4, 6, 2,9, 7, 3, 8, 5, 1],
[3, 5, 9, 2, 1, 8, 6, 4, 7],
[8, 1, 7, 6, 4, 5, 2, 3, 9],
[7, 3, 6, 5, 2, 9, 4, 1, 8],
[2, 8, 5, 4, 6, 1, 9,7, 3],
[1, 9, 4, 8, 3, 7,5, 2, 6],

[9, 7, 8,1, 5, 2, 3, 6, 4],
[6, 2, 3, 7, 9, 4, 1, 8, 5],
[5, 4, 1, 3, 8, 6, 7, 9, 2]]


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
            
                
def add_arrays(game_board):

    possible_nums = []
    for i in range(9):
        for j in range(9):
    
            value = game_board[i][j]
            if type(value) is not list:value = [value]
           
            if value == [0]:
                #check row
                possible_nums = list(range(1, 10))
                for k in range(9):
                    if game_board[i][k] in possible_nums:
                        possible_nums.remove(game_board[i][k])
                # check COLUMN
                for k in range(9):
                    if game_board[k][j] in possible_nums:
                        possible_nums.remove(game_board[k][j])
                # check 3x3 space
                row_start = i - i % 3
                col_start = j - j % 3

                for x in range(row_start, row_start+3):
                    for y in range(col_start, col_start+3):
                        if game_board[x][y] in possible_nums:
                            possible_nums.remove(game_board[x][y])
                possible_numbers_grid[i][j] = possible_nums
            else: 
                possible_nums = game_board[i][j]
                # print("after first iter" , possible_nums)
                possible_numbers_grid[i][j] = possible_nums

    return possible_numbers_grid  



   

def runthrough3(rungrid):
#print("STARTING RUNTHROUGH ")
    
    gcope = copy.deepcopy(rungrid)
    
    for i in range(9):
        for j in range(9):
            if type(gcope[i][j]) is not int: [gcope[i][j]] = gcope[i][j]
    
    
    grid = create_arrays(gcope)
    
    
   # print("AFTER ADDING ARRAYS IN RUNTHROUGH ")
    #print_pos_grid(grid)
   
    
    total_changes = 1
    
    intial_solved = solved_square(grid)
    basic = 0
    candidate_lines = 0
    hidden = 0
    xwings = 0
    
    while total_changes != 0:
    #run until 0 changes for all
        
       # print(" Basic Solve 2")
        grida, changes = basic_solve2(grid)
        basic  = basic + changes
        #print_pos_grid(grida)
        
        
       # print("BASIC CHANGES " , changes)
        
        #print("GRID BEFORE HIDDEN")
        #print_pos_grid(grida)
        
       # print(" Hidden ")
        gridb, removed = gen_hidden_loop(grida) 
        
        
        hidden = hidden + removed
        #print("Hidden Changes " , hidden)
        
        "Instead of basic solve, could add array update to remove method in hidden"
        #gridb2, count2 = basic_solve(gridb)
        
        #print(" Candidate lines ")
        gridcl, count = check_lonely_nums(gridb)
        
        candidate_lines = candidate_lines + count
       # print("Candidate lines Removed", candidate_lines)
    
        #Already updating arrays within CL
        
        
        gridx, xwingcount = xwing(gridcl)
        xwings = xwingcount + xwings
       # print("total removed from xwing", xwingcount )
        #print_pos_grid(gridc)
        
        
        #print("TOTAL CHANGES IN RUNTHROUGH Loop ", total_changes)
        # print("------------------------------------------")
        
        update_changes, gridx = update_array(gridx)
        print("newly changed from final update_array", update_changes)
        basic = update_changes + basic
        
        total_changes = (changes + count + removed + xwingcount)
    
    solved_after_run = solved_square(gridx)
    difficulty_dictionary = {"Basic": basic, "Hidden": hidden, "Candidates": candidate_lines, "Xwing": xwings, "Solved": solved_after_run}
    #print("diff_dict" , difficulty_dictionary)
    
  
        
 
    # print("xwings: ", xwings)
    # print("(doubs/trips): ", hidden)
    # print("candidate lines: ", candidate_lines)
    # print("basic solve: ", basic)
    # print("initial solved: ", intial_solved)
    
    check = copy.deepcopy(gridx)
    checkas = back_to_board(check)    
    
    #print(solved_square(gridx), "AFTER!!!! full runthrough", comp_sq(checkas))
        
    return gridx , difficulty_dictionary

def get_difficulty_level(board):
    # Easy = 0 
    # Medium = 1
    # hard = 2 
    
    level = 0
    grid, mydict = runthrough3(board)
    
    print(mydict)
    
    
 
    if  (mydict["Basic"] <= 10) and (mydict["Hidden"] >=4) or (mydict["Candidates"] >=4) or (mydict["Solved"] <=35):
        level = 1 
    elif (mydict["Xwing"] >= 1 ) or (mydict["Hidden"] >=8) or (mydict["Solved"] <= 30):
        level =2
        
    #global difficulty_level
    return level


def get_difficulty_level2(mydict):
    # Easy = 0 
    # Medium = 1
    # hard = 2 
    
    level = 0
    
    
   # print(mydict)
    
    
 
    if  (mydict["Basic"] <= 10) and (mydict["Hidden"] >=4) or (mydict["Candidates"] >=4) or (mydict["Solved"] <=75):
        level = 1 
    elif (mydict["Xwing"] >= 1 ) or (mydict["Hidden"] >=8) or (mydict["Candidates"] >=8) or (mydict["Solved"] <= 60):
        level =2
        
    #global difficulty_level
    return level



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


def fill_withsolve(gridarry, gridzero):

    #gridarr = find_array(gridarry)
    
    empty = find_empty(gridzero)
    #print("array for fill is at ", gridarr)
 
    
    if not empty:
        # print("....................................................")
        #print("..............no more arrays in fill...............")
 
        return True
    
    row, col = empty
   # print("LOOKING TO SET ARRAY", gridarry[row][col] , "at ", (row,col))
   
   
    '''could use gridarray, just never update the arrays, '''
   
    nums = gridarry[row][col]
    #nums = [1,2,3,4,5,6,7,8,9]
    
    num_valid = 0
                

    for num in nums:
       # print("trying ", num, "for position", (row,col), "from array", gridzero[row][col])
        if is_valid(gridzero, (row, col), num):
            num_valid +=1
            
            gridzero[row][col]= num
            
           
            if fill_withsolve(gridarry, gridzero):
               
                return True
         
            gridzero[row][col] = 0
        
     
    return False


def clue_count(grid):
    count = solved_square(grid)
    if (count > 17) and (count < 40):
        return True
    return False

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
        #print("random num in get random is ", random_num)
    
        position = (ran_row, ran_col)
    
    if random_num != 0:
        
    
    
    
        return ran_row, ran_col
    


glob_difflevel = 9


''' Takes filled board and removes one num at a time'''
def create_unique( orig_board, difficulty): 
    arrayboard = copy.deepcopy(orig_board)
    
    
    
     
    zerosboard = copy.deepcopy(orig_board)
    # print("START OF CREATE UNIQUE")
    # print("                                    ")
    # print("                                    ")
    # print("                                    ")
    #print("clue count is ", clue_count(arrayboard))
    count = 0
  
    
    
    
    while comp_sq(zerosboard) > 17:
    #while count < 60:
    
        rand_row = 0
        rand_col = 0
      
        rand_row, rand_col = get_random_num(zerosboard)
    
       
        remove_backup = zerosboard[rand_row][rand_col]
        
       # print("REMOVING NEXT CLUE FROM CREATE_UNIQUE>>>>>>>>>>>>>>>>>>>>", (rand_row, rand_col) ,"CLUE COUNT IS", comp_sq(zerosboard))
        
        zerosboard[rand_row][rand_col] = 0
        arrayboard[rand_row][rand_col] = 0
       
        #print_grid(arrayboard)
            
        solution_count = try_to_solve2(arrayboard,  orig_board, difficulty)
        #print(solution_count, "is solution count AFTER TRY TO SOLVE ")
        
       
       # print(glob_difflevel, "is glob_difflevel")
       
        count  += 1
        #print("count is ", count)
    
        #print("CURRENT COMP SQUARE", comp_sq(arrayboard))
        
        if count == 250:
            print("OG OG GRID")
            print_grid(orig_board)
        
            
            print("COUNT IS ", count)
            count = 0
            print("HELLOOOOOOOOOOOOOOOO")
            #mynewgame, orig_board = new_sudoku_board(difficulty)
            complete_grid2 = create_grid_fill()
            arrayboard = copy.deepcopy(complete_grid2)
    
            zerosboard = copy.deepcopy(complete_grid2)
            
            orig_board = complete_grid2
            print("NEW BOARD - reset")
            print(".....................................................")
            print(".....................................................")
            print(".....................................................")
            print("NEW OG GRID")
            print_grid(orig_board)
            #create_unique(orig_board, difficulty)
            continue
            print(".....................................................")
            print(".....................................................")
            print(".....................................................")

        
        
        
        
        
        if solution_count == True:
            if (comp_sq(zerosboard) < 35):
               # print("FOUND solutiONNnnnnnnnn", comp_sq(zerosboard))
                #print("FOUND solutiONNnnnnnnnn")
                #print("FOUND solutiONNnnnnnnnn")
               # print("FOUND solutiONNnnnnnnnn")

                #level2 = get_difficulty_level(arrayboard)
                #print("difficulty level is ", level2)
                
            
                #if (level2 == difficulty) and (num_frequency(zerosboard) == True):
                if (glob_difflevel == difficulty) and (num_frequency(zerosboard) == True):
            
                    # print("difficulty is ", difficulty)
            
                    # if (comp_sq(zerosboard) < 26) and (num_frequency(zerosboard) == True):
                
                    print("difficulty level is ", difficulty)
            
            
                    print("I am here")
                    #print("Count is ", count)
                    
                    print("Completed squares is", comp_sq(zerosboard))
                 
                    
                   
                    return orig_board, zerosboard
                    
                
         
        elif (solution_count == False) or (num_frequency(zerosboard) == False) :
            #print("solution_count is greater than 1: backup at create_unique", solution_count)
            
            arrayboard[rand_row][rand_col] = remove_backup
           # print("Changing removed clue in ARRAYSBOARD back to ", arrayboard[rand_row][rand_col], "at", (rand_row, rand_col))
            
            zerosboard[rand_row][rand_col] = remove_backup
             #print("Changing removed clue in ZEROSBOARD back to ", arrayboard[rand_row][rand_col], "at", (rand_row, rand_col))
            
   # print("COUNT IS", count)
   # print("Complete squares (not met at min)", comp_sq(zerosboard))
   
   

    return orig_board, zerosboard
   
    
   
            
   
        
def set_arrays(grid):
    num_list = [1,2,3,4,5,6,7,8,9]
    row = 0
    col = 0
    for i in range(9):
        for j in range(9):
            if isinstance(grid[i][j], int): 
                if grid[i][j] == 0:
                    grid[i][j] = num_list
                    row = i
                    col = j
            else:
                for n in grid[i][j]:
                #print("looking at ", (i,j), grid[i][j])
                    if n == 0:
                        grid[i][j] = num_list
                        row = i
                        col = j
                        print("grid spot is now ", grid[i][j])
    
    ucount , grid = update_array(grid)
    
    #print("after update array", (row,col), "is", grid[row][col])
    
    #print("during set array")
   # print_pos_grid(grid)
    
    return grid  

def back_to_board(grid):
    #print("PRINTING GRID IN BACK TO BOARD")
    #print_grid(grid)
    for i in range(9):
        for j in range(9):
            if type(grid[i][j]) is int: grid[i][j] = [grid[i][j]]
            
            if len(grid[i][j]) > 1: 
                grid[i][j] = 0
            
            if type(grid[i][j]) is list: [grid[i][j]] = grid[i][j]
    return grid
   

        
def try_to_solve (array2, og_board, difficulty):
    ''' Shoudl just make this a return True/False
    
    True : Only one valid solution is found that matches. If any other matches found, false.
    False: More than one valid solution found (doesn't match Og). OR - no solutions found after reviewing all arrays.
    
    
    
    '''
    
    #arraysadd = add_arrays(array2)
    #print("running through try_to_solve.....................")
    
    
    
   
    arrayrun, diff_dict = runthrough3(array2)
    
    diff_level = get_difficulty_level(diff_dict)
    
    
    
    
    #print("AFTER FIRST RUN")
    #print_pos_grid(arrayrun)
   # print("solved squares after runthrough", solved_square(arrayrun))
    
    arrayb = copy.deepcopy(arrayrun)
    zeros = back_to_board(arrayrun)
    
    print("START OF TRY TO SOLVE:")
    
 
    #print_pos_grid(arrayb)
    random_count = 0
    trycount = 1
    multiple_solutions = 0
    valid_count = 0
    invalid_boards = 0
    
    #count for how many valid matching solutions are found.
    solutions = 0 

    if find_array(arrayb) == None:
        print("no arrays")
        #print(arrayb)
        #return trycount
    
    #print("clue count is ", comp_sq(zeros2))
    ''' SHOULD ADD A VALID CHECK HERE'''
    if comp_sq(zeros) == 81:
        
        return True

    count_loop = 0
    
    #print("rand backup is ", rand_backup, "at" , (rand_row, rand_col))
    backup_arrays = copy.deepcopy(arrayb)
    backup_zeros = copy.deepcopy(zeros)
    
    trysolve = copy.deepcopy(arrayb)
    # while there are still arrays after a runthgouh (should skip for most clue removals.)
    if find_array(arrayb) != None:   
    #while count_loop < 25:
        
        for i in range(9):
            for j in range(9):
                if zeros[i][j] == 0:
                    backup_sol = trysolve[i][j]
                    #print("Completed squares before num assign:", comp_sq(zeros))
                    
                    #print("backup in TRYTOSOLVE is ", backup_sol)
                    trynums = trysolve[i][j]
                    random_count += 1
                    
                    for num in trynums:
                        arrayb[i][j] = [num]
                        zeros[i][j] = num
                        #print("TRY TO SOLVE: trying nums ", trynums, "at", (i,j), "with num,", num)

                       
                        
                        
                        count_loop += 1
                        solve_attempt = copy.deepcopy(trysolve)
                        #mini_arr_update(solve_attempt, (i,j))
                        
                        # fuck = copy.deepcopy(solve_attempt)
                        # fuck2 = back_to_board(fuck)
                        # print("After setting TRYNUM, updated arrays")
                        # if comp_sq(fuck2) == 81:
                        #     print("after adding num in trysolve, total solved is ", comp_sq(fuck2))
                        #     if test_if_equal(solve_attempt, og_board) == False:
                        #         trycount += 1
                        #         return True
                      
                        # print("BEFore fillwithsolve")
                        # print_pos_grid(solve_attempt)
                        solve_zeros = copy.deepcopy(zeros)
                        
                        if fill_withsolve(solve_attempt, solve_zeros) == True:
                            #trycount += 1
                            #count_loop += 1
                            print("fill_withsolve is completed , printing solve_attempt")
                            print_pos_grid(solve_attempt)

                            # print("......................................")
                            # print("OG board")
                            # print_grid(og_board)
                            
                            if is_valid_fill(solve_attempt) == True:
                                valid_count += 1
                                #print_grid(solve_attempt)
                           
                                #print("fill_withsolve made a VALID board")
                            
                                if test_if_equal(solve_attempt, og_board) == False:
                                    
                                    print("boards did not match")
                                    print("!!!!!!!!!!!!!!!!!!!!")
                                    print("!!!!!!!!!!!!!!!!!!!!")
                                    #print_grid(solve_attempt)
                                    

                                
                                    trycount += 1
                                    multiple_solutions += 1
                                    #continue
                                    if trycount >= 2:
                                        print("trycount greater or equal than 2, returning count")
                                        return False
                                else:
                                    #test_if_equal(solve_attempt, og_board) == True:
                                    #print("TEST WAS EQUAL!!!!!!!")
                                    # print_grid(solve_attempt)
                                    # print("......................................")
                                    # print("OG board")
                                    # print_grid(og_board)
                                    #trycount +=1
                                    solutions += 1
                                    continue
                            else:
                                #is_valid_fill(solve_attempt) == False:
                                print("BOARD NOT VALID")
                                invalid_boards += 1
                                multiple_solutions += 1
                                 
                
                        arrayb[i][j] = backup_sol
                        arrayb = backup_arrays
                        
                        #print("resetting array in TRY_TO_sOLVE", arrayb[i][j])
                        zeros[i][j] = 0
                        zeros = backup_zeros
                        random_count -= 1
            print("Try_to_solve, tried all arrays ", i, j, "matches were:", solutions, "multi-solutions:", multiple_solutions)
        # # if valid_count == 0:
        # #     return valid_count
        #     #There were NO solutions 
        # print(trycount, "is TRYCOUNT.")
        # print(random_count, "is random count")
        # print("valid count is ", valid_count)
        # print("ADDITIONAL MATCHES ", multiple_solutions)
        # print("MATCHED solutions", solutions)
        # print("Complete but invalid boards", invalid_boards)
        # print("count loop is ", count_loop)
        
        
        
        
        if (solutions >= 1) and (multiple_solutions == 0) and (diff_level == difficulty):
            return True
        else:
            return False
            
    
    
    # if (trycount > 1) or (valid_count == 0):
    #     return False
    # elif trycount == 1:
    #     return True
    
    
    
    
    #return trycount    
    
    
    
    
def try_to_solve2 (array2, orig, difficulty):
    ''' Shoudl just make this a return True/False
    
    True : Only one valid solution is found that matches. If any other matches found, false.
    False: More than one valid solution found (doesn't match Og). OR - no solutions found after reviewing all arrays.
    
    
    
    '''
    #print("start of try to solve ", comp_sq(array2))
    #print_grid(array2)
    
    #print("running through try_to_solve.....................")
    
    arrayrun, diff_dict= runthrough3(array2)
    
    diff_level = get_difficulty_level2(diff_dict)
    # print("Difficulty level is ", diff_level)
    # print("Desired difficulty is ", difficulty)
    # print("DIFF DICT: ", diff_dict)
    
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
    #elif multiple_solutions >= 1:
    return False
    

def solve_loop (arrayb, zeros, og_board, solutions, multiple_solutions):
    
    #print("arrayb at solve loop start")
    #print_pos_grid(arrayb)
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
    #print("rand backup is ", rand_backup, "at" , (rand_row, rand_col))
    backup_arrays = copy.deepcopy(arrayb)
    backup_zeros = copy.deepcopy(zeros)
    backup_zeros = back_to_board(backup_zeros)
    #print("Backup Arrays")
    #print_pos_grid(backup_arrays)
    
    trysolve = copy.deepcopy(arrayb)
    
    
    tryzero = copy.deepcopy(arrayb)
   # print("TRY ZERO IS ")
    tryzero = back_to_board(tryzero)
    #print_grid(tryzero)
    # while there are still arrays after a runthgouh (should skip for most clue removals.)
    if find_array(arrayb) != None:   
    #while count_loop < 25:
        #print("find array found an array")
        
        for i in range(9):
            for j in range(9):
                if tryzero[i][j] == 0:
                    backup_sol = trysolve[i][j]
                    #print("Completed squares before num assign:", comp_sq(zeros))
                    
                    #print("backup in TRYTOSOLVE is ", backup_sol)
                    trynums = arrayb[i][j]
                    arrays_total += 1
                    array_len = array_len + len(trynums)
                    arrays_checked[(i,j)] = trynums
                    
                    
                    for num in trynums:
                        
                        # if no_solution_count == trying_array_length:
                        #     break
                        
                        count_loop += 1
                        #print_grid(tryzero)
                        if is_valid(tryzero, (i, j), num):
                            
                            # trysolve[i][j] = [num]
                            # mini_arr_update(trysolve, (i,j))
                            # print("Trysolve looks like:")
                            # print_pos_grid(trysolve)
                            
                            
                            
                            
                            #tryzero[i][j] = num
                            
                            
                            
                            

                            solve_attempt = copy.deepcopy(trysolve)
                            
                            solve_attempt[i][j] = [num]
                            mini_arr_update(solve_attempt, (i,j))
                        
                      
                            # print("BEFore fillwithsolve (after mini update)")
                            # print_pos_grid(solve_attempt)
                            
                            solve_zeros = copy.deepcopy(solve_attempt)
                            solve_zeros = back_to_board(solve_zeros)
                            #print("................solve zeros.................")
                            #print_grid(solve_zeros)
                           # print("TRY TO SOLVE: trying nums ", trynums, "at", (i,j), "with num,", num)
                            
                        
                            if fill_withsolve(solve_attempt, solve_zeros) == True:
                                
                                # print("Grid after fill with solve")
                                # print("ORIGINAL")
                                # print_grid(og_board)
                                # print("........................")
                                # print("Solve_zeros")
                                # print_grid(solve_zeros)
                                # print("Completed squares", comp_sq(solve_zeros))
                                # solved_squares = 0
                                # if find_array(solve_attempt) == None:
                                    
                                #     solve_copy = copy.deepcopy(solve_attempt)
                                #     test = back_to_board(solve_copy)
                                solved_squares = comp_sq(solve_zeros)
                                if solved_squares != 81:
                                    #board not solved
                                    #print("Board not solved, reset and try next num", (i,j), num)
                                    invalid_boards += 1
                                    continue
                            
                                    #print("fill_withsolve is completed , printing solve_attempt")
                                    #print_pos_grid(solve_attempt)
                                    #total_filled_boards += 1
                                    # print("......................................")
                                    # print("OG board")
                                    # print_grid(og_board)
                                else:
                                    if is_valid_fill(solve_zeros) == True:
                                        valid_boards += 1
                                    # print("Grid after is_valid_fill")
                                    # print_grid(solve_attempt)
                           
                                    # print("fill_withsolve made a VALID board")
                                
                                        if test_if_equal(solve_zeros, og_board) == False:
                                            key += 1
                                    
                                            # print("boards did not match", (i,j))
                                            # print("!!!!!!!!!!!!!!!!!!!!")
                                            # print("!!!!!!!!!!!!!!!!!!!!")
                                           # print_grid(og_board)
                                           
                                                                                      
                                            second_solution[key] = solve_zeros
                                  
                                            multiple_solutions += 1
                                        #continue
                                    #continue
                                        if multiple_solutions >= 1:
                                           # print("trycount greater or equal than 2, returning count")
                                            return solutions, multiple_solutions
                                        elif test_if_equal(solve_zeros, og_board) == True:
                                           # print("TEST WAS EQUAL!!!!!!!")
                                            # print_grid(solve_attempt)
                                            # print("......................................")
                                            # print("OG board")
                                            # print_grid(og_board)
                                            #trycount +=1
                                            solutions += 1
                                            #continue
                                        else: 
                                            #print("Something else is happening after a valid board found")
                                            # if find_array != None:
                                            #     print("Why are there arrays in solve zeros?!")
                                            #     print_pos_grid(solve_zeros)
                                            # else:
                                            #     print_grid(solve_zeros)
                                            something_else += 1
                                    else:
                               
                                     #   print("BOARD NOT VALID at above pos")
                                        # if find_array != None:
                                        #     print_pos_grid(solve_zeros)
                                        # else:
                                        #     print_grid(solve_zeros)
                                        invalid_boards += 1
                                    #solutions = 0
                                    #multiple_solutions = 0
                            else: 
                                ''' When fill with solve is FALSE - it means it retraced all steps and tried all pathes, no solutions found!!'''
                                
                                #solve_loop(solve_attempt, solve_zeros, og_board, solutions, multiple_solutions)
                               # print("FILL WITH SOLVE NOT TRUE")
                                # if find_array != None:
                                #     print_pos_grid(solve_attempt)
                                # else:
                                #     print_grid(solve_attempt)
                                invalid_boards += 1
                        
                        
                        #else:
                          # print( "Num not valid in grid" )
                                 
                        
                        #print("Resetting trysolve boards", num)
                        trysolve[i][j] = backup_sol
                        solve_attempt = trysolve
                        #print("Trysolve backed up")
                        #print_pos_grid(trysolve)
                        
                            #print("resetting array in TRY_TO_sOLVE", arrayb[i][j])
                        solve_zeros[i][j] = 0
                        solve_zeros = tryzero
                        
                    #print("Try_to_solve, tried all arrays ", i, j, "matches were:", solutions, "multi-solutions:", multiple_solutions)
       
      
    # print("TOTAL FILLED BOARDS::::::::::", total_filled_boards)
    # print("Valid boards: ", valid_boards)
    # print("Additional Solutions ", multiple_solutions)
    # print("Board was the same", solutions)
    # print("Valid boards match total sol/mult sol", valid_boards, (multiple_solutions + solutions))
    # print("invalid boards", invalid_boards)
    # print("Loops and Array nums checked: ", count_loop, array_len)
    # if something_else > 0:
    #     print("SOMETHING ELSE IS HAPPENING", something_else)
       

    
    return solutions, multiple_solutions


                    
                    
                



def new_sudoku_board(difficulty):
    
    complete_grid = create_grid_fill()
    
    #game_board = copy.deepcopy(complete_grid)
    
    #arr = copy.deepcopy(complete_grid)
     
    #zer = copy.deepcopy(complete_grid)
 
    
    orig, zeros = create_unique(complete_grid, difficulty)
    
    return zeros, orig


# difficult = 2
# mynewgame, original = new_sudoku_board(difficult)

# print("MY NEW GAME")
# print_grid(mynewgame)
# print("                                       ")
# print("                                       ")
# print_grid(original)



# myarrays= create_arrays(mynewgame)
# ugh, myarrays = update_array(myarrays)
# # print_pos_grid(myarrays)

# array_display(myarrays, "hello")
   
# # # # # attempt = try_to_solve2(evil_sudoku, evil_orig)
# # # # # print("here is my count ", attempt)  

# print("GOT IT NOW COUNT SOLUTIONS!!!!!!!!")
# print("GOT IT NOW COUNT SOLUTIONS!!!!!!!!")
# print("GOT IT NOW COUNT SOLUTIONS!!!!!!!!")
# print("GOT IT NOW COUNT SOLUTIONS!!!!!!!!")
# print("GOT IT NOW COUNT SOLUTIONS!!!!!!!!")
# print("GOT IT NOW COUNT SOLUTIONS!!!!!!!!")
# print("GOT IT NOW COUNT SOLUTIONS!!!!!!!!")

    
    
#solutions, multiple_sol = solve_loop(myarrays, mynewgame, original, 0,0)


# testarr = create_arrays(evil_sudoku)

# c, uatest = update_array(testarr)

# solv, multsol = solve_loop(uatest, testarr, evil_orig, 0,0)
    
    
    
    
    
    
    
    