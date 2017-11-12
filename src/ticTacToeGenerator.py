import random

import numpy as np

__author__ = 'joshuajcarson'
__project__ = 'TicTacToeAI'


class GameBoard(object):
    def topRow(self):
        return np.array([0, 1, 2])

    def middleRow(self):
        return np.array([3, 4, 5])

    def bottomRow(self):
        return np.array([6, 7, 8])

    def leftColumn(self):
        return np.array([0, 3, 6])

    def middleColumn(self):
        return np.array([1, 4, 7])

    def rightColumn(self):
        return np.array([2, 5, 8])

    def backSlash(self):
        return np.array([0, 4, 8])

    def forwardSlash(self):
        return np.array([2, 4, 6])

    def __init__(self):
        self.playerOneMark = 1
        self.playerTwoMark = -1
        self.board = self.createEmptyBoard()
        self.playHistory = []
        self.overallHistory = []
        self.overallResults = []

    def getPlayHistory(self):
        return self.playHistory

    def createEmptyBoard(self):
        return np.zeros((9, 1))

    def set_board(self, new_board):
        self.board = new_board
        self.playHistory.append(self.board.copy())

    def makeMove(self, spot, player):
        self.board[spot] = player
        self.playHistory.append(self.board.copy())

    def possibleMoves(self):
        return np.where(self.board == 0)[0]

    def createMatrixFromPossibleMoves(self, playerMark):
        returnMatrix = []
        possible_moves = self.possibleMoves()
        for x in range(0, len(possible_moves)):
            to_be_added = self.board.copy()
            to_be_added[possible_moves[x]] = playerMark
            returnMatrix.append(to_be_added)
        return returnMatrix

    def playRandomMove(self, playerMark):
        possible_moves = self.createMatrixFromPossibleMoves(playerMark)
        move_to_pick = random.randint(0, len(possible_moves) - 1)
        self.set_board(possible_moves[move_to_pick])
        return

    def didPlayerOneWin(self):
        return self.didPlayerWin(self.playerOneMark * 3)

    def didPlayerTwoWin(self):
        return self.didPlayerWin(self.playerTwoMark * 3)

    def didPlayerWin(self, totalToTarget):
        if (np.sum(self.board[self.topRow()]) == totalToTarget) | \
                (np.sum(self.board[self.middleRow()]) == totalToTarget) | \
                (np.sum(self.board[self.bottomRow()]) == totalToTarget) | \
                (np.sum(self.board[self.leftColumn()]) == totalToTarget) | \
                (np.sum(self.board[self.middleColumn()]) == totalToTarget) | \
                (np.sum(self.board[self.rightColumn()]) == totalToTarget) | \
                (np.sum(self.board[self.backSlash()]) == totalToTarget) | \
                (np.sum(self.board[self.forwardSlash()]) == totalToTarget):
            return True
        return False

    def printGameState(self):
        print(str(self.board[0][0]) + '|' + str(self.board[1][0]) + '|' + str(self.board[2][0]))
        print(str(self.board[3][0]) + '|' + str(self.board[4][0]) + '|' + str(self.board[5][0]))
        print(str(self.board[6][0]) + '|' + str(self.board[7][0]) + '|' + str(self.board[8][0]))

    def playOneFullRandomGame(self):
        self.board = self.createEmptyBoard()
        for x in range(0, 9):
            if x % 2 == 0:
                self.playRandomMove(self.playerOneMark)
            else:
                self.playRandomMove(self.playerTwoMark)
            if self.didPlayerOneWin():
                return self.playerOneMark
            if self.didPlayerTwoWin():
                return self.playerTwoMark
        return 0


dumb = GameBoard()
for _ in range(0, 200):
    results = dumb.playOneFullRandomGame()
    for y in range(0, len(dumb.playHistory)):
        dumb.overallHistory.append(dumb.playHistory[y])
        dumb.overallResults.append(results)
    dumb.playHistory = []
