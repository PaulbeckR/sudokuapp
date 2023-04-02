# import pygame

# initialize pygame

# pygame.init()

# # set window size and title
# WINDOW_SIZE = (540, 600)
# WINDOW_TITLE = 'Sudoku Board'
# screen = pygame.display.set_mode(WINDOW_SIZE)
# pygame.display.set_caption(WINDOW_TITLE)

# # define colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GRAY = (200, 200, 200)

# # set font
# FONT_SIZE = 50
# font = pygame.font.Font(None, FONT_SIZE)

# # define grid size and spacing
# GRID_SIZE = 60
# GRID_SPACING = 5

# # create empty Sudoku board
# board = []
# for i in range(9):
#     row = []
#     for j in range(9):
#         row.append(0)
#     board.append(row)

# # set initial cursor position
# cursor_pos = (0, 0)

# # set initial mode to 'solution'
# mode = 'solution'

# # define function to draw Sudoku board
# def draw_board():
#     # draw background
#     screen.fill(WHITE)
    
#     # draw grid lines
#     for i in range(10):
#         if i % 3 == 0:
#             thickness = 4
#         else:
#             thickness = 1
#         pygame.draw.line(screen, BLACK, (GRID_SPACING, i * GRID_SIZE + GRID_SPACING), 
#                          (9 * GRID_SIZE + GRID_SPACING, i * GRID_SIZE + GRID_SPACING), thickness)
#         pygame.draw.line(screen, BLACK, (i * GRID_SIZE + GRID_SPACING, GRID_SPACING), 
#                          (i * GRID_SIZE + GRID_SPACING, 9 * GRID_SIZE + GRID_SPACING), thickness)
    
#     # draw numbers
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] != 0:
#                 number = font.render(str(board[i][j]), True, BLACK)
#                 screen.blit(number, (j * GRID_SIZE + GRID_SPACING + FONT_SIZE / 3, 
#                                      i * GRID_SIZE + GRID_SPACING))
                
#     # draw cursor
#     pygame.draw.rect(screen, BLACK, (cursor_pos[1] * GRID_SIZE + GRID_SPACING, 
#                                      cursor_pos[0] * GRID_SIZE + GRID_SPACING, 
#                                      GRID_SIZE, GRID_SIZE), 3)
    
#     # draw mode indicator
#     if mode == 'solution':
#         mode_text = font.render('SOLUTION MODE', True, BLACK)
#     else:
#         mode_text = font.render('CANDIDATE MODE', True, BLACK)
#     screen.blit(mode_text, (GRID_SPACING, 550))

# # draw initial board
# draw_board()

# # main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 cursor_pos = (max(cursor_pos[0] - 1, 0), cursor_pos[1])
#             elif event.key == pygame.K_DOWN:
#                 cursor_pos = (min(cursor_pos[0] + 1, 8), cursor_pos[1])
#             elif event.key == pygame.K_LEFT:
#                 cursor_pos = (cursor_pos[0], max(cursor_pos[1] - 1, 0))
#             elif event
