"""!
main.py
"""

import pandas as pd
from src.analysers.sleep_analyser import analyse_sleep_data
from src.utilities.utilities import write_to_master
from src.utilities.puller import get_fitbit_data

if __name__ == "__main__":
   # access fitbit developper API access token
    token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkNUOFIiLCJzdWIiOiI2ODNTM04iLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNTgwMDYwNzM4LCJpYXQiOjE1Nzk0NTc2Mzl9.VJ3koawBSoWLVVjxPN6IzxSlNzbVZvv6KrNuePQSBxI'
    
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

    analyse_sleep_data()

