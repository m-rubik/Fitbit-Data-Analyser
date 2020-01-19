# -*- coding: utf-8 -*-
"""
Created on Fri May 25 14:24:47 2018

@author: Mason

Notes:
- To re-generate access token view HowTo.txt
- Fitbit limit 150 request per hour, so watch for this!
"""

import requests
import pandas as pd
import numpy as np
import json
import os
import re
import datetime
import statistics
import matplotlib.pyplot as plt
import operator

def getData(date,token):
    try:
        date = date.strftime('%Y-%m-%d')
        url = 'https://api.fitbit.com/1/user/-/activities/heart/date/' + date + '/1d/1sec/time/00:00/23:59.json'
        filename = 'HRdata' + date + '.json'
        info = requests.get(url=url, headers={'Authorization':'Bearer ' + token})
        data = info.json()

        # Uncomment to see raw data from request
        # print(r)

        filepath = './Data/' + filename

        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(filepath, 'w') as f:
            json.dump(data, f)
            print (date,'fetched and saved.')
    except Exception as e:
        print(e)

def writeToMaster():
    try:
        filepath = './Data/Master.txt'
        if os.path.exists(filepath):
            os.remove(filepath) 
        with open(filepath, 'w') as outfile:
            for file in os.listdir("./Data"):
                if file.endswith(".json"):
                    with open("./Data/"+file) as infile:
                        for line in infile:
                            outfile.write(line)
                    print(file,'copy to Master.txt complete.')
    except Exception as e:
        print(e)

def read_from_file(filename):
    try:
        filepath = './Data/'+filename
        if os.path.exists(filepath):
            text =''
            for line in open(filepath,"r", encoding='utf-8'):
                text += line
            print('Reading from',filename,'complete.')
            return text
        else:
            raise Exception("Path to file cannot be found.")
    except Exception as e:
        print(e)

if __name__ == '__main__':

    # access fitbit developper API access token
    token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkNUOFIiLCJzdWIiOiI2ODNTM04iLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNTgwMDYwNzM4LCJpYXQiOjE1Nzk0NTU5Mzh9.K5II2pzOXNiH5CsLb8lDRKv19Rl0UhuwiPuHBWHBPvQ&user_id=683S3N&scope=sleep+nutrition+activity+profile+social+location+settings+heartrate+weight&token_type=Bearer&expires_in=604800'
    
    start_date = '2018-01-06'
    end_date = '2018-01-11'
    dates = pd.date_range(start = pd.to_datetime(start_date), end = pd.to_datetime(end_date)).tolist()

    ## GET ALL DATA AND STORE ON A DAY-TO-DAY BASIS
    try:
        for date in dates:
            getData(date,token)
    except Exception as e:
        print(e)

    ## CREATE MASTER JSON FILE
    writeToMaster()

    ## READ FROM A SPECIFIED FILE
    # masterText = read_from_file('HRdata2018-10-15.json')
    masterText = read_from_file('Master.txt')

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

    print('Data points to organize:',len(masterData))
    for data in masterData:
        value = timeDict.get(data[1])
        value.append(int(data[4]))
    print('Data points organized.')
    

    for time, values in timeDict.items():
        if values:
            dataDict[time]=statistics.mean(values)
    
    sortedDataDict = sorted(dataDict.items(), key=operator.itemgetter(0))
    x, y = zip(*sortedDataDict)

    plt.figure(1) 
    plt.plot(y,'r')
    plt.title("Average daily BPM", fontsize=18)

    locs, labels = plt.xticks()           # Get locations and labels
    #plt.xticks(np.arange(0,len(timeList)),timeList, rotation=90)  # Set locations and labels

    ax = plt.gca()
    ax.set_xlabel('Time (seconds)', fontsize=18)
    ax.set_ylabel('BPM', fontsize=18)

    plt.show()



    
