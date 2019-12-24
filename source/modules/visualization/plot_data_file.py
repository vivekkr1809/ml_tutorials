from mpl_toolkits.mplot3d import axes3d
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import click

from modules.utils.parse_data_file import ParseDataJSON


class PlotNumpyData2D():
  """docstring for PlotNumpyData"""
  def __init__(self, x_data, y_data, plot_information, label=None):
    self.x_data = x_data
    self.y_data = y_data
    self.parsed_plot_information = plot_information
    self.label = label if label is not None else None

  def check_shape(self):
    # Make sure that the lengths of the arrays are the same
      assert(np.size(self.x_data, 0)==np.size(self.y_data,0))	
      try:
        self.x_data.shape[1]
      except IndexError:
        self.x_data = (np.asmatrix(self.x_data)).T
      try:
        self.y_data.shape[1]
      except IndexError:
        self.y_data = (np.asmatrix(self.y_data)).T

  def plot(self):
    self.check_shape()
    if self.decoration_file is None:
      markers_to_use = ["o", "*", "X", "s", "p", "P", "H", "D", "v", "^", "<", ">", "8"]
      colors_to_use = ["xkcd:purple", "xkcd:green", "xkcd:blue", "xkcd:pink", "xkcd:brown", "xkcd:red", "xkcd:orange", "xkcd:magenta", "xkcd:brick"]
    # Parse the plot information
    self.parsed_plot_information.parse_data()
    fig, ax = plt.subplots(figsize=(12, 9))
    plt.grid(True)
    plt.rc('font', size=20)
    plt.tick_params(labelsize=20)
    if(self.x_data.shape[1]==1):
      for i in range(self.y_data.shape[1]):
        plt.plot(np.ravel(self.x_data[:,0]), np.ravel(self.y_data[:,i]), linestyle=self.parsed_plot_information.data_dict["LineStyle"][i], linewidth=2, marker=markers_to_use[i], color=colors_to_use[i], label = self.parsed_plot_information.data_dict["LabelInfo"][i])
    else:
      for i in range(self.y_data.shape[1]):
       plt.plot(np.ravel(self.x_data[:,i]), np.ravel(self.y_data[:,i]), linestyle=self.parsed_plot_information.data_dict["LineStyle"][i], linewidth=2, marker=markers_to_use[i], color=colors_to_use[i], label = self.parsed_plot_information.data_dict["LabelInfo"][i])

    plt.title(self.parsed_plot_information.data_dict["PlotTitle"], fontsize=20)
    plt.xlabel(self.parsed_plot_information.data_dict["XaxisLabel"], fontsize = 20)
    plt.ylabel(self.parsed_plot_information.data_dict["YaxisLabel"], fontsize = 20)
    plt.legend(loc='best', ncol=4, mode="expand")
    plt.savefig(self.parsed_plot_information.data_dict["SaveAsFile"]+'.svg', bbox_inches='tight', format='svg', dpi=self.parsed_plot_information.data_dict["DPIValue"])


class PlotNumpyData3D():
  """docstring for PlotNumpyData3D"""
  def __init__(self, x_data, y_data, z_data, plot_information):
    self.x_data = x_data
    self.y_data = y_data
    self.z_data = z_data
    self.parsed_plot_information = plot_information
  def plot_scatter(self):
    print("Plotting 3D data")
    fig = plt.figure(figsize=(12,9))
    ax = fig.gca(projection='3d')
    ax.tick_params(labelsize=14)
    ax.scatter3D(self.x_data, self.y_data, self.z_data)
    plt.title(self.parsed_plot_information["PlotTitle"], fontsize=16)
    ax.set_xlabel(self.parsed_plot_information["XaxisLabel"], fontsize = 16)
    ax.set_ylabel(self.parsed_plot_information["YaxisLabel"], fontsize = 16)
    ax.set_zlabel(self.parsed_plot_information["ZaxisLabel"], fontsize = 16)
    plt.show()

    

if __name__ == '__main__':
  main()
