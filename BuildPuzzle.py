from random import *
'''
Initial build of completed and valid Sudoku puzzle. All rows / cols / box's only have numbers 1-9

 

'''

# Creates complete and valid Sudoku board
def create_grid_fill():


    grid = [[0 for _ in range(9)] for _ in range(9)]
    fill_grid(grid)
    return grid

#Back solver to fill in grid with valid numbers only
def fill_grid(grid):
    #Get empty (0) square.
    empty = find_empty(grid)
    
    if not empty:
        #If none empty, board is complete.
        return True
    row, col = empty
    nums = [i for i in range(1, 10)]
    shuffle(nums)
    #try random number 1-9 to enter into empty location.
    for num in nums:
        if is_valid(grid, (row, col), num):
            grid[row][col] = num
            #check if completed grid.
            if fill_grid(grid):
                return True
            #reset square to 0 if next num not valid.
            grid[row][col] = 0
    return False

#Find any value in grid still equal to 0 and return the position.
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

#Check if number is valid: number for new square is not found in the same row / col / box.
def is_valid(grid, pos, num):
    #check the row
    for i in range(9):
        if grid[pos[0]][i] == num and pos[1] != i:
            
            return False
    #check the col
    for i in range(9):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False
    #check the square
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    return True

#Print grid using formating to look like Sudoku board in terminal. ** Used throughout program/files.
def print_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------+------+-------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()




