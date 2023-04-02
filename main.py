
import sys

import pygame

# import os
#import psycopg2

#DATABASE_URL = os.environ['DATABASE_URL']
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')
# os.environ['SDL_VIDEODRIVER']= "dummy"#
# port = int(os.environ.get("PORT", 5000))


from BuildPuzzle import *
from PreparePuzzle import*
from BackSolver import*
# from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.font.init()

pygame.display.list_modes()



new_game, solved_bored = new_sudoku_board()
print_grid(new_game)

print(".........OG board............")
print_grid(solved_bored)

current_game = new_game


background_color = (50,245,243)

black = (0,0,0)
x = 0
y = 0
diff = 55
val=0
cell_size = diff/9

font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)
font3 = pygame.font.SysFont("comicsans", 10)
notes = [[[0] * 10 for _ in range(9)] for _ in range(9)]

#nums = [1,2,3,4,5,6,7,8,9]
# def create_notes():
#     nums = [1,2,3,4,5,6,7,8,9]
#     grid = [[0 for _ in range(9)] for _ in range(9)]
#     notes_list = []
#     for i in range(9):
#         for j in range(9):
#             if new_game[i][j] == 0: 
#                 grid[i][j] = nums
#             elif new_game[i][j] != 0:
#                 grid[i][j] = [new_game[i][j]] 
                
#     return grid

# candidates_edit = create_notes()
            
notes2 = set()
    

notes_dict = {}
notes_mode = False
notes_board = [(0 for _ in range(9)] for _ in range(9)]
#print(notes_board)

# Functions to highlight a cell. cord(pos) gets the coordinates of a given pos(i,j) and sets it to xy 

# draw_box() highlights the cell user selected

def cord(pos):
    global x 
    x = pos[0]//diff
    global y 
    y = pos[1]//diff
                


def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * diff-3, (y + i)*diff), (x * diff + diff + 3, (y + i)*diff), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* diff, y * diff ), ((x + i) * diff, y * diff + diff), 7)

# creates the drawn box with gridlines.     
def draw():
    for j in range(9):
        for i in range(9):
            if new_game[i][j] != 0:
                #fills already complete numbers with blue.
                pygame.draw.rect(screen, (152,245,255), (j * diff, i * diff, diff + 1, diff + 1))
                
                #Fills in given numbers and centers them.
                text1=font1.render(str(new_game[i][j]),1,black)                
                screen.blit(text1, (j*diff + 15, i * diff + 1))
                
            # elif len(new_game[i][j]) > 1: 
            #     for i in range(3):
            #         for j in range(3):
                        
            #else:
            #if notes_mode:    #new_game[i][j] = notes[x][y]
    for k in range(9):
        for l in range(9):
            #
    #        # if len(current_game[k][l]) > 1:
            if new_game[l][k] == 0:
                #if ( x == k) and( y == l):
                    
                for m in range(3):
                    for n in range(3):
                #print(i,j)
                        note_val = notes[int(k)][int(l)][m*3+n+1]
                            #for note_val in new_game[i][j]:
                        #print("note val", note_val)
                        if note_val != 0:
                    
                            x_offset = n * diff // 3 
                            y_offset = m * diff // 3 
                            text = font3.render(str(note_val),1, black)
                            screen.blit(text, (k*diff+x_offset+5, l*diff+y_offset+4))


                        
                
                
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, black, (0, i *diff), (500, i*diff), thick)
        pygame.draw.line(screen, black, (i*diff, 0), (i*diff, 500), thick)
        
def erase_note():
    notes[x][y][val] = None
    
    

        
def draw_val(val, notes_mode = False):
   
    if notes_mode: 
        
        
        # note_val = []
        # if val in notes[int(y)][int(x)][int(val)]:
        #     for n in notes[int(y)][int(x)][int(val)]
        #notes[int(x)][int(y)][int(val)] = not notes[int(x)][int(y)][int(val)]
       # print("notes at draw val", notes[int(x)][int(y)][int(val)])
        
       
        for i in range(3):
            for j in range(3):
                #print(i,j)
                note_val = notes[int(i)][int(j)][i*3+j+1]
                #print("note val", note_val)
                if note_val != 0:
                    
                    x_offset = i * diff // 3 
                    y_offset = j * diff // 3 
                    text = font3.render(str(note_val),1, black)
                    screen.blit(text, (i*diff+x_offset+5, j*diff+y_offset+4))
        
                    
        
                    
    else:
        
        val = int(val)
        text1=font1.render(str(val), 1, black)
        screen.blit(text1, (x *diff +15, y*diff + 15))
        
    
def raise_error1():
    text1 = font1.render("Wrong!!", 1, black)
    screen.blit(text1, (20,570))
    
def raise_error2():
    text1 = font1.render("Wrong, not a valid key", 1, black)
    screen.blit(text1, (20,570))
    
def valid(grid,row,col,val, notes_mode = False):
    

    for i in range(9):
        if grid[row][i] == val:
            if notes_mode:
                print(f"Note: {val} already exists in row {row}")
            return False
        if grid[i][col] == val:
            if notes_mode:
                print(f"Note: {val} already exists in column {col}")
            return False
    box_row = (row//3) *3 
    box_col = (col//3) *3 
    
    for i in range(3):
        for j in range(3):
            if grid[box_row+i][box_col+j] == val:
                if notes_mode: 
                    print(f"Note: {val} already exists in the box {box_row//3, box_col//3}")
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
    text1 = font1.render("Finished: press R or D", 1, black)
    screen.blit(text1, (20,570))
    


    

   
flag1= 0
flag2=0
flag3 = 0
rs=0
  
error = 0
    
pygame.display.set_caption("Sudoku!!!")
while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                #notes_mode = not notes_mode
                #notes_board = create_notes(new_game)
                notes_mode = True
                flag3 = 1
            elif event.key == pygame.K_s:
                notes_mode = False
                flag3 = 0
            
            # else:
            #     event.unicode.isnumeric() and int(event.unicode) in range(1,10)
            #     val = int(event.unicode)
            #     draw_val(val, notes_mode)
            #     pygame.display.update()

            
               
            if event.key == pygame.K_LEFT:
                x-=1
                notes2.clear()
                flag1=1
            if event.key == pygame.K_RIGHT:
                x+=1
                notes2.clear()
                flag1=1
            if event.key == pygame.K_UP:
                y-=1
                notes2.clear()
                flag1=1
            if event.key == pygame.K_DOWN:
                y+= 1
                notes2.clear()
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
        if flag3 ==1:
            #draw_val(val, notes_mode = True)
             
            text3 = font2.render("Note mode is ON",1, black)
            screen.blit(text3, (20,560))
        else:
            text4 = font2.render("Note mode if OFF ",1,black)
            screen.blit(text4, (20,580))
        
        if flag2== 1:
            if solve(new_game,0,0) == False:
                error = 1
            else:
                rs = 1
                flag2 = 0
        
        
        if notes_mode == False:
            if val != 0:
                draw_val(val, notes_mode = False)
                if valid(new_game, int(y), int(x), val, False) == True:
                    new_game[int(y)][int(x)] = val
                    notes_board[int(x)][int(y)] = [0]
                    flag1 = 0
                else:
                    new_game[int(y)][int(x)] = 0
                    notes_board[int(x)][int(y)] = notes_board[int(x)][int(y)]
                    raise_error2()
                val = 0
        if notes_mode == True:
            
            if val not in notes[int(x)][int(y)]:
                print("bef for position" , notes[int(x)][int(y)])
                print("val is", val)
                notes2.add(val)
                
                
                notes[int(x)][int(y)][int(val)] = val
                notes_board[int(x)][int(y)] = notes2
                
                print("notes for position" , notes[int(x)][int(y)])
                print("notes board", notes_board[x][y])
                draw_val(val, notes_mode = True)
                
                
                   
            else:
                notes[int(x)][int(y)][int(val)] = 0
                if val in notes2:
                    notes2.discard(val)
                draw_val(val, notes_mode = True)
                
                notes_board[int(x)][int(y)] = notes2
                
            
            
            
                    
                    
          
            
            
            
            


                    
        if error == 1:
            raise_error1()
        if rs==1:
            result()
        draw()
        if flag1==1:
            draw_box()
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        instruction()
        pygame.display.update()
# pygame.quit()
    

                
                 
          







               
        