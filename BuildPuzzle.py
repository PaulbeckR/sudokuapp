from random import *



def create_grid_fill():


    grid = [[0 for _ in range(9)] for _ in range(9)]
    fill_grid(grid)
    return grid


def fill_grid(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    row, col = empty
    nums = [i for i in range(1, 10)]
    shuffle(nums)
    for num in nums:
        if is_valid(grid, (row, col), num):
            grid[row][col] = num
            if fill_grid(grid):
                return True
            grid[row][col] = 0
    return False


def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


def is_valid(grid, pos, num):
    for i in range(9):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(9):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    return True


def print_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------+------+-------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()


#new_grid = create_grid_fill()

#print_grid(new_grid)

# print(new_grid)





