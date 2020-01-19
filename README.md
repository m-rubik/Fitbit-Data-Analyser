# Fitbit-Data-Analyser

Analyses data obtained from a Fitbit Charge 2.

## Installation

Clone the source directory, then:

```bash
cd Fitbit-Data-Analyser
pipenv install --sequential
```

## Usage

### Getting a Fitbit API Token

To do this, you must have made a Fitbit dev account and have created your own app
Check this out: http://shishu.info/2016/06/how-to-download-your-fitbit-second-level-data-without-coding/

1. Open https://dev.fitbit.com/apps/
2. Application "Getting Heart Rate Intraday"
3. Open OAuth 2.0 tutorial page in new tab
4. Click the generated URL
5. Copy the part after the # in the URL (access_token=xxxxxxxx)
6. Paste into "Parse response"
7. Copy token
8. Paste token in main.py (Replacing the old expired token)

### Getting data from Fitbit API

In main.py:
1. enter a date range
2. uncomment the section on querying the fitbit API
3. Run main.py

### Analysing Data

In main.py
1. Comment-out the section on querying the fitbit API
2. Make calls to whatever analyse functions you want


## Reference
https://dev.fitbit.com/build/reference/web-api/sleep-v1/

