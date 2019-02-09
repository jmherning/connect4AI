
import numpy as np
import random


class Agent:
    '''Base class for intelligent agents'''

    def __init__(self, team, environment):
        self.percepts = [] # available move choices
        self.team = team
        self.environment = Environment()
        self.nextMove = (0, 0, 0) # (row, col, piece)
        self.availableMoves = []
        self.lastMove = (0, 0, 0) # (row, col, piece)

    # process environment percepts
    def sense(self, percepts, environment):
        self.percepts.append(percepts)
        self.availableMoves = environment.getPossibleMoves()
        self.lastMove = environment.lastMove
        if self.lastMove[2] != 0:
            self.environment.setPiece(self.lastMove[0], self.lastMove[1], self.lastMove[2])

    # think about what action to take
    def think(self):
        pass

    # return action agent decided on
    def action(self):
        return self.nextMove

# agent makes only random moves
class PureRandomMoveAgent(Agent):

    def __init__(self, team, environment):
        super().__init__(team, environment)

    def think(self):

        numAvailableMoves = len(self.availableMoves)
        i = random.randint(0, numAvailableMoves - 1)
        move = self.availableMoves[i]
        self.nextMove = (move[0], move[1], self.team)
        self.environment.drop_piece(self.nextMove[0], self.team)


# Environment for Agent to interact
# In this case a connect4 game board
class Environment:

    def __init__(self):
        self.width = 7
        self.height = 6
        self.board = np.zeros((self.height, self.width))
        self.lastMove = (0, 0, 0) # (row, col, piece)



    # resets board with all zeroes
    def reset(self):
        self.board.fill(0)

    # string representation of environment
    def printBoard(self):
        print("  0  1  2  3  4  5  6")
        print(np.flip(self.board, 0))

    # return piece if inside board
    # returns 0 if outside board
    # also returns zero if space is blank
    def getPiece(self, col, row):
        if row < 0 or row > self.height- 1:
            return 0
        if col < 0 or col > self.width - 1:
            return 0
        return self.board[row][col]

    # sets piece value of given location
    def setPiece(self, col, row, piece):
        self.board[row][col] = piece

    def isPossibleWin(self, col, row, piece):
        pass

    def numAvailableMoves(self):
        pass

    def countPossibleWins(self, team):
        pass


    def drop_piece(self, col, piece):
        row = self.nextOpenRow(col)
        self.lastMove = (col, row, piece)
        self.board[row][col] = piece



    def getPossibleMoves(self):
        possibleMoves = []
        for col in range(self.width):
            if self.columNotFull(col):
                row = self.nextOpenRow(col)
                possibleMoves.append((col, row))
        return possibleMoves

    # return next open row for given colum
    def nextOpenRow(self, col):
        for row in range(self.height):
            if self.board[row][col] == 0:
                return row

    # checks if colum is not full
    def columNotFull(self, col):
        return self.board[self.height-1][col] == 0

    #checks for a win from a winning piece
    def checkWin(self, piece):
        # Check horizontal
        for c in range(self.width - 3):
            for r in range(self.height):
                if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece and \
                        self.board[r][c + 3] == piece:
                    return True
        # Check vertical
        for c in range(self.width):
            for r in range(self.height - 3):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and \
                        self.board[r + 3][c] == piece:
                    return True
        # Check diagonal positive
        for c in range(self.width - 3):
            for r in range(self.height - 3):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][
                    c + 2] == piece and self.board[r + 3][c + 3] == piece:
                    return True
        # Check diagonal negative
        for c in range(self.width - 3):
            for r in range(3, self.height):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][
                    c + 2] == piece and self.board[r - 3][c + 3] == piece:
                    return True


# Simulation for AI
class Simulation:

    def __init__(self):
        self.environment = Environment()



    def newAgent(self, team, type):
        if type == "Random":
            return PureRandomMoveAgent(team, self.environment)
        return PureRandomMoveAgent(team, self.environment)


    def reset(self):


        agent1 = self.newAgent(1, "Random")
        agent2 = self.newAgent(2, "Random")
        self.agents = [agent1, agent2]

    def run(self):


        winner = 0
        turn = 0

        self.reset()
        while winner == 0:
            self.agents[turn].sense([], self.environment)
            self.agents[turn].think()
            move = self.agents[turn].action()
            self.environment.drop_piece(move[0], move[2])

            # Print environment
            print("------------------------")
            self.environment.printBoard()
            print("player{} drops in col: {}".format(move[2], move[0]))

            if self.environment.checkWin(move[2]):
                winner = move[2]
                print("Player{} Wins".format(move[2]))

            turn = 1 -turn

    def update(self):
        pass

    def draw(self):
        pass

    def gameloop(self):
        pass



test = Simulation()
test.run()


















