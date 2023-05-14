from BuildPuzzle import *
from PreparePuzzle import *
from FindSolutions import *
from CandidateLines import *
from Hidden import *


from TestingDisplay import *

from GridDict import*





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



    

    
    
    

        
    
    
    
    
    
    












            
            
            
            
            




        
        
        
        
    
    








