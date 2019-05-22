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

# Les get the data from the wikipedia from the link of all companies and search for a specific table
# You have to use the (Show inspection element of the html source file to know from where to start)

def save_sp500_tickers():
    resp    = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup    = bs.BeautifulSoup(resp.text,features="lxml") # Now you store the website .html file as a .txt file
    table   = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]: # tr: table row for your current table
        ticker = row.findAll('td')[0].text # getting the zero-column where the name of companies are.(colum name: Ticker symbol), also as this is a soup object we convert it to a text.count
        tickers.append(ticker)
    # Now we will save the file we created as an pickle object to not request from the website everytime
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)

    print(tickers)
    return tickers

save_sp500_tickers()

