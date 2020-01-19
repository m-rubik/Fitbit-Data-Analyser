from src.utilities.utilities import read_from_file
import statistics
import pandas as pd
import regex as re
import numpy as np
import matplotlib.pyplot as plt
import operator
from src.plot.plot_heart_rate import plot_average_BMP

def analyse_heart_rate():
        
    masterText = read_from_file('./Data/HR/Master.txt')

    masterCheck = re.compile(r"(\"time\": \")([0-9]+:[0-9]+:[0-9]+)(.*?)(\"value\": )([0-9]+)",re.MULTILINE)
    masterData = masterCheck.findall(masterText)

    times = pd.date_range("00:00", "23:59", freq="1S").time

    timeDict = {}
    dataDict = {}
    timeList = list()
    for ts in times:
        timeDict[ts.strftime('%H:%M:%S')] = list()
        dataDict[ts.strftime('%H:%M:%S')] = 0
        timeList.append(ts.strftime("%H:%M:%S"))

    print('HR data points to organize:',len(masterData))
    for data in masterData:
        value = timeDict.get(data[1])
        value.append(int(data[4]))
    print('HR data points organized.')
    
    for time, values in timeDict.items():
        if values:
            dataDict[time]=statistics.mean(values)
    
    sortedDataDict = sorted(dataDict.items(), key=operator.itemgetter(0))
    x, y = zip(*sortedDataDict)

    plot_average_BMP(x, y, timeList)

  