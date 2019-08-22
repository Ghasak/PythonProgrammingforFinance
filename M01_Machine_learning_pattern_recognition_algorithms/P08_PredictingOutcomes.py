"""
    Machine learning with finance - Pattern Recognition for
        Algorithmic Forex and Stock Trading: Finding Patterns: Pattern Finding and Storing:
"""
messagex = "Predicting outcomes with Pattern Recognition: Machine Learning for Algorithmic Trading p. 8"

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

# Loading my tools that I created:
print(os.getcwd())
#sys.path.append('/Users/ghasak/Desktop/My_DATA_MP/Learning/04_PythonforFinance/')
sys.path.append(os.getcwd()+"/")
#/Users/ghasak/Desktop/My_DATA_MP/Learning/04_PythonforFinance/GTools/NiceOutPutClass.py
from GTools.NiceOutPutClass import session_info


#print(os.getcwd())
#"/Desktop/My_DATA_MP/Learning/04_PythonforFinance"
CURRENT_PATH  = os.getcwd()
DATA_LOCATION = os.path.join(CURRENT_PATH,"M01_Machine_learning_pattern_recognition_algorithms/GBPUSD" )

# Put the data in global location
def convert_date(date_bytes):
    return mdates.strpdate2num('%Y%m%d%H%M%S')(date_bytes.decode('ascii'))  # strpdate2num ,datestr2num

date,bid,ask = np.loadtxt(os.path.join(DATA_LOCATION,"GBPUSD1d.txt"),
                                                          unpack= True,
                                                          delimiter= ',',
                                                          converters={0:convert_date})

# Adding a global variable
avgLine = ((bid + ask) /2)

# Starting Part -6
patternAr     = []
performanceAr = []
patForRec = []

# def percentChange(startPoint, currentPoint):
#     # Import either the division or using float such as (float()) this part of python
#     return ((float(currentPoint)-startPoint)/abs(startPoint))*100

#@Antonio Constandinou @Luis Teixeira Antonio, I am sorry for the delay! Next time poke at me some more!- Comments from Sentdex.Both of you should try changing your percent change function to:
def percentChange(startPoint,currentPoint):
    try:
        x = ((float(currentPoint)-startPoint)/abs(startPoint))*100.00
        if x == 0.0:
            return 0.000000001
        else:
            return x
    except:
        return 0.0001


def patternStorage():
    patStartTime = time.time()

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


def currentPattern():
    cp1  = percentChange(avgLine[-11], avgLine[-10])
    cp2  = percentChange(avgLine[-11], avgLine[-9])
    cp3  = percentChange(avgLine[-11], avgLine[-8])
    cp4  = percentChange(avgLine[-11], avgLine[-7])
    cp5  = percentChange(avgLine[-11], avgLine[-6])
    cp6  = percentChange(avgLine[-11], avgLine[-5])
    cp7  = percentChange(avgLine[-11], avgLine[-4])
    cp8  = percentChange(avgLine[-11], avgLine[-3])
    cp9  = percentChange(avgLine[-11], avgLine[-2])
    cp10 = percentChange(avgLine[-11], avgLine[-1])

    patForRec.append(cp1)
    patForRec.append(cp2)
    patForRec.append(cp3)
    patForRec.append(cp4)
    patForRec.append(cp5)
    patForRec.append(cp6)
    patForRec.append(cp7)
    patForRec.append(cp8)
    patForRec.append(cp9)
    patForRec.append(cp10)

    #print(patForRec)


# Starting with Part 7

def patternRecognition():

    for eachPattern in patternAr:
        sim1  = 100.00 - abs(percentChange(eachPattern[0], patForRec[0]))
        sim2  = 100.00 - abs(percentChange(eachPattern[1], patForRec[1]))
        sim3  = 100.00 - abs(percentChange(eachPattern[2], patForRec[2]))
        sim4  = 100.00 - abs(percentChange(eachPattern[3], patForRec[3]))
        sim5  = 100.00 - abs(percentChange(eachPattern[4], patForRec[4]))
        sim6  = 100.00 - abs(percentChange(eachPattern[5], patForRec[5]))
        sim7  = 100.00 - abs(percentChange(eachPattern[6], patForRec[6]))
        sim8  = 100.00 - abs(percentChange(eachPattern[7], patForRec[7]))
        sim9  = 100.00 - abs(percentChange(eachPattern[8], patForRec[8]))
        sim10 = 100.00 - abs(percentChange(eachPattern[9], patForRec[9]))

        print(sim1, sim2,sim3,sim4)
        howSim = (sim1+sim2+sim3+sim4+sim5+sim6+sim7+sim8+sim9+sim10)/100.00

        if howSim > 99:
            patdex = patternAr.index(eachPattern)

            print(50 * "#")
            print(50 * "#")
            print(patForRec)
            print(50 * "=")
            print(50 * "=")
            print(eachPattern)
            print(50 * "-")
            print(f"Predicted outcome = {performanceAr[patdex]}")
            print(50 * "#")
            print(50 * "#")


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




# Individual method to see the dataset column distributed without pandas
def See_the_dataset():
    Table = (date,bid,ask) # converted to a tuple
    for index in range(len(Table[0][:])):
        print(Table[0][index],"\t",Table[1][index],"\t",Table[2][index])


# Starting point for our Python Script
if __name__ == "__main__":
    output1 = session_info(messagex)
    output1.Initial_run()
    #output1.add_line()
    #graphRaxFx()
    #patternFinder()
    totalStart = time.time()
    patternStorage()
    currentPattern()
    patternRecognition()
    totalTime = time.time()-totalStart
    print(f"Entir processing time took: {totalTime} second")
    output1.Finishing_run()

