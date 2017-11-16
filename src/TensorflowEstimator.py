import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

import src.ticTacToeGenerator


def main():
    tttGameBoard = src.ticTacToeGenerator.GameBoard()
    tttGameBoard.generate_100_games_random()
    board_train, board_test, result_train, result_test = train_test_split(tttGameBoard.overallHistory,
                                                                          tttGameBoard.overallResults,
                                                                          test_size=0.20)

    feature_columns = [tf.feature_column.numeric_column("x", shape=[9])]

    classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                            hidden_units=[10, 20, 10],
                                            n_classes=3,
                                            model_dir="/tmp/ttt_model")

    estimator = tf.estimator.LinearRegressor(feature_columns=feature_columns,
                                             model_dir="/tmp/ttt_model_regressor")

    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": np.array(board_train)},
        y=np.array(result_train),
        num_epochs=None,
        shuffle=True)

    classifier.train(input_fn=train_input_fn, steps=2000)
    estimator.train(input_fn=train_input_fn, steps=1000)

    test_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": np.array(board_test)},
        y=np.array(result_test),
        num_epochs=1,
        shuffle=False)

    # ("\nTest Accuracy: {0:f}\n".format(classifier.evaluate(input_fn=test_input_fn)["accuracy"]))
    print("\nTest Accuracy: {0:f}\n".format(estimator.evaluate(input_fn=test_input_fn)["loss"]))

    new_samples = np.array(
        [[0.0, 0.0, 1.0, 1.0, -1.0, 0.0, 0.0, 0.0, 0.0],
         [0.0, 0.0, 1.0, 1.0, -1.0, 0.0, 1.0, -1.0, 0.0]], dtype=np.float32)
    predict_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": new_samples},
        num_epochs=1,
        shuffle=False)

    predictions = list(classifier.predict(input_fn=predict_input_fn))
    predicted_classes = [p["classes"] for p in predictions]

    linearPredictions = list(estimator.predict(input_fn=predict_input_fn))
    predicted_move_scores = [p['predictions'] for p in linearPredictions]
    best_move = predicted_move_scores.index(max(predicted_move_scores))

    print("New Samples, Class Predictions:    {}\n".format(predicted_classes))
    print(best_move)


if __name__ == "__main__":
    main()
