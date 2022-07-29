# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:18:15 2022
@author: mratna
"""

#These packages are going to be used throughout. So, Please install them before using the script.
import pandas as pd
import os
import numpy as np
from datetime import datetime

#Section 1 - For both Budget and Finance values (till 1-153)
#Change the folder directory to the place where Goal and Forecast Excel file is kept
os.chdir(r'C:\Users\mratna\Documents\XPO\Finance\Goal_forecasting\March 22\March-V2')

#Reading Budget and Forecast data
#Assuming there are 2 worksheets in the Excel and 1st one is for Goal

df_bud=pd.read_excel(r'Daily Mar FC 2+10 20220308.xlsx',sheet_name=0)
df_fc=pd.read_excel(r'Daily Mar FC 2+10 20220308.xlsx',sheet_name=1)

#Selecting only 6 relevant columns from Goal and Forecasting data
df_bud_1=df_bud[['PICKUP_DATE','SHPMT_CNT','WGT','NET_REV','NET_REV_NET_FSC','LoH','FSC%','Ton-miles','FSC Retention']]
df_fc_1=df_fc[['PICKUP_DATE','SHPMT_CNT','WGT','NET_REV','NET_REV_NET_FSC','LoH','FSC%','Ton-miles','FSC Retention']]

#Selecting only non-blank goal and forecasting data
df_bud_1.dropna(subset=['SHPMT_CNT'], inplace=True)
df_fc_1.dropna(subset=['SHPMT_CNT'], inplace=True)

#Remove last 2 columns which has aggregated values
df_bud_2=df_bud_1.iloc[:(len(df_bud_1)-2)]
df_fc_2=df_fc_1.iloc[:(len(df_fc_1)-2)]

#Read Last year's same month Data (Previous Year)
#Assuming it's a csv file and kept in the same folder as the Goal and Forecast Excel file
df_sic=pd.read_csv(r'C:\Users\mratna\Documents\XPO\Finance\Goal_forecasting\March 22\March 1+11\bquxjob_5eb08771_17f26ea7bdf.csv')

# % Calculation for SIC data of last year
df_sic['shipment_count_%']=df_sic['SHIPMENT_COUNT']/sum(df_sic['SHIPMENT_COUNT'])
df_sic['net_revenue_%']=df_sic['NET_REVENUE']/sum(df_sic['NET_REVENUE'])
df_sic['weight_%']=df_sic['WEIGHT']/sum(df_sic['WEIGHT'])
df_sic['net_revenue_less_fsc_%']=df_sic['NET_REVENUE_LESS_FSC']/sum(df_sic['NET_REVENUE_LESS_FSC'])
df_sic['length_of_haul_%']=df_sic['LENGTH_OF_HAUL']/(df_sic['LENGTH_OF_HAUL'].mean())

#Take only date column from either forecast or goal data
df_wrk_day=df_fc_2['PICKUP_DATE']

#Repeat working days (23) - number of SIC times (697 times)  - Using Numpy
np.tile(np.arange(len(df_sic)), len(df_wrk_day))
np.repeat(np.arange(len(df_sic)), len(df_wrk_day))
df_sic_2=df_sic.iloc[np.tile(np.arange(len(df_sic)), len(df_wrk_day))]
df_sic_2.reset_index(drop=True)

#Repeat working days (20) - number of SIC times (693 times) 
df_wrk_day_rep=df_wrk_day.loc[df_wrk_day.index.repeat(len(df_sic))].reset_index(drop=True)

#Add Date column in repeated SIC data
df_sic_2['PICKUP_DATE']=df_wrk_day_rep.values

#Modify Date columns of Bud and FC data
df_fc_2['PICKUP_DATE']=df_fc_2['PICKUP_DATE'].astype(str)
df_bud_2['PICKUP_DATE']=df_bud_2['PICKUP_DATE'].astype(str)

#df_fc_2['PICKUP_DATE'].dtypes
df_fc_2['PICKUP_DATE'].value_counts()

#df_fc_2['PICKUP_DATE'].strftime()
df_sic_2['PICKUP_DATE']=df_sic_2['PICKUP_DATE'].astype(str)
df_sic_2['PICKUP_DATE'].dtypes
df_sic_2['PICKUP_DATE']=df_sic_2['PICKUP_DATE']+[' 00:00:00']

#Left Join repeated SIC Data with Bud and FC data
df_fc_final=df_sic_2.merge(df_fc_2, on='PICKUP_DATE', how='left')
df_bud_final=df_sic_2.merge(df_bud_2, on='PICKUP_DATE', how='left')

#Calculate final columns with relevant column headers
df_fc_final['OutboundRevenueShipmentsForecast']=(df_fc_final['shipment_count_%']*df_fc_final['SHPMT_CNT'])
df_fc_final['OutboundRevenueWeightForecast']=(df_fc_final['weight_%']*df_fc_final['WGT'])
df_fc_final['OutboundRevenueForecast']=(df_fc_final['net_revenue_%']*df_fc_final['NET_REV'])
df_fc_final['OutboundRevenueLessFSCForecast']=(df_fc_final['net_revenue_less_fsc_%']*df_fc_final['NET_REV_NET_FSC'])
df_fc_final['OutboundRevenueLengthofHaulForecast']=(df_fc_final['length_of_haul_%']*df_fc_final['LoH'])

df_bud_final['OutboundRevenueShipments']=round((df_bud_final['shipment_count_%']*df_bud_final['SHPMT_CNT']),2)
df_bud_final['OutboundRevenueWeight']=round((df_bud_final['weight_%']*df_bud_final['WGT']),5)
df_bud_final['OutboundRevenue']=round((df_bud_final['net_revenue_%']*df_bud_final['NET_REV']),2)
df_bud_final['OutboundRevenueLessFSC']=round((df_bud_final['net_revenue_less_fsc_%']*df_bud_final['NET_REV_NET_FSC']),2)
df_bud_final['OutboundRevenueLengthofHaul']=round((df_bud_final['length_of_haul_%']*df_bud_final['LoH']),2)

#Selecting only relevant columns
df_fc_final_1=df_fc_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueShipmentsForecast']]
df_fc_final_1.columns = [*df_fc_final_1.columns[:-1], 'GOAL_VAL_QTY']
df_fc_final_1['GOAL_MTRC_CD']='OutboundRevenueShipmentsForecast'
df_fc_final_2=df_fc_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueWeightForecast']]
df_fc_final_2.columns = [*df_fc_final_2.columns[:-1], 'GOAL_VAL_QTY']
df_fc_final_2['GOAL_MTRC_CD']='OutboundRevenueWeightForecast'
df_fc_final_3=df_fc_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueForecast']]
df_fc_final_3.columns = [*df_fc_final_3.columns[:-1], 'GOAL_VAL_QTY']
df_fc_final_3['GOAL_MTRC_CD']='OutboundRevenueForecast'
df_fc_final_4=df_fc_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueLessFSCForecast']]
df_fc_final_4.columns = [*df_fc_final_4.columns[:-1], 'GOAL_VAL_QTY']
df_fc_final_4['GOAL_MTRC_CD']='OutboundRevenueLessFSCForecast'
df_fc_final_5=df_fc_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueLengthofHaulForecast']]
df_fc_final_5.columns = [*df_fc_final_5.columns[:-1], 'GOAL_VAL_QTY']
df_fc_final_5['GOAL_MTRC_CD']='OutboundRevenueLengthofHaulForecast'

df_bud_final_1=df_bud_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueShipments']]
df_bud_final_1.columns = [*df_bud_final_1.columns[:-1], 'GOAL_VAL_QTY']
df_bud_final_1['GOAL_MTRC_CD']='OutboundRevenueShipments'
df_bud_final_2=df_bud_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueWeight']]
df_bud_final_2.columns = [*df_bud_final_2.columns[:-1], 'GOAL_VAL_QTY']
df_bud_final_2['GOAL_MTRC_CD']='OutboundRevenueWeight'
df_bud_final_3=df_bud_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenue']]
df_bud_final_3.columns = [*df_bud_final_3.columns[:-1], 'GOAL_VAL_QTY']
df_bud_final_3['GOAL_MTRC_CD']='OutboundRevenue'
df_bud_final_4=df_bud_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueLessFSC']]
df_bud_final_4.columns = [*df_bud_final_4.columns[:-1], 'GOAL_VAL_QTY']
df_bud_final_4['GOAL_MTRC_CD']='OutboundRevenueLessFSC'
df_bud_final_5=df_bud_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueLengthofHaul']]
df_bud_final_5.columns = [*df_bud_final_5.columns[:-1], 'GOAL_VAL_QTY']
df_bud_final_5['GOAL_MTRC_CD']='OutboundRevenueLengthofHaul'

#Put all columns under one column header as 'GOAL_VAL_QTY'
df_fc_final_6=df_fc_final_1.append(df_fc_final_2)
df_fc_final_7=df_fc_final_6.append(df_fc_final_3)
df_fc_final_8=df_fc_final_7.append(df_fc_final_4)
df_fc_final_9=df_fc_final_8.append(df_fc_final_5)
df_fc_final_9['GOAL_REF_LVL_CD']='SICTMZ'


df_bud_final_6=df_bud_final_1.append(df_bud_final_2)
df_bud_final_7=df_bud_final_6.append(df_bud_final_3)
df_bud_final_8=df_bud_final_7.append(df_bud_final_4)
df_bud_final_9=df_bud_final_8.append(df_bud_final_5)
df_bud_final_9['GOAL_REF_LVL_CD']='SICTMZ'

#Single File with both Budget and Forecast data
df_bud_fc=df_bud_final_9.append(df_fc_final_9)
df_bud_fc['WHSE_LST_UPDT_DT']=''
df_bud_fc['WHSE_LST_UPDT_BY']=''
df_bud_fc['GOAL_VAL_EFF_DT']=df_bud_fc['PICKUP_DATE']
df_bud_fc['GOAL_VAL_EXPR_DT']=df_bud_fc['PICKUP_DATE']
df_bud_fc['GOAL_CD']=df_bud_fc['REF_SIC_CD']

#Renaminng column headers to the standard and rearranging order of columns
df_bud_fc_final=df_bud_fc[['GOAL_MTRC_CD','GOAL_REF_LVL_CD','GOAL_CD','GOAL_VAL_EFF_DT','GOAL_VAL_EXPR_DT','GOAL_VAL_QTY',
                           'WHSE_LST_UPDT_DT','WHSE_LST_UPDT_BY']]

#Output files with today's date in the filename
timestamp = str(datetime.today().strftime('%Y-%m-%d'))
df_bud_final_9.to_csv(r'Budget_Goal_Load '+str(timestamp)+'.csv')
df_fc_final_9.to_csv(r'Forecast_Goal_Load '+str(timestamp)+'.csv')
df_bud_fc_final.to_csv(r''+str(timestamp)+'_Goal_Loader.csv')




#Section 2 - For only Finance values (Till last)
#Change the folder directory to the place where Goal and Forecast Excel file is kept
    import pandas as pd
    import os
    import numpy as np
    from datetime import datetime
    
    os.chdir(r'C:\Users\mratna\Documents\XPO\Finance\Goal_forecasting\March 22\March-V3')
    
    #Reading Budget and Forecast data
    #Assuming there are 2 worksheets in the Excel and 1st one is for Goal 
    
    df_fc=pd.read_excel(r'Daily Mar Bud & FC 2+10 20220309.xlsx',sheet_name=1)
    
    #Selecting only 6 relevant columns from Goal and Forecasting data
    df_fc_1=df_fc[['PICKUP_DATE','SHPMT_CNT','WGT','NET_REV','NET_REV_NET_FSC','LoH','FSC%','Ton-miles','FSC Retention']]
    
    #Selecting only non-blank goal and forecasting data
    df_fc_1.dropna(subset=['SHPMT_CNT'], inplace=True)
    
    #Remove last 2 columns which has aggregated values
    df_fc_2=df_fc_1.iloc[:(len(df_fc_1)-2)]
    
    #Read Last year's same month Data (Previous Year)
    #Assuming it's a csv file and kept in the same folder as the Goal and Forecast Excel file
    df_sic=pd.read_csv(r'bquxjob_5eb08771_17f26ea7bdf.csv')
    
    # % Calculation for SIC data of last year
    df_sic['shipment_count_%']=df_sic['SHIPMENT_COUNT']/sum(df_sic['SHIPMENT_COUNT'])
    df_sic['net_revenue_%']=df_sic['NET_REVENUE']/sum(df_sic['NET_REVENUE'])
    df_sic['weight_%']=df_sic['WEIGHT']/sum(df_sic['WEIGHT'])
    df_sic['net_revenue_less_fsc_%']=df_sic['NET_REVENUE_LESS_FSC']/sum(df_sic['NET_REVENUE_LESS_FSC'])
    df_sic['length_of_haul_%']=df_sic['LENGTH_OF_HAUL']/(df_sic['LENGTH_OF_HAUL'].mean())
    
    #Take only date column from either forecast or goal data
    df_wrk_day=df_fc_2['PICKUP_DATE']
    
    #Repeat working days (20) - number of SIC times (693 times)  - Using Numpy
    np.tile(np.arange(len(df_sic)), len(df_wrk_day))
    np.repeat(np.arange(len(df_sic)), len(df_wrk_day))
    df_sic_2=df_sic.iloc[np.tile(np.arange(len(df_sic)), len(df_wrk_day))]
    df_sic_2.reset_index(drop=True)
    
    #Repeat working days (20) - number of SIC times (693 times) 
    df_wrk_day_rep=df_wrk_day.loc[df_wrk_day.index.repeat(len(df_sic))].reset_index(drop=True)
    
    #Add Date column in repeated SIC data
    df_sic_2['PICKUP_DATE']=df_wrk_day_rep.values
    
    #Modify Date columns of Bud and FC data
    df_fc_2['PICKUP_DATE']=df_fc_2['PICKUP_DATE'].astype(str)
    df_sic_2['PICKUP_DATE']=df_sic_2['PICKUP_DATE'].astype(str)
    df_sic_2['PICKUP_DATE']=df_sic_2['PICKUP_DATE']+[' 00:00:00']
    
    #Left Join repeated SIC Data with Bud and FC data
    df_fc_final=df_sic_2.merge(df_fc_2, on='PICKUP_DATE', how='left')
    
    #Calculate final columns with relevant column headers
    df_fc_final['OutboundRevenueShipmentsForecast']=(df_fc_final['shipment_count_%']*df_fc_final['SHPMT_CNT'])
    df_fc_final['OutboundRevenueWeightForecast']=(df_fc_final['weight_%']*df_fc_final['WGT'])
    df_fc_final['OutboundRevenueForecast']=(df_fc_final['net_revenue_%']*df_fc_final['NET_REV'])
    df_fc_final['OutboundRevenueLessFSCForecast']=(df_fc_final['net_revenue_less_fsc_%']*df_fc_final['NET_REV_NET_FSC'])
    df_fc_final['OutboundRevenueLengthofHaulForecast']=(df_fc_final['length_of_haul_%']*df_fc_final['LoH'])
    
    #Selecting only relevant columns
    df_fc_final_1=df_fc_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueShipmentsForecast']]
    df_fc_final_1.columns = [*df_fc_final_1.columns[:-1], 'GOAL_VAL_QTY']
    df_fc_final_1['GOAL_MTRC_CD']='OutboundRevenueShipmentsForecast'
    df_fc_final_2=df_fc_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueWeightForecast']]
    df_fc_final_2.columns = [*df_fc_final_2.columns[:-1], 'GOAL_VAL_QTY']
    df_fc_final_2['GOAL_MTRC_CD']='OutboundRevenueWeightForecast'
    df_fc_final_3=df_fc_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueForecast']]
    df_fc_final_3.columns = [*df_fc_final_3.columns[:-1], 'GOAL_VAL_QTY']
    df_fc_final_3['GOAL_MTRC_CD']='OutboundRevenueForecast'
    df_fc_final_4=df_fc_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueLessFSCForecast']]
    df_fc_final_4.columns = [*df_fc_final_4.columns[:-1], 'GOAL_VAL_QTY']
    df_fc_final_4['GOAL_MTRC_CD']='OutboundRevenueLessFSCForecast'
    df_fc_final_5=df_fc_final[['REF_SIC_CD','PICKUP_DATE','OutboundRevenueLengthofHaulForecast']]
    df_fc_final_5.columns = [*df_fc_final_5.columns[:-1], 'GOAL_VAL_QTY']
    df_fc_final_5['GOAL_MTRC_CD']='OutboundRevenueLengthofHaulForecast'
    
    #Put all columns under one column header as 'GOAL_VAL_QTY'
    df_fc_final_6=df_fc_final_1.append(df_fc_final_2)
    df_fc_final_7=df_fc_final_6.append(df_fc_final_3)
    df_fc_final_8=df_fc_final_7.append(df_fc_final_4)
    df_fc_final_9=df_fc_final_8.append(df_fc_final_5)
    df_fc_final_9['GOAL_REF_LVL_CD']='SICTMZ'
    df_fc_final_9['WHSE_LST_UPDT_DT']=''
    df_fc_final_9['WHSE_LST_UPDT_BY']=''
    df_fc_final_9['GOAL_VAL_EFF_DT']=df_fc_final_9['PICKUP_DATE']
    df_fc_final_9['GOAL_VAL_EXPR_DT']=df_fc_final_9['PICKUP_DATE']
    df_fc_final_9['GOAL_CD']=df_fc_final_9['REF_SIC_CD']
    
    #Renaminng column headers to the standard and rearranging order of columns
    df_fc_final_10=df_fc_final_9[['GOAL_MTRC_CD','GOAL_REF_LVL_CD','GOAL_CD','GOAL_VAL_EFF_DT','GOAL_VAL_EXPR_DT','GOAL_VAL_QTY',
                               'WHSE_LST_UPDT_DT','WHSE_LST_UPDT_BY']]
    
    #Output files with today's date in the filename
    timestamp = str(datetime.today().strftime('%Y-%m-%d'))
    df_fc_final_10.to_csv(r'Forecast_Goal_Load '+str(timestamp)+'.csv')
    
    
    
    
    