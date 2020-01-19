# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20:08:51 2019

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

from plotPAA import plotPAA
from plotSST import plotSST
from plotCycles import plotCycles

def getData(date,token):
    try:
        date = date.strftime('%Y-%m-%d')
        url = 'https://api.fitbit.com/1/user/-/sleep/date/' + date + '.json'
        filename = 'Sleepdata' + date + '.json'
        info = requests.get(url=url, headers={'Authorization':'Bearer ' + token})
        data = info.json()

        # Uncomment to see raw data from request
        # print(data)

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

def readFromFile(filename):
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
    token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkNUOFIiLCJzdWIiOiI2ODNTM04iLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyaHIgcnNsZSIsImV4cCI6MTU0NzI2MDMwMywiaWF0IjoxNTQ2NjU1NTAzfQ.ylGS1Lae259Bk2wzgNfn_hUYAdM9AtkD8cQWyoNOwks'
    
    start_date = '2018-10-10'
    end_date = '2018-12-31'
    dates = pd.date_range(start = pd.to_datetime(start_date), end = pd.to_datetime(end_date)).tolist()

    ## GET ALL DATA AND STORE ON A DAY-TO-DAY BASIS
    # try:
    #     for date in dates:
    #         getData(date,token)
    # except Exception as e:
    #     print(e)

    ## CREATE MASTER JSON FILE
    # writeToMaster()

    ## READ FROM A SPECIFIED FILE
    # masterText = readFromFile('HRdata2018-10-15.json')
    masterText = readFromFile('Master.txt')

    basicInfoCheck = re.compile(r"(\"awakeningsCount\").*?([0-9]+).*?(\"duration\").*?([0-9]+).*?(\"efficiency\").*?([0-9]+).*?(\"endTime\").*?([0-9]+-[0-9]+-[0-9]+[A-z]{1})([0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]+).*?(\"isMainSleep\").*?([A-z]{4,5})",re.MULTILINE)
    basicInfo = basicInfoCheck.findall(masterText)

    cycleInfoCheck = re.compile(r"(\"timeInBed\").*?([0-9]+).*?(\"deep\").*?([0-9]+).*?(\"light\").*?([0-9]+).*?(\"rem\").*?([0-9]+).*?(\"wake\").*?([0-9]+).*?(\"totalMinutesAsleep\").*?([0-9]+)",re.MULTILINE)
    cycleInfo = cycleInfoCheck.findall(masterText)

    startInfoCheck = re.compile(r"(\"startTime\").*?([0-9]+-[0-9]+-[0-9]+[A-z]{1})([0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]+).*?(\"totalSleepRecords\").*?([0-9]{1})",re.MULTILINE)
    startInfo = startInfoCheck.findall(masterText)

    ## IDK, figure this shit out
    realbasicInfo = list()
    for basic in basicInfo:
        if basic[10] == 'true':
            realbasicInfo.append(basic)

    realstartInfo = list()
    for start in startInfo:
        if start[4] == '1':
            realstartInfo.append(basic)

    # plotSST(realbasicInfo,realstartInfo)

    ## FUTURE TO-DO???
    # sleepInfoCheck = re.compile(r"(\"dateTime\").*?([0-9]{2}:[0-9]{2}:[0-9]{2}).*?(\"value\").*?([1-3])",re.MULTILINE)
    # sleepInfo = sleepInfoCheck.findall(masterText)

    # plotPAA(cycleInfo)
    plotCycles(cycleInfo)

    print(0)
