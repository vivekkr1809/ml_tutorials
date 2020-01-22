#Import the standard modules
import numpy as np
import numpy.linalg as LA
import sympy as sp
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import click
import os
import platform
import sys
import time

# sklearn modules
from sklearn import preprocessing


class TransformData(object):
  """docstring for TransformData"""
  def __init__(self, arg):
    self.arg = arg

  def get_combined_train_target_file():
    pass

  def get_combined_test_target_file():
    pass    


class DensityTransform(TransformData):
  """docstring for DensityTransform"""
  def __init__(self, outputfile):
    self.arg = arg


class CompressiveStrengthTransform(TransformData):
  """docstring for CompressiveStrengthTransform"""
  def __init__(self, arg):
    self.arg = arg
    

class PorosityTransform(TransformData):
  """docstring for PorosityTransform"""
  def __init__(self, arg):
    self.arg = arg
    