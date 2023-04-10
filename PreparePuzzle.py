# from BuildPuzzle import*
# import random
# """
# Function sets difficulty level based on provided entry - easy med hard
# """

# base = 3
# side = base*base

# # method for removing numbers. Mirroring?
# game = []


# def initial_board(grid):
#     game_board = []
    
#     #81 squares 
#     squares = side*side
#     #bigger fraction = fewer numbers
#     empties = squares * 9 // 13
#     for p in sample(range(squares), empties):
#         grid[p//side][p % side] = 0

#     for line in grid:
#         game_board.append([n for n in line])
#         # print(*(f"{n or '.':{numSize}} " for n in line))
#     return game_board


# # need to check if game_board has at least one of each number
# def all_nums(grid):
    
#     numbers = set()
#     for i in range(9):
#         for j in range(9):
            
#             num = grid[i][j]
#             numbers.add(num)
#     if len(numbers) < 9:
#         return False
#     return True
            
# def new_game_board(grid):
      
#     tryagain = True

#     while tryagain == True:
        
#         game = initial_board(grid)
#         if all_nums(game) == True:
#             tryagain = False
#             return game
             
                   






# def comp_sq(grid):
#     completed = 0
#     for i in range(9):
#         for j in range(9):
#             if grid[i][j] !=  0:
#                 completed += 1
#     return completed

# def random_square(grid):
    
#     row = [0,1,2,3,4,5,6,7,8]
#     col = [0,1,2,3,4,5,6,7,8]
    
#     already_selected = []
#     rand_row = 0

#     rand_col = 0 
       
#     rand_row = random.choice(row)
#     rand_col = random.choice(col)
  
#     print("Random Square ", (grid[rand_row][rand_col]), "at ,", (rand_row, rand_col))
    
#     position = (rand_row, rand_col)
#     return position
            
# # testrandom = random_square(grid)
# # print("Test Random ", testrandom)


# def print_game(game_board):
#     for i in range(9):
#         if i % 3 == 0 and i != 0:
#             print("------+------+-------")
#         for j in range(9):
#             if j % 3 == 0 and j != 0:
#                 print("|", end=" ")
#             print(game_board[i][j], end='')
#         print()


# # new_game = new_game_board(new_grid)
# # print_game(new_game)
# # print("Above is printed new_gam from create new game board")


# def completed_count(game_board):
#     completed = 81
#     for i in range(9):
#         for j in range(9):
#             if game_board[i][j] == int :
#                 game_board[i][j] = [game_board[i][j]]
            
#             if len(game_board[i][j] ) >= 2:
#                 completed -= 1
#     return completed


# #print("Squares completed at START", completed_count(new_game))

# '''Takes a grid 'game_board' as generated by new_game_board. Identifies for all elements that are =  0 (not completed) 
# what possible numbers 0-9 may be possible. Stores these possible numbers in a new grid called possible_numbers_grid 
# which returned by the function. 

# The possible_numbers_grid is then used as the output stored in any variable that is created and calls 
# create_arrays using the current game "new_game" - from above. 

# '''


# possible_numbers_grid = [[0 for _ in range(9)] for _ in range(9)]
# # #print(possible_numbers_grid)
# # notes = [[[0] * 10 for _ in range(9)] for _ in range(9)]

# #print(notes)


# def create_arrays(game_board):

#     possible_nums = []
#     for i in range(9):
        
#         for j in range(9):
#             # May need to change this as it stores a single variable. Rather than storing all variables in
#             # my possible_numbers_grid, I should leave them empty?
#             value = game_board[i][j]
#             if type(value) is not list: value = [value]
#             # if value >= 1:
#             #     #print("before pos nums" , game_board[i][j])
#             #     possible_nums = game_board[i][j]
#             #     # print("after first iter" , possible_nums)
#             #     possible_numbers_grid[i][j] = possible_nums
#             #if type(value) is not int: [value] = value
#             if value == [0]:
#                 #  if its not a number, and its blank. Determine if 0-9 is in a row/col/box and store
#                 # any nums not found in array at position.
#                 # checking ROW
#                 possible_nums = list(range(1, 10))
#                 for k in range(9):
#                     if game_board[i][k] in possible_nums:
#                         possible_nums.remove(game_board[i][k])
#                 # check COLUMN
#                 for k in range(9):
#                     if game_board[k][j] in possible_nums:
#                         possible_nums.remove(game_board[k][j])
#                 # check 3x3 space
#                 row_start = i - i % 3
#                 col_start = j - j % 3

#                 for x in range(row_start, row_start+3):
#                     for y in range(col_start, col_start+3):
#                         if game_board[x][y] in possible_nums:
#                             possible_nums.remove(game_board[x][y])
#                 possible_numbers_grid[i][j] = possible_nums
#             else: 
#                 possible_nums = game_board[i][j]
#                 # print("after first iter" , possible_nums)
#                 possible_numbers_grid[i][j] = possible_nums

#     return possible_numbers_grid


# def print_pos_grid(thisgrid):
#     for i in range(9):
#         if i % 3 == 0 and i != 0:
#             print("--------------+-----------------+-------------------")

#         for j in range(9):
#             if j % 3 == 0 and j != 0:
#                 print("||", end=" ")
            
#             print(thisgrid[i][j], end="::")
#         print()

# # new_grid = create_grid_fill()
# # new_game = new_game_board(new_grid)
# # #print_pos_grid(new_game)
# # print_grid(new_game)
# #test_bs = single_solution_prep(new_game)
# #pos_nums_grid = create_arrays(new_game)



# # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# # print("Printing Pos_nums_grid: this is the grid that calls create_arrays")

# #print_pos_grid(test_bs)