from PreparePuzzle import *

# Now that I have a game board, I have started a solution with finding all single nums.

# I have my possible_numbers_grid and game_board that I want to populate. and grid that is the orig.


# functions for general check / num in row / col / square

# Check if num in row/ column or grid - will be the num of length of 1
# called to update the array list for
'''
Starting with pos_nums_grid. Begins finding total solution. First three functions are gen-use functions for determining
if the number provided (myint) also exists in the same row / col / 3x3 grid as either a 
'''


def num_row(grid, myint, pos):
    # pos is the potition myint is at. also provides row location
    for row_i in range(0, len(grid)):
        for col_j in range(0, len(grid)):
            # if the search int is in any row / col or 3x3, return true

            # k will be my checking loop: check each row index 0-9

            # going into each array:
            # for myint in gamegrid[pos[0]][pos[1]]:
            for each_position_row in range(9):
                for element in grid[pos[0]][each_position_row]:

                    if myint == element and (row_i, col_j) != pos:
                        return True


def num_col(grid, myint, pos):
    # if the search int is in any  col o
    # found a match.
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):

            # for myint in gamegrid[pos[0]][pos[1]]:
            for k in range(9):
                for element in grid[k][pos[1]]:
                    if myint == element and (i, j) != pos:
                        return True


def num_inmini(gridagain, myint, pos):
    # returns TRUE if it finds a match. I want

    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            for element in gridagain[i][j]:
                if element == myint and (i, j) != pos:
                    return True


def only_option(gamegrid):
    # print("-------------------------------")
    #  print("START OF ONLY OPTION")
    # print("--------------------------------")
    change_count = 0
    for i in range(9):
        for j in range(9):
            # if the length is greater than 1

            # print("ONLY_OPTION:: gamegrid position checked is:  ", gamegrid[i][j])
            if len(gamegrid[i][j]) > 1:
                # for k in the range of nums stored in my array at [i][j]
                # for my number in my list of numbers at a position.
                for k in gamegrid[i][j]:
                    #print("Checking ", k, "of ", gamegrid[i][j])

                    if any(k in gamegrid[i][x] for x in range(9) if (i, x) != (i, j)):
                        gamegrid[i][j] = gamegrid[i][j]
                        #print(k, "was found to be in one or more ROWS")

                    else:
                        gamegrid[i][j] = [k]
                        change_count += 1
                        #print(k, "was NOT!!!! found to be in one or more ROWS", k, "is assigned to position",
                        # gamegrid[i][j])
                        continue

                    if any(k in gamegrid[x][j] for x in range(9) if (x, j) != (i, j)):
                        #print(k, "was found to be in one or more COLS")
                        gamegrid[i][j] = gamegrid[i][j]

                    else:
                        gamegrid[i][j] = [k]
                        change_count += 1
                         #print(k, "was NOT!!!! found to be in one or more COLS", k, "is assigned to position",
                        #      gamegrid[i][j])
                        continue

                    if any(k in gamegrid[x][y] for x in range(i - i % 3, i - i % 3 + 3) for y in
                           range(j - j % 3, j - j % 3 + 3) if (x, y) != (i, j)):
                        # print(k, "was found to be in one or more BOXES")
                        gamegrid[i][j] = gamegrid[i][j]
                    else:
                        # print(k, "was NOT!!!! found to be in one or more BOXES of ", gamegrid[i][j])

                        gamegrid[i][j] = [k]
                        change_count += 1
                        # print( "Position is now: ", gamegrid[i][j])
                        continue
    print("change count is ", change_count)

    return change_count, gamegrid


# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print("FIRST TEST USING Just printing NEXT_grid. This test TESTS ONLY OPTION")
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

# print("printing ponumgrid" ,pos_nums_grid)
# next_grid = only_option(pos_nums_grid)
# print("printing next grid" ,next_grid)


def print_updated_grid(thisgrid):
    # print("printing updated grid")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("--------------+-----------------+-------------------")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("||", end=" ")

            print(*thisgrid[i][j], end=" : ")
        print()


# print_updated_grid(next_grid)
#print("end of next_grid")


def print_count(grid):
    count = 0
    solved = 0
    for i in range(9):
        for j in range(9):
            count = 0
            for k in grid[i][j]:
                count += 1
            # print("count at ", grid[i][j], "is" , count)
            if count == 1:
                solved += 1

    return solved


# print("Total solved is ", print_count(next_grid))


# print("Squares completed after next grid" , print_count(next_grid))




# so now I have run through to check any single nums in an array
# and I run this new grid back through create_arrays to update the arrays for any changes.
# grid_with_reset_arrays = create_arrays(next_grid)
# print("printing next one" ,grid_with_reset_arrays)
# print("count of next_one" ,print_count(next_grid))

def update_array(thisgrid):
    print(":::::::::::::::::::::::::::::::::::")
    print("UPDATING ARRAY :::: UPDATING ARRAY")
    print(":::::::::::::::::::::::::::::::::::")
    
    array_update = 0
    count = 0
    for i in range(0, len(thisgrid)):
        for j in range(0, len(thisgrid)):
            # if grid is equal to 1 do nothing
            if len(thisgrid[i][j]) == 1:
                # print("Checking this array" , thisgrid[i][j])

                # it's longer than one, check if any row/col/3x3 has matching
                for element in thisgrid[i][j]:
                    # print("Element ", element, "is being checked from ", thisgrid[i][j])
                    if any(element in thisgrid[i][x] for x in range(9) if (i, x) != (i, j)):
                        # print("it was found in one of the ROWS")

                        for row_position in range(9):
                            if len(thisgrid[i][row_position]) > 1:
                                #print("ROW array", thisgrid[i][row_position], " > than 1 and checked 4 ", element)
                                for n in thisgrid[i][row_position]:
                                    #print("element ", n, "is being checked against k")
                                    if n == element and j != row_position:
                                        #print("n is equal to k and j is not equal to l")
                                        thisgrid[i][row_position].remove(element)
                                        array_update += 1
                                        #print(element, "was removed from ", thisgrid[i][row_position])

                    if any(element in thisgrid[x][j] for x in range(9) if (x, j) != (i, j)):
                        #print("it was found in one of the COLUMNS")

                        for col_position in range(9):
                            if len(thisgrid[col_position][j]) > 1:
                                #print("this COLUMN ", thisgrid[col_position][j], "> 1, checking for ",   element)
                                for n in thisgrid[col_position][j]:
                                    #print("element ", n, "is being checked against ", element)
                                    if n == element and (i, j) != (col_position, j):
                                        #print("n is equal to k and j is not equal to l")
                                        #print("The array that needs to be adjusted is: ", thisgrid[col_position][j])
                                        thisgrid[col_position][j].remove(element)
                                        array_update += 1
                                        #print(element, "was removed from ", thisgrid[col_position][j])

                    if num_inmini(thisgrid, element, (i, j)):

                        #print("it was found in one of the BOXES")

                        box_x = j // 3  # j
                        box_y = i // 3  # i
                        for y in range(box_y * 3, box_y * 3 + 3):

                            for x in range(box_x * 3, box_x * 3 + 3):

                                for n in thisgrid[y][x]:
                                    if n == element and (i, j) != (y, x):
                                        #print("n is equal to k and j is not equal to x")
                                        #print("The array that needs to be adjusted is: ", thisgrid[y][x])
                                        thisgrid[y][x].remove(element)
                                        array_update += 1
                                        #print(element, "was removed from ", thisgrid[y][x])

    return array_update, thisgrid


# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print("LAST TEST USING UPDATE ARRAY NEXT")
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# grid_after_update = update_array(next_grid)
# print("Printing next_grid - after calling update_array")
# print_updated_grid(grid_after_update)
# print("Squares after recheck", print_count(grid_after_update))

# print("grid after update" , grid_after_update)

# once_more = only_option(grid_after_update)
# print_updated_grid(once_more)
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print("FINAL TEST USING UPDATE ARRAY NEXT")
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# final = update_array(once_more)
# print_updated_grid(final)
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print("FINAL2 TEST USING UPDATE ARRAY NEXT")
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# final2= only_option(final)
# final2= update_array(final2)
# print_updated_grid(final2)


# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print("FINAL3 TEST USING UPDATE ARRAY NEXT")
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# final3= only_option(final2)
# final3= update_array(final3)
# print_updated_grid(final3)

# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print("FINAL4TEST USING UPDATE ARRAY NEXT")
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# final4= only_option(final3)
# final4= update_array(final4)
# print_updated_grid(final4)

def test_if_equal(game_grid, original):
    return game_grid == original


# print(test_if_equal(final,new_grid))


'''Multiple tests until no more changes left 
'''


def basic_solve(grid):
    print(":::::::::::::::::::::::::::::::::::")
    print("STARTING BASIC SOLVE")
    print(":::::::::::::::::::::::::::::::::::")
    change_count = 1
    # array_update = 1

    while change_count > 0:
        change_count, grid = only_option(grid)
        array_update, grid = update_array(grid)
        print(print_count(grid))
        print("change_count ", change_count)
        print("array_update ", array_update)

        if change_count == 0 and array_update == 0:
            break

    return grid


change_count = 0
array_update = 0


 