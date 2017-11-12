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

    def test_shouldCreateGameBoardWithNineSpots(self):
        self.assertEqual(len(self.board), 9)

    def test_shouldSayAllSpotsAreOpenByDefault(self):
        self.assertEqual(9, len(self.gameBoard.possibleMoves()))

    def test_shouldCreateGameBoardWithAllZeroValues(self):
        self.assertFalse(np.any(self.board))

    def test_shouldDefinePlayerOneMarkAsOne(self):
        self.assertEqual(self.gameBoard.playerOneMark, 1)

    def test_shouldDefinePlayerTwoMarkAsNegativeOne(self):
        self.assertEqual(self.gameBoard.playerTwoMark, -1)

    def test_shouldMarkSpecificSpotWithPlayerValue(self):
        randomSpotToTest = random.randint(0, 8)
        self.gameBoard.makeMove(randomSpotToTest, self.gameBoard.playerOneMark)
        self.assertEqual(self.board[randomSpotToTest][0], self.gameBoard.playerOneMark)

    def test_shouldRemoveSpotAsPossibleSpotAfterMarked(self):
        randomSpotToTest = random.randint(0, 8)
        self.gameBoard.makeMove(randomSpotToTest, self.gameBoard.playerOneMark)
        possibleSpots = self.gameBoard.possibleMoves()
        howManyOfTheRandomSpotFoundInPossibleMoves = len(np.where(possibleSpots == randomSpotToTest)[0])
        self.assertEqual(0, howManyOfTheRandomSpotFoundInPossibleMoves)

    def test_shouldStoreNothingBeforeAnyPlayIsMade(self):
        play_history = self.gameBoard.getPlayHistory()
        self.assertEqual(0, len(play_history))

    def test_shouldStoreTheLastPlayMadeForTheFirstPlay(self):
        self.gameBoard.makeMove(0, self.gameBoard.playerOneMark)
        play_history = self.gameBoard.getPlayHistory()
        self.assertEqual(1, len(play_history))
        self.assertEqual(1, np.sum(play_history))
        self.assertEqual(1, play_history[0][0])

    def test_shouldStoreThePlaysMadeInOrder(self):
        self.gameBoard.makeMove(0, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(1, self.gameBoard.playerOneMark)
        play_history = self.gameBoard.getPlayHistory()
        self.assertEqual(2, len(play_history))
        self.assertEqual(3, np.sum(play_history))
        self.assertEqual(1, play_history[0][0])
        self.assertEqual(1, play_history[1][0])
        self.assertEqual(1, play_history[1][1])

    def test_shouldClearHistoryWhenBoardIsEmptyed(self):
        self.gameBoard.makeMove(0, self.gameBoard.playerOneMark)
        self.gameBoard.createEmptyBoard()
        self.gameBoard.makeMove(3, self.gameBoard.playerTwoMark)
        play_history = self.gameBoard.getPlayHistory()
        self.assertEqual(1, len(play_history))

    def test_setBoardShouldChangeTheExistingBoardToThePassedInBoard(self):
        to_be_set = self.board.copy()
        to_be_set[2] = -1
        self.gameBoard.set_board(to_be_set)
        self.assertTrue(np.allclose(self.gameBoard.board, to_be_set))

    def test_shouldLeaveOtherSpotsOpenAfterMark(self):
        randomSpotToTest = random.randint(0, 8)
        self.gameBoard.makeMove(randomSpotToTest, self.gameBoard.playerOneMark)
        possibleSpots = self.gameBoard.possibleMoves()
        self.assertEqual(len(possibleSpots), 8)

    def test_shouldClaimPlayerOneDidNotWinByDefault(self):
        self.assertFalse(self.gameBoard.didPlayerOneWin())

    def test_shouldCreateMatrixOfFutureStateFromPossibleMoveAndImpactNoOtherSpace(self):
        possible_moves_matrix = self.gameBoard.createMatrixFromPossibleMoves(self.gameBoard.playerOneMark)
        self.assertEqual(9, np.sum(possible_moves_matrix))
        for x in range(0, 9):
            self.assertEqual(self.gameBoard.playerOneMark, possible_moves_matrix[x][x])

    def test_shouldPlayerOneOfTheMovesFromThePossibleMoves(self):
        possible_moves_matrix = self.gameBoard.createMatrixFromPossibleMoves(self.gameBoard.playerOneMark)
        self.gameBoard.playRandomMove(self.gameBoard.playerOneMark)
        for x in range(0, len(possible_moves_matrix)):
            if np.allclose(possible_moves_matrix[x], self.gameBoard.board):
                self.assertTrue(True)
                return
        self.assertTrue(False, "None of the possible moves was the move chosen")

    def test_shouldClaimTopRowAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(0, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(1, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(2, self.gameBoard.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimMiddleRowAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(3, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(4, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(5, self.gameBoard.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimBottomRowAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(6, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(7, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(8, self.gameBoard.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimLeftColumnAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(0, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(3, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(6, self.gameBoard.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimMiddleColumnAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(1, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(4, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(7, self.gameBoard.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimRightColumnAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(2, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(5, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(8, self.gameBoard.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimBackSlashAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(0, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(4, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(8, self.gameBoard.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimForwardSlashAsWinForPlayerOneIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(2, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(4, self.gameBoard.playerOneMark)
        self.gameBoard.makeMove(6, self.gameBoard.playerOneMark)
        self.assertTrue(self.gameBoard.didPlayerOneWin())

    def test_shouldClaimPlayerTwoDidNotWinByDefault(self):
        self.assertFalse(self.gameBoard.didPlayerTwoWin())

    def test_shouldClaimTopRowAsWinForPlayerTwoIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(0, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(1, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(2, self.gameBoard.playerTwoMark)
        self.assertTrue(self.gameBoard.didPlayerTwoWin())

    def test_shouldClaimMiddleRowAsWinForPlayerTwoIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(3, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(4, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(5, self.gameBoard.playerTwoMark)
        self.assertTrue(self.gameBoard.didPlayerTwoWin())

    def test_shouldClaimBottomRowAsWinForPlayerTwoIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(6, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(7, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(8, self.gameBoard.playerTwoMark)
        self.assertTrue(self.gameBoard.didPlayerTwoWin())

    def test_shouldClaimLeftColumnAsWinForPlayerTwoIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(0, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(3, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(6, self.gameBoard.playerTwoMark)
        self.assertTrue(self.gameBoard.didPlayerTwoWin())

    def test_shouldClaimMiddleColumnAsWinForPlayerTwoIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(1, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(4, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(7, self.gameBoard.playerTwoMark)
        self.assertTrue(self.gameBoard.didPlayerTwoWin())

    def test_shouldClaimRightColumnAsWinForPlayerTwoIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(2, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(5, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(8, self.gameBoard.playerTwoMark)
        self.assertTrue(self.gameBoard.didPlayerTwoWin())

    def test_shouldClaimBackSlashAsWinForPlayerTwoIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(0, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(4, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(8, self.gameBoard.playerTwoMark)
        self.assertTrue(self.gameBoard.didPlayerTwoWin())

    def test_shouldClaimForwardSlashAsWinForPlayerTwoIfAllMarkedTheSame(self):
        self.gameBoard.makeMove(2, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(4, self.gameBoard.playerTwoMark)
        self.gameBoard.makeMove(6, self.gameBoard.playerTwoMark)
        self.assertTrue(self.gameBoard.didPlayerTwoWin())


if __name__ == '__main__':
    main()
