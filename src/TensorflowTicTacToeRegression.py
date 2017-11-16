import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

import src.ticTacToeGenerator


def main():
    tttGameBoard = src.ticTacToeGenerator.GameBoard()
    feature_columns = [tf.feature_column.numeric_column("x", shape=[9])]

    estimator = tf.estimator.LinearRegressor(feature_columns=feature_columns,
                                             model_dir="/tmp/ttt_model_regressor")

    # Generate random data to train again
    tttGameBoard.generate_100_games_random()

    board_train, board_test, result_train, result_test = train_test_split(tttGameBoard.overallHistory,
                                                                          tttGameBoard.overallResults,
                                                                          test_size=0.20)

    input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": np.array(board_train)},
        y=np.array(result_train),
        num_epochs=None,
        shuffle=True)

    estimator.train(input_fn=input_fn, steps=100)

    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": np.array(board_train)},
        y=np.array(result_train),
        batch_size=4,
        num_epochs=100,
        shuffle=False)
    test_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": np.array(board_test)},
        y=np.array(result_test),
        batch_size=4,
        num_epochs=100,
        shuffle=False)

    train_metrics = estimator.evaluate(input_fn=train_input_fn)
    eval_metrics = estimator.evaluate(input_fn=test_input_fn)
    print("train metrics: %r" % train_metrics)
    print("eval metrics: %r" % eval_metrics)

    player_one_wins, player_two_wins, ties = 0, 0, 0
    for x in range(len(tttGameBoard.winnerResults)):
        if tttGameBoard.winnerResults[x] == tttGameBoard.playerOneMark:
            player_one_wins += 1
        elif tttGameBoard.winnerResults[x] == tttGameBoard.playerTwoMark:
            player_two_wins += 1
        else:
            ties += 1
    print("Player One Wins: " + str(player_one_wins) +
          " Player Two Wins: " + str(player_two_wins) +
          " Ties: " + str(ties))

    # Generate random data to train again
    tttGameBoard.clear_history()
    tttGameBoard.generate_100_games_predict_player_one_random_player_two(estimator)

    board_train, board_test, result_train, result_test = train_test_split(tttGameBoard.overallHistory,
                                                                          tttGameBoard.overallResults,
                                                                          test_size=0.20)

    input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": np.array(board_train)},
        y=np.array(result_train),
        num_epochs=None,
        shuffle=True)

    estimator.train(input_fn=input_fn, steps=100)

    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": np.array(board_train)},
        y=np.array(result_train),
        batch_size=4,
        num_epochs=100,
        shuffle=False)
    test_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": np.array(board_test)},
        y=np.array(result_test),
        batch_size=4,
        num_epochs=100,
        shuffle=False)

    train_metrics = estimator.evaluate(input_fn=train_input_fn)
    eval_metrics = estimator.evaluate(input_fn=test_input_fn)
    print("train metrics: %r" % train_metrics)
    print("eval metrics: %r" % eval_metrics)

    player_one_wins, player_two_wins, ties = 0, 0, 0
    for x in range(len(tttGameBoard.winnerResults)):
        if tttGameBoard.winnerResults[x] == tttGameBoard.playerOneMark:
            player_one_wins += 1
        elif tttGameBoard.winnerResults[x] == tttGameBoard.playerTwoMark:
            player_two_wins += 1
        else:
            ties += 1
    print("Player One Wins: " + str(player_one_wins) +
          " Player Two Wins: " + str(player_two_wins) +
          " Ties: " + str(ties))


if __name__ == "__main__":
    main()
