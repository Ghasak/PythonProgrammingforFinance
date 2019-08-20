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

