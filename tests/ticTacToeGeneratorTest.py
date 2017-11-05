import random
from unittest import TestCase, main

import numpy as np

from src import ticTacToeGenerator

__author__ = 'joshuajcarson'
__project__ = 'TicTacToeAI'


class TicTacToeGeneratorMethods(TestCase):
    def setUp(self):
        self.gameBoard = ticTacToeGenerator.gameBoard()
        self.board = self.gameBoard.board
        self.playerOneMark = 1
        self.stateColumn = 'state'

    def test_shouldCreateGameBoardWithNineSpots(self):
        self.assertEqual(len(self.board.index), 9)

    def test_shouldCreateGameBoardWithAllZeroValues(self):
        self.assertFalse(np.any(self.board))

    def test_shouldMarkSpecificSpotWithPlayerValue(self):
        randomSpotToTest = random.randint(0, 8)
        self.gameBoard.makeMove(randomSpotToTest, self.playerOneMark)
        self.assertEqual(self.board.get_value(randomSpotToTest, self.stateColumn), self.playerOneMark)

    def test_shouldHaveColumnCalledState(self):
        self.assertTrue(self.stateColumn in self.board.columns.values)

    def test_shouldClaimPlayerOneDidNotWinByDefault(self):
        self.assertFalse(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimTopRowAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(0, self.playerOneMark)
        self.gameBoard.makeMove(1, self.playerOneMark)
        self.gameBoard.makeMove(2, self.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())


if __name__ == '__main__':
    main()
