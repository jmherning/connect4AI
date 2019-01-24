
import numpy as np

ROW_COUNT = 6
COL_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board

def drop_piece(baord, row, col, piece):
    baord[row][col] = piece

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Check horizontal
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # Check vertical
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # Check diagonal positive
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # Check diagonal negative
    for c in range(COL_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True





board = create_board()
print_board(board)

game_over = False
turn = 0



while not game_over:
    #Ask for player 1 input
    if turn == 0:
        col = int(input("Player1 make your selection:"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            print("row:{}  col: {}".format(row, col))
            drop_piece(board, row, col, 1)
            print_board(board)

            if winning_move(board, 1):
                print("Player 1 Wins!")
                game_over = True

    #Ask for player 2 input
    else:
        col = int(input("Player2 make your selection:"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            print("row:{}  col: {}".format(row, col))
            drop_piece(board, row, col, 2)
            print_board(board)

            if winning_move(board, 2):
                print("Player 2 Wins!")
                game_over = True



    turn += 1
    turn = turn % 2

