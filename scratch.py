def get_box_dict(grid, pos):
    
    #NEED TO use POS or establish it before making dictionary. 
    x = pos[0]
    y = pos[1]
    
    pos_dic = {}
    num_dic = {}
  
    # create box guides 
 
    for i in range(9):
        pos_dic[i] = (x,y) 
    print("pos dic is ", pos_dic)
    
    box_row = x // 3
    box_col = y // 3
    
    #going three at a time
    count = 0
    list_box_arrays = []
    list_positions = []
    for row in range(box_row * 3, box_row * 3 + 3):
        for col in range(box_col * 3, box_col * 3 + 3):
                        
            list_box_arrays.append(grid[row][col])
            # print("position is ", (row,col))
            list_positions.append((row,col))
            
            # print("list_positions added ", list_positions)
            
            # print("List is ", list_box_arrays)
    for i in list_box_arrays:    
            # create dictionary of all values in box. 
        num_dic[count] = i
        count += 1
    count2 = 0  
    for k in list_positions:
        pos_dic[count2] = k
        count2 += 1
 
    return num_dic, pos_dic
            
test_num, test_pos = get_box_dict(grid, (0,1))

print(test_num)
print(test_pos)


row_0 = set()
row_1 = set()
row_2 = set()

col_0 = set()
col_1 = set()
col_2 = set()

for i, value in enumerate(test_num.values()):
    if i < 3:
        if len(value) > 1:
            row_0.update(value)
    elif i < 6:
        if len(value) > 1:
            row_1.update(value)
    else:
        if len(value) > 1:
            row_2.update(value)

for i, value in enumerate(test_num.values()):
    if (i == 0 or i == 3 or i == 6):
        if len(value) > 1:
            col_0.update(value)
    elif (i == 1 or i == 4 or i == 7):
        if len(value) > 1:
            col_1.update(value)
    else:
        if len(value) > 1:
            col_2.update(value)

print(row_0)
print(row_1)
print(row_2)
print(col_0)
print(col_1)
print(col_2)

# Now find if any number in row_0 is NOT in row_1 or row2. 

for number in row_0:
    if number not in row_1 and number not in row_2:
        lonely_row_int = number
        print("row_0", lonely_row_int)
for number in row_1: 
    if number not in row_0 and number not in row_1:
        lonely_row_1 = number
        print("row_1", lonely_row_1)
for number in row_2:
    if number not in row_0 and number not in row_1:
        lonely_row_2 = number
        print("row_2", lonely_row_2)
for number in col_0:
    if number not in col_1 and number not in col_2:
        lonely_col_0 = number
        print("lonely_col_0", lonely_col_0)
for number in col_1: 
    if number not in col_0 and number not in col_1:
        lonely_col_1 = number
        print("col_1", lonely_col_1)
for number in col_2:
    if number not in col_0 and number not in col_1:
        lonely_col_2 = number
        print("col2", lonely_col_2)

            # now add all columns 
for single_col_combine in range(3):
                    
    if len(grid[single_col_combine][col]) > 1:
                    # update all squares in each row of a column to my set. 
                    single_col.update(grid[single_col_combine][col])
                    print("adding to single_col set ", grid[single_col_combine][col], "from", (single_col_combine, col))
                else:
                    single_col.add(0)
                    print("adding to single_col", 0 , "at ", (single_col_combine, col))
                    # update single column list to col list
            box_cols.append(single_col)
            print("box_cols ", box_cols)
            
        