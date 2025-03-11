# https://pandas-gbq.readthedocs.io/en/latest/howto/authentication.html#authenticating-with-a-user-account

import pandas_gbq

from google.oauth2 import service_account
import streamlit as st


# https://docs.streamlit.io/develop/tutorials/databases/bigquery
creds = st.secrets["gcp_service_account"]
credentials = service_account.Credentials.from_service_account_info(creds)

sql = """
SELECT *
FROM `bigquery-public-data.cfpb_complaints.complaint_database`
LIMIT 10
"""

df = pandas_gbq.read_gbq(sql, credentials=credentials)

print(df)
