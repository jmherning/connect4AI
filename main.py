from board import Board





b = Board()
game_over = False
turn = 0

while not game_over:
    # Ask for player 1 input
    if turn == 0:
        col = int(input("Player1 make your selection:"))  # forced merge conflict
        if b.is_valid_location(col):
            row = b.get_next_open_row(col)
            print("row:{}  col: {}".format(row, col))
            b.drop_piece(row, col, 1)
            b.print_board()

            if b.winning_move(1):
                print("Player 1 Wins!")
                game_over = True

    # Ask for player 2 input
    else:
        col = int(input("Player2 make your selection:"))

        if b.is_valid_location(col):
            row = b.get_next_open_row(col)
            print("row:{}  col: {}".format(row, col))
            b.drop_piece(row, col, 2)
            b.print_board()

            if b.winning_move(2):
                print("Player 2 Wins!")
                game_over = True

    turn += 1
    turn = turn % 2
