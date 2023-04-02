from BuildPuzzle import*
from scratch import*
from TestingDisplay import *

import copy

'''
Complete solve function for new game board. Then, calculate possible iterations with number of randoms chosen
in the solve function, 

Start with first rand - smallest in length. save length.

update board, 

get next rand - save length.

update  board... 

As board updates rand arrays should get smaller/fewer. Multiplying these together should give possible iterations. 

Try to solve all possible iterations, stop and backtrack if board not valid. 

if more than one board found, board not unique. 

'''

# sample_grid = [[3,6,5,8,0,0,2,0,0],
# [0,0,0,2,0,0,6,9,0],
# [0,8,0,7,0,4,0,0,0],
# [2,0,1,3,8,5,4,0,7],
# [0,3,0,9,7,6,0,0,0],
# [0,0,0,0,0,0,0,0,0],
# [4,2,6,0,1,0,0,0,0],
# [7,0,0,4,2,0,9,0,0],
# [0,0,9,6,0,0,5,0,0]]

# print_grid(sample_grid)

# original = [[3,6,5,8,9,1,2,7,4],
# [1,4,7,2,5,3,6,9,8],
# [9,8,2,7,6,4,1,3,5],
# [2,9,1,3,8,5,4,	6,7],
# [5,3,4,9,7,6,8,2,1],
# [6,7,8,1,4,2,3,5,9],
# [4,2,6,5,1,9,7,8,3],
# [7,5,3,4,2,8,9,1,6],
# [8,1,9,6,3,7,5,4,2]]

# print_grid(original)



# rand_nums2 = [8,3,7,1,1,1,6]

# rand_list2 = [(0, 3), (0, 0), (1, 2), (1, 0), (2, 6), (2, 6), (5, 0)]


# array_grid = create_arrays(sample_grid)




def valid_solution(validgrid):
    for i in range(9):
        for j in range(9):
            if is_valid(validgrid, (i,j), validgrid[i][j]) == False:
                return False
    return True





def possible_iterations(board, rand_list, rand_nums, original):
    
    random_dict = dict()
    
    length_of_choices = []
    
    grid = copy.deepcopy(board)
    overwrite = copy.deepcopy(board)
  
    count = 0
    random_dict = dict(zip(rand_list, rand_nums))
        
    print("DICTIONARY IS ", random_dict)
    
    #have positions and the numbers UESD for solution. Try all alternatives. Calculate all alternatvies.
    print("Start of loop through dictionary")
    for position, numbers in random_dict.items():
            
        row = position[0]
        col = position[1]
        print("position is", (row,col))
                
        print("START OF LOOP THROUGH GRID ARRAY") 
        
        for pos_num in grid[row][col]:
                
            print("Possible numbers at position", position, "is ", grid[row][col])
            if type(numbers) is not list: numbers = [numbers]
            if pos_num not in numbers:
                    
                length_of_choices.append(len(grid[row][col]))
                print(length_of_choices, "Length of choices")
                    
                grid[row][col] = [pos_num]
                print(grid[row][col], "is set as new num at", (row,col))
                    
                    
                runthrough(grid)
                    
                if solved_square(grid) == 81:   
                #Check if Board is valid, if not, set rand as clue and try next rand.
                    if valid_solution(grid) == True:
                        print("found a second solution: ")
                        
                        break
                    elif valid_solution(grid) == False:
                        print("BOARD NOT VALID")
                        tryagain = copy.deepcopy(board)
                        #set board to have correct choice
                        overwrite[row][col] = numbers
                        tryagain[row][col] = numbers
                        print("reset position to ", tryagain[row][col])
                        
                        grid = tryagain
                        
                        #add wrong number to list of numbers (to keep searching alternatives with unused nums)
                        numbers.append(pos_num)
                        print("new numbers are ", numbers)
                        continue
                    
                    else:
                        if test_if_equal(grid, original) == True:
                          
                            return "BOARD IS UNIQUE, only one solution"
                    
                        
                        
                    #try to solve with first alternative choice. Will have new rand_nums/rand_list with updated possible answers                 
                   # grid, rand_list, rand_nums = solve_grid(grid, original, overwrite)
                   
                
        print("new rand list ", rand_list, "new rand_nums ", rand_nums)
        count += 1
                                 
# can use find_array, random_guessing                    
                    
def all_iterations(board, original, sample):
    grid = copy.deepcopy(board)
    orig = copy.deepcopy(original)
    
    print_pos_grid(grid)
    
    random_count = 0
    count = 0
    start_at = 0
    continue_trying = True
    
    #runthrough(grid)

    while count <= 100:
        print("count is ", count )
        
        print(solved_square(grid), "solved out of 81")
        if solved_square(grid) == 81:
            
            
            if valid_solution(grid) == True:
                
                if test_if_equal(grid, orig) == False:
                    print("found another solution")
                    
                    continue_trying = False
                    return grid
                    
                    
                    
                elif test_if_equal(grid, orig) == True:
                    print("found same solution, keep looking")
                            
            elif valid_solution(grid) == False:
                
                print_pos_grid(grid)
                print("grid not valid ")
               
                tryagain = copy.deepcopy(board)
                    
                grid = tryagain
                grid[row][col] = backup
        
        else:
            
            array = find_array(grid)
           
            
            row = array[0]
            col = array[1]
            print("my array is ", grid[row][col], "at position", (array[0], array[1]))
            
            backup = grid[row][col]
            print("back up is ", backup)
            
            
            for num in grid[row][col]:
                
                grid[row][col] = num
                sample[row][col] = num
                print("position is now ", grid[row][col], "at", (row,col))
                backup.remove(num)
                print("removed num from back up", backup)
                
                if not is_valid(sample, (row,col), num):
                    print("position wasn't valid, try remaining backup")
                    #should allow me to store 2 item as back up, then one item if no more options. THen as 
                    # I loop around, will find next array for len greater than 1... 
                    grid[row][col] = backup
                    print("position is now ", grid[row][col], "at", (row,col))
                    sample[row][col]  = 0
                       
                else:
                    print("position is valid, keep going ")
   
        #runthrough(grid)
        count += 1
        
    return grid

'''
Backtracking solver using 'random' selection of available nums for a solution. Backtracks when invalid
found. 

'''
def fill_grid2(grid2, sampleg):
   
    #print("solved squares before next array are ", solved_square(grid2))
    array = find_array(grid2)
    if not array:
        return True
    row, col = array
    #added suffle feature to support random selection during rounds.
    #print("row col is ", (row,col))
    #print("square is ", grid2[row][col])
    #print("back up position is ", backup, "at ", (row,col))
    
    #For each available candidate at array location:
    for num in grid2[row][col]:
        #print("trying ", num, "for position", (row,col), "from array", grid2[row][col])
        #check if valid. 
        if is_valid(sampleg, (row, col), num):
            #set initial array as backup
            backup = grid2[row][col]
            
            #set number as solution
            grid2[row][col] = [num]
            
            #set number as solution 
            sampleg[row][col]= num
            
            #print("adding ", grid2[row][col], "to position", (row,col))
            
            #keep trying to fill using same selection process - if false, number wasn't valid. 
            #triggers backup 
            if fill_grid2(grid2, sampleg):
                return True

            #reset to backup
            grid2[row][col] = backup
           
            #reset to unsolved
            sampleg[row][col] = 0
            #print("solved squares are ", solved_square(grid2))
            
            #print(num, "wasn't valid, setting as back up", grid2[row][col])
    return False


'''
Same as fillgrid but adding runthrough as partial solver into it instead of using the solve function from scratch



'''
def fill_withsolve(gridarr, gridzero):
    
    gridarr = runthrough(gridarr)
    
    array = find_array(gridarr)
    if not array:
        return True
    row, col = array
    print("LOOKING TO SET ARRAY", gridarr[row][col] )
    for num in gridarr[row][col]:
        #print("trying ", num, "for position", (row,col), "from array", grid2[row][col])
        #check if valid. 
        if is_valid(gridzero, (row, col), num):
            #set initial array as backup
            backup = gridarr[row][col]
            
            #set number as solution
            gridarr[row][col] = [num]
            print("setting new position", (row,col), "to", num)
            
            
            #set number as solution 
            gridzero[row][col]= num
            
            #print("adding ", grid2[row][col], "to position", (row,col))
            
            #keep trying to fill using same selection process - if false, number wasn't valid. 
            #triggers backup 
            if fill_withsolve(gridarr, gridzero):
                
                return True

            #reset to backup
            gridarr[row][col] = backup
           
            #reset to unsolved
            gridzero[row][col] = 0
            #print("solved squares are ", solved_square(grid2))
            
            #print(num, "wasn't valid, setting as back up", grid2[row][col])
    return False
    
    
    


            

def back_to_board(grid):
    for i in range(9):
        for j in range(9):
            if type(grid[i][j]) is int: grid[i][j] = [grid[i][j]]
            
            if len(grid[i][j]) > 1: 
                grid[i][j] = 0
            
            if type(grid[i][j]) is list: [grid[i][j]] = grid[i][j]
    return grid
                


''''
Takes grid (with arrays), sets to gameboard (with 0's ), tries to solve. 

Fillgrid2 should always return with at least the same board we started with. Could attempt to run a few times
or remove any random numbers selected previously (minimize guessing). If all solutions tried and no board found
then we have a unique board. If another solution found, board not unique.

 
'''
            
def get_solutions(grid2):
    arraycopy = copy.deepcopy(grid2)
    blanked = back_to_board(grid2)
    
    print("printing blanked")
    print_grid(blanked)
    print(blanked)
    print("array copy ")
    print_grid(arraycopy)
        
    #This SHOULD fill in my grid until solved... 
    fill_withsolve(arraycopy, blanked)
    print("after grid fill")
    print_grid(arraycopy) 
       
   
    return arraycopy
    
'''
Createnew returns: gridarray (arrays), original (completed), arraycopy(deep copy of array)

'''
# mygrid, orig, arrcopy = create_new()


# # arrcopy becomes "overwrite", returned as game_board and final. It will have arrays.     
# #final , randlist, randnums , grid_o = solve_grid(mygrid, orig, arrcopy) 



# print("................FINAL - arrays..................")
# print_grid(arrcopy)
# print("...............................")
# print("...................................")

# # WITH SOLVE GRID
# #test = get_solutions(final)

# # WITH FILL_WITHSOLVE
# test = get_solutions(arrcopy)
        


def solution_rounds(grid, grid_o):
    
    #rounds = 3
   # while rounds > 0:

    if test_if_equal(grid, grid_o) != True:
        print("two solutions, printing grid2:")
        print_grid(grid)
        print("ORIGINAL::::::::::::::::::::")
        print_grid(grid_o)
        
        
           
        return False
            
    else:
        print("SAME SOLUTION")
            
           # rounds -= 1
        return True


# finaltest = solutionrounds(test, orig)

# print(finaltest)

# if finaltest == True:
#     print(" I FOUND A UNIQUE BOARD")
    


# print("................Test - completed board after fill grid..................")
# print_grid(test)
# print("...................................")
# print("...................................")
# print("...................................")

# print("................Original - completed board..................")
# print_grid(orig)
  
    
def find_unique():
    
    board_isunique = False
    count = 0
    
    while board_isunique == False:
        
        count += 1
        
        mygrid, orig, arrcopy = create_new()
        print("NEWEST ARRCOPY ::::::::::::::::::::::::::::::::::::::::::")
        print_pos_grid(arrcopy)
    
        test = get_solutions(arrcopy)
        print("test is ................")
        print_pos_grid(test)
        
        if solution_rounds(test, orig) == True:
            board_isunique == True
            unique_board = back_to_board(arrcopy)
            return unique_board, count
        elif solution_rounds(test, orig) == False:
            print("starting over")
            print("INITAL GAMEBOARD WAS ")
            print_grid(back_to_board(mygrid))
            continue
  
        
uni = find_unique()

print_grid(uni)

array_display(uni)