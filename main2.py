from BuildPuzzle import *
from PreparePuzzle import *
from PerfectPairs import *
from FindSolutions import *
from TestingDisplay import * 
from CandidateLines import *


'''
Build Puzzle: 

1. create a new grid that is completely filled with create_grid_fill. Returns grid, no parameters. 


'''

grid_new = create_grid_fill()  


'''
Prepare Puzzle: 

1. new_game_board : Takes grid created and removes random set of numbers from grid, replacing them with 0. Returns game_board. 
2. create_arrays:   Takes grid (game_board) and replaces all empty squares with an array of possible numbers. 

3. print_pos_grid: takes grid and returns printed grid for terminal
'''

grid_game = new_game_board(grid_new)
grid = create_arrays(grid_game)

solved = completed_count(grid)

print("Solved Squares at Create Arrays ", solved)

array_display(grid, "Create Arrays")


'''
Find Solutions: 

Contains several functions for starting backsolving; num_row, num_col and num_inmini return True if a number is found in the associated col/row/box and not in the same position as the current search item.

1. only_option: Takes grid, searches for each square if a number in the array of possible numbers (length > 1) is found in any associated row/col or the box. if NOT, it sets the number as the only
    number for the position (only option). Returns updated grid. 
2. update_array: Takes grid, searches through each square in 9x9, updates the arrays based on solutions found from previous functions. 

3. basic_solve: combinds only_option and update_array in a loop and completes only when no changes have been counted for an entire cycle through. 


'''


final_solutions_test = basic_solve(grid)

print_pos_grid(final_solutions_test)

solved = completed_count(final_solutions_test)

print("Solved Squares at BASIC SOLUTION Test ", solved)

array_display(final_solutions_test, "Basic Solve / Find Solutions")


'''
Perfect Pairs: Uses the perfect pairs / naked pairs sudoku strategy. 

1. perfect_pairs: Takes grid, searches through rows / cols / boxes and identifies any naked pairs (length of 2, same numbers), removes any of those numbers from arrays in the same col/row that are not also 
    in the same box. 


'''
#original_test_test = copy.deepcopy(test_test)


perf_pair_test  = basic_solve(perfect_pairs(final_solutions_test))

print_updated_grid(perf_pair_test)

solved = completed_count(perf_pair_test)

print("Solved Squares at CPERFECT PAIRS  ", solved)


array_display(perf_pair_test, "Perfect Pairs")


'''
Candidate Lines: 

1. 



'''


cl_grid , total_returned = check_lonely_nums(perf_pair_test)

final = basic_solve(cl_grid)

print_pos_grid(cl_grid)            
print(total_returned,  "total removed from num arrays after candidate lines. ")


solved = completed_count(cl_grid)


print("Solved Squares at CANDIDATE LINES  ", solved)

solved = completed_count(final)
print("Final solved ", final)


array_display(cl_grid, "Candidate Lines" )
array_display(final, "Final")


