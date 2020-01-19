# Fitbit-Data-Analyser

Analyses data obtained from a Fitbit Charge 2.

## Installation

Clone the source directory, then:

```bash
cd Fitbit-Data-Analyser
pipenv install --sequential
```

## Usage

1. Create a folder in the home directory named Data. In here, place all your Fitbit data
2. Run from main.py

## Obtaining Fitbit Data

1. Open https://dev.fitbit.com/apps/
2. Application "Getting Heart Rate Intraday"
3. Open OAuth 2.0 tutorial page in new tab
4. Click the generated URL
5. Copy the part after the # in the URL (access_token=xxxxxxxx)
6. Paste into "Parse response"
7. Copy token
8. Re-place expired token in HeartRatePuller.py

## Reference
https://dev.fitbit.com/build/reference/web-api/sleep-v1/