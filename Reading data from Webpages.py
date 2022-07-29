# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:56:26 2022

@author: mratna
"""

import pandas as pd
import selenium 
from selenium import webdriver as wb
from time import sleep

webD=wb.Chrome(r"C:\Users\mratna\Documents\Python Scripts\chromedriver.exe")
webD.get('https://xpologistics-my.sharepoint.com/:x:/g/personal/mckenna_phillips_xpo_com/ER7cXFI8U7BNmsCEDRKRVQgBARaMPyjKb94J1b6UT2-50w')

username = 'manish.ratna@xpo.com'
password = '7'

webD.find_element_by_id("i0116").send_keys(username)
sleep(4)
webD.find_element_by_id("idSIButton9").click()
sleep(4)
webD.find_element_by_id("i0118").send_keys(password)
sleep(4)
webD.find_element_by_id("idSIButton9").click()
sleep(4)
#webD.find_element_by_id("idDiv_SAOTCS_Proofs").click()
webD.find_element_by_xpath('//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div/div/div[2]').click()
sleep(4)
webD.find_element_by_id("idSIButton9").click()
sleep(4)
rows=1+len(webD.find_elements_by_xpath('//*[@id="m_excelWebRenderer_ewaCtl_gridDiv"]/table/tbody/tr'))

rows=1+len(webD.find_elements_by_tagname('//*[@id="m_excelWebRenderer_ewaCtl_gridDiv"]/table/tbody/tr'))

condition = True
while condition:
    productInfoList=webD.find_elements_by_class_name('ewr-grdblkflow')   
    for el in productInfoList:
        pp1=el.find_elements_by_tag_name('h4')[-1]
print(len(productInfoList))

#webD.find_element_by_xpath('//*[@id="m_excelWebRenderer_ewaCtl_contentAreaDiv"]/div[3]').click()
# //*[@id="m_excelWebRenderer_ewaCtl_sheetContentDiv"]
# //*[@id="m_excelWebRenderer_ewaCtl_sheetContentDiv_Flow_0"]/div/div[2]/div/canvas[1]
# //*[@id="m_excelWebRenderer_ewaCtl_gridDiv"]/table/tbody/tr[1]/td[1]
# find_element_by_tag_name
# //*[@id="m_excelWebRenderer_ewaCtl_gridDiv"]/table/tbody/tr[1]/td[1]/div/div[1]/a[1]
# //*[@id="m_excelWebRenderer_ewaCtl_contentAreaDiv"]/div[3]
