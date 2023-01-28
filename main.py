import pygame 

from BuildPuzzle import *
from PreparePuzzle import*
pygame.font.init()
pygame.init()

complete_board = create_grid_fill()

#previous: 
#new_grid = create_grid_fill()

#print_grid(new_grid)

#print(new_grid)

# prepare puzzle
new_game = new_game_board(complete_board)
current_game = new_game

background_color = (50,245,243)
screen = pygame.display.set_mode((500,600))
black = (0,0,0)
x = 0
z = 0
diff = 500/9
value=0

font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

def cord(pos):
    global x 
    x = pos[0]//diff
    global z 
    z = pos[1]//diff
                


def highlightbox():
    for k in range(2):
        pygame.draw.line(window, black, (x*diff-3, (z+k)*diff), (x *diff+d diff+3, (z +k)*diff),7)
        pygame.draw.line(window, (0, 0, 0), ( (x + k)* diff, z * diff ), ((x + k) * diff, z * diff + diff), 7)


def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT, or R to EMPTY", 1, black)
    text2 = font2.render("ENTER VALUES and PRES ENTER to VISUALIZE", 1, black)
    screen.blit(text1, (20,520))
    screen.blit(text2,(20,540))
    
def result():
    text1 = font1.renter("Finished: press R or D", 1, black)
    screen.blit(text1, (20,570))
    
def draw():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                pygame.draw.rect(screen,(152,245,255), (i *diff, j*diff + 1, diff +1))
                    text1=font1.render(str(new_game[i][j]))
                    screen.blit(text1, (i*diff + 15, j * diff + 15))
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, black, (0, i *diff), (500, i*diff), thick)
        pygame.draw.line(screen, black, (i*diff, 0), (i*diff, 500), thick)
        
def draw_val(val):
    text1=font1.render(str(val), 1, black)
    screen.blit(text1, (x *dif +15, y*diff + 15))
    
def raise_error1():
    text1 = font1.render("Wrong!!", 1, black)
    screen.blit(text1, (20,570))
    
def raise_error2():
    text1 = font1.renter("Wrong, not a valid key", 1, black)
    screen.blit(text1, (20,570))
    
def valid(m,i,j,val):
    for it in range(9):
        if m[i][it] == val:
            return False
        if m[it][j] == val:
            return False
    it = i//3
    jt = j//3
    
    for i in range(it *3, it *3 +3):
        for j in range(jt *3, jt*3 +3):
            if m[i][j] == val:
                return False
    return True







# def place(window,pos):
    # board_font = pygame.font.SysFont('Arial', 30, bold=False, italic=False)
    # i,j = pos[0], pos[1]
    
while True:
    for e in pygame.event.get():
        
        if (e.type == pygame.QUIT):
            pygame.quit()
            return
        if e.type == pygame.KEYDOWN:
                #if complete_board[i-1][j-1] != 0:
                 #   return
            if e.key == pygame.K_LEFT:
                i-=1
                flag1=1
            if e.key == pygame.K_RIGHT:
                i+=1
                flag1=1
            if e.key == pygame.K_UP:
                j-+1
                flag1=1
            if e.key == pygame.K_DOWN:
                y+= 1
                flag1=1
            if e.key == pygame.K_DOWN:
                y+= 1
                flag1=1
            if e.key == pygame.K_1:
                val =1
            if e.key == pygame.K_2:
                val = 2
            if e.key == pygame.K_3:
                val = 3
            if e.key == pygame.K_4:
                val = 4
            if e.key == pygame.K_5:
                val = 5
            if e.key == pygame.K_6:
                val = 6
            if e.key == pygame.K_7:
                val = 7
            if e.key == pygame.K_8:
                val = 8
            if e.key == pygame.K_9:
                val = 9
            if e.key == pygame.K_ENTER:
                flag2 = 1
                
            if e.key == pygame.K_r:
                rs=0
                error =0
                flag2=0
                new_game = [[0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0]]
            if e.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                new_game = current_game
            if flag2== 1:
                if solve(grid,0,0) == False:
                    error = 1
                else:
                    rs = 1
                    flag2 = 0
            if val!= 0:
                draw_val(val)
                if valid(new_game,int(x), int(y), val) == True:
                    new_game[int(x)][int(y)] = val
                    flag1 = 0
                else:
                    grid[int(x)][int(y)] = 0
                    raise_error2()
                val = 0
            if error == 1:
                raise_error1()
            if rs==1:
                result()
            draw()
            if flag1==1:
                draw_box()
            instruction()
            pygame.display.update()
                
                 
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






def fillvalue(value):
    text1 = font.render(str(value), 1, black)
    window.blit(text1, (x*diff + 15, z*diff +15))
    
def validvalue(m,k,l, value):
    for it in range(9):
        if m[k][it] == value:
            return False
        if m[it][l] == value:
            return False
    it = k//3
    jt = l//3
    for k in range(it*3, it *3+3):
        if m[k][l] == value:
            return False
    return True


               
                
#game1 = game()           