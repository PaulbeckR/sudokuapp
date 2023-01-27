from BuildPuzzle import *
from FindSolutions import *
from PreparePuzzle import *
from PerfectPairs import *
from GraphicsBuild import *

# from build puzzle



#previous
#new_game = new_game_board(new_grid)
print_game(new_game)
print("Above is printed new_gam from create new game board")
print("Squares completed at START", completed_count(new_game))



pos_nums_grid = create_arrays(new_game)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Printing Pos_nums_grid: this is the grid that calls create_arrays")

print_pos_grid(pos_nums_grid)


#find solutions





test_test = basic_solve(pos_nums_grid)
print_updated_grid(test_test)

#perfect pairs

current_test = perfect_pairs(test_test)
print(" current test is here"  , current_test)
print_updated_grid(current_test)


game1 = game()