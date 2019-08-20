"""
    Machine learning with finance - Pattern Recognition for
        Algorithmic Forex and Stock Trading: Quick look at our Data: Machine learning for Stocks and Forex Technical Analysis
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

#print(os.getcwd())
"/Desktop/My_DATA_MP/Learning/04_PythonforFinance"
CURRENT_PATH  = os.getcwd()
DATA_LOCATION = os.path.join(CURRENT_PATH,"M01_Machine_learning_pattern_recognition_algorithms/GBPUSD" )

#print(DATA_LOCATION)

def convert_date(date_bytes):
    return mdates.strpdate2num('%Y%m%d%H%M%S')(date_bytes.decode('ascii'))  # strpdate2num ,datestr2num


def graphRaxFx():

    ''' Getting the dataset from our current file
        [Note] Possible output (The strpdate2num class was deprecated in Matplotlib 3.1 and will be removed in 3.3. Use time.strptime or dateutil.parser.parse or datestr2num instead.)
    '''
    date,bid,ask = np.loadtxt(os.path.join(DATA_LOCATION,"GBPUSD1d.txt"),
                                                          unpack= True,
                                                          delimiter= ',',
                                                          converters={0:convert_date})
    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan= 40, colspan = 40)

    ax1.plot(date,bid)
    ax1.plot(date,ask)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    plt.grid(True)
    plt.show()


class session_info():
    from datetime import date
    from datetime import datetime
    T0 = datetime.now()

    def __init__(self, your_string):
        self.your_string = your_string
        self.len_string  = len(your_string)
        self.len_string_adding = len("Today's date:"+str(session_info.T0))

    def Initial_run(self):

        self.len_string = len(self.your_string)
        print(self.len_string*"=")
        print(self.your_string)
        print(self.len_string*"=")
        print(self.len_string_adding*"-")
        print("Today's date:", session_info.T0.strftime("%d/%m/%Y %H:%M:%S"))
        print(self.len_string_adding*"-")


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



if __name__ == "__main__":
    output1 = session_info("Quick look at our Data: Machine learning for Stocks and Forex Technical Analysis")
    output1.Initial_run()
    graphRaxFx()
    output1.Finishing_run()



