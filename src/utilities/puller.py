"""!
All functions required for obtaining Fitbit data through the API

Note: Fitbit has placed a limit of 150 requests per hour.
"""

import requests
import os
import json

def get_fitbit_data(date, token, category):
    date = date.strftime('%Y-%m-%d')
    if category == "HR":
        data_folder = "HR"
        url = 'https://api.fitbit.com/1/user/-/activities/heart/date/' + date + '/1d/1sec/time/00:00/23:59.json'
    elif category == "Sleep":
        data_folder = "Sleep"
        url = 'https://api.fitbit.com/1/user/-/sleep/date/' + date + '.json'
    elif category == "Activity":
        data_folder = "Activity"
        url = 'https://api.fitbit.com/1/user/-/activities/date/' + date + '.json'
    else:
        return 1
    try:
        filename = data_folder + "data" + date + '.json'
        info = requests.get(url=url, headers={'Authorization':'Bearer ' + token})
        data = info.json()

        filepath = './Data/' + data_folder + "/" + filename

        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(filepath, 'w') as f:
            json.dump(data, f)
            print(date,'fetched and saved.')
    except Exception as e:
        print(e)