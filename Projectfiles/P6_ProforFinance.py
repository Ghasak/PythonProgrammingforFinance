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

save_sp500_tickers()

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

    non_valid_company = ["BDX","BBT","CF","COST","DOW","EVRG","HIG"]
    for ticker in tickers:
        print(ticker)
        if ticker in non_valid_company:
            continue
        else:
            if not os.path.exists(ResourceDir+"/resources/stock_dfs/{}.csv".format(ticker)):
                df = web.DataReader(ticker.replace('.','-'), 'yahoo', start, end)
                df.to_csv(ResourceDir+"/resources/stock_dfs/{}.csv".format(ticker))
            else:
                print('Already have {}'.format(ticker))


get_data_from_yahoo()

