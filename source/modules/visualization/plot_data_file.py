import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import click

from .parse_data_file import ParseDataJSON


class PlotNumpyData():
  """docstring for PlotNumpyData"""
  def __init__(self, x_data, y_data, plot_information_file, decoration_file=None):
    self.x_data = x_data
    self.y_data = y_data
    self.parsed_plot_information = ParseDataJSON(plot_information_file)
    self.decoration_file = decoration_file if decoration_file is not None else None
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
    plt.ylim(-500,1200)
    plt.xlim(0,2500)
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

class PlotDataFrame():
  """docstring for PlotDataFrame"""
  def __init__(self, x_data, y_data, plot_information_file,  decoration_file=None):   
    self.x_data = x_data
    self.y_data = y_data
    self.parsed_plot_information = ParseDataJSON(plot_information_file)
    self.decoration_file = decoration_file if decoration_file is not None else None
  def check_shape(self):
    assert(self.x_data.shape[0]==self.y_data.shape[0])

  def plot(self):
    self.check_shape()
    if self.decoration_file is None:
      markers_to_use = ["o", "*", "X", "s", "p", "P", "H", "D", "v", "^", "<", ">", "8"]
      colors_to_use = ["xkcd:purple", "xkcd:green", "xkcd:blue", "xkcd:pink", "xkcd:brown", "xkcd:red", "xkcd:orange", "xkcd:magenta", "xkcd:brick"]
    self.parsed_plot_information.parse_data()
    fig, ax = plt.subplots(figsize=(12, 9))
    plt.grid(True)
    plt.rc('font', size=20)
    plt.tick_params(labelsize=20)
    
    plt.ylim(,)
    if(self.x_data.shape[1]==1):
      for i in range(self.y_data.shape[1]):
        plt.plot(self.x_data.iloc[:,0], self.y_data.iloc[:,i], linestyle=self.parsed_plot_information.data_dict["LineStyle"][i], linewidth = 4, marker=markers_to_use[i], color=colors_to_use[i], label = self.parsed_plot_information.data_dict["LabelInfo"][i])
    else:
      for i in range(self.y_data.shape[1]):
        plt.plot(self.x_data.iloc[:,i], self.y_data.iloc[:,i], linestyle=self.parsed_plot_information.data_dict["LineStyle"][i], marker=markers_to_use[i], color=colors_to_use[i],label= self.parsed_plot_information.data_dict["LabelInfo"][i])

    plt.title(self.parsed_plot_information.data_dict["PlotTitle"], fontsize=20)
    plt.xlabel(self.parsed_plot_information.data_dict["XaxisLabel"], fontsize = 20)
    plt.ylabel(self.parsed_plot_information.data_dict["YaxisLabel"], fontsize = 20)
    plt.legend(loc='best')
    plt.savefig(self.parsed_plot_information.data_dict["SaveAsFile"]+'.svg', bbox_inches='tight', format='svg', dpi=self.parsed_plot_information.data_dict["DPIValue"])


@click.command()
@click.argument('data_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('plot_information_file', type=click.Path(exists=True, dir_okay=False))
def main(data_file, plot_information_file):
  data = np.genfromtxt(data_file, delimiter=',')
  plot_object = PlotNumpyData(data[:,0], data[:,1], plot_information_file)
  plot_object.plot()
  return 0

if __name__ == '__main__':
  main()
