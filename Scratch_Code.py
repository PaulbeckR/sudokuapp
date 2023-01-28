'''
Original main.py code

'''



from BuildPuzzle import *
from FindSolutions import *
from PreparePuzzle import *
from PerfectPairs import *
from main import *

# from build puzzle



#previous
#new_game = new_game_board(new_grid)
print_game(new_game)
print("Above is printed new_gam from create new game board")
print("Squares completed at START", completed_count(new_game))



pos_nums_grid = create_arrays(new_game)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Printing Pos_nums_grid: this is the grid that calls create_arrays")

print_pos_grid(pos_nums_grid)


#find solutions

test_test = basic_solve(pos_nums_grid)
print_updated_grid(test_test)

#perfect pairs

current_test = perfect_pairs(test_test)
print(" current test is here"  , current_test)
print_updated_grid(current_test)


game1 = game()

'''
Additional features for user selections in game. Also includes
initial game() function.

'''
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