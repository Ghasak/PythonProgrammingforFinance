# MACHINE LEARNING WITH FINANCE:
Machine leanring with finance - pattern recognition for algorithmic Forex and Stock Trading
## P01- Intro
We will use the machine learning analysis and trading algorithm.
Our data is organized as:
First column is date which is formated as:

```py
ex: 2013 05 01 00 00 00
```

## P02- Quick look at the data
Adding the following function

```py
def convert_date(date_bytes):
    return mdates.strpdate2num('%Y%m%d%H%M%S')(date_bytes.decode('ascii'))  # strpdate2num ,datestr2num

```
Then Getting the data using

```py
def graphRaxFx():
    date,bid,ask = np.loadtxt(os.path.join(DATA_LOCATION,"GBPUSD1d.txt"),
                                                          unpack= True,
                                                          delimiter= ',',
                                                          converters={0:convert_date})
```
There is an deprecation with matplotlib library: as

```v
The strpdate2num class was deprecated in Matplotlib 3.1 and will be removed in 3.3
Use time.strptime or dateutil.parser.parse or datestr2num instead

```
More are here: https://www.reddit.com/r/learnpython/comments/3o2f36/following_sentdex_in_python_3/

## P03_ Machine Learning and Pattern Recognition for Stocks and Forex Part 3

This one we have tweaked the axises and added some other features on top of Part 4. Also I have added a function to see the data as:

```py

def See_the_dataset():
    date,bid,ask = np.loadtxt(os.path.join(DATA_LOCATION,"GBPUSD1d.txt"),
                                                          unpack= True,
                                                          delimiter= ',',
                                                          converters={0:convert_date})
    Table = (date,bid,ask) # converted to a tuple
    for index in range(len(Table[0][:])):
        print(Table[0][index],"\t",Table[1][index],"\t",Table[2][index])


```
## P04_ Percent Change: Machine Learning for Automated Trading in Forex and Stocks Part 4
Mainly an explanation on using the stock data and how to get the percentage of changing over open and closing price data. Added only the percentChange function.

## P05_ Finding Patterns: Machine Learning for Automated Trading in Forex and Stocks Part 5
There is a function called reduce which is basically works as following

```py
def do_sum(x1, x2): return x1 + x2

def my_reduce(func, seq):
     first = seq[0]
     for i in seq[1:]:
         first = func(first, i)
     return first


print(my_reduce(do_sum, [1, 2, 3, 4]))

```
The results are:

```v
10
```
if you use the one from python then you can do

```py
from functools import reduce
def do_sum(x1, x2):
    return x1 + x2

print(reduce(do_sum, [1, 2, 3, 4]))
```
* [HINT] read more here: https://www.python-course.eu/lambda.php
* or here: https://medium.com/better-programming/lambda-map-and-filter-in-python-4935f248593


