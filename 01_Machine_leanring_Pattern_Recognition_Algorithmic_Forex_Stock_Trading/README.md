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
