from main import*


def check_correct(new_game, complete_board):
    for i in range(9):
        for j in range(9):
            if new_game[i][j] == complete_board[i][j]:
                return True
            
            return "Game is not correct"    