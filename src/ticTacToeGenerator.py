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

    def createEmptyBoard(self):
        return np.zeros((9, 1))

    def makeMove(self, spot, player):
        self.board[spot][0] = player

    def possibleMoves(self):
        return self.board == 0

    def didPlayerOneWin(self):
        if (np.sum(self.board[self.topRow()]) == 3) | \
                (np.sum(self.board[self.middleRow()]) == 3) | \
                (np.sum(self.board[self.bottomRow()]) == 3) | \
                (np.sum(self.board[self.leftColumn()]) == 3) | \
                (np.sum(self.board[self.middleColumn()]) == 3) | \
                (np.sum(self.board[self.rightColumn()]) == 3) | \
                (np.sum(self.board[self.backSlash()]) == 3) | \
                (np.sum(self.board[self.forwardSlash()]) == 3):
            return True
        return False
