import pygame 

from BuildPuzzle import *
from PreparePuzzle import*

complete_board = create_grid_fill()

#previous: 
#new_grid = create_grid_fill()

#print_grid(new_grid)

#print(new_grid)

# prepare puzzle
new_game = new_game_board(complete_board)

background_color = (50,245,243)
black = (0,0,0)

def place(window,pos):
    board_font = pygame.font.SysFont('Arial', 30, bold=False, italic=False)
    i,j = pos[0], pos[1]
    
    while True:
        for e in pygame.event.get():
        
            if (e.type == pygame.QUIT):
                pygame.quit()
                return
            if e.type == pygame.KEYDOWN:
                if complete_board[i-1][j-1] != 0:
                    return
        
                if (e.key == 48):
                    new_game[i-1][j-1] = e.key-48
                    pygame.draw.rect(window, background_color, (j*50+5, i*50+5, 50-10, 50-10))
                    pygame.display.update()
                    return
            
                if (0< e.key-48 < 10): 
                    pygame.draw.rect(window, background_color, (j*50+5, i*50+5, 50-10, 50-10))
                    val = new_game.board_font.render(str(e.key-48), True, black)
                    window.blit(val, (j*50 + 15, i*50 +5))
                    new_game[i-1][j-1] = e.key-48
                    pygame.display.update()
                    return
def game():
    pygame.init()
    window = pygame.display.set_mode((550, 600))
    pygame.display.set_caption("Sudoku Project")
    window.fill(background_color)
    board_font = pygame.font.SysFont('Arial', 30)
    
    for i in range(0,10):
        if (i % 3 == 0):
             if(i%3 == 0):
                pygame.draw.line(window, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500),4)
                pygame.draw.line(window, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i),4)
 
        pygame.draw.line(window, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        pygame.draw.line(window, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
        pygame.display.update()
            
    for r_square in range(0,len(new_game[0])):
        for c_square in range(0,len(new_game[0])):
            if(new_game[r_square][c_square] > 0 and new_game[r_square][c_square] <10):
                
                val = board_font.render(str(new_game[r_square][c_square]), True, (100,100,200) )
                window.blit(val, ((c_square +1)*50 +15, (r_square +1)*50 + 5))
    
    pygame.display.update()
    
    while True:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP and e.button ==1:
                coordinates = pygame.mouse.get_pos()
                place(window, (coordinates[0]//50, coordinates[1]//50))
                
            if (e.type == pygame.QUIT):
                pygame.quit()
                return
game()                
                
game1 = game()           