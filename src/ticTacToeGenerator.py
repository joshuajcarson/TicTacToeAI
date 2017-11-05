import numpy as np
import pandas as pd


class gameBoard(object):
    def __init__(self):
        self.data = []
        self.stateColumn = 'state'
        self.playerOneMark = 1
        self.playerTwoMark = -1
        self.board = self.createEmptyBoard()

    def createEmptyBoard(self):
        return pd.DataFrame({self.stateColumn: np.zeros((9,))})

    def makeMove(self, spot, player):
        self.board.at[spot, self.stateColumn] = player

    def possibleMoves(self):
        return self.board.query(str(self.stateColumn, " == 0"))

    def didPlayerOneWin(self):
        if sum(self.board[0:3]['state']) == 3:
            return True
        return False
