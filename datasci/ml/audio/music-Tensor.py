"""17:00
 Valerio Velardo - The Sound of AI

A simple neural network (multilayer perceptron) using TensorFlow 2
and Keras and train it to perform the arithmetic sum.
https://www.youtube.com/watch?v=JdXxaZcQer8&list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf&index=9
https://github.com/musikalkemist/DeepLearningForAudioWithPython/blob/master/9-%20How%20to%20imlement%20a%20simple%20neural%20network%20with%20TensorFlow/code/mlp.py
"""
import tensorflow as tf
from sklearn.model_selection import train_test_split
import numpy as np
from random import random


def generate_dataset(num_samples, test_size=0.33):
    """Generates train/test data for sum operation
      :param num_samples (int): Num of total samples in dataset
      :param test_size (int): Ratio of num_samples used as test set
        """
    # build inputs/targets for sum operation: y[0][0] = x[0][0] + x[0][1]
    x = np.array([[random() / 2 for _ in range(2)]
                  for _ in range(num_samples)])

    y = np.array([[i[0] + i[1]] for i in x])

    x_train, x_test, y_train, y_test = \
        train_test_split(x, y, test_size=test_size)
    return x_train, x_test, y_train, y_test


if __name__ == "__main__":
    ratio = 0.3  # Ratio of samples used as test set
    samplesSize = 2000  # num of  samples
    x_train, x_test, y_train, y_test = \
        generate_dataset(samplesSize, ratio)

    # build model with 3 layers: 2 -> 5 -> 1
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(5, input_dim=2, activation="sigmoid"),
        tf.keras.layers.Dense(1, activation="sigmoid")
    ])

    # choose optimiser  (SGD stochastic gradient descent)
    optimizer = tf.keras.optimizers.SGD(lr=0.1)  # lr = learning_rate

    # compile model
    model.compile(optimizer=optimizer, loss='mse')  # MSE mean squared error

    # train model
    model.fit(x_train, y_train, epochs=10)