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
y = 0
diff = 500/9
val=0

font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

# Functions to highlight a cell. cord(pos) gets the coordinates of a given pos(i,j) and sets it to xy 

# draw_box() highlights the cell user selected

def cord(pos):
    global x 
    x = pos[0]//diff
    global z 
    y = pos[1]//diff
                


def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * diff-3, (y + i)*diff), (x * diff + diff + 3, (y + i)*diff), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* diff, y * diff ), ((x + i) * diff, y * diff + diff), 7)

# creates the drawn box with gridlines.     
def draw():
    for i in range(9):
        for j in range(9):
            if new_game[i][j] != 0:
                #fills already complete numbers with blue.
                pygame.draw.rect(screen, (152,245,255), (i * diff, j * diff, diff + 1, diff + 1))
                
                #Fills in given numbers and centers them.
                text1=font1.render(str(new_game[i][j]),1,black)                
                screen.blit(text1, (i*diff + 15, j * diff + 1))
                
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, black, (0, i *diff), (500, i*diff), thick)
        pygame.draw.line(screen, black, (i*diff, 0), (i*diff, 500), thick)
        
def draw_val(val):
    text1=font1.render(str(val), 1, black)
    screen.blit(text1, (x *diff +15, y*diff + 15))
    
def raise_error1():
    text1 = font1.render("Wrong!!", 1, black)
    screen.blit(text1, (20,570))
    
def raise_error2():
    text1 = font1.render("Wrong, not a valid key", 1, black)
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

def solve(grid, i , j):
    while grid[i][j] != 0:
        if i < 8:
            i+=1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    
    for it in range(1,10):
        if valid(grid,i,j,it) == True:
            grid[i][j] = it
            global x,y
            x = i
            y = j
            screen.fill((255,255,255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid,i,j)==1:
                return True
            else:
                grid[i][j] = 0
            screen.fill((255,255,255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
        return False





def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT, or R to EMPTY", 1, black)
    text2 = font2.render("ENTER VALUES and PRES ENTER to VISUALIZE", 1, black)
    screen.blit(text1, (20,520))
    screen.blit(text2,(20,540))
    
def result():
    text1 = font1.renter("Finished: press R or D", 1, black)
    screen.blit(text1, (20,570))
    
run = True
flag1= 0
flag2=0
rs=0
error = 0
    
while run:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            cord(pos)
        if event.type == pygame.KEYDOWN:
               
            if event.key == pygame.K_LEFT:
                x-=1
                flag1=1
            if event.key == pygame.K_RIGHT:
                x+=1
                flag1=1
            if event.key == pygame.K_UP:
                y-=1
                flag1=1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1=1
            if event.key == pygame.K_1:
                val =1
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
                
            if event.key == pygame.K_r:
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
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                new_game = current_game
        if flag2== 1:
            if solve(new_game,0,0) == False:
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
                new_game[int(x)][int(y)] = 0
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
pygame.quit()
                
                 
          







               
        