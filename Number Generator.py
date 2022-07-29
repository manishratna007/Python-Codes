# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:52:46 2022

@author: mratna
"""
#Import Libraries
import pandas as pd
import numpy as np
import random
from random import shuffle

df=pd.read_excel(r'C:\Users\mratna\Downloads\HP_Telco_Code.xlsx',sheet_name="Sheet1")

df['Min Num'].head
df['Max Num'].head
len(df['Min Num'])
len(df['Max Num'])

df['Min Num'][0]

sample=range(df['Min Num'][0],df['Max Num'][0])

sample_df=pd.DataFrame(range(df['Min Num'][0],df['Max Num'][0]),columns=['Mobile'])
len(sample)
sample_df.head
type(sample)

final_df=pd.DataFrame([])

for i in range(1001,2000):
    sample=pd.DataFrame(range(df['Min Num'][i],df['Max Num'][i]),columns=['Mobile'])
    final_df=final_df.append(sample)
    print(sample)
    
final_df.head
len(final_df)

final_df1=final_df['Mobile'].append(df['Max Num'])

final_df.head
len(final_df)

final_unique=final_df.drop_duplicates()
len(final_unique)

final_unique_random= final_unique.sample(frac=1).reset_index(drop=True)
len(final_unique_random)

final_unique_random.to_csv(r'C:\Users\mratna\Downloads\HP_2.csv')

print(9999901+19999802)

for i in range(19999802,89899101,950000): #25400888,
    #print(i)
    df1 = final_unique_random.iloc[i:i+950000]
    df1.to_csv('HP_Set-4_numbers'+str(i)+'.csv',index=False)
    

import os
os.getcwd() 
os.chdir(r'C:\Users\mratna\Downloads\split_csv_pandas')
