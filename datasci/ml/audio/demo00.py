"""
Valerio Velardo - The Sound of AI
  3- Implementing an artificial neuron from scratch
  https://github.com/musikalkemist/DeepLearningForAudioWithPython/
  https://www.youtube.com/watch?v=qxIaW-WvLDU
"""
import math


def sigmoid(x):
    y = 1.0 / (1 + math.exp(-x))
    return y


def activate(inputs, weights):
    """Computes activation of neuron based on input signals and connection
       weights.
       Output = f(x_1*w_1 + x_2*w_2 + ... + x_k*w_k), where 'f' is the
       sigmoid function.
       Args:
           inputs (list): Input signals
           weights (list): Connection weights
       Returns:
           output (float): Output value
       """

    # compute the sum of the product of the input signals and the weights
    # here we're using pythons "zip" function to iterate two lists together
    h = 0
    for x, w in zip(inputs, weights):
        h += x*w

    # process sum through sigmoid activation function
    return sigmoid(h)


if __name__ == "__main__":
    input = [0.5, 0.3, 0.2]
    weights = [0.4, 0.7, 0.2]
    output = activate(input, weights)
    print(output)


