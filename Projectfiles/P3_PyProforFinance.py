# -----------------------------------------------------
# Intro and Getting Stock Price Data
# - Python Programming for Finance p.3
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

df['100ma'] = df['Adj Close'].rolling(window = 100).mean()

print(df.head())
df.dropna(inplace = True) # Drope the Nan values

print(df.head())

df['100ma'] = df['Adj Close'].rolling(window = 100, min_periods = 0).mean()

print(df.head())

# -----------------------------------------------------
ax1 = plt.subplot2grid((6,1),(0,0), rowspan= 5, colspan= 1)
ax2 = plt.subplot2grid((6,1),(5,0), rowspan= 1, colspan= 1, sharex = ax1)
# The sharex is the parameter to make a sync for the two figures when you draw them and zoom on one figure the other figure will change

ax1.plot(df.index,df['Adj Close'])
ax1.plot(df.index,df['100ma'])
ax2.bar(df.index,df['Volume'])

plt.show()



