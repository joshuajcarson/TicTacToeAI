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

    def set_board(self, new_board):
        self.board = new_board

    def makeMove(self, spot, player):
        self.board[spot][0] = player

    def possibleMoves(self):
        return self.board == 0

    def createMatrixFromPossibleMoves(self, playerMark):
        returnMatrix = []
        possible_moves = self.possibleMoves()
        for x in range(0, len(possible_moves)):
            to_be_added = self.board.copy()
            to_be_added[x] = playerMark
            returnMatrix.append(to_be_added)
        return returnMatrix

    def didPlayerOneWin(self):
        return (self.didPlayerWin(self.playerOneMark * 3))

    def didPlayerTwoWin(self):
        return (self.didPlayerWin(self.playerTwoMark * 3))

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
