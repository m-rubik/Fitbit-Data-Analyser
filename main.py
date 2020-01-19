"""!
main.py
"""

import pandas as pd
from src.analysers import sleep_analyser, heart_rate_analyser
from src.utilities.utilities import write_to_master, read_from_file
from src.utilities.puller import get_fitbit_data

if __name__ == "__main__":
   # access fitbit developper API access token
    token = read_from_file("token.txt")
    print(token)
    
    start_date = '2018-10-10'
    end_date = '2018-12-31'
    dates = pd.date_range(start = pd.to_datetime(start_date), end = pd.to_datetime(end_date)).tolist()

    # Query data from the Fitbit API
    # try:
    #     for date in dates:
    #         get_fitbit_data(date,token,"HR")
    # except Exception as e:
    #     print(e)
    # write_to_master("HR")

    sleep_analyser.analyse_sleep_data()
    heart_rate_analyser.analyse_heart_rate()

