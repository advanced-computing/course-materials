# run with:
#
#   streamlit run examples/bigquery/query.py

import pandas_gbq
import streamlit as st
from google.oauth2 import service_account

# https://docs.streamlit.io/develop/tutorials/databases/bigquery
creds = st.secrets["gcp_service_account"]
credentials = service_account.Credentials.from_service_account_info(creds)

sql = """
SELECT *
FROM `bigquery-public-data.cfpb_complaints.complaint_database`
LIMIT 10
"""

df = pandas_gbq.read_gbq(sql, credentials=credentials)

st.markdown("# Data from BigQuery")

df
