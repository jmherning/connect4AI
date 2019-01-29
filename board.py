# board for connect4
# stores data, drawn elsewhere

import numpy as np


class Board:

    def __init__(self):
        self.row_size = 6
        self.col_size = 7
        self.board = self.create_board()

    def create_board(self):
        board = np.zeros((self.row_size, self.col_size))
        return board

    # Drops piece in colum into first valid row
    # ->Add valid row detection
    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[5][col] == 0

    def get_next_open_row(self, col):
        for r in range(self.row_size):
            if self.board[r][col] == 0:
                return r

    def print_board(self):
        print(np.flip(self.board, 0))




    # Detects a winning move
    # If 4 in a row return true
    # ->Find a better way to do this later
    def winning_move(self, piece):
        # Check horizontal
        for c in range(self.col_size - 3):
            for r in range(self.row_size):
                if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece and self.board[r][c + 3] == piece:
                    return True
        # Check vertical
        for c in range(self.col_size):
            for r in range(self.row_size - 3):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and self.board[r + 3][c] == piece:
                    return True
        # Check diagonal positive
        for c in range(self.col_size - 3):
            for r in range(self.row_size - 3):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][c + 2] == piece and self.board[r + 3][c + 3] == piece:
                    return True
        # Check diagonal negative
        for c in range(self.col_size - 3):
            for r in range(3, self.row_size):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][c + 2] == piece and self.board[r - 3][c + 3] == piece:
                    return True

