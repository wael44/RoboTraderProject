import pandas as pd 
import numpy as np

from sklearn.preprocessing import *






class Standardizer :

    def __init__(self,data):
        self.data=data
        self.StandardScalerTransformer=None
        self.MinMaxScalerTransformer=None
        

    def StandardScaler(self):
        """
            Fitting a StandardScaler and transform the data
        """
        self.StandardScalerTransformer=StandardScaler().fit(self.data)
        return self.StandardScalerTransformer.transform(self.data)

    def MinMaxScaler(self):
        pass
    