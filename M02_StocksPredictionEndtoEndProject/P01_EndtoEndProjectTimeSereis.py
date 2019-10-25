#



# Obtaining the dataset from :
# https://community.tableau.com/docs/DOC-1236

#/Users/ghasak/Desktop/My_DATA_MP/Learning/04_PythonforFinance/M02_StocksPredictionEndtoEndProject/DataSet/Sample - Superstore.xls

import os
import sys
print(os.getcwd())

import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib

matplotlib.rcParams['axes.labelsize']  = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color']      = 'k'


