import sys
import copy
import pygame
import threading
import pygame_menu
from pygame_menu import themes

from BuildPuzzle import *
from PreparePuzzle import*
from BackSolver import*
#from SudokuGenerator import *

pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.font.init()

pygame.display.list_modes()

difficulty = 0

game = None
solved_board = None

difficulty = 0
def set_difficulty_level(selected: tuple, value: any):
    global difficulty
   
    diff_level = value
    difficulty = diff_level
    

def show_start_screen():
        mainmenu = pygame_menu.Menu("Sudoku Time!!", screen_height, screen_width,
                                theme= pygame_menu.themes.THEME_BLUE)
        #mainmenu.add.text_input("Name: ", default = 'username', maxchar = 20)
        mainmenu.add.button('Play', play_game)

        mainmenu.add.selector('Difficulty:', [('Easy', 0),('Medium',1), ('Hard', 2), ('Very Hard', 3)], onchange= set_difficulty_level)
        
        mainmenu.add.button('Quit', pygame_menu.events.EXIT)

        mainmenu.mainloop(screen)

def show_game_over_screen():
    background_color2 = (100, 25, 100)
    screen.fill(background_color2)
    font = pygame.font.Font(None, 75)
    text = font.render("Game Over", True, (255,255,255))
    text1= font.render("Want to play again?",True, (225,225,225))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    text1_rect = text1.get_rect(center=(screen_width // 2, screen_height-100 // 2))

    screen.blit(text, text_rect)
    screen.blit(text1, text1_rect)
    pygame.display.update()
    
    mouse = pygame.mouse.get_pos()
    if text_rect.collidepoint(mouse):
        pygame.quit()
    if text1_rect.collidepoint(mouse):
        show_start_screen()
        
   
def loading_screen():
    background_color2 = (100, 25, 150)
    screen.fill(background_color2)
    font = pygame.font.Font(None, 75)
    text = font.render("Loading...", True, (255,255,255))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.update()

def load_new_game_data():
    global difficulty
    level = difficulty
    #sudoku = SudokuBoard()
    #solved_board, game = sudoku.new_sudoku_board(level)
    game, solved_board = new_sudoku_board(level)

    #diff_dictionary = sudoku.get_difficulty_dict()
    #print(diff_dictionary)
    return game, solved_board


def load_game_data_thread():
    global game, solved_board
    game, solved_board = load_new_game_data()
    

    
def play_game():
    global game, solved_board
    global difficulty
    # Load game data in a separate thread
    load_thread = threading.Thread(target=load_game_data_thread)
    load_thread.start()

    # Wait for game data to finish loading
    while load_thread.is_alive():
        loading_screen()

   

    # Run game loop
    start_game_loop(game, solved_board)
    
    
      
def start_game_loop(new_game, solved_board):
    
    mygame = copy.deepcopy(new_game)
    colorsgrid = copy.deepcopy(new_game)
    running = True
    #sudoku = SudokuBoard()
    print("New GAME")
    print_grid(mygame)
    print("                       ")
    print("SOLUTION")
    print_grid(solved_board)

    current_game = mygame


    objects = []

    black = (0,0,0)
    preset_board_color = (125,216,230)
    user_color = (175,112,211)
    preset_font_color = (0,0,0)
    user_font_color = (255,255,255)
    x = 0
    y = 0
    diff = 55
    val=0
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
    #notes_board = [[0 for _ in range(9)] for _ in range(9)]
    

    def board_colors_preset(grid):
        board_colors = []
        for row in grid:
            new_row = []
            for cell in row:
                if cell != 0:
                    new_row.append((cell,True))
                else:
                    new_row.append((cell,False))
            board_colors.append(new_row)
        return board_colors
    
    
    thisboard = board_colors_preset(colorsgrid)                            
    

    def cord(pos):
        global x 
        if pos[0] < 500:
            x = pos[0]//diff
        global y 
        if pos[1] <500:
            y = pos[1]//diff
            
        

    def draw_box():
        for i in range(2):
            pygame.draw.line(screen, (200, 0, 70), (x * diff, (y + i)*diff), (x * diff + diff , (y + i)*diff), 3)
            pygame.draw.line(screen, (200, 0,70), ( (x + i)* diff, y * diff ), ((x + i) * diff, y * diff + diff), 3)

# creates the drawn box with gridlines.     
    def draw():

        for j in range(9):
            for i in range(9):
                
                color = preset_board_color if thisboard[i][j][1] else user_color
                font_color = preset_font_color if thisboard[i][j][1] else user_font_color
                
                if mygame[i][j] != 0:
                    #fills already complete numbers with blue.
                    pygame.draw.rect(screen, color, (j * diff, i * diff, diff + 1, diff + 1))
                    
                    #Fills in given numbers and centers them.
                    text1=font1.render(str(mygame[i][j]),1,font_color)                
                    screen.blit(text1, (j*diff + 15, i * diff + 1))


        for k in range(9):
            for l in range(9):
                draw_inside_square(notes, (k,l), 0, False)
        if flag4 ==1:
            for i in range(9):
                for j in range(9):                
                    draw_inside_square(notes, (i,j), 0, False)
        
        if flag5 ==1:
            for i in range(9):
                for j in range(9):
                    draw_inside_square(notes, (i,j), 0, False)
        
        for i in range(10): 
            if i % 3 == 0:
                thick = 7
            else:
                thick = 1
            pygame.draw.line(screen, black, (0, i *diff), (game_height - 3, i*diff), thick)
            pygame.draw.line(screen, black, (i*diff, 0), (i*diff, game_width - 3), thick)
    


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
                            
                if (note_val != 0) and (mygame[col_pos][row_pos] == 0):
                        
                    x_offset = sq_col * diff // 3 
                    y_offset = sq_row * diff // 3 
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
                'normal': '#87CEFA',
                'hover': '#483D8B',
                'pressed' :'#FFFFE0'
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


        
    def handle_mouse_click(pos):
        for row in range(9):
            for col in range(9):
                rect = pygame.Rect(col * diff, row *diff, diff , diff )
                if rect.collidepoint(pos):
                    draw_box()
                    
                    return row, col
                 
    def update_notes2():
        
        arr_board = create_arrays(mygame)
        
       
        for i in range(9):
            for j in range(9):
                if type(arr_board[i][j]) is not list: arr_board[i][j] = [arr_board[i][j]]
                
                if len(arr_board[i][j]) > 1:  
                    for ele in arr_board[i][j]:
                        notes[int(j)][int(i)][int(ele)] = ele
                        
                        notes2.add(ele)
                        draw_inside_square(notes, (j,i), ele, False)
    
                elif len(arr_board[i][j]) == 1:
                    for num in arr_board[i][j]:
                        if mygame[i][j] != num:
                            notes[int(j)][int(i)][int(num)] = num
                            notes2.add(num)
                            draw_inside_square(notes, (j,i), num, False)
        
        
                    
                   
                        
      
      

        
    def draw_val(val, notes_mode = False):
    
        if notes_mode: 

        
            for i in range(3):
                for j in range(3):
                    note_val = notes[int(i)][int(j)][i*3+j+1]
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

    def solve(grid, original, i , j):
        # other solve will need to check if equal to orig board.
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
        text1 = font2.render("Use Mouse or Arrow Keys to navigate", 1, black)
        text2 = font2.render("PRESS ENTER to COMPLETE and check solution", 1, black)
        text4 = font2.render("PRESS N to enter NOTES", 1, black)
        text3 = font2.render("Enter Notes: ", 1, black)
        screen.blit(text1, (20,520))
        screen.blit(text2,(20,540))
        screen.blit(text4, (20, 580))
        screen.blit(text3,(20,600))
        
    def result():
        
        show_game_over_screen()
        
        
  
    customButton = Button(600, 200, 125, 45, 'Update Notes', update_notes2, onePress = False)

    flag1= 0
    flag2=0
    flag3 = 0
    flag4 = 0
    flag5 = 0
    rs=0
    
    error = 0
    
    
    pygame.display.set_caption("Sudoku!!!")
    while running:
        screen.fill((255,255,255))
        draw_box()
        
   
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                cord(pos)
                # #flag1 = 1
                print(pos)
                if customButton.buttonRect.collidepoint(event.pos):
                    flag4 = 1
                    
                
                if pos[0] < 500 and pos[1] < 500:
                    y, x = handle_mouse_click(event.pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    if notes_mode == False:
                        notes_mode = True
                        notes2.clear()
                        flag3 = 1
                    else:
                        notes_mode = False
                        notes2.clear()
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
            
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    val =1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    val = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    val = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    val = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    val = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    val = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    val = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    val = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    val = 9
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_EQUALS:
                    flag2 = 1
                
                
                if event.key == pygame.K_r:
                    rs=0
                    error =0
                    flag2=0
                    mygame = [[0,0,0,0,0,0,0,0,0],
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
                    mygame = current_game
                    notes = reset_notes
                    
            if flag1==1:
                if (-1 < x < 9) and ( -1 < y < 9):
                    draw_box()
            if flag3 ==1:
           
             
                text3 = font2.render("ON",1, (127,255,0))
                screen.blit(text3, (145,600))
            else:
                text4 = font2.render(" OFF ",1, (255,0,0))
                screen.blit(text4, (140,600))
        
            if flag2== 1:

                    
                if test_if_equal(mygame, solved_board) == False:
                    error = 1
                else:

                    rs = 1
                    flag2 = 0

        
        
            if notes_mode == False:
                if val != 0:
                    draw_val(val, notes_mode = False)
                    if valid(mygame, int(y), int(x), val, False) == True:
                        mygame[int(y)][int(x)] = val
                        
                        #notes_board[int(x)][int(y)] = [0]
                        flag1 = 0
                    else:
                        mygame[int(y)][int(x)] = 0
                    
                        raise_error2()
                    val = 0
            if notes_mode == True:

                if val not in notes[int(x)][int(y)]:
                  
    
                    notes[int(x)][int(y)][int(val)] = val
                    

                    #draw_val(val, notes_mode = True)
          
                else:
                    notes[int(x)][int(y)][int(val)] = 0
                 
                    #draw_val(val, notes_mode = True)

                val = 0    
            for object in objects:
                object.process()
   

                    
            if error == 1:
                raise_error1()
            if rs==1:
                running = False
                result()
            draw()

        
            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()
            instruction()
            pygame.display.update()

show_start_screen()


                
                 
          







               
        