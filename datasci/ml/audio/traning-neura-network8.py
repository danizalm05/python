"""
Valerio Velardo - The Sound of AI
  8- TRAINING A NEURAL NETWORK: Implementing back propagation and gradient descent
  https://www.youtube.com/watch?v=Z97XGNUUx9o&list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf&index=8
 https://github.com/musikalkemist/DeepLearningForAudioWithPython/tree/master/8-%20Training%20a%20neural%20network:%20Implementing%20back%20propagation%20from%20scratch/code

  """
import numpy as np


#  MLP  Multilayer Perceptron


class MLP:
    def __init__(self, num_inputs=3, hidden_layers=[3, 3], num_outputs=2):
        """Constructor for the MLP.  (Multi layer Perceptron)
       Args:
            num_inputs (int): Number of inputs
            hidden_layers (list): A list of ints for the hidden layers
            num_outputs (int): Number of outputs
    """

        self.num_inputs = num_inputs
        self.hidden_layers = hidden_layers
        self.num_outputs = num_outputs

        # create a generic representation of the layers
        layers = [num_inputs] + hidden_layers + [num_outputs]
        print(layers)  # [3, 3, 3, 2]
        weights = []
        for i in range(len(layers) - 1):  # len(layers) = 3
            w = np.random.rand(layers[i], layers[i + 1])  # [3x3], [3x3], [3x2],
            weights.append(w)
            # print(i, "]", w)

        self.weights = weights

        # for w in self.weights:
        #  print("-----------\n", w)

        # save derivatives per layer
        derivatives = []
        for i in range(len(layers) - 1):
            d = np.zeros((layers[i], layers[i + 1]))# d is a matrix of size layers[i] X layers[i + 1]
            derivatives.append(d)

        self.derivatives = derivatives  # list of 3 arrays of zeros   [3x3], [3x3], [3x2]

        # save activations per layer
        activations = []
        for i in range(len(layers)):
            a = np.zeros(layers[i])

            activations.append(a)
        self.activations = activations# list of  vectors of zeros [3, 3, 3, 2]



    def forward_propagate(self, inputs):
        """Computes forward propagation of the network based on input signals.
        Args:
            inputs (ndarray): Input signals
        Returns:
            activations (ndarray): Output values

        """
        # the input layer activation is just the input itself
        activations = inputs

        # save the activations for backpropogation
        self.activations[0] = activations



        for w in self.weights:
            #  matrix multiplication between previous activation and weight matrix
            net_inputs = np.dot(activations, w)
            # print("-----------\n", w)

            activations = self._sigmoid(net_inputs)

        return activations

    def _sigmoid(self, x):
        y = 1.0 / (1 + np.exp(-x))
        return y


if __name__ == "__main__":
    # create a Multilayer Perceptron
    mlp = MLP()
    # set random values for network's input
    inputs = np.random.rand(mlp.num_inputs)

    # perform forward propagation
    output = mlp.forward_propagate(inputs)

    # 16:00 
    print("Network Inputs  : {}".format(inputs))
    print("Network Output: {}".format(output))