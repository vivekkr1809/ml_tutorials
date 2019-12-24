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


class ComplexFeatureData():
	"""docstring for ComplexData"""
	def __init__(self, feature_file, target_file, label):
		self.feature_file = feature_file
		self.target_file = target_file
		self.label = label

	def read_features(self):
		self.features = np.loadtxt(self.feature_file, delimiter=',', dtype=np.complex128)

	def split_real_imag(self):
		self.read_features()
		self.real_vals = [x.real for x in self.features]
		self.real_vals = np.array(self.real_vals)
		self.imag_vals = [x.imag for x in self.features]
		self.imag_vals = np.array(self.imag_vals)

	def extract_labels(self):
		target_data = pd.read_csv(self.target_file)
		self.target = target_data[[self.label]].copy()
		self.target.dropna(inplace=True)
		self.target = self.target.reset_index(drop=True)
		self.target = self.target.to_numpy().flatten()

	def plot_feature_label_surface(self):
		self.split_real_imag()
		self.extract_labels()
		n_labels = self.target.size
		temp = self.target.argsort()
		ranks = np.empty_like(temp)
		ranks[temp] = np.arange(len(self.target))

		x_axis_vals = [i+1 for i in range(512)]
		x_axis_vals = np.array(x_axis_vals)

		y_min_lim = np.amin(self.real_vals)
		y_max_lim = np.amax(self.real_vals)

		z_min_lim = np.amin(self.imag_vals)
		z_max_lim = np.amax(self.imag_vals)

		for i in range(n_labels):
			ax = plt.axes(projection='3d')
			ax.set_ylim([y_min_lim,y_max_lim])
			ax.set_zlim([z_min_lim,z_max_lim])
			ax.scatter3D(x_axis_vals, self.real_vals[i,:], self.imag_vals[i,:], label=str(round(self.target[i],2)))
			plt.legend(loc='upper left')
			plt.savefig('./results/density_dinst_all'+"_"+ str(ranks[i])+'.png',bbox_inches='tight', format='png', dpi=100)
			plt.close()




@click.command()
@click.argument('train_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('target_file', type=click.Path(exists=True, dir_okay=False))
def main(train_file, target_file):
	print('Visualize complex data')
	complex_data = ComplexFeatureData(train_file, target_file, "Density")
	complex_data.plot_feature_label_surface()
	return 0
	

if __name__=='__main__':
	main()	
