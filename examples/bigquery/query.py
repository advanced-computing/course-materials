# https://pandas-gbq.readthedocs.io/en/latest/howto/authentication.html#authenticating-with-a-user-account

import pandas_gbq

from google.oauth2 import service_account
import streamlit as st


# https://docs.streamlit.io/develop/tutorials/databases/bigquery
creds = st.secrets["gcp_service_account"]
credentials = service_account.Credentials.from_service_account_info(creds)

df = pandas_gbq.read_gbq(
    "SELECT * FROM `bigquery-public-data.cfpb_complaints.complaint_database` LIMIT 10",
    project_id=creds["project_id"],
    credentials=credentials,
)

print(df)
