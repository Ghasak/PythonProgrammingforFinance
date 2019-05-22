# -----------------------------------------------------
# Intro and Getting Stock Price Data
# - Python Programming for Finance p.2
# -----------------------------------------------------
# -----------------------------------------------------
import os
import os.path as path
# Resource file export
#ResourceDir =  path.abspath(path.join(__file__ ,"../..")) # It doesn't work so far.
#ResourceDir = path.abspath(path.join(os.getcwd(),"../..")) # To go two directories,
#ResourceDir = path.abspath(path.join(os.getcwd(),"../"))    # To go one directory back.
ResourceDir = os.getcwd()
# https://stackoverflow.com/questions/27844088/python-get-directory-two-levels-up
# -----------------------------------------------------
# Installing packages -
# -----------------------------------------------------
import datetime as dt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web # This package replaced an old one

style.use('ggplot')
#start = dt.datetime(2000,1,1)
#end = dt.datetime(2016,12,31)
# -----------------------------------------------------
# You will need to run this one in the begging to pull the TSLA data
# df = web.DataReader('TSLA','yahoo',start,end)

# print(df.head())
# # print(ResourceDir)
# df.to_csv(ResourceDir+'/resources/tsla.csv')

# -----------------------------------------------------
df = pd.read_csv(ResourceDir+ '/resources/tsla.csv', parse_dates = True, index_col = 0)
#print(df.head())

# -----------------------------------------------------
#df.plot() # pandas has option to call the matplotlib inside
#plt.show()

# Adj. price column only
df['Adj Close'].plot()
plt.show()

# -----------------------------------------------------
print(df['Adj Close'])

# -----------------------------------------------------
print(df[['Open','Close','Volume']])
