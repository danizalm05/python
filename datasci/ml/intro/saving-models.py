"""
linear-regression
Create multiple models and saving ones that generate the best scores.
 https://techwithtim.net/tutorials/machine-learning-python/saving-models/
"""
#Import Libraries
import numpy as np
import pandas as pd
from sklearn import linear_model
import sklearn
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from matplotlib import style
import pickle