# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:48:48 2020

@author: user
"""


import pandas as pd
import numpy as np
import os
import glob



################################################################# campaign #######################################################################

os.chdir(r'C:\Users\user\Downloads\madhu\campaign\campaign')

entries = os.listdir(r'C:\Users\user\Downloads\madhu\campaign\campaign')

len(entries)


extension = 'xlsx'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)


result_obj = pd.concat([pd.read_excel(file) for file in entries])


result_obj.to_excel('campaign_with_dup',index=False)
result_obj.columns

df_campaign_final = result_obj[['phone','source']]
df_campaign_final.shape


df_camp = df_campaign_final.drop_duplicates(subset=['phone'])
df_camp.shape


################################################################# DIA;ER SET-2 #######################################################################




os.chdir(r'C:\Users\user\Downloads\madhu\campaign\DIALER-SET2_12-13-2020')

entries_DIALERET2 = os.listdir(r'C:\Users\user\Downloads\madhu\campaign\DIALER-SET2_12-13-2020')

len(entries_DIALERET2)



extension = 'xlsx'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)


result_DIAELERSET2 = pd.concat([pd.read_excel(file) for file in entries_DIALERET2])

result_DIAELERSET2.shape
result_DIAELERSET2.columns







a = lambda x : len(x)

result_DIAELERSET2_1 = result_DIAELERSET2.copy()

result_DIAELERSET2_1['phone'] = result_DIAELERSET2_1['phone'].astype(str)

mob_length = result_DIAELERSET2_1['phone'].apply(a)
mob_length.unique()


b = lambda x : '' if  x.startswith('5') else x

result_DIAELERSET2_1['phone'] = result_DIAELERSET2_1['phone'].apply(b)


result_DIAELERSET2_2 = result_DIAELERSET2_1.drop_duplicates(subset=['phone'])

result_DIAELERSET2_2.shape


result_DIAELERSET2_2.columns

result_DIAELERSET2_3 = result_DIAELERSET2_2.copy()

result_DIAELERSET2_3['source']= 'Dialer-set2'


DIALERSET2FINAL = result_DIAELERSET2_3[['phone','source']]
DIALERSET2FINAL.shape


################################################################# SURVEY #######################################################################


result_obj.shape
result_obj.head(10)



os.chdir(r'C:\Users\user\Downloads\madhu\campaign')



df1= pd.read_excel('WB_PhoneNumbers_Survey (2).xlsx',sheet_name=0)
df1['source'] = "survey"

df1 = df1[['phone','source']]
df1.shape
#df1.to_excel('WB_PhoneNumbers_Surveywith_dup_1.xlsx',index=False)
#df1.shape
df2= pd.read_excel('WB_PhoneNumbers_Survey (2).xlsx',sheet_name=1)
df2['source'] = "survey"

df2 = df2[['phone','source']]


DF_SURVEY_FINAL = pd.concat([df1,df2])
DF_SURVEY_FINAL.shape
DF_SUR = DF_SURVEY_FINAL.drop_duplicates(subset=['phone'])

DF_SUR.shape


################################################## DAILER #########################################################################################################
m = ['phone']
df_dialer1 = pd.read_excel('Dialer Report Survey 26Aug To 8Dec.xlsx',sheet_name=0)
df_dialer1.columns = m
df_dialer1['district'] = ""
df_dialer1['ac'] = ""
df_dialer1['gender'] = ""
df_dialer1['age'] = ""
df_dialer1['social_category'] = ""
df_dialer1['source'] = "Dialer-set1"
df_dialer1.shape

df_dialer1 = df_dialer1[['phone','source']]



df_dialer2 = pd.read_excel('Dialer Report Survey 26Aug To 8Dec.xlsx',sheet_name=1)
df_dialer2.columns = m

df_dialer2['district'] = ""
df_dialer2['ac'] = ""
df_dialer2['gender'] = ""
df_dialer2['age'] = ""
df_dialer2['social_category'] = ""
df_dialer2['source'] = "Dialer-set1"
df_dialer2.shape

df_dialer2 = df_dialer2[['phone','source']]






df_dialer3 = pd.read_excel('Dialer Report Survey 26Aug To 8Dec.xlsx',sheet_name=2)
df_dialer3.columns = m
df_dialer3['district'] = ""
df_dialer3['ac'] = ""
df_dialer3['gender'] = ""
df_dialer3['age'] = ""
df_dialer3['social_category'] = ""
df_dialer3['source'] = "Dialer-set1"
df_dialer3.shape

df_dialer3 = df_dialer3[['phone','source']]


DF_DIALER_FINAL =  pd.concat([df_dialer1,df_dialer2,df_dialer3])
DF_DIALER_FINAL.shape
DF_dia = DF_DIALER_FINAL.drop_duplicates(subset=['phone'])
DF_dia.shape


DF_sur.shape

###########################################################################################################################################################


final_compiled_data = pd.concat([df_camp,DIALERSET2FINAL,DF_SUR,DF_dia])

final_compiled_data.shape


df_camp.shape
DIALERSET2FINAL.shape
DF_SUR.shape
DF_dia.shape




final_comp = final_compiled_data.drop_duplicates(subset=['phone'])

final_comp.shape


dialer = final_comp[final_comp['source'] == "survey"]

dialer.shape

ivr_1 = dialer.iloc[0:857758]
ivr_2 = dialer.iloc[857758:1600001]
ivr_3 = dialer.iloc[1600001:2400001]
ivr_4 = dialer.iloc[2400001:3069886]

ibbb = dialer.iloc[3069886:3269886]



ivr_1.shape



ivr_1.to_excel('survey_v1.xlsx',index=False)



ivr_2.to_excel('campaign_v2.xlsx',index=False)
ivr_3.to_excel('campaign_v3.xlsx',index=False)
ivr_4.to_excel('campaign_v4.xlsx',index=False)






ivr_2 = final_comp.iloc[652417:1304833]

ivr_2.shape

ivr_2.to_excel('dialer_set_1_v2.xlsx',index=False)



ivr_1 = final_comp.iloc[1600001:2400000]
ivr_1 = final_comp.iloc[2400001:3200000]






################################################## SURVEY  #########################################################################################################


DF_DIALER_FINAL.shape

DF_CAMPIGN_1 = pd.read_excel('campaign0.xlsx')
DF_CAMPIGN_2 = pd.read_excel('campaign1.xlsx')
DF_CAMPIGN_3 = pd.read_excel('campaign2.xlsx')
DF_CAMPIGN_4 = pd.read_excel('campaign3.xlsx')



df_campaign_final  =pd.concat([DF_CAMPIGN_1,DF_CAMPIGN_2,DF_CAMPIGN_3,DF_CAMPIGN_4])
df_campaign_final.shape

df_campaign_final = df_campaign_final[['phone','source']]



df_camp = df_campaign_final.drop_duplicates(subset=['phone'])
df_camp.shape



df_camp = df_camp[['phone','source']]
df_camp.shape


without_dup_3['source'].head(10)

without_dup_3 = without_dup_2.copy()
without_dup_3['source'] = "Dialer-set2"

without_dup_3 = without_dup_3[['phone','source']]
without_dup_3.shape



final_compiled_data = pd.concat([df_camp,DF_SUR,DF_dia,without_dup_3])


final_comp = final_compiled_data.drop_duplicates(subset=['phone'])


final_comp.shape


ivr_1 = final_comp.iloc[1:800000]
ivr_1 = final_comp.iloc[800001:1600000]
ivr_1 = final_comp.iloc[1600001:2400000]
ivr_1 = final_comp.iloc[2400001:3200000]


final_compiled_data.shape

df_camp.shape
DF_SUR.shape
DF_dia.shape
without_dup_3.shape


final = final_compiled_data.drop_duplicates(subset=['phone'])

dialer = final_comp[final_comp['source'] == "Dialer-set2"]

dialer.shape


l = ['phone']








for i in range(len(entries)):
    df = pd.read_excel(entries[i])
    print(i)
    df.columns = l
    df['district'] = ""
    df['ac'] = ""
    df['gender'] = ""
    df['age'] = ""
    df['social_category'] = ""
    df['source'] = "campaign"
    df.to_excel('campaign{}.xlsx'.format(i),index=False)
    
df.head(10)
  df.shape  
    df.to_exce
    
df.columns    
    
    




################################################## DIALER set-2  #########################################################################################################





import pandas as pd
import os

os.chdir(r'C:\Users\user\Downloads\madhu\campaign')

os.getcwd()

 df = pd.read_excel('campaign0.xlsx',sheet_name = 0)
l = ['month','phone']
df.columns

for i in range(8,10):
    df = pd.read_excel('Survey Data _12-10-2020.xlsx',sheet_name = i)
    df.columns = l    
    print(df.columns)
    print(df.shape)
    df.to_excel('dialer{}.xlsx'.format(i),index=False)
    
    


os.chdir(r'C:\Users\user\Downloads\madhu\campaign\Dialer_10-12-2020')
entries = os.listdir(r'C:\Users\user\Downloads\madhu\campaign\Dialer_10-12-2020')

len(entries)






result_obj = pd.concat([pd.read_excel(file) for file in entries])

result_obj.shape

without_dup = result_obj.drop_duplicates(subset=['phone'])

without_dup.shape



df1 = 


a = lambda x : len(x)

without_dup_1 = without_dup.copy()

without_dup_1['phone'] = without_dup_1['phone'].astype(str)

mob_length = without_dup_1['phone'].apply(a)



b = lambda x : '' if  x.startswith('5') else x

without_dup_1['phone'] = without_dup_1['phone'].apply(b)


without_dup_2 = without_dup_1.drop_duplicates(subset=['phone'])

without_dup_2.shape




mob_length.nunique()


result_obj.to_excel('campaign_with_dup',index=False)







DF_DIALER_SET2 = pd.read_excel('campaign0.xlsx')




df_campaign_final  =pd.concat([DF_CAMPIGN_1,DF_CAMPIGN_2,DF_CAMPIGN_3,DF_CAMPIGN_4])
df_campaign_final.shape


df_camp = df_campaign_final.drop_duplicates(subset=['phone'])
df_camp.shape










