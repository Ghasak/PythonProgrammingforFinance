"""
    Machine learning with finance - Pattern Recognition for
        Algorithmic Forex and Stock Trading: Intro
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

#print(os.getcwd())
"/Desktop/My_DATA_MP/Learning/04_PythonforFinance"
CURRENT_PATH  = os.getcwd()
DATA_LOCATION = os.path.join(CURRENT_PATH,"M01_Machine_learning_pattern_recognition_algorithms/GBPUSD" )

#print(DATA_LOCATION)

def convert_date(date_bytes):
    return mdates.strpdate2num('%Y%m%d%H%M%S')(date_bytes.decode('ascii'))  # strpdate2num ,datestr2num


def graphRaxFx():
    date,bid,ask = np.loadtxt(os.path.join(DATA_LOCATION,"GBPUSD1d.txt"),
                                                          unpack= True,
                                                          delimiter= ',',
                                                          converters={0:convert_date})

