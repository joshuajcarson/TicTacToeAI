import random
from unittest import TestCase, main

import numpy as np

import src.ticTacToeGenerator

__author__ = 'joshuajcarson'
__project__ = 'TicTacToeAI'


class TicTacToeGeneratorMethods(TestCase):
    def setUp(self):
        self.gameBoard = src.ticTacToeGenerator.GameBoard()
        self.board = self.gameBoard.board
        self.playerOneMark = 1

    def test_shouldCreateGameBoardWithNineSpots(self):
        self.assertEqual(len(self.board), 9)

    def test_shouldCreateGameBoardWithAllZeroValues(self):
        self.assertFalse(np.any(self.board))

    def test_shouldMarkSpecificSpotWithPlayerValue(self):
        randomSpotToTest = random.randint(0, 8)
        self.gameBoard.makeMove(randomSpotToTest, self.playerOneMark)
        self.assertEqual(self.board[randomSpotToTest][0], self.playerOneMark)

    def test_shouldClaimPlayerOneDidNotWinByDefault(self):
        self.assertFalse(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimTopRowAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(0, self.playerOneMark)
        self.gameBoard.makeMove(1, self.playerOneMark)
        self.gameBoard.makeMove(2, self.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimMiddleRowAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(3, self.playerOneMark)
        self.gameBoard.makeMove(4, self.playerOneMark)
        self.gameBoard.makeMove(5, self.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimBottomRowAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(6, self.playerOneMark)
        self.gameBoard.makeMove(7, self.playerOneMark)
        self.gameBoard.makeMove(8, self.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimLeftColumnAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(0, self.playerOneMark)
        self.gameBoard.makeMove(3, self.playerOneMark)
        self.gameBoard.makeMove(6, self.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimMiddleColumnAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(1, self.playerOneMark)
        self.gameBoard.makeMove(4, self.playerOneMark)
        self.gameBoard.makeMove(7, self.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimRightColumnAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(2, self.playerOneMark)
        self.gameBoard.makeMove(5, self.playerOneMark)
        self.gameBoard.makeMove(8, self.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimBackSlashAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(0, self.playerOneMark)
        self.gameBoard.makeMove(4, self.playerOneMark)
        self.gameBoard.makeMove(8, self.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimForwardSlashAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(2, self.playerOneMark)
        self.gameBoard.makeMove(4, self.playerOneMark)
        self.gameBoard.makeMove(6, self.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

if __name__ == '__main__':
    main()
