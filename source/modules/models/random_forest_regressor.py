"""
class sklearn.ensemble.RandomForestRegressor(n_estimators=’warn’, criterion=’mse’, max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=’auto’, max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False)
"""
import pickle
import sys
import numpy as np
from sklearn.ensemble import RandomForestRegressor
sys.path.append('source')

class RandomForestModel(object):
    def __init__(self):
        self.regmodel = RandomForestRegressor(n_estimators=25, criterion='mse', random_state=0, max_depth=20)
        self.name = 'RandomForest'

    def get_params(self):
        return self.regmodel.get_params()

    def save(self, filename):
        with open(filename, 'wb') as ofile:
            pickle.dump(self.regmodel, ofile, pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        with open(filename, 'rb') as ifile:
            self.regmodel = pickle.load(ifile)
