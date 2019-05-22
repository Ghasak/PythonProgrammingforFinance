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
# packages for P4
# -----------------------------------------------------
# from matplotlib.finance import candlestick_ohlc
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
# Added later due to warning for future consideration.
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
# -----------------------------------------------------
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

# -----------------------------------------------------
# starting with re-sampling
# You can make it weekly or monthly e.g. 'Min'..etc
# Here we will do every 10 days take the mean,
# Open high low close also can do which we will work on it now, it will shrink our data.

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

print(df_ohlc)
df_ohlc.reset_index(inplace = True)
print(df_ohlc)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

print(df_ohlc)
# -----------------------------------------------------

# -----------------------------------------------------
ax1 = plt.subplot2grid((6,1),(0,0), rowspan= 5, colspan= 1)
ax2 = plt.subplot2grid((6,1),(5,0), rowspan= 1, colspan= 1, sharex = ax1)

ax1.xaxis_date()
candlestick_ohlc(ax1,df_ohlc.values,width=2, colorup = 'g') # Green up the color
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()
