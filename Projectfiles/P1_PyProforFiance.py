# -----------------------------------------------------
# Intro and Getting Stock Price Data
# - Python Programming for Finance p.1
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
start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)
# -----------------------------------------------------

df = web.DataReader('TSLA','yahoo',start,end)

print(df.head())
print(df.tail())
