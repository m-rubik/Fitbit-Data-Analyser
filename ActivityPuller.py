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

def getData(date,token):
    try:
        date = date.strftime('%Y-%m-%d')
        url = 'https://api.fitbit.com/1/user/-/activities/date/' + date + '.json'
        filename = 'ActivityData' + date + '.json'
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
    token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkNUOFIiLCJzdWIiOiI2ODNTM04iLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNTQ4NDczMjU2LCJpYXQiOjE1NDc4Njg0NTZ9.bM7RtwsZl0veBJN4EMcWjs1_uEfR6fT9enWmsuQwVV8'
    
    start_date = '2018-11-07'
    end_date = '2018-12-31'
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
    # masterText = readFromFile('HRdata2018-10-15.json')
    masterText = readFromFile('Master.txt')

    basicInfoCheck = re.compile(r"{\"(activity).*?(total).*?(distance)\": ([0-9]+.[0-9]+).*?(elevation)\": ([0-9]+.[0-9]+).*?(floors)\": ([0-9]+).*?(restingHeartRate)\": ([0-9]+).*?(sedentaryMinutes)\": ([0-9]+).*?(steps)\": ([0-9]+)",re.MULTILINE)
    basicInfo = basicInfoCheck.findall(masterText)

    print(0)
