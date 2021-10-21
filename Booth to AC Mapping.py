# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:35:21 2021

@author: manis
"""
import pandas as pd
import numpy as np

vill=pd.read_excel(r'C:\Users\ipac\Downloads\Booth to AC Mapping\Booth to AC Mapping\Dist_Village_GP_Mapping_AC_07092021_v1.xlsx')
booth=pd.read_excel(r'C:\Users\ipac\Downloads\Booth to AC Mapping\Booth to AC Mapping\GA 2017AE PS Mapping.xlsx')

vill.head
booth.head
vill.describe

len(vill)
len(booth)

#booth['PS Name'] = booth['PS Name'].str.replace('Govt.', '')

##Find most frequent words which needs to be replaced
booth['value']=1
sentence=booth.groupby('value')['PS Name'].apply(' '.join).reset_index()
sentence.to_csv(r'C:\Users\ipac\Downloads\Booth to AC Mapping\Booth to AC Mapping\sentence.csv')
len(sentence)
sentence['PS Name'].str.count(' ')
row=sentence['PS Name'].str.split(" ",expand=True).T
row.replace('', np.nan, inplace=True)
row.dropna(inplace=True)
row.columns=['words_v1']
row_freq=row['words_v1'].value_counts()
row[0]
row_freq.to_csv(r'C:\Users\ipac\Downloads\Booth to AC Mapping\Booth to AC Mapping\row.csv')

#Remove in-appropriate and most frequent words after inspection
booth['PS Name'] = booth['PS Name'].str.replace('Institute', '')

#Use of fuzzy lookup to find the similar words
import fuzzywuzzy
#from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#Find 
choices=vill['AC No'].astype(str)+'_'+vill['Village Name']
word=booth['AC No'].astype(str)+'_'+booth['PS Name']

word[0]
#words=word[0:20,]
villagename=[]
ratio=[]
parameter=[]
#type(similar)
for i in word:
    sim=process.extract(i, choices, limit=1)
    villagename.append((sim[0][0]))
    ratio.append((sim[0][1]))
    parameter.append((sim[0][2]))
    #print(sim)

#len(similar)


booth['village']=villagename
booth['ratio']=ratio
booth['ratio2']=parameter

booth[['AC_2','Village']] = booth.village.str.split("_",expand=True)

booth['AC_Check'] = (booth['AC No']==booth['AC_2']).astype(int)

booth.to_csv(r'C:\Users\ipac\Downloads\Booth to AC Mapping\Booth to AC Mapping\sample.csv')
