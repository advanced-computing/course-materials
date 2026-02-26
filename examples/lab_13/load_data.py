# and we will store the data in bigquery
import json
import os

import pandas_gbq  # type: ignore
import yfinance as yf  # type: ignore  # for downloading stock data
from google.oauth2 import service_account

PROJECT_ID = "sipa-advanced-computing"
TABLE = "stock_data.msft"


def get_price_data():
    dat = yf.Ticker("MSFT")
    msft_df = dat.history(period="1mo")
    return msft_df


def get_bq_credentials():
    # Load the data from BigQuery
    scopes = [
        "https://www.googleapis.com/auth/cloud-platform",
    ]

    # getting the credentials from the environment variable
    bq_credentials = os.environ["BQ_LAB13"]
    bq_credentials = json.loads(bq_credentials)
    # as json file
    credentials = service_account.Credentials.from_service_account_info(
        bq_credentials, scopes=scopes
    )
    return credentials


def get_bq_data():
    # Load the data from BigQuery into a DataFrame
    query = f"SELECT * FROM `{TABLE}`"

    # getting the credentials
    credentials = get_bq_credentials()

    df = pandas_gbq.read_gbq(query, project_id=PROJECT_ID, credentials=credentials)

    return df


def update_data():
    # get the data from yfinance
    msft_df = get_price_data()
    # get the data from bigquery
    bq_df = get_bq_data()

    # getting the credentials
    credentials = get_bq_credentials()

    # comparing latest date from bq and msft_df
    bq_latest_date = bq_df["Date"].max()
    msft_latest_date = msft_df.index.max()
    # if the latest date from msft_df is greater than bq_latest_date, we add new data to bq
    if msft_latest_date > bq_latest_date:
        # get the new data from msft_df
        new_data = msft_df[msft_df.index > bq_latest_date]
        # add the new data to bq
        pandas_gbq.to_gbq(
            new_data,
            TABLE,
            project_id=PROJECT_ID,
            if_exists="append",
            credentials=credentials,
        )
        print("Data updated")
    else:
        print("No new data")


if __name__ == "__main__":
    # update the data
    update_data()
