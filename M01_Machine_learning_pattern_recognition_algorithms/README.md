# MACHINE LEARNING WITH FINANCE:
Machine leanring with finance - pattern recognition for algorithmic Forex and Stock Trading

# Running from Ipython

```c
%run M01_Machine_learning_pattern_recognition_algorithms/P05_Finding_Patterns.py
```
# Running from VS-Code
Command + Shift + R, lunch the code . in the parent directory where you have the virtualenv directory.

# Running from Terminal
```c
python M01_Machine_learning_pattern_recognition_algorithms/P05_Finding_Patterns.py
```
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


## P06_Pattern Finding and Storing: Machine Learning for Algorithmic Trading in Forex and Stocks Part 6

We will save our work here and add more functionality. As we proceed, the value that we have expected in our current script shows pattern is a list of the ticks from 1 to 10 added to the global array.

```py
The length of patternAr     = 61971
The length of performanceAr = 61971
Pattern storage took:1.4507629871368408 second
================================================================================================
Pattern Finding and Storing: Machine Learning for Algorithmic Trading in Forex and Stocks Part 6
================================================================================================
Starting  time at = 21/08/2019 00:58:50
Executing time at = 21/08/2019 00:58:51
[Done] exited with code = 0 in 0:00:01.450952 seconds
```

## P07_Current Pattern: Machine Learning for Algorithmic Trading in Forex and Stocks
We will start the current pattern recognition.
we have added the function called patternRecognition thats all.

## P08_Predicting outcomes with Pattern Recognition: Machine Learning for Algorithmic Trading p. 8
Here we will add the following:
```py
# Correction to the percentChange function as

def percentChange(startPoint,currentPoint):
    try:
        x = ((float(currentPoint)-startPoint)/abs(startPoint))*100.00
        if x == 0.0:
            return 0.000000001
        else:
            return x
    except:
        return 0.0001
```

