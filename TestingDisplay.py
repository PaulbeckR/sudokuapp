'''
File to support creating two desting displays. 1 for holding the final grid and the other that will contain arrays. 


'''
import pygame
from BuildPuzzle import*
from PreparePuzzle import *


# first display that will hold just the grid with arrays. 

def array_display(grid):
    pygame.init()
    
    grid = grid
    screen = pygame.display.set_mode((800,800))
    pygame.font.init()
    pygame.display.set_caption("Sudoku")

    pygame.display.list_modes()

    background_color = (50,245,243)

#complete_board = create_grid_fill()
#new_game = new_game_board(complete_board)
#grid = create_arrays(new_game)

    black = (0,0,0)
    x = 0
    y = 0
    diff = 600/9
    val=0

    font1 = pygame.font.SysFont("comicsans", 20)
    font2 = pygame.font.SysFont("comicsans", 20)
    font3 = pygame.font.SysFont("Arial", 12)

    def cord(pos):
        global x 
        x = pos[0]//diff
        global y 
        y = pos[1]//diff
                

#Highlights the selected cell.
    def draw_box():
        for i in range(2):
            pygame.draw.line(screen, (255, 0, 0), (i * diff-3, (j + i)*diff), (i * diff + diff + 3, (j + i)*diff), 7)
            pygame.draw.line(screen, (255, 0, 0), ( (i + i)* diff, j * diff ), ((i + i) * diff, j * diff + diff), 7)

# creates the drawn box with gridlines.     
    def draw(grid):
        for j in range(len(grid[i])):
            for i in range(len(grid)):
                #if grid[i][j] != 0:
                #fills already complete numbers with blue.
                if len(grid[i][j]) == 1:
                    pygame.draw.rect(screen, (152,245,255), (i * diff, j * diff, diff + 1, diff + 1))
                
                #Fills in given numbers and centers them.
                    text1=font1.render(str(grid[i][j]),1,black)                
                    screen.blit(text1, (i*diff + 15, j * diff + 20))
                else:
                    text1=font3.render(str(grid[i][j]),1,black)  
                                
                    screen.blit(text1, (i*diff + 10, j * diff + 15))
                    
    #draw horiz/vert lines          
        for i in range(10):
            if i % 3 == 0:
                thick = 7
            else:
                thick = 1
            pygame.draw.line(screen, black, (0, i *diff), (600, i*diff), thick)
            pygame.draw.line(screen, black, (i*diff, 0), (i*diff, 600), thick)


    run = True
    while run:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for j in range(9):
            for i in range(9):
                #if grid[i][j] != 0:
                #fills already complete numbers with blue.
                if len(grid[i][j]) == 1:
                    pygame.draw.rect(screen, (152,245,255), (j * diff, i * diff, diff + 1, diff + 1))
                
                #Fills in given numbers and centers them.
                    text1=font1.render(str(grid[i][j]),1,black)                
                    screen.blit(text1, (j*diff + 15, i * diff + 20))
                else:
                    text1=font3.render(str(grid[i][j]),1,black)  
                                
                    screen.blit(text1, (j*diff + 10, i * diff + 15))
        for i in range(10):
            if i % 3 == 0:
                thick = 7
            else:
                thick = 1
            pygame.draw.line(screen, black, (0, i *diff), (600, i*diff), thick)
            pygame.draw.line(screen, black, (i*diff, 0), (i*diff, 600), thick)
        pygame.display.update()
    pygame.quit()





