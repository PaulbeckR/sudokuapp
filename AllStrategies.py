# from BuildPuzzle import*
# from PreparePuzzle import * 
# from scratch import*


# ''''

# Contains method to check all strategies and solve a grid - with arrays. 

# Just to test use of runthrough: 

# '''
# # boards using 8//13 prepare 
# board1 = [[0, 0, 7, 0, 0, 4, 0, 8, 0],
# [8, 3, 0, 6, 0, 9, 4, 0, 5],
# [0, 5, 2, 0, 0, 0, 0, 0, 9],

# [0, 0, 0, 9, 0, 5, 0, 0, 0],
# [6, 0, 0, 0, 0, 2, 0, 0, 0],
# [0, 1, 9, 0, 0, 0, 5, 4, 2],

# [0, 9, 6, 0, 0, 1, 8, 5, 0],
# [0, 4, 0, 0, 0, 0, 2, 3, 0],
# [0, 0, 0, 4, 0, 8, 9, 0, 6]]

# array1 = create_arrays(board1)

# board2 = [[0, 0, 3, 0, 6, 5, 4, 0, 0], [8, 7, 6, 3, 0, 0, 0, 0, 0], [1, 5, 0, 8, 0, 0, 0, 0, 3], 
#           [3, 0, 1, 9, 0, 4, 2, 0, 0], [4, 0, 0, 0, 0, 0, 9, 0, 0], [0, 0, 0, 5, 0, 3, 0, 0, 6], 
#           [0, 1, 0, 4, 3, 8, 0, 6, 0], [0, 0, 7, 2, 0, 0, 0, 8, 0], [6, 0, 0, 0, 9, 7, 3, 0, 0]]

# array2 = create_arrays(board2)

# board3 = [[9, 7, 3, 0, 8, 0, 0, 0, 0], [2, 0, 6, 7, 4, 5, 3, 9, 0], [8, 5, 4, 6, 0, 0, 0, 0, 0], 
#           [1, 4, 5, 0, 6, 0, 9, 7, 0], [0, 2, 0, 3, 0, 0, 0, 5, 1], [6, 0, 9, 0, 0, 7, 0, 0, 0], 
#           [0, 6, 0, 0, 2, 0, 0, 3, 4], [0, 0, 2, 0, 7, 0, 0, 0, 6], [0, 0, 0, 0, 0, 0, 5, 2, 0]]

# #array3 = create_arrays(board3)




# def runthrough2(grid):
    
#     create_arrays(grid)
    
#     total_changes = 10 
    
#     intial_solved = solved_square(grid)
#     basic = 0
#     candidate_lines = 0
#     hidden = 0
#     xwings = 0
    
#     while total_changes != 0:
#     #run until 0 changes for all
#         grida, changes = basic_solve(grid)
#         print(" Basic Solve")
#         #print_pos_grid(grida)
#         total_changes = changes
#         basic += changes
#         print("TOTAL CHANGES " , total_changes)
        

#         gridcl, count = check_lonely_nums(grida)
#         print(" Candidate lines ")
#         print_pos_grid(gridcl)
#         # print("solved squares ", remaining_arrays(grid))
#         total_changes += count
#         candidate_lines += count
#         print("TOTAL CHANGES " , total_changes)
    
#         gridb, removed = gen_hidden_loop(gridcl) 
        
#         total_changes += removed
#         print(" Hidden ")
#         #print_pos_grid(gridb)
#         hidden += removed
#         print("TOTAL CHANGES " , total_changes)
        
#         gridb2, count2 = basic_solve(gridb)
#         gridc, xwingcount = xwing(gridb2)
#         xwings += xwingcount
#         print("total removed from xwing", xwingcount )
#         print_pos_grid(gridc)
#         total_changes += xwingcount + count2
        
#         print("TOTAL CHANGES IN RUNTHROUGH ", total_changes)
#         print("------------------------------------------")
    
#     print("xwings total ", xwings)
#     print("hidden (doubs/trips)", hidden)
#     print("candidate lines ", candidate_lines)
#     print("basic solve ", basic)
#     print("initial solved ", intial_solved)
        
#     return gridc



# # gridarray, original, game_board = create_new()

# # print_grid(game_board)

# # print("solved squares of initial grid with arrays ", solved_square(gridarray))


# # #print_pos_grid(array1)
# # grid_test = runthrough2(array1)

# # print_pos_grid(grid_test)

# # print("solved squares AFTER runthrough ", solved_square(grid_test))