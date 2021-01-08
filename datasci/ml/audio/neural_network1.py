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
        w = np.random.rand(layers[i], layers[i + 1])  # 3x3, 3x3, 3x2,
        weights.append(w)
        print(i, "]", w)

    self.weights = weights    
    #5:30
    #print(self.weights)





if __name__ == "__main__":
    # create a Multilayer Perceptron
    mlp = MLP()