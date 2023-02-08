from BuildPuzzle import *
from PreparePuzzle import *
from FindSolutions import *
import random
import copy
'''
1. Build complete puzzle
2. Take out random cell, set to 0 

3. Test to solve
    - Fill in and check if valid (Solve function to fill in cells)
    - If only one possible option, is valid
    - If more than one possible option, try additional and count solutions
        - Use (get arrays) - to get possible options before attempting to solve. Contrains the search. 
        - Stop if more than one is found - not valid, 
            - back track to last removed and try removing another cell. 
4. Only one solution = valid. 
5. Finished if Valid and at least 17 clues.






'''

grid2 = create_grid_fill()

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# MAke list of all positions and shuffle randomly.
#returns random list of positions to remove. all_positions
def suffle_positions(grid):
    
    all_positions = []
    for i in range(9):
        for j in range(9):
            all_positions.append((i,j))
            
    random.shuffle(all_positions)
    
    return all_positions

def find_array(grid):
    for i in range(9):
        for j in range(9):
            for k in range(10):
                k = 2
                if len(grid[i][j]) == k:
                    return (i,j)
    return None


def re_zero (grid):
    for i in range(9):
        for j in range(9):
            if len(grid[i][j]) > 1:
                grid[i][j] = 0 
    return grid


def remove_squares(grid, all_positions):
    grid_copy = copy.deepcopy(grid):
    
    #Sets count, used for indicating which position from list to remove.
    remove_count = 0
    clues = 81
    position = (0,0)
    
    #remove up to 17 clues, if more are removed, board not valid.
    while clues >= 17:
        
        for k in len(all_positions):
            position = all_positions[k]

        #set random sq to 0
        grid[position[0]][position[1]] = 0 
        
        solve_me(grid)
            
        
    






## THIS ONE IS MINE
def solve_me(grid): 
  
    
    
    total_count = print_count(grid_copy)
    attempts = 0
    
    #while there are still un-solved squares   
    while total_count < 81:
    
        # previous while start: find_array(grid_copy) != None:
        #take the first array found (smallest array) 
        position = find_array(grid_copy)
        
        
        # Choose one option / Backsolving - sets a solve path 1
        orig_array = grid[position[0]][position[1]]
        grid_copy = copy.deepcopy(grid)
        
        for k in grid[position[0]][position[1]]:
            grid[position[0]][position[1]] = k 
            if not find_array(grid)
                counter += 1 
                break
            else:
                solve_me(grid):
                    return True
        
        
        
        solutions = 0 
        
        # solve any remaining, update arrays.      
        grid_copy = basic_solve(grid_copy)
        
        
        
        #update total count
        total_count = print_count(grid_copy)
        
    if total_count == 81:
        

    return grid_copy


# My solve 

def solve_grid (grid):
    
    










def is_valid2(grid, row, col, num):
    # Check row
    for i in range(9):
        if grid[row][i] == num:
            return False
    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False
    # Check 3x3 grid
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[row_start + i][col_start + j] == num:
                return False
    return True

def solve_sudoku (grid, row, col, count_clues):
    
    #remove until no fewer than 17 clues remain 
    if count_clues >=  17 : 
        return True
    #for each position in all_positions (basically starts at the beginning of random list)
    for i in range(row, 9):
        for j in range(col, 9):
            if grid[i][j] != 0:
                continue 
            for num in range(1,10):
                if is_valid2(grid, i , j,num):
                    grid[i][j] = num
                      
                    if solve_sudoku(grid, i,j, count_clues + 1):
                        return True
                    grid[i][j] = 0
            return False
    return True


def count_solutions(grid, count_clues):
    #make a copy of the grid
    grid_copy = [row[:] for row in grid]
    count = 0
    #try to solve the grid, if we solve it, count  + 1
    solve_sudoku(grid_copy,0,0, count_clues)
    count += 1
    
    # Then, for each item of the grid, 
    for i in range(9):
        for j in range(9):
            #if the grid is 0 
            if grid[i][j] != 0:
                #set as back up
                backup = grid[i][j]
                #then set the grid to 0 
                grid[i][j] = 0
                if solve_sudoku(grid_copy, i, j, count_clues + 1):
                    count += 1
                else:
                                       
                    grid[i][j] = backup
    return count
               
               



def final_solve(grid):
    
    count_clues = 0
    
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                count_clues += 1
    
    print("Count_Clues " , count_clues)
    
    while count_clues < 17 or count_clues > 25:
        if count_solutions(grid, count_clues) == 1:
            for i in range(9):
                for j in range(9):
                    if grid[i][j] == 0:
                        backup = grid[i][j]
                        grid[i][j] = 0
                        if count_solutions(grid, count_clues) != 1:
                            grid[i][j] = backup
                            count_clues -= 1
                            print("count clues subtracted, ", count_clues)
        else:
            for i in range(9):
                for j in range(9):
                    if grid[i][j] == 0:
                        grid[i][j] = backup
                        count_clues += 1
                        print("Count clues ", count_clues)
                        break
                if grid[i][j] != 0:
                    break
    return grid

lkj = final_solve(grid)

print_grid(lkj)


      
                    
                  
                        
                         
                          
                           
                    

                
              
       

        
        
        
        
        



            