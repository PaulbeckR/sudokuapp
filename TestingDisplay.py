# '''
# File to support creating two desting displays. 1 for holding the final grid and the other that will contain arrays. 


# '''
# import pygame
# from BuildPuzzle import*
# from PreparePuzzle import *



# # first display that will hold just the grid with arrays. 

# def array_display(grid,title):
#     pygame.init()
    
#     grid = grid
#     screen = pygame.display.set_mode((800,800))
#     pygame.font.init()
#     pygame.display.set_caption(str(title))

#     pygame.display.list_modes()

#     background_color = (50,245,243)



#     black = (0,0,0)
#     x = 0
#     y = 0
#     diff = 600/9
#     val=0

#     font1 = pygame.font.SysFont("comicsans", 20)
#     font2 = pygame.font.SysFont("comicsans", 20)
#     font3 = pygame.font.SysFont("Arial", 12)

#     def cord(pos):
#         global x 
#         x = pos[0]//diff
#         global y 
#         y = pos[1]//diff
                

# #Highlights the selected cell.
#     def draw_box():
#         for i in range(2):
#             pygame.draw.line(screen, (255, 0, 0), (i * diff-3, (j + i)*diff), (i * diff + diff + 3, (j + i)*diff), 7)
#             pygame.draw.line(screen, (255, 0, 0), ( (i + i)* diff, j * diff ), ((i + i) * diff, j * diff + diff), 7)

# # creates the drawn box with gridlines.     
#     def draw(grid):
#         for j in range(len(grid[i])):
#             for i in range(len(grid)):
#                 #if grid[i][j] != 0:
#                 #fills already complete numbers with blue.
#                 if len(grid[i][j]) == 1:
#                     pygame.draw.rect(screen, (152,245,255), (i * diff, j * diff, diff + 1, diff + 1))
                
#                 #Fills in given numbers and centers them.
                
#                     text1=font1.render(str(grid[i][j]),1,black)                
#                     screen.blit(text1, (i*diff + 15, j * diff + 20))
#                 else:
#                     # text, font, colour, x,y,screen, allowed_width
#                     wrap_text_display(grid[i][j], font3, black, i*diff, j*diff,screen, 12)
#                     print("text1", text1)
                    
#                    # text1=font3.render(str(grid[i][j]),1,black)  
                                
#                     #screen.blit(text1, (i*diff + 10, j * diff + 15))
                    
#         #draw horiz/vert lines          
#         for i in range(10):
#             if i % 3 == 0:
#                 thick = 7
#             else:
#                 thick = 1
#             pygame.draw.line(screen, black, (0, i *diff), (600, i*diff), thick)
#             pygame.draw.line(screen, black, (i*diff, 0), (i*diff, 600), thick)


#     run = True
#     while run:
#         screen.fill((255,255,255))
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#         for j in range(9):
#             for i in range(9):
#                 #if grid[i][j] != 0:
#                 #fills already complete numbers with blue.
#                 if type(grid[i][j]) is int: grid[i][j] = [grid[i][j]]
#                 if len(grid[i][j]) == 1:
#                     pygame.draw.rect(screen, (152,245,255), (j * diff, i * diff, diff + 1, diff + 1))
                
#                 #Fills in given numbers and centers them.
#                     text1=font1.render(str(grid[i][j]),1,black)                
#                     screen.blit(text1, (j*diff + 15, i * diff + 20))
#                 else:
                    
#                     wrap_text_display(grid[i][j], font3, black, i*diff, j*diff,screen, 400) 
#                    # screen.blit(text1, (i*diff + 10, j * diff + 15))
#         for i in range(10):
#             if i % 3 == 0:
#                 thick = 7
#             else:
#                 thick = 1
#             pygame.draw.line(screen, black, (0, i *diff), (600, i*diff), thick)
#             pygame.draw.line(screen, black, (i*diff, 0), (i*diff, 600), thick)
#         pygame.display.update()
#     pygame.quit()


# def wrap_text_display(number_list, font, colour, x,y,screen, allowed_width):
#     #splitting numbers array into 
#     numbers_string = ",".join(map(str, number_list))
#     numbers = numbers_string.split(",")
    
#     #create lines
#     lines = []
    
    
#     while len(numbers) > 0:
#         #fill each line to their max
#         line_numbers = []
#         line_width = 0
#         while len(numbers) > 0: 
#             #print(f"Current line width: {line_width}")
#             #fit_length, fit_height = font.size(' '.join(line_numbers + numbers[:1]))
#             #next_number_width = font.metrics(numbers[0])[0][4]
#             #print(f"Next number width: {next_number_width}")
#             if line_width + font.metrics(numbers[0])[0][4] > allowed_width:
                
#                 break
#             line_width += font.metrics(numbers[0])[0][4]
            
#             line_numbers.append(numbers.pop(0))
#             #print(line_numbers, "are line numbers")
       

#         lines.append(','.join(line_numbers))
#     #print(f"Lines: {lines}")
   
    
#     y_offset = 0
#     for line in lines:
#         fit_length, fit_height = font.size(line)
        
#         tx = x  
#         ty = y 
        
#         font_surface = font.render(line, True, colour)
#         #print("font surface is : ", font_surface)
#        # screen.blit(text1, (j*diff + 15, i * diff + 20))
#         screen.blit(font_surface, (ty + 20, tx + 20 ))
        
#         #y_offset += fit_height
        
#     return font_surface




# #complete_board = create_grid_fill()
# #new_game = new_game_board(complete_board)
# #grid = create_arrays(new_game)
# #print_pos_grid(grid)
# #array_display(grid)


