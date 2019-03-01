# Connect4
# By Jason Herning
# hw1 for CS405 Artificial Intelligence Fundamentals
# updated 02-25-2019

# used Dr. Metzgar's example as a general template

import numpy as np
import random
import  math

# Agent Base Class
class Agent:

    def __init__(self, team):
        self._team = team
        self._enemy = self.getEnemy()
        self._env = Board() # The current game board
        self._availableMoves = [] # All possible moves
        self._nextMove = 0
        self._lastMove = 0


    # Update  environment/board
    # pass game board as environment
    # updates available moves
    def sense(self, board):
        self._env = board
        self._availableMoves = self._env.getAvailabeMoves()

    # think about what action to take
    def think(self):
        pass

    # return action agent decided on
    def action(self):
        return self._nextMove

    # sets enemy piece
    def getEnemy(self):
        if self._team == 1:
            return 2
        return 1

    def getTeam(self):
        return self._team

    def getMoves(self):
        return self._availableMoves

# agent makes only random moves
class randomAgent(Agent):

    def __init__(self, team):
        super().__init__(team)

    def think(self):
        i = random.randint(0, len(self._availableMoves) - 1)
        move = self._availableMoves[i]
        self._nextMove = move[0]


class HumanAgent(Agent):

    def __init__(self, team):
        super().__init__(team)

    def think(self):
        print(self._env)
        self._nextMove = int(input("Make your move human: "))




# used this as help https://github.com/KeithGalli/Connect4-Python/blob/master/connect4_with_ai.py
# Agent that runs Min/Max Agent
class minMaxAgent(Agent):

    def __init__(self, team):
        super().__init__(team)

    def minMax(self, board, depth, maxPlayer):
        moves = board.getAvailabeMoves()
        terminal = self.terminalNode(board)
        if depth == 0 or terminal:
            if terminal: # if reached terminal node.
                if self.checkWinSelf(board): # Check if self Won
                    return (None, 1000000)
                elif self.checkWinEnemy(): # Check if enemy Won
                    return (None, -1000000)
                else: # No more valid moves.
                    return (None, 0)
            else: #Depth is zero.
                return None, self.scorePosition(board, self.getTeam())
        if maxPlayer:
            value = -math.inf
            column = random.choice(board.getAvailabeMoves())
            for col in board.getAvailabeMoves():
                boardCopy = board.copy()
                boardCopy.dropPiece(col, self.getTeam())
                newScore = self.minMax(boardCopy, depth-1, False)[1]
                if newScore > value:
                    value = newScore
                    column = col
            return column, value
        else: # Minimizing player
            value = math.inf
            column = random.choice(board.getAvailabeMoves())
            for col in board.getAvailabeMoves():
                boardCopy = board.copy()
                boardCopy.dropPiece(col, self.getTeam())
                newScore = self.minMax(boardCopy, depth - 1, True)[1]
                if newScore > value:
                    value = newScore
                    column = col
            return column, value



    def scorePosition(self, board, piece):
        return 1


    def terminalNode(self, board):
        return board.checkWin(self.getTeam()) or board.checkWin(self.getEnemy()) or len(board. getAvailabeMoves()) == 0


    # checks for self win in board input.
    def checkWinSelf(self, board):
        return board.checkWin(self.getTeam())

    # checks for enemy win in board input.
    def checkWinEnemy(self, board):
        return board.checkWin(self.getEnemy())







# Board for connect 4
# Allows all the necessary functions of the connect 4 board
# Allows width and height change
class Board:

    #defaults at standard Width and Height, 7 columns and 6 rows
    def __init__(self, width=7, height=6):
        self._width = width
        self._height = height
        self._board = np.zeros((self._height, self._width))
        self._lastMove = ()

    # resets board with all zeroes
    def clearBoard(self):
        self._board.fill(0)


    # return piece if inside board
    # returns 0 if outside board
    # also returns zero if space is blank
    def getPiece(self, col, row):
        if row < 0 or row > self._height - 1:
            return 0
        if col < 0 or col > self._width - 1:
            return 0
        return self._board[row][col]

    def dropPiece(self, col, piece):
        row = self.nextOpenRow(col)
        self._lastMove = (col, row)
        self._board[row][col] = piece


    # string representation of environment
    def __str__(self):
        sb = str(np.flip(self._board, 0))
        sb = sb.replace(" ", "")
        sb = sb[:-1]
        sb = sb[1:]
        sb = sb.replace("]", "")
        sb = sb.replace("[", "|")
        sb = sb.replace(".", "|")
        nr = " "
        for col in range(self._width):
            nr = nr + str(col) + " "
        nr = nr + "\n"
        sb = nr + sb
        return sb

    #------------------------------------------------
    #----------------Helper functions----------------
    #------------------------------------------------

    # sets piece value of given location
    def setPiece(self, col, row, piece):
        self._board[row][col] = piece

    # return next open row for given colum
    def nextOpenRow(self, col):
        for row in range(self._height):
            if self._board[row][col] == 0:
                return row

    # checks if colum is not full
    def columNotFull(self, col):
        return self._board[self._height - 1][col] == 0

    # return width
    def getWidth(self):
        return self._width

    # return height
    def getHeight(self):
        return self._height

    def getAvailabeMoves(self):
        availabeMoves = []
        for col in range(self._width):
            if self.columNotFull(col):
                row = self.nextOpenRow(col)
                availabeMoves.append((col, row))
        return availabeMoves


    # checks for a win for given piece
    def checkWin(self, piece):
        # Check horizontal
        for col in range(self._width - 3):
            for row in range(self._height):
                if self._board[row][col] == piece and self._board[row][col + 1] == piece and self._board[row][col + 2] == piece and \
                        self._board[row][col + 3] == piece:
                    return True
        # Check vertical
        for col in range(self._width):
            for row in range(self._height - 3):
                if self._board[row][col] == piece and self._board[row + 1][col] == piece and self._board[row + 2][col] == piece and \
                        self._board[row + 3][col] == piece:
                    return True
        # Check diagonal positive
        for col in range(self._width - 3):
            for row in range(self._height - 3):
                if self._board[row][col] == piece and self._board[row + 1][col + 1] == piece and self._board[row + 2][
                    col + 2] == piece and self._board[row + 3][col + 3] == piece:
                    return True
        # Check diagonal negative
        for col in range(self._width - 3):
            for row in range(3, self._height):
                if self._board[row][col] == piece and self._board[row - 1][col + 1] == piece and self._board[row - 2][
                    col + 2] == piece and self._board[row - 3][col + 3] == piece:
                    return True


# Class for setting up simulation
class Simulation:

    def __init__(self):
        self._env = Board()
        self._gamecount = 0
        self._player1Wins = 0
        self._player2Wins = 0
        self._draws = 0


    def newAgent(self, team, type):
        if type == "random":
            return randomAgent(team)
        elif type == "human":
            return HumanAgent(team)
        elif type == "minmax":
            return minMaxAgent(team)
        else:
            return randomAgent(team)


    # runs single game with 2 agents as input
    def playGame(self, agent1, agent2):
        gameOver = False
        turn = 0
        totalTurns = 0
        winner = 0
        agents = [agent1, agent2]
        currentTeam = 0

        while not gameOver:
            currentTeam = agents[turn].getTeam()
            agents[turn].sense(self._env)
            agents[turn].think()
            move = agents[turn].action()
            self._env.dropPiece(move, currentTeam)
            turn = 1 - turn
            totalTurns += 1

            if self._env.checkWin(currentTeam):
                gameOver = True
                winner = currentTeam

        if winner == 1:
            self._player1Wins += 1
        elif winner == 2:
            self._player2Wins += 1
        else:
            self._draws += 1
        self._gamecount += 1

        # Prints end game data
        print(self._env)
        print("Player{} drops winning move in col: {}".format(currentTeam, move))
        print("Total Turns Taken:{}".format(totalTurns))

        # Clears board for next game
        self._env.clearBoard()

    # runs simulation
    def run(self, iterations):
        print("Select Agent 1")
        print("Options are 'human' or  'random' or 'minmax'.\n")
        p1 = input("p1: ")

        print("Select Agent 2")
        print("Options are 'human' or  'random' or 'minmax'.\n")
        p2 = input("p2: ")


        agent1 = self.newAgent(1, p1)
        agent2 = self.newAgent(2, p2)

        while self._gamecount < iterations:
            print("Game:{}".format(self._gamecount + 1))
            self.playGame(agent1, agent2)

        print("Simulation Complete")
        print("games Played:{}".format(self._gamecount))
        print("Wins by player1:{}".format(self._player1Wins))
        print("Wins by player2:{}".format(self._player2Wins))
        print("Draws:{}".format(self._draws))

if __name__ == "__main__":
    print("Welcome to Connect 4!\n")
    gameCount = int(input("How many games should we run? "))
    test = Simulation()
    test.run(gameCount)


# b.printBoard()
