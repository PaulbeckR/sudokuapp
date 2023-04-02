import sys

import pygame
import threading
import pygame_menu
from pygame_menu import themes

from BuildPuzzle import *
from PreparePuzzle import*
from BackSolver import*

pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((800,800))
pygame.font.init()

pygame.display.list_modes()

difficulty = 0

new_game = None
solved_bored = None

difficulty = 0
def set_difficulty_level(selected: tuple, value: any):
    global difficulty
   
    diff_level = value
    difficulty = diff_level
    

def show_start_screen():
        mainmenu = pygame_menu.Menu("Sudoku Time!!", 800,800,
                                theme= pygame_menu.themes.THEME_SOLARIZED)
        mainmenu.add.text_input("Name: ", default = 'username', maxchar = 20)
        mainmenu.add.button('Play', play_game)

        mainmenu.add.selector('Difficulty:', [('Easy', 0),('Medium',1), ('Hard', 2)], onchange= set_difficulty_level)
        
        mainmenu.add.button('Quit', pygame_menu.events.EXIT)

        mainmenu.mainloop(screen)
        
        
def loading_screen():
    font = pygame.font.Font(None, 36)
    text = font.render("Loading...", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

def load_new_game_data():
    global difficulty
    level = difficulty
    new_game, solved_bored = new_sudoku_board(level)
    return new_game, solved_bored


def load_game_data_thread():
    global new_game, solved_bored
    new_game, solved_bored = load_new_game_data()
    

    
def play_game():
    global new_game, solved_bored
    global difficulty
    # Load game data in a separate thread
    load_thread = threading.Thread(target=load_game_data_thread)
    load_thread.start()

    # Wait for game data to finish loading
    while load_thread.is_alive():
        loading_screen()

   

    # Run game loop
    start_game_loop(new_game, solved_bored)
    
    
      
def start_game_loop(new_game, solved_bored):
    running = True
   
    print("New GAME")
    print_grid(new_game)
    print("                       ")
    print("SOLUTION")
    print_grid(solved_bored)

    current_game = new_game

    background_color = (50,245,243)
    objects = []

    black = (0,0,0)
    x = 0
    y = 0
    diff = 55
    val=0
    cell_size = diff/9
    game_height = 500
    game_width = 500

    font1 = pygame.font.SysFont("comicsans", 40)
    font2 = pygame.font.SysFont("comicsans", 20)
    font3 = pygame.font.SysFont("comicsans", 10)
    font4 = pygame.font.SysFont("comicsans", 15)
    notes = [[[0] * 10 for _ in range(9)] for _ in range(9)]
    reset_notes = notes
         
    notes2 = set()

    notes_mode = False
    notes_board = [[0 for _ in range(9)] for _ in range(9)]
    arr_board = [[0 for _ in range(9)] for _ in range(9)]

    def cord(pos):
        global x 
        if pos[0] < 500:
            x = pos[0]//diff
        global y 
        if pos[1] <500:
            y = pos[1]//diff
            
        

    def draw_box():
        for i in range(2):
            pygame.draw.line(screen, (200, 0, 70), (x * diff, (y + i)*diff), (x * diff + diff , (y + i)*diff), 5)
            pygame.draw.line(screen, (200, 0,70), ( (x + i)* diff, y * diff ), ((x + i) * diff, y * diff + diff), 5)

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
                    
        square = []
        for k in range(9):
            for l in range(9):
                draw_inside_square(notes, (k,l), 0, False)
        if flag4 ==1:
            for i in range(9):
                for j in range(9):                
                        # #if any(num for num in notes[int(k)][int(l)] != 0) :
                    draw_inside_square(notes, (i,j), 0, False)
        
        if flag5 ==1:
            for i in range(9):
                for j in range(9):
                    # #if any(num for num in notes[int(k)][int(l)] != 0) :
                    draw_inside_square(notes, (i,j), 0, False)
        
        for i in range(10): 
            if i % 3 == 0:
                thick = 7
            else:
                thick = 1
            pygame.draw.line(screen, black, (0, i *diff), (500, i*diff), thick)
            pygame.draw.line(screen, black, (i*diff, 0), (i*diff, 500), thick)
    


    def draw_inside_square(numbers, position, single, grid = False):
        row_pos = position[0]
        col_pos = position[1]
        note_val = 0

        for sq_col in range(3):
            for sq_row in range(3):
                    
                if single != 0:
                    note_val = single
                else:
                    note_val = numbers[row_pos][col_pos][sq_row*3+ sq_col+1]
                            
                if (note_val != 0) and (new_game[col_pos][row_pos] == 0):
                        
                    x_offset = sq_col * diff // 3 
                    #print("x_offset is ", x_offset)
                    y_offset = sq_row * diff // 3 
                    #print("y_offset is ", y_offset)
                    text = font3.render(str(note_val),1, black)
                    if not grid:
                        screen.blit(text, (row_pos*diff+x_offset+5, col_pos*diff+y_offset+4))
                    else:
                        screen.blit(text, (col_pos*diff+x_offset+5, row_pos*diff+y_offset+4))
                

    class Button(): 
        
        def __init__(self, x, y, width, height, buttonText = 'Button', onclickFunction = None, onePress = False):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.onclickFunction = onclickFunction
            self.onePress = onePress
            self.alreadyPressed = False

            self.fillColors = {
                'normal': '#ffffff',
                'hover': '#666666',
                'pressed' :'#333333'
            }
            
            
            self.buttonSurface = pygame.Surface((self.width, self.height))
            self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
            self.buttonSurf = font4.render(buttonText, True, (20,20,20))
            
            objects.append(self)
            
            
        def process(self):
            mousePos = pygame.mouse.get_pos()
            self.buttonSurface.fill(self.fillColors['normal'])
            if self.buttonRect.collidepoint(mousePos):
                self.buttonSurface.fill(self.fillColors['hover'])
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    self.buttonSurface.fill(self.fillColors['pressed'])
                    if self.onePress:
                        self.onclickFunction()
                    elif not self.alreadyPressed:
                        self.onclickFunction()
                        self.alreadyPressed = True
                else:
                    self.alreadyPressed = False
                    
            self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
            ])
            screen.blit(self.buttonSurface, self.buttonRect)


        
    class Square():
        def __init__(self):
            global x
            global y
            self.rect = pygame.draw.rect(screen, (152,245,255), (y * diff, x * diff, diff + 1, diff + 1))
    square = Square()

    def update_notes2():
  
        arr_board = create_arrays(new_game)
        
        for i in range(9):
            for j in range(9):
                if type(arr_board[i][j]) is not list: arr_board[i][j] = [arr_board[i][j]]
                
                if len(arr_board[i][j]) > 1:
                #if new_game[i][j] == 0:
                    # print("entering arr ", arr_board[i][j], "in", (i,j))
                    for ele in arr_board[i][j]:
                        notes[int(j)][int(i)][int(ele)] = ele
                        notes2.add(ele)
                        draw_inside_square(notes, (j,i), ele, False)
      
        print("Notes row 0 is ")
        print(notes[int(0)])

        
    def draw_val(val, notes_mode = False):
    
        if notes_mode: 

        
            for i in range(3):
                for j in range(3):
                # print((i,j), "is position in draw_val")
                    note_val = notes[int(i)][int(j)][i*3+j+1]
                    #print("note val", note_val)
                    if note_val != 0:
                        
                        x_offset = i * diff // 3 
                        y_offset = j * diff // 3 
                        #print("num just added to", (i*diff+x_offset+5, j*diff+y_offset+4))
                        text = font3.render(str(note_val),1, black)
                        screen.blit(text, (i*diff+x_offset+5, j*diff+y_offset+4))                    
        else:  
            val = int(val)
            #print("solution just added to", (x *diff +15, y*diff + 15) )
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

    def solve(grid, original, i , j):
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
        text2 = font2.render("ENTER VALUES and PRES ENTER to COMPLETE", 1, black)
        
        screen.blit(text1, (20,520))
        screen.blit(text2,(20,540))
        
    def result():
        text1 = font1.render("Finished!! GOOD JOB: press R or D", 1, black)
        screen.blit(text1, (20,640))
        
    
    customButton = Button(600, 200, 125, 45, 'Update Notes', update_notes2)

    flag1= 0
    flag2=0
    flag3 = 0
    flag4 = 0
    flag5 = 0
    rs=0
  
    error = 0

    pygame.display.set_caption("Sudoku!!!")
    while True:
        screen.fill((255,255,255))
   
        for event in pygame.event.get():
            
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                cord(pos)
                #flag1 = 1
                if customButton.buttonRect.collidepoint(event.pos):
                    flag4 = 1
                
                elif square.rect.collidepoint(event.pos):
                    flag1=1
                #cell_x, cell_y = event.pos[0] // diff, event.pos[1] // diff
                
                
             
                
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                #notes_mode = not notes_mode
                #notes_board = create_notes(new_game)
                    notes_mode = True
                    flag3 = 1
                if event.key == pygame.K_s:
                    notes_mode = False
                    flag3 = 0
            
                if event.key == pygame.K_LEFT:
                    if x == 0:
                        x = 8
                    else:
                        x-=1
                    
                    notes2.clear()
                    flag1=1
                if event.key == pygame.K_RIGHT:
                    if x == 8:
                        x =0
                    else:
                                           
                        x+=1
                    notes2.clear()
                    flag1=1
                if event.key == pygame.K_UP:
                    if y == 0:
                        y =8
                    else:
                        y-=1
                    notes2.clear()
                    flag1=1
                if event.key == pygame.K_DOWN:
                    if y ==8:
                        y = 0
                    else:
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
                    notes = reset_notes
            if flag3 ==1:
            #draw_val(val, notes_mode = True)
             
                text3 = font2.render("Note mode is ON",1, black)
                screen.blit(text3, (20,560))
            else:
                text4 = font2.render("Note mode if OFF ",1,black)
                screen.blit(text4, (20,580))
        
            if flag2== 1:
                if solve(new_game,solved_bored,0,0) == False:
                    error = 1
                else:
                    rs = 1
                    flag2 = 0

        
        
            if notes_mode == False:
                if val != 0:
                    draw_val(val, notes_mode = False)
                    if valid(new_game, int(y), int(x), val, False) == True:
                        new_game[int(y)][int(x)] = val
                        print_grid(new_game)
                    
                    
                        notes_board[int(x)][int(y)] = [0]
                        flag1 = 0
                    else:
                        new_game[int(y)][int(x)] = 0
                    #notes_board[int(x)][int(y)] = notes_board[int(x)][int(y)]
                        raise_error2()
                    val = 0
            if notes_mode == True:
  
                # print("trying", (x,y))
                # print("Notes in while ", notes[x][y], "trying", (x,y))
            
                if val not in notes[int(x)][int(y)]:
                   # print("bef for position" ,(x,y), notes[int(x)][int(y)])
                    # print("val is", val)
                    notes2.add(val)
                
                
                
                    notes[int(x)][int(y)][int(val)] = val
                    notes_board[int(x)][int(y)] = notes2

                    draw_val(val, notes_mode = True)
                
                
                   
                else:
                    notes[int(x)][int(y)][int(val)] = 0
                    if val in notes2:
                        notes2.remove(val)
                    draw_val(val, notes_mode = True)
                
                    notes_board[int(x)][int(y)] = notes2
            notes2.clear()
    
            for object in objects:
                object.process()
   

                    
            if error == 1:
                raise_error1()
            if rs==1:
                result()
            draw()
            if flag1==1:
                if (-1 < x < 9) and ( -1 < y < 9):
                    draw_box()
        
            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()
            instruction()
            pygame.display.update()

show_start_screen()
    

                
                 
          







               
        