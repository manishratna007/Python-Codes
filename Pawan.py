# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:41:39 2022

@author: mratna
"""
import pandas as pd
import os

os.chdir(r'C:\Users\mratna\Downloads\PAWAN')

df17 = pd.read_csv('Last 5 days\feedback-log-punjab2br-all-2022-02-17-1404.csv')

df17_party_list=df17['will_vote_for'].unique()
df17_party_list['count']=df17.groupby(['will_vote_for']).size()

df17_party=[]
df17_party['will_vote_for']=pd.DataFrame(df17.groupby(['will_vote_for']).size())
df17_party['Vote_sum']=df17_party.groupby(['will_vote_for']).sum()

df17_party.dtypes
df17_party.head()

punjab_codes=pd.read_excel(r'punjabCodes.xlsx', sheet_name = 'Sheet1')

punjab_codes.head()

party_code=punjab_codes.iloc[0:12,0:2]

