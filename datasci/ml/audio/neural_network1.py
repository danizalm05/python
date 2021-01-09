"""
Valerio Velardo - The Sound of AI
  6- Implementing a neural network from scratch in Python
  https://github.com/musikalkemist/DeepLearningForAudioWithPython
  https://www.youtube.com/watch?v=0oWnheK-gGk
  """
import numpy as np
#MLP  Multilayer Perceptron
class MLP:
  def __init__(self, num_inputs=3, hidden_layers=[3, 3], num_outputs=2):
    """Constructor for the MLP. Takes the number of inputs,
            a variable number of hidden layers, and number of outputs
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
    print(layers)#[3, 3, 3, 2]
    weights = []
    for i in range(len(layers) - 1):  # len(layers) = 3
        w = np.random.rand(layers[i], layers[i + 1])  # [3x3], [3x3], [3x2],
        weights.append(w)
        #print(i, "]", w)

    self.weights = weights    


    #for w in self.weights:
       # print("-----------\n", w)

  def forward_propagate(self, inputs):
        """Computes forward propagation of the network based on input signals.
        Args:
            inputs (ndarray): Input signals
        Returns:
            activations (ndarray): Output values

        """
        # the input layer activation is just the input itself
        activations = inputs
        for w in self.weights:
            # calculate matrix multiplication between previous activation and weight matrix
            net_inputs = np.dot(activations, w)
            print("-----------\n", w)
if __name__ == "__main__":
    # create a Multilayer Perceptron
    mlp = MLP()
    # set random values for network's input
   # inputs = np.random.rand(mlp.num_inputs)

    # perform forward propagation
    #mlp.forward_propagate(inputs)

    #11:00