# Intro and Getting Stock Price Data
## - Python Programming for Finance p.1
Hello and welcome to a Python for Finance tutorial series. In this series, we're going to run through the basics of importing financial (stock) data into Python using the Pandas framework. From here, we'll manipulate the data and attempt to come up with some sort of system for investing in companies, apply some machine learning, even some deep learning, and then learn how to back-test a strategy. I assume you know the fundamentals of Python. If you're not sure if that's you, click the fundamentals link, look at some of the topics in the series, and make a judgement call. If at any point you are stuck in this series or confused on a topic or concept, feel free to ask for help and I will do my best to help.

A common question that I am asked is whether or not I make a profit investing or trading with these techniques. I mostly play with finance data for fun and to practice my data analysis skills, but it actually does also influence my investment decisions to this day. I do not do active algorithmic trading with programming at the time of my writing this, but I have, and I have actually made a profit, but it's a lot more work than you might think to algorithmically trade. Finally, the knowledge about how to manipulate and analyze financial data, as well as how to backtest trading stategies, has *saved* me a ton of money.

None of the strategies presented here will make you an ultra wealthy person. If they would, I'd probably keep them to myself! The knowledge itself, however, can save you money, and even make you money.

Alright great, let's get started. To begin, I am using Python 3.5, but you should be able to get by with later versions. I will assume you already have Python installed. If you do not have 64 bit Python, but do have a 64bit operating system, get 64 bit Python, it'll help you a bit later. If you're on a 32 bit operating system, I am sorry for your situation, but you should be fine to follow most of this anyway.

Required Modules to start:
```
Numpy
Matplotlib
Pandas
Pandas-datareader
BeautifulSoup4
scikit-learn / sklearn
```
# My Note
explain about the adj Close is for splitting the share of stocks for a company when they have so high price.
* DateReader from pandas is used to read from the website a dataframe that we will use in our analysis
* You can also use (** ipython**) similar to Juypter NoteBook to read data and work interactively.

# Inspiration

https://pythonprogramming.net/getting-stock-prices-python-programming-for-finance/
