"""
Created on Sun Nov  5 05:43:08 2017

@author: joshuajcarson
"""

import numpy as np
import pandas as pd

class gameBoard(object):
    def __init__(self):
        self.data = []
        self.board = gameBoard.createEmptyBoard()

    @staticmethod
    def createEmptyBoard():
        return pd.DataFrame({'state' : np.zeros((9,))})

    def makeMove(self, spot, player):
        self.board.at[spot, 'state'] = player
        
    def possibleMoves(self):
        return self.board.query("state == 0")
    
    