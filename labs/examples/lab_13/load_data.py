# and we will store the data in bigquery
import pandas_gbq
import pydata_google_auth
from google.oauth2 import service_account
import os
import json

import yfinance as yf # for downloading stock data

def get_price_data():
    dat = yf.Ticker("MSFT")
    msft_df = dat.history(period='1mo')
    return msft_df

def get_bq_credentials():
    # Load the data from BigQuery
    SCOPES = [
        'https://www.googleapis.com/auth/cloud-platform',
        'https://www.googleapis.com/auth/drive',
    ]

    # getting the credentials from the environment variable
    bq_credentials = os.environ.get('BQ_LAB13')
    bq_credentials = json.loads(bq_credentials)
    # as json file
    credentials = service_account.Credentials.from_service_account_info(
        bq_credentials,
        scopes=SCOPES
    )
    return credentials

def get_bq_data():
    
    # Load the data from BigQuery into a DataFrame
    query = "SELECT * FROM `stock_data.msft`"

    # getting the credentials
    credentials = get_bq_credentials()

    df = pandas_gbq.read_gbq(query, project_id='sipa-adv-c-roberto', credentials=credentials)
    
    return df

def update_data():
    # get the data from yfinance
    msft_df = get_price_data()
    # get the data from bigquery
    bq_df = get_bq_data()
    
    # comparing latest date from bq and msft_df
    bq_latest_date = bq_df['Date'].max()
    msft_latest_date = msft_df.index.max()
    # if the latest date from msft_df is greater than bq_latest_date, we add new data to bq
    if msft_latest_date > bq_latest_date:
        # get the new data from msft_df
        new_data = msft_df[msft_df.index > bq_latest_date]
        # add the new data to bq
        pandas_gbq.to_gbq(new_data, 'stock_data.msft', project_id='sipa-adv-c-roberto', if_exists='append')
        print("Data updated")
    else:
        print("No new data")

if __name__ == "__main__":
    # update the data
    update_data()