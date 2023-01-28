from main import*


def check_correct(new_game, complete_board):
    for i in range(9):
        for j in range(9):
            if new_game[i][j] == complete_board[i][j]:
                return True
            
            return "Game is not correct"    
        
The loop thats keep the window running
while run:

      # White color background
        screen.fill((255, 255, 255))
      # Loop through the events stored in event.get()
        for event in pygame.event.get():
            # Quit the game window
             if event.type == pygame.QUIT:
                  run = False
           # Get the mouse position to insert number
             if event.type == pygame.MOUSEBUTTONDOWN:
                 flag1 = 1
                 pos = pygame.mouse.get_pos()
                 get_cord(pos)
                 
           # Get the number to be inserted if key pressed
              if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_LEFT:
                             x-= 1
                             flag1 = 1
                    if event.key == pygame.K_RIGHT:
                            x+= 1
                            flag1 = 1
                    if event.key == pygame.K_UP:
                            y-= 1
                            flag1 = 1
                    if event.key == pygame.K_DOWN:
                            y+= 1
                            flag1 = 1
                    if event.key == pygame.K_1:
                            val = 1
                    if event.key == pygame.K_2:
                             val = 2
                    if event.key == pygame.K_3:
                             val = 3
                    if event.key == pygame.K_4:
                             val = 4
                    if event.key == pygame.K_5:
                             val = 5
                    if event.key == pygame.K_6:
                             val = 6
                    if event.key == pygame.K_7:
                             val = 7
                    if event.key == pygame.K_8:
                             val = 8
                    if event.key == pygame.K_9:
                             val = 9
                    if event.key == pygame.K_RETURN:
                             flag2 = 1
                    # If R pressed clear the sudoku board
                    if event.key == pygame.K_r:
                             rs = 0
                            error = 0
                            flag2 = 0
                            grid =[
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0]
                            ]
                   # If D is pressed reset the board to default
                   if event.key == pygame.K_d:
                            rs = 0
                            error = 0
                            flag2 = 0
                            grid =[
                            [7, 8, 0, 4, 0, 0, 1, 2, 0],
                            [6, 0, 0, 0, 7, 5, 0, 0, 9],
                            [0, 0, 0, 6, 0, 1, 0, 7, 8],
                            [0, 0, 7, 0, 4, 0, 2, 6, 0],
                            [0, 0, 1, 0, 5, 0, 9, 3, 0],
                            [9, 0, 4, 0, 6, 0, 0, 0, 5],
                            [0, 7, 0, 3, 0, 0, 0, 1, 2],
                            [1, 2, 0, 0, 0, 7, 4, 0, 0],
                            [0, 4, 9, 2, 0, 6, 0, 0, 7]
                            ]
             if flag2 == 1:
                  if solve(grid, 0, 0)== False:
                           error = 1
                  else:
                           rs = 1
                           flag2 = 0
             if val != 0: 
                  draw_val(val)
                  # print(x)
                  # print(y)
                  if valid(grid, int(x), int(y), val)== True:
                           grid[int(x)][int(y)]= val
                           flag1 = 0
                  else:
                           grid[int(x)][int(y)]= 0
                           raise_error2()
                  val = 0

            if error == 1:
                    raise_error1()
            if rs == 1:
                    result()
            draw()
            if flag1 == 1:
                    draw_box()
            instruction()


            # Update window
            pygame.display.update()


# Quit pygame window
pygame.quit()