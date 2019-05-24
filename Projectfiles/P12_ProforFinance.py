# -----------------------------------------------------
# Intro and Getting Stock Price Data
# - Python Programming for Finance p.3
# -----------------------------------------------------
# -----------------------------------------------------
import os
import os.path as path
# Resource file export
# ResourceDir =  path.abspath(path.join(__file__ ,"../..")) # It doesn't work so far.
# ResourceDir = path.abspath(path.join(os.getcwd(),"../..")) # To go two directories,
# ResourceDir = path.abspath(path.join(os.getcwd(),"../"))    # To go one directory back.
ResourceDir = os.getcwd()
# https://stackoverflow.com/questions/27844088/python-get-directory-two-levels-up
# -----------------------------------------------------
# Installing packages -
# -----------------------------------------------------
# Exporting Direcotry : ResourceDir+ '/resources/
import bs4 as bs
import pickle
import requests
import datetime as dt
import os
import pandas as pd
import pandas_datareader as web
# -----------------------------------------------------
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

import numpy as np
import pickle
from collections import Counter


# Les get the data from the wikipedia from the link of all companies and search for a specific table
# You have to use the (Show inspection element of the html source file to know from where to start)

def save_sp500_tickers():
    resp    = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup    = bs.BeautifulSoup(resp.text,features="lxml") # Now you store the website .html file as a .txt file
    table   = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]: # tr: table row for your current table
        ticker = row.findAll('td')[0].text.replace('.','-') # getting the zero-column where the name of companies are.(column name: Ticker symbol), also as this is a soup object we convert it to a text.count
        # mapping = str.maketrans(".","-")
        # ticker = ticker.translate(mapping)
        mapping = str.maketrans(".","-")
        ticker = ticker.translate(mapping)

        ticker = ticker.rstrip()
        tickers.append(ticker)
    # Now we will save the file we created as an pickle object to not request from the website everytime
    with open(ResourceDir+"/resources/sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)

    print(tickers)
    return tickers

#save_sp500_tickers()

# -----------------------------------------------------
def get_data_from_yahoo(reload_sp500 = False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open(ResourceDir+"/resources/sp500tickers.pickle","rb") as f: # rb for read the file
            tickers = pickle.load(f)

    if not os.path.exists(ResourceDir+"/resources/stock_dfs/"): # Create a directory to export data to it.
        os.makedirs(ResourceDir+"/resources/stock_dfs/")

    start   = dt.datetime(2001,1,1)
    end     = dt.datetime(2016,12,31)
    #counter = 1

    non_valid_company = ["BDX","BBT","CF","COST","DOW","EVRG","EW","HIG", "COTY", "LIN", "OKE","JNJ","PNW","PPG","DGX","VMC","ZBH"]
    tickers_len = len(tickers)-1
    for index,ticker in enumerate(tickers):
        print(index,ticker)
        #print("\n")
        #os.system('clear')
        if ticker in non_valid_company:
            continue
        else:
            if not os.path.exists(ResourceDir+"/resources/stock_dfs/{}.csv".format(ticker)):
                #counter = counter+1
                df = web.DataReader(ticker, 'yahoo', start, end)
                df.to_csv(ResourceDir+"/resources/stock_dfs/{}.csv".format(ticker))
            else:
                print('Already have {}'.format(ticker))

        if index == tickers_len:
            print("All companies are finished")


#get_data_from_yahoo()

# -----------------------------------------------------
non_valid_company = ["BDX","BBT","CF","COST","DOW","EVRG","EW","HIG", "COTY", "LIN", "OKE","JNJ","PNW","PPG","DGX","VMC","ZBH"]
def compile_data():
    with open(ResourceDir+"/resources/sp500tickers.pickle","rb") as f:
        tickers = pickle.load(f)
        print(tickers)
        tickers = [item for item in tickers if item not in non_valid_company]
        #tickers = tickers.remove(non_valid_company)

    main_df = pd.DataFrame()

    for count,ticker in enumerate(tickers):
        df = pd.read_csv(ResourceDir+"/resources/stock_dfs/{}.csv".format(ticker))
        df.set_index('Date', inplace = True)

        df.rename(columns = {'Adj Close': ticker}, inplace = True) # changed the column name.
        df.drop(['Open', 'High', 'Low', 'Close','Volume'], axis= 1, inplace = True)


        if main_df.empty:
            main_df = df

        else:
            main_df = main_df.join(df, how = 'outer')

        if count % 10 == 0:
            print(count)

    print(main_df.head())
    main_df.to_csv(ResourceDir+"/resources/sp500_joined_closes.csv")


#compile_data()

# -----------------------------------------------------


def visualize_data():
    df = pd.read_csv(ResourceDir+"/resources/sp500_joined_closes.csv")
    # plt.plot(df['AAP']) # Or you can use df.plot['AAP'] # This is for Apple Company
    # plt.show()

    df_corr = df.corr()
    print(df_corr.head())

    data = df_corr.values
    fig = plt.figure()

    ax = fig.add_subplot(1,1,1)

    heatmap = ax.pcolor(data, cmap = "RdYlGn") # Before it was: plt.cm.RdYlGn

    fig.colorbar(heatmap)

    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor = False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor = False)

    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation = 90)

    heatmap.set_clim(-1,1)

    plt.tight_layout()
    plt.show()


# visualize_data()

# -----------------------------------------------------
# Starting with P.9 with Processing data for Machine Learning - Python Programming for Finance

def process_data_for_labels(ticker):
    hm_days = 7  # doese the price goes up or down
    df = pd.read_csv(ResourceDir+"/resources/sp500_joined_closes.csv", index_col= 0)
    tickers = df.columns.values.tolist()
    # print(tickers)
    df.fillna(0,inplace = True)

    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker,i)] = (df[ticker].shift(-i) - df[ticker])/ df[ticker]

    df.fillna(0, inplace = True)
    return tickers, df


# process_data_for_labels('XOM')


# -----------------------------------------------------
# A binary selection P.10

def buy_sell_hold(*args):       # passing any number of args to our function
    cols = [c for c in args]
    requirement  = 0.02
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1

    return 0


# -----------------------------------------------------
def extract_featuresets(ticker):

    tickers , df = process_data_for_labels(ticker)

    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,
                                        df['{}_1d'.format(ticker)],
                                        df['{}_2d'.format(ticker)],
                                        df['{}_3d'.format(ticker)],
                                        df['{}_4d'.format(ticker)],
                                        df['{}_5d'.format(ticker)],
                                        df['{}_6d'.format(ticker)],
                                        df['{}_7d'.format(ticker)]))

    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread:', Counter(str_vals))
    df.fillna(0, inplace = True)

    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace = True)

    df_vals = df[[ticker for ticker in tickers]].pct_change() # Got Normalized
    df_vals = df_vals.replace([np.inf, -np.inf], 0 )
    df_vals.fillna(0, inplace = True)

    X = df_vals.values
    y = df['{}_target'.format(ticker)].values

    return X, y, df



extract_featuresets('XOM')


