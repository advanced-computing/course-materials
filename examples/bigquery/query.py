# https://pandas-gbq.readthedocs.io/en/latest/howto/authentication.html#authenticating-with-a-user-account

import pandas_gbq

from google.oauth2 import service_account
import json

SCOPES = [
    "https://www.googleapis.com/auth/cloud-platform",
]

with open("sipa-adv-c-aidan-demo-3b12-77031d991edd.json") as f:
    creds = json.load(f)

credentials = service_account.Credentials.from_service_account_info(creds)

df = pandas_gbq.read_gbq(
    "SELECT * FROM `bigquery-public-data.cfpb_complaints.complaint_database` LIMIT 10",
    project_id=creds["project_id"],
    credentials=credentials,
)

print(df)
