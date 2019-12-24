"""
Plot the GPR attribute for a given physical value
"""
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
from mpl_toolkits import mplot3d



class ComplexData():
  """docstring for ComplexData"""
  def __init__(self, numpy_data):
    self.complex_data = np.loadtxt(numpy_data, delimiter=',', dtype=np.complex128)

  def split_real_imag(self):
    self.real_vals = [x.real for x in self.complex_data]
    self.real_vals = np.asarray(self.real_vals)
    self.imag_vals = [x.imag for x in self.complex_data]
    self.imag_vals = np.asarray(self.imag_vals)

  def return_numpy_array(self):
    self.dict_var={}
    self.dict_var["RealValues"] = self.real_vals
    self.dict_var["ImaginaryValues"] = self.imag_vals

def main():
  return 0

if __name__=='__main__':
  main()  

