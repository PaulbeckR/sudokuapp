#from BuildPuzzle import*
import random
from GridDict import *
from Hidden import*
from CandidateLines import*
from FindSolutions import*
"""
Initial code to remove random numbers from the board to create a Sudoku game board. 

* Does NOT ensure uniqueness. Not used for primary backsolving algorithm. 


"""


'''Counts how many single digit squares are in board'''
def solved_square(grid):
    count = 0
    for i in range(9):
        for j in range(9):
            if type(grid[i][j]) is not list: grid[i][j] = [grid[i][j]]

            if len(grid[i][j]) == 1:
                count += 1
    return count             


# Determin how many squares have a number that is not 0. 
def comp_sq(grid):
    completed = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j] !=  0:
                completed += 1
    return completed

def random_square(grid):
    
    row = [0,1,2,3,4,5,6,7,8]
    col = [0,1,2,3,4,5,6,7,8]
    
    already_selected = []
    rand_row = 0

    rand_col = 0 
       
    rand_row = random.choice(row)
    rand_col = random.choice(col)
  
    print("Random Square ", (grid[rand_row][rand_col]), "at ,", (rand_row, rand_col))
    
    position = (rand_row, rand_col)
    return position
            


#Another board printing function. COULD PROBABLY DELETE THIS.
def print_game(game_board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------+------+-------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(game_board[i][j], end='')
        print()


#Count completed squares for boards that contain arrays of possible numbers.
def completed_count(game_board):
    completed = 81
    for i in range(9):
        for j in range(9):
            if game_board[i][j] == int :
                game_board[i][j] = [game_board[i][j]]
            
            if len(game_board[i][j] ) >= 2:
                completed -= 1
    return completed


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

'''Takes a sudoku board with missing squares. Identifies for all elements that are =  0 (not completed) 
what possible numbers 0-9 may be possible. Stores these possible numbers in a new grid called possible_numbers_grid 
which returned by the function. 

The possible_numbers_grid is then used as the output stored in any variable that is created and calls 
create_arrays using the current game.

Used in primary backsolving function.   

'''

#Set empty grid.
possible_numbers_grid = [[0 for _ in range(9)] for _ in range(9)]


def create_arrays(game_board):

    possible_nums = []
    for i in range(9):
        
        for j in range(9):

            value = game_board[i][j]
            if type(value) is not list: value = [value]
            
            #set to list for continuity
            if value == [0]:
                #  if its not a number, determine if 0-9 is in a row/col/box and store any numbers not found.
                
                # checking ROW
                possible_nums = list(range(1, 10))
                for k in range(9):
                    if game_board[i][k] in possible_nums:
                        possible_nums.remove(game_board[i][k])
                        
                # check COLUMN
                for k in range(9):
                    if game_board[k][j] in possible_nums:
                        possible_nums.remove(game_board[k][j])
                
                # check BOX
                row_start = i - i % 3
                col_start = j - j % 3

                for x in range(row_start, row_start+3):
                    for y in range(col_start, col_start+3):
                        if game_board[x][y] in possible_nums:
                            possible_nums.remove(game_board[x][y])
                possible_numbers_grid[i][j] = possible_nums
            else: 
                #completed square, keep the number.
                possible_nums = game_board[i][j]
                
                possible_numbers_grid[i][j] = possible_nums

    return possible_numbers_grid

#Yet another printing function, prints arrays/clues as well as completed squares.
def print_pos_grid(thisgrid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("--------------+-----------------+-------------------")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("||", end=" ")
            
            print(thisgrid[i][j], end="::")
        print()

