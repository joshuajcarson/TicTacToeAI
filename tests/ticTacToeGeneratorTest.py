"""
Created on Sun Nov  5 09:15:51 2017

@author: joshuajcarson
"""

import unittest
import numpy as np
import random
from src import ticTacToeGenerator as classUnderTest

class TicTacToeGeneratorMethods(unittest.TestCase):
    def setUp(self):
        self.gameBoard = classUnderTest.gameBoard()
        self.board = self.gameBoard.board
        self.defaultPlayerMark = 1
    
    def test_shouldCreateGameBoardWithNineSpots(self):
        self.assertEqual(len(self.board.index), 9)
        
    def test_shouldCreateGameBoardWithAllZeroValues(self):
        self.assertFalse(np.any(self.board))
    
    def test_shouldMarkSpecificSpotWithPlayerValue(self):
        randomSpotToTest = random.randint(0, 8)   
        self.gameBoard.makeMove(randomSpotToTest, self.defaultPlayerMark)
        self.assertEqual(self.board.get_value(randomSpotToTest, 'state'), self.defaultPlayerMark)

if __name__ == '__main__':
    unittest.main()