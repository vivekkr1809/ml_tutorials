import numpy as np
import numpy.linalg as LA
import sympy as sp
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import os
import platform
import sys
import time

from modules.utils.parse_data_file import ParseDataJSON
from modules.utils.analyze_complex_data import ComplexData

# from modules.visualization.plot_data_file import PlotNumpyData2D
from modules.visualization.plot_data_file import PlotNumpyData3D

from modules.models.random_forest_regressor import RandomForestModel


# Define spliting here?
# Which is the best object
def split_test_train_data():
  return 0


# MIA is a 1-D Complex Data
def using_mia_as_features(model_input):
  features_data= ComplexData(model_input["data_files"]["feature_file"])
  # Split the real and imaginary values
  features_data.split_real_imag()
  # Read the label files
  
  # Feature to predict
  # Set 0: Density
  # Set 1: Compressive Strength
  # Set 2: Porosity
  property_to_predict = model_input["data_files"]["physical_property"][2]

  target_data = pd.read_csv(model_input["data_files"]["target_file"])
  target = target_data[[property_to_predict]].copy()

  target.dropna(inplace=True)
  target = target.reset_index(drop=True)
  target = target.to_numpy().flatten()

  print(target)
  sys.exit()
  # TO DO: Assert that sizes are the same

  # Plot the initial feature vs label
  plot_feature_label_object = PlotNumpyData3D(features_data.real_vals, features_data.imag_vals, target, model_input["feature_vs_label_plot_information"])

  plot_feature_label_object.plot_scatter()

  # 

  return 0

def using_meanav_as_features(model_input):
  # Read the features
  features_data = pd.read_csv(model_input["data_files"]["feature_file"], header=None)
  features_data = features_data.to_numpy()
  # print(features_data)
  # print(features_data.std(axis=0))
  # print(features_data.mean(axis=0))
  # plt.plot(features_data.std(axis=0)/features_data.mean(axis=0))
  # plt.show()
  # Read the target data
  target_data = pd.read_csv(model_input["data_files"]["target_file"])
  # Loop over all the physical properties to predict
  for p in (model_input["data_files"]["physical_property"]):  
    target = target_data[[p]].copy()
    target.dropna(inplace=True)
    target = target.reset_index(drop=True)
    target = target.to_numpy().flatten()
    plot_feature_label_object = PlotNumpyData2D(features_data, target, model_input["feature_vs_label_plot_information"], p)
  
  return 0


# The main file
def main():
  model_input = ParseDataJSON('model_input.json')
  model_input.parse_data()
  # using_mia_as_features()
  using_meanav_as_features(model_input.data_dict["meanav"])
  return 0

if __name__ == '__main__':
  main()
