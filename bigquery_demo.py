# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:03:38 2022

@author: mratna
"""

from dse_google_cloud_utils import auth
from google.cloud import bigquery

creds = auth.authenticate_oauth_console(
    scopes=[
        "https://www.googleapis.com/auth/bigquery",
        "https://www.googleapis.com/auth/cloud-platform"
    ],
    cache=True
)

client = bigquery.Client(project="ltl-prd-data-user", credentials=creds)

df = client.query("""
    SELECT COUNT(*) AS _COUNT
    FROM ltl-prd-datahub.ALL_LOOKER_VIEW.SCO_TRIP_NODE_ACTIVITY_RDS_VW
""").result().to_dataframe()

import pandas as pd
from pandas.io import gbq

query = "SELECT count(*) FROM `bigquery-public-data.bitcoin_blockchain.transactions`"
df_train = pd.read_gbq(project_id='luminous-bazaar-330807', query=query, dialect='standard')

import pandas as pd
#from pandas.io import gbq

query = "select count(distinct PSTL_CD)	 from `ltl-prd-datahub.ALL_DATAHUB_VIEW.GEO_POSTAL_CODE_RDS_VW`"
df_train = pd.read_gbq(project_id='ltl-prd-data-user', query=query, dialect='standard')