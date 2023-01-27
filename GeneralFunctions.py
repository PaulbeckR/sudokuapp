def get_box_elements(grid,i,j):
    box_i = i // 3
    box_j = j // 3
    box_elements=[]
    for row in range(box_i*3, box_i*3 + 3):
        for col in range(box_j*3, box_j*3 + 3):
            #what follows here will do for each element in a box.
            box_elements.append(grid[row][col])
    return box_elements

#my_box = get_box_elements(grid, 6,4)
# print(my_box)

#location will be box, row, col. nums will be a list
#def remove_nums(grid, location,  nums):
 #   if location == square:

  #  any(nums in location for range(9))

