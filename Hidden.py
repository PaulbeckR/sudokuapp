from BuildPuzzle import *
from PreparePuzzle import *


'''
Hidden pairs/triples are if only two/three numbers are available in a box row or col. Finding this can eliminate other options in the arrays of the pair, as well as any options for 

that pair in the associated row/col. 


lonely numbers but set to 2 nums in two squares of the same row/box col/box? 

dictionaries, position / array to map through for



'''

'''
Method to take each box/row /col to "set search parameter" 
    1. Box - take given box start and search each of the 9 squares. 
    2. Row - take given box start and search each of the 3 rows 
    3. Col - take given box start and search each of teh 3 cols. 
    



'''

grid_new = create_grid_fill()  
grid_game = new_game_board(grid_new)
grid = create_arrays(grid_game)

print_pos_grid(grid)

def hidden_search(grid, box):
    
    # Set starting row / col 
    row_start = box[0] *3
    col_start = box[1] *3 
    
    row_end = row_start + 3
    col_end = col_start + 3

    box_dict = dict()
    row_dict = dict()
    col_dict = dict()
    
    #keys represent each number 1-9
    keys = range(10)

    for i in keys:
        print("KEY CHECKED IS ", i)
        
        bnum_positions = []
        #Search each Square of the BOX
        for row_square in range(row_start, row_end): 
            for col_square in range(col_start, col_end):
                #print("square position is ", (row_square,col_square))
                
                # if the array is more than 1
                if len(grid[row_square][col_square]) > 1:
                    #print("square array more than one")
                    
                    for number in grid[row_square][col_square]:
                        #print("number is , ", number)                    

                        if number == i:
                            #print("number == i")
                            bnum_positions.append((row_square,col_square))        
                            #print("added to dict at , " , i , "for position", (row_square, col_square))
                            
        #Add that list of positions to the dictionary at the corresponding Key - i
        box_dict[i] = bnum_positions

        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("START OF ROW DICTIONARY")
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
 
    #Search through rows: 
    for row in range(row_start, row_end):        
        line0 = dict()    
        for k in keys: 
            #print(" K IS ::::::::::", k)   
        
            rnum_positions = []  
            #for row in range(row_start, row_end):      
            for col in range(9):
                #print("ROW CHECK POSITION IS  ", (row,col))
                if len(grid[row][col]) > 1:
                    for number in grid[row][col]:
                        if number == k:
                            rnum_positions.append((row,col))
                            #print("added to dict at , " , k , "for position", (row, col))
            line0[k] = rnum_positions
            #print("Line0 is ", line0)
        row_dict[row] = line0
        
        #print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        #print("START OF COL DICTIONARY")
        #print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
          
    for col in range(col_start, col_end):
        
        line0 = dict()    
        for k in keys: 
            #print(" K IS ::::::::::", k)   
        
            cnum_positions = []  
            #for row in range(row_start, row_end):
   
            for row in range(9):
                #print("ROW CHECK POSITION IS  ", (row,col))
                if len(grid[row][col]) > 1:
                    for number in grid[row][col]:
                        if number == k:
                            cnum_positions.append((row,col))
                            #print("added to dict at , " , k , "for position", (row, col))
            line0[k] = cnum_positions
            #print("Line0 is ", line0)
        col_dict[col] = line0   
         
    return box_dict, col_dict  , row_dict
 
# TESTING HIDDEN SEARCH           
# box_test, col_test, row_test = hidden_search(grid, (0,0))

# Reformat Dictionary: Use position as keys.
def position_dict(grid, box):
    row_start = box[0] *3
    col_start = box[1] *3 
    
    row_end = row_start + 3
    col_end = col_start + 3

    box_dict = dict()
    row_dict = dict()
    col_dict = dict()
    
    #Search through box.     
    for r_square in range(row_start, row_end):
        for c_square in range(row_start, row_end): 
            # if the square holds more than one num:
            if len(grid[r_square][c_square]) > 1:
                #set position as key
                position = (r_square, c_square)
                numbers_l = []
                
                for number in grid[r_square][c_square]:
                    numbers_l.append(number)
                    
                
                box_dict[position] = numbers_l
                
            
    

#print("box_test" , box_test)

#print("col_test" , col_test)

#print("row_test" , row_test)


## now I have a box by box dictionary of all my nums. 

## hidden pairs/triples will have keys that exist only two or three times per location

print(col_test.get(0))

test_hidden = {1 : [(0,0),(0,1)], 2:[(0,0), (0,1)], 3:[(0,0), (0,2), (0,3)], 4: [(0,0), (0,5), (0,6)], 5: [], 6: [(0,0), (0,3), (0,4),(0,6),(0,8)]}

# Double = two numbers available in the same two places. 

# Triple = three numbers available in the same two to three places. 

# 1. Reduce dictionary to just items with three locations.

new_dict = dict()
for key1, value1 in test_hidden.items():
    print("length", len(value1))
    if len(value1) > 1 and len(value1) < 4:
        new_dict[key1] = value1
        
print("new_dict", new_dict)


def hidden_pair(dict)
# For each dict item of length
    pair = dict()
    for key1, value1 in box_test.items():
     
    # test all other items in dict to see if match: pair/trip
    
        for key2, value2 in box_test.items():
        
        #cant be same ite
            if key1 != key2:
            
                if len(value1) == 2 and len(value2) == 2 and set(value1) == set(value2):
                    print("matched ", key1, key2)
                    pair[key1] = value1
                    pair[key2] = value2 
    return pair
    
            
# Triple: Either standard hidden triple (same three nums in three positions)

# OR three numbers accross three positions, but can be of length 1 or 2 

# 1,2  2,3 , 1,2,3 

# Three numbers ONLY available in three boxes. 

def hidden_trip(dict)


    new_dict = dict()
    for key1, value1 in dict.items():
        print("length", len(value1))
        if len(value1) > 1 and len(value1) < 4:
            new_dict[key1] = value1
    
    trip = dict()
    
    # if 3 squares hold 3 numbers and only those numbers. 
    
    for key1 , value1 in dict.items():
        


        






        
        

    











