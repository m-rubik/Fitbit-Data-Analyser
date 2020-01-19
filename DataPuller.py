import requests
import os
import json
import pandas as pd

def getDateData(date,token,dataCategory):
    try:
        date = date.strftime('%Y-%m-%d')
        url = 'https://api.fitbit.com/1/user/-/activities/heart/date/' + date + '/1d/1sec/time/00:00/23:59.json'
        filename = 'HRdata' + date + '.json'
        info = requests.get(url=url, headers={'Authorization':'Bearer ' + token})
        data = info.json()

        # Uncomment to see raw data from request
        # print(r)

        filepath = './Data/'+dataCategory+'/' + filename

        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(filepath, 'w') as f:
            json.dump(data, f)
            print (date,'fetched and saved.')
    except Exception as e:
        print(e)

def writeToMaster(dataCategory):
    try:
        filepath = './Data/'+dataCategory+'/Master.txt'
        if os.path.exists(filepath):
            os.remove(filepath) 
        with open(filepath, 'w') as outfile:
            for file in os.listdir("./Data"+dataCategory):
                if file.endswith(".json"):
                    with open("./Data/"+dataCategory+"/"+file) as infile:
                        for line in infile:
                            outfile.write(line)
                    print(file,'copy to Master.txt complete.')
    except Exception as e:
        print(e)

def getData(token,start_date,end_date,dataCategory):
    # access fitbit developper API access token
    token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkNUOFIiLCJzdWIiOiI2ODNTM04iLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNTQ4NDczMjU2LCJpYXQiOjE1NDc4Njg0NTZ9.bM7RtwsZl0veBJN4EMcWjs1_uEfR6fT9enWmsuQwVV8'

    start_date = '2018-01-06'
    end_date = '2018-01-11'
    dates = pd.date_range(start = pd.to_datetime(start_date), end = pd.to_datetime(end_date)).tolist()

    ## GET ALL DATA AND STORE ON A DAY-TO-DAY BASIS
    try:
        for date in dates:
            getDateData(date,token,dataCategory)
    except Exception as e:
        print(e)

    ## CREATE MASTER JSON FILE
    writeToMaster(dataCategory)