'''
Create final sudoku class that includes initial build of board and back solver. To merge BackSolver.py and BuildPuzzle.py files.

'''
from random import shuffle
from BackSolver import *

class SudokuBoard:
    def __init__(self, grid = None):
        self.grid = grid if grid else [[0 for _ in range(9)] for _ in range(9)]
        self.solved_board = None
        self.difficulty = None
        self.glob_difflevel = 9

        self.my_dict = dict()
        self.difficulty_dictionary = dict()
        
        
      # Getter for the difficulty dictionary
    def get_difficulty_dict(self):
        return self.my_dict

    # Getter for the zeros board
    def get_zeros_board(self):
        return self.grid

    # Getter for the solution board
    def get_solution_board(self):
        if self.solved_board is None:
            print("The sudoku board is not yet solved.")
        else:
            return self.solved_board
    
    #creates full sudoku grid to derive game board from
    def create_new_grid(self):
        self.fill_grid()
        return self.grid
    
    
    #finds empty cell of 9x9 grid to fill
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i,j 
        return None
    
    #checks if the number entered is valid
    def is_valid(self, grid, pos, num):
        for i in range(9):
            if self.grid[pos[0]][i] == num and pos[1] != i:
                return False
            if self.grid[i][pos[1]] == num and pos[0] != i:
                return False
        box_x = pos[1] //3
        box_y = pos[0] //3
        for i in range(box_y *3, box_y *3 + 3):
            for j in range(box_x * 3, box_x *3 + 3):
                if self.grid[i][j] == num and (i,j) != pos:
                    return False
        return True
    # part of creating initial sudoku solution
    def fill_grid(self):
        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty
        nums = [i for i in range(1,10)]
        shuffle(nums)

        for num in nums:
            if self.is_valid(self.grid, (row, col), num):
                self.grid[row][col] = num
                
                if self.fill_grid():
                    return True
                self.grid[row][col] = 0
        return False
    
    def print_grid(self, grid=None):
        if grid is None:
            grid = self.grid
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("---------+---------+---------")
            for j in range(9):
                if j % 3 ==0 and j != 0:
                    print("|", end = " ")
                print(grid[i][j], end= " ")
            print()
        
    #method to make sure all numbers are listed at least once in the finished game board
    def num_frequency(self):
        
        num_list = [1,2,3,4,5,6,7,8,9]
        num_set = set()
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] in num_list:
                    num_set.add(self.grid[i][j])
        return len(num_set) == 9
    
    # loops through game board to remove all possible clues based on several strategies
    def run_all_strategies(self,rungrid):
    
        gcope = copy.deepcopy(rungrid)

        for i in range(9):
            for j in range(9):
                if type(gcope[i][j]) is not int: [gcope[i][j]] = gcope[i][j]

        #method defined in other .py file, creates list of possible numbers for each empty square of sudoku board
        grid = create_arrays(gcope)

        total_changes = 1
        basic = 0
        candidate_lines = 0
        hidden = 0
        xwings = 0

        # run until no changes found. removes all possiblen umbers based on strategies
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
            #removes candidates from any identified x-wings
            gridx, xwingcount = xwing(gridcl)
            xwings = xwingcount + xwings

            #loop through grid and remove any candidates that are no longer valid
            update_changes, gridx = update_array(gridx)
            
            basic = update_changes + basic
            
            total_changes = (changes + count + removed + xwingcount)

        solved_after_run = solved_square(gridx)
        self.difficulty_dictionary = {"Basic": basic, "Hidden": hidden, "Candidates": candidate_lines, "Xwing": xwings, "Solved": solved_after_run}
        return gridx 



    #set difficulty level parameters
    def get_difficulty_level2(self):

        level = 0
        mydict = self.difficulty_dictionary

        if  (mydict["Basic"] <= 10) and (mydict["Hidden"] >=4) or (mydict["Candidates"] >=4):
            level = 1 
        elif (mydict["Xwing"] >= 1 ):
            level =2
            
        #self.glob_difflevel = level
        
        return level


    #checks if each square is valid
    def is_valid_fill(self):
        for i in range(9):
            for j in range(9):

                if not self.is_valid(self.grid, (i,j) ,self.grid[i][j]):
                    return False
        return True

    # #shuffles posisitions
    # def shuffle_positions(self):

    #     all_positions = []
    #     for i in range(9):
    #         for j in range(9):
    #             all_positions.append((i,j))
                
    #     random.shuffle(all_positions)

    #     return all_positions

    #back solver to solve board, connects to solve_loop to find all possible solutions to sudoku board
    def fill_withsolve(self, gridarry, gridzero):

        empty = self.find_empty(gridzero)
        if not empty:
            return True

        row, col = empty


        '''could use gridarray, just never update the arrays, '''

        nums = gridarry[row][col]    
        num_valid = 0
                    
        for num in nums:
            if self.is_valid(gridzero, (row, col), num):
                num_valid +=1
                gridzero[row][col]= num
                if self.fill_withsolve(gridarry, gridzero):
                    return True
                
                gridzero[row][col] = 0
        return False


    # gets a random numb from a position in the game board
    def get_random_num(self):
        non_zero_positions = [(i,j) for i in range(9) for j in range(9) if self.grid[i][j] != 0]
        return random.choice(non_zero_positions)
        # rows = [0,1,2,3,4,5,6,7,8]
        # cols = [0,1,2,3,4,5,6,7,8]

        # random_num = 0
        # while random_num == 0:

        #     ran_row = random.choice(rows)
        #     ran_col = random.choice(cols)

        #     random_num = self.grid[ran_row][ran_col]
            

        # if random_num != 0:
        #     return ran_row, ran_col



   #main backsolving function: removes one square from solution and then checks for unique solutions

    ''' Takes filled board and removes one num at a time'''
    def create_unique(self, orig_board, difficulty): 
        arrayboard = copy.deepcopy(orig_board)
        zerosboard = copy.deepcopy(orig_board)
        count = 0
        clue_max = 35

        #sets limit to game board at 17 clues
        while comp_sq(zerosboard) > 17:

            rand_row = 0
            rand_col = 0
            
            rand_row, rand_col = self.get_random_num()
            remove_backup = zerosboard[rand_row][rand_col]
            zerosboard[rand_row][rand_col] = 0
            arrayboard[rand_row][rand_col] = 0
            
            # try to solve after removing a square, find possible solutions
            solution_count = self.try_to_solve2(arrayboard,  orig_board)
            count  += 1

            #limit set to start over with new solution board
            if count == 100:
                count = 0
                print("Reset" )
                complete_grid2 = self.create_new_grid()
                arrayboard = copy.deepcopy(complete_grid2)
                zerosboard = copy.deepcopy(complete_grid2)
                orig_board = complete_grid2
                continue

            if solution_count == True:
                if (comp_sq(zerosboard) < clue_max):
                    self.glob_difflevel = self.get_difficulty_level2()
                    if (self.glob_difflevel == difficulty) and (self.num_frequency() == True):  
                        print(my_dict)
                        return orig_board, zerosboard
            elif (solution_count == False) or (self.num_frequency() == False) :
                arrayboard[rand_row][rand_col] = remove_backup
                zerosboard[rand_row][rand_col] = remove_backup
        print("BAD BOARD")
        return orig_board, zerosboard

        # returns a game board with possible solution arrays to zeros for any unsolved square
    def back_to_board(self, grid):

        for i in range(9):
            for j in range(9):
                if type(self.grid[i][j]) is int: self.grid[i][j] = [self.grid[i][j]]
                
                if len(self.grid[i][j]) > 1: 
                    self.grid[i][j] = 0
                
                if type(self.grid[i][j]) is list: [self.grid[i][j]] = self.grid[i][j]
        return grid

    # checks difficulty level of current board, runs through strategy loop to remove clues - constrained search
    # runs solve_loop to check all posible solutions to find unique solution or multiple solutions
    def try_to_solve2 (self,array2, orig):

        arrayrun = self.run_all_strategies(array2)

        # diff_level = self.get_difficulty_level2(diff_dict)
        
        # self.my_dict = diff_dict

        
        # self.glob_difflevel = diff_level

        Aa = copy.deepcopy(arrayrun)
        Zz = self.back_to_board(arrayrun)

        
        mult= 0
        sol = 0 

        if (comp_sq(Zz) == 81):
            return True

        solutions, multiple_solutions = self.solve_loop(Aa, Zz, orig, sol, mult)


        if (solutions >0) and (multiple_solutions == 0):
            return True

        return False

    # tries all remaining possible solutions 
    def solve_loop (self,arrayb, zeros, og_board, solutions, multiple_solutions):

        valid_boards = 0
        
        
        arrays_checked = dict()

        arrays_total = 0
        array_len = 0

        second_solution = dict()
        key = 0

        backup_zeros = copy.deepcopy(zeros)
        backup_zeros = self.back_to_board(backup_zeros)
        try_arrays = copy.deepcopy(arrayb)
        tryzero = copy.deepcopy(arrayb)
        tryzero = self.back_to_board(tryzero)
        # while there are still arrays after a runthgouh (should skip for most clue removals.)
        if find_array(arrayb) != None:   
            for i in range(9):
                for j in range(9):
                    if tryzero[i][j] == 0:
                        backup_sol = try_arrays[i][j]
                        trynums = arrayb[i][j]
                        arrays_total += 1
                        array_len = array_len + len(trynums)
                        arrays_checked[(i,j)] = trynums
                        
                        for num in trynums:
                            
                            if self.is_valid(tryzero, (i, j), num):
                                solve_attempt = copy.deepcopy(try_arrays)
                                solve_attempt[i][j] = [num]
                                mini_arr_update(solve_attempt, (i,j))

                                solve_zeros = copy.deepcopy(solve_attempt)
                                solve_zeros = self.back_to_board(solve_zeros)
                            
                                if self.fill_withsolve(solve_attempt, solve_zeros) == True: 
                                    solved_squares = comp_sq(solve_zeros)
                                    if solved_squares == 81:
                                        #board not solved

                                        if self.is_valid_fill(solve_zeros) == True:
                                            valid_boards += 1
                                    
                                            if test_if_equal(solve_zeros, og_board) == False:
                                                key += 1                                        
                                                second_solution[key] = solve_zeros
                                        
                                                multiple_solutions += 1
                                        
                                                if multiple_solutions >= 1:
                                                    return solutions, multiple_solutions
                                            elif test_if_equal(solve_zeros, og_board) == True:
                                                solutions += 1
                            try_arrays[i][j] = backup_sol
                            solve_attempt = try_arrays

                            solve_zeros[i][j] = 0
                            solve_zeros = tryzero
                
        return solutions, multiple_solutions


    #creates new solution and new game board
    def new_sudoku_board(self, difficulty):


        complete_grid = self.create_new_grid()

        orig, zeros = self.create_unique(complete_grid, difficulty)

        return zeros, orig
    
    
sudoku = SudokuBoard()
zeros, orig = sudoku.new_sudoku_board(2)

difficulty_dict = sudoku.get_difficulty_dict()
zeros_board = sudoku.get_zeros_board()
solution_board = sudoku.get_solution_board()
print(zeros)

sudoku.print_grid(zeros)
