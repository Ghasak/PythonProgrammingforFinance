"""
    Machine learning with finance - Pattern Recognition for
        Algorithmic Forex and Stock Trading: Finding Patterns: Pattern Finding and Storing:
"""
message = "Pattern Finding and Storing: Machine Learning for Algorithmic Trading in Forex and Stocks Part 6"

import os
import sys
import time
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates  as mdates
from functools import reduce # This one for the reduce function.

#print(os.getcwd())
"/Desktop/My_DATA_MP/Learning/04_PythonforFinance"
CURRENT_PATH  = os.getcwd()
DATA_LOCATION = os.path.join(CURRENT_PATH,"M01_Machine_learning_pattern_recognition_algorithms/GBPUSD" )

# Put the data in global location
def convert_date(date_bytes):
    return mdates.strpdate2num('%Y%m%d%H%M%S')(date_bytes.decode('ascii'))  # strpdate2num ,datestr2num

date,bid,ask = np.loadtxt(os.path.join(DATA_LOCATION,"GBPUSD1d.txt"),
                                                          unpack= True,
                                                          delimiter= ',',
                                                          converters={0:convert_date})

# Starting Part -6
patternAr     = []
performanceAr = []





def percentChange(startPoint, currentPoint):
    # Import either the division or using float such as (float()) this part of python
    return ((float(currentPoint)-startPoint)/abs(startPoint))*100



def patternStorage():
    patStartTime = time.time()
    avgLine = ((bid + ask) /2)
    x = len(avgLine) - 30 # it will stop at the 30th

    y = 11 # starting point, ignore the first point
    while y < x:
        pattern = []
        # for every point along the way, the starting point stay the same
        p1  = percentChange(avgLine[y-10],avgLine[y-9])
        # We will chaneg only the end time
        p2  = percentChange(avgLine[y-10],avgLine[y-8])
        p3  = percentChange(avgLine[y-10],avgLine[y-7])
        p4  = percentChange(avgLine[y-10],avgLine[y-6])
        p5  = percentChange(avgLine[y-10],avgLine[y-5])
        p6  = percentChange(avgLine[y-10],avgLine[y-4])
        p7  = percentChange(avgLine[y-10],avgLine[y-3])
        p8  = percentChange(avgLine[y-10],avgLine[y-2])
        p9  = percentChange(avgLine[y-10],avgLine[y-1])
        p10 = percentChange(avgLine[y-10],avgLine[y-0])

        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]

        try:
            averageOutcome  = reduce(lambda x , y : x+y, outcomeRange)/len(outcomeRange)
        except Exception as e:
            print(str(e))
            averageOutcome = 0

        futureOutcome = percentChange(currentPoint, averageOutcome)

        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)

        # Now we will add our global arrays
        patternAr.append(pattern)
        performanceAr.append(futureOutcome)
        y += 1
        print(f"Iteration No.{y}")
    patEndTime = time.time()
    print(f"The length of patternAr     = {len(patternAr)}")
    print(f"The length of performanceAr = {len(performanceAr)}")
    print(f"Pattern storage took:{patEndTime-patStartTime} second")



def graphRaxFx():

    ''' Getting the dataset from our current file
        [Note] Possible output (The strpdate2num class was deprecated in Matplotlib 3.1 and will be removed in 3.3. Use time.strptime or dateutil.parser.parse or datestr2num instead.)
    '''

    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan= 40, colspan = 40)
    ax1.plot(date,bid)
    ax1.plot(date,ask)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(30)
    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask - bid), facecolor = 'g', alpha = 0.3)
    plt.subplots_adjust(bottom= 0.23)
    plt.grid(True)
    plt.show()














class session_info():
    ''' - This class is used just to organize our output'''
    # Class variables
    from datetime import date
    from datetime import datetime
    T0 = datetime.now()

    # Constructor
    def __init__(self, your_string):
        self.your_string = your_string
        self.len_string  = len(your_string)
        self.len_string_adding = len("Today's date:"+str(session_info.T0))
    # This method for showing starting running - time
    def Initial_run(self):

        self.len_string = len(self.your_string)
        print(self.len_string*"=")
        print(self.your_string)
        print(self.len_string*"=")
        print(self.len_string_adding*"-")
        print("Today's date:", session_info.T0.strftime("%d/%m/%Y %H:%M:%S"))
        print(self.len_string_adding*"-")

    # This method for showing finishing running - time
    def Finishing_run(self):
        from datetime import datetime
        Tx = datetime.now() #date.today()

        TPassed = Tx - session_info.T0
        print(self.len_string*"=")
        print(self.your_string)
        print(self.len_string*"=")
        print("Starting  time at = {}".format(self.T0.strftime("%d/%m/%Y %H:%M:%S")))
        print("Executing time at = {}".format(Tx.strftime("%d/%m/%Y %H:%M:%S")))
        print(f"[Done] exited with code = 0 in {TPassed} seconds")

# Individual method to see the dataset column distributed without pandas
def See_the_dataset():
    Table = (date,bid,ask) # converted to a tuple
    for index in range(len(Table[0][:])):
        print(Table[0][index],"\t",Table[1][index],"\t",Table[2][index])


# Starting point for our Python Script
if __name__ == "__main__":
    output1 = session_info(message)
    output1.Initial_run()
    #graphRaxFx()
    #patternFinder()
    patternStorage()
    output1.Finishing_run()



