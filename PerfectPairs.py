from FindSolutions import *

''''
Script to support advanced solve solutions. From https://www.sudokuoftheday.com/techniques/hidden-pairs-triples

Candidate Lines: 

Finding any numbers 0-9 that occur only on a single 3x3 row or column. Where 4 may only occur (exist in array) in 
in positions (7,8) and (8,8). for the last 3x3 box. Any other 4s listed in arrays of column 7 would be ineligible.
This is because of a natural limit set by the 4 being required in column 7 AND in the last box.


Double Pairs: 


Multiple Lines: 
When searching across entire columns or rows of 3x3 sections, if a number is only available for 2/3 cols/rows 
for two boxes, and the third box contains the number in multiple rows. The third box may eliminate any of that number
from spaces that occupy the two rows/cols that are limited by the initial two boxxes. 

Naked Pairs (easiest to program)

If in any given 3x3, row , or column; if two numbers are listed as the only options for two boxes (1,5) (1,5).
any other array in the 3x3, row or col that is SHARED by the matching pair can remove the associated numbers as
options. The same can be done for triples (2,4) (4,7) (2,7)

Hidden pair / triple

if you have a pair (1,3) (1,2,3) in any 3x3, row,col and the 1 and 3 are not available elsewhere. The two can be 
removed , as well as the 1,3 from the subsequent row/col/3x3 positions.


'''


# take a given grid that contains arrays for unsolved positions. Search for any pairs. Where in a single
# row/ col / 3x3 grid two arrays contain two digits that are NOT in

# also want to update any arrays as I go


# do rows/cols first
# do I count frequency and

# only perfect pairs (1,5) (1,5)


# - in most recent test: It found the perfect pair in the BOX first, rather than col. and it removed a number from
# the second paired element. It didnt continue down the col, as it had skipped to box, and so missed removing two elements
# from two seperate squares.
def perfect_pairs(grid):
    # start comparisons with first element.
    for i in range(9):
        for j in range(9):

            # only if it is more than 1. Ideally for simplicity, it would be length 2 or 3
            if len(grid[i][j]) == 2:  # or len(grid[i][j]) ==3:
                print("This is the current array being checked ", grid[i][j])
                # then the array I want to compare first will be [i][j]. AND i want to compare for the row,
                # col and box.

                first_arr = grid[i][j]
                for l in range(9):
                    if len(grid[i][l]) == 2:  # or len(grid[i][l]) == 3:
                        print("Comparing first_arr to ", grid[i][l])
                        # if the first arr and the position being searched are a match (and not the same location)
                        if first_arr == grid[i][l] and (i, j) != (i, l):
                            print("Found a perfect pair in the ROW")
                            # IF I WANT TO CHECK MORE THAN TWO, this needs to change. Count if onl 2 spots.
                            # create array based on shared numbers.
                            numbers_to_remove = first_arr
                            for r in range(9):
                                if len(grid[i][r]) > 1 and (i, r) != (i, j) and (i, l):
                                    for n in grid[i][r]:
                                        print("checking each N in ", grid[i][r])
                                        if n in numbers_to_remove:
                                            print(n, "was removed from ", grid[i][r])

                                            grid[i][r].remove(n)
                                            print(n, "was removed from ", grid[i][r])

                for v in range(9):
                    if len(grid[v][i]) == 2:  # or len
                        print("comparing first_arr to ", grid[v][j])
                        if first_arr == grid[v][j] and i != v:
                            print("Found a perfect pair in the COLUMN")
                            numbers_to_remove = first_arr
                            for r in range(9):
                                if len(grid[r][j]) > 1 and r != i and v:
                                    for n in grid[r][j]:
                                        print("checking each N in ", grid[r][j])
                                        if n in numbers_to_remove:
                                            print(n, "was removed from ", grid[r][j])

                                            grid[r][j].remove(n)
                                            print(n, "was removed from ", grid[r][j])
                box_start_row = i // 3
                box_start_col = j // 3

                for row_element in range(box_start_row * 3, box_start_row * 3 + 3):
                    for col_element in range(box_start_col * 3, box_start_col * 3 + 3):
                        # for each element of my square, find one that only has two elements.
                        if len(grid[row_element][col_element]) == 2:
                            # set to variable compare for easier typing. This is same as first_arr
                            compare = grid[row_element][col_element]
                            # if compare and first_arr are the same NUMBERS, but NOT the same position:
                            if first_arr == compare and (i, j) != (row_element, col_element):
                                print("fount a perfect pair in the BOX ", grid[row_element][col_element],
                                      (row_element, col_element))
                                # I found a pair, now I want to search for any other numbers that are in remaining arrays.
                                numbers_to_remove = first_arr
                                # search through box again.
                                for alt_box_row in range(box_start_row * 3, box_start_row * 3 + 3):
                                    for alt_box_col in range(box_start_col * 3, box_start_col * 3 + 3):
                                        # look inside any that are greater than 1
                                        if len(grid[alt_box_row][alt_box_col]) > 1:
                                            for number in grid[alt_box_row][alt_box_col]:
                                                print("checking each number ", number, "in",
                                                      grid[alt_box_row][alt_box_col], (alt_box_row, alt_box_col))
                                                # if the number exists in my numbers to remove AND its NOT in the i,j position or my second pair position:
                                                if number in numbers_to_remove and (alt_box_row, alt_box_col) != (
                                                i, j) and (row_element, col_element):
                                                    print(number, "was removed from ", grid[alt_box_row][alt_box_col])
                                                    grid[alt_box_row][alt_box_col].remove(number)
                                                    print(number, "was removed from ", grid[alt_box_row][alt_box_col])
    return grid


#hope  = perfect_pairs(pos_nums_grid)
#print_updated_grid(pos_nums_grid)