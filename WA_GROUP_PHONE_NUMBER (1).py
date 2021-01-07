# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 00:11:42 2020

@author: user
"""


# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 16:14:52 2020

@author: ASHU BABA
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 23:30:53 2020

@author: ASHU BABA
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import xlsxwriter
 
# Replace below path with the absolute path
# to chromedriver in your computer
chrome_path=r"C:\Users\user\Desktop\CHROME_DRIVER\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 40)
 
# Replace 'Friend's Name' with the name of your friend  
# or the name of a group  


# Replace the below string wit[h your own message
#target=['Falta update 2',	'Falta update 1',	'Bishnupur Update 1',	'Bishnupur Update 2',	'Metiaburuz Update 1',	'Budge Budge Update 2',	'Budge Budge Update 1',	'Satgachia Update 1',	'Satgachia Update 2',	'Mahestala Update 1',	'Mahestala Update 2',	'TOLLYGUNGE Update 1',	'Tollygunge Update 2',	'Behala Purba Update 1',	'Behala Purba Update 2',	'Behala paschim update 1',	'Behala Paschim update 2',	'Bhangore update 1',	'Bhangore update 2',	'Bhangore update 3',	'Baruipur Purba Update 1',	'Baruipur Purba Update 3',	'Baruipur Purba update 4',	'Baruipur Purba Update 5',	'Sonarpur Dakshin Update 1',	'Sonarpur North Update 1',	'Sonarpur North Update 2',	'Dum Dum Update 1',	'Dum Dum Update 2',	'Barrackpore Update 1',	'Khardaha Update 2',	'Khardaha Update 1',	'Kamarhati update 2',	'Kamarhati update 1',	'Naihati Update 1',	'Naihati Update 2',	'AC Rajarhat Update 2',	'AC Rajarhat Update 1',	'Jagatdal update 1',	'Jagatdal update 2',	'Amdanga Update 2',	'Amdanga Update 1',	'North Dumdum Update 1',	'North Dumdum Update 2',	'Baranagar update 1',	'Baranagar Update 2',	'Bongaon Uttar Update 1',	'Bongaon Uttar Update 2',	'Bongaon Dakshin Update 1',	'Bongaon Dakshin Update 2',	'Bagdah Update 3',	'Bagdah Update 2',	'Bagdah Update 1',	'Gaighata Update 1',	'Gaighata Update 2',	'Swarupnagar Update 1',	'Swarupnagar Update 2',	'Basirhat Uttar Update 1',	'Basirhat Uttar Update 3',	'Basirhat Uttar Update 2',	'Madhyamgram Update 1',	'Deganga Update 1',	'HABRA UPDATE 1',	'HABRA  UPDATE 2',	'Ashoknagar Update 1',	'Ashoknagar Update 2',	'Hingalganj Update 1',	'Hingalganj Update 2',	'Haroa Update 2',	'Haroa Update 1',	'Baduria update 3',	'Baduria Update 2',	'Baduria update 1',	'SANDESHKHALI UPDATE 2',	'SANDESHKHALI UPDATE 1',	'Deganga Update 2',	'Basirhat Dakshin Update 3',	'Basirhat Dakshin Update 2',	'Basirhat Dakshin Update 1',	'Bidhannagar Update 1',	'Bidhannagar Update 2',	'Minakhan Update 3',	'Minakhan Update 2',	'Barasat Update 1',	'Barasat Update 2',	'Barasat Update 3',	'Madhyamgram Update 2',	'Kashipur Update 10',	'Kashipur Update 8',	'Kashipur Update 1',	'Kashipur Update 3',	'Kashipur Update 2',	'Kashipur Update 9',	'Kashipur Update 4',	'Kashipur Update 6',	'Kashipur Update 7',	'Kashipur Update 5',	'Kashipur Update 12',	'Raghunathpur Update 4',	'Raghunathpur Update 9',	'Raghunathpur Update 8',	'Raghunathpur Update 3',	'Raghunathpur Update 11',	'Raghunathpur Update 10',	'Raghunathpur Update 6',	'Raghunathpur Update 1',	'Raghunathpur Update 7',	'Raghunathpur Update 12',	'Raghunathpur Update 2',	'Raghunathpur Update 5',	'Purulia AC Update 1',	'Purulia AC Update 2',	'Purulia AC Update 3',	'Purulia AC Update 4',	'Purulia AC Update 5',	'Purulia AC Update 6',	'Purulia AC Update 7',	'Purulia AC Update 8',	'Purulia AC Update 9',	'Purulia AC Update 10',	'Purulia AC Update 11',	'Purulia AC Update 12',	'Manbazar Update 10',	'Manbazar Update 11',	'Manbazar Update 12',	'Bandwan Update 1',	'Bandwan Update 2',	'Bandwan Update 4',	'Bandwan Update 5',	'Bandwan Update 6',	'Bandwan Update 9',	'Bandwan Update 10',	'Bandwan Update 14',	'Bandwan Update 15',	'Bandwan Update 16',	'Bandwan Update 18',	'Bandwan Update 19',	'Bandwan Update 25',	'Joypur update 7',	'Joypur update 3',	'Joypur update 5',	'Joypur update 2',	'Joypur update 10',	'Joypur update 11',	'Joypur update 9',	'Joypur update 12',	'Joypur update 1',	'Joypur update 6',	'Joypur update 8',	'Joypur update 4',	'Bagmundi Update 1',	'Bagmundi Update 2',	'Bagmundi Update 3',	'Bagmundi Update 4',	'Bagmundi Update 5',	'Bagmundi Update 8',	'Bagmundi Update 10',	'Baghmundi Update 11',	'Bagmundi Update 12',	'Bagmundi Update 13',	'Bagmundi Update 14',	'Balarampur update 1',	'Balarampur update 3',	'Balarampur update 7',	'Balarampur update 6',	'Balarampur update 2',	'Balarampur update 10',	'Balarampur update 9',	'Balarampur update 12',	'Balarampur update 8',	'Balarampur update 4',	'Balarampur update 5',	'Balarampur update 5',	'Para Update 1',	'Para Update 5',	'Para Update 6',	'Para Update 3',	'Para Update 7',	'Para Update 2',	'Para Update 4',	'Para Update 8',	'Para Update 9',	'Para Update 4',	'Bankura AC Update 1',	'Taldangra Update 1',	'Taldangra Update 2',	'Taldangra Update 3',	'Ranibandh Update 2',	'Ranibandh Update 1',	'Chhatna Update 2',	'Chhatna Update 1',	'Saltora Update 1',	'Saltora Update 2',	'Saltora Update 1',	'Barjora update 1',	'Barjora update 2',	'INDAS UPDATE 1',	'INDAS UPDATE 2',	'Kotulpur Update 1',	'ONDA UPDATE 1',	'KHANAKUL UPDATE 1',	'Bagnan Update 1',	'Bagnan Update 2',	'Uluberia Purba Update 1',	'Uluberia Purba Update 2',	'Uluberia Dakshin Update 1',	'Uluberia Dakshin Update 2',	'Shyampur Update 1',	'Shyampur Update 2',	'Sankrail Update 2',	'Sankrail Update 1',	'Uluberia Uttar Update 1',	'Uluberia Uttar Update 2',	'Udaynarayanpur Update 2',	'Udaynarayanpur Update 1',	'Basanti Update 1',	'Basanti Update 2',	'Gosaba Update 2',	'Canning Purba Update 2',	'Canning Purba Update 1',	'Canning Paschim Update 1',	'Kultali update 1',	'Kultali update 2',	'Sagar Update 1',	'Sagar Update 2',	'Raidighi update 1',	'Raidighir update 2',	'Mandirbazar update 2',	'Mandirbazar update 1',	'Kolkata Port Update 1',	'Kolkata Port Update 2',	'Bhabanipur Update 2',	'Bhabanipur Update 1',	'Kulpi Update 1',	'Kulpi Update 2',	'Patharpratima updat 1',	'Patharpratima update 2',	'Magrahat Paschim Update 1',	'Magrahat Paschim Update 2',	'Magrahat purba update 1',	'MAGHRAHAT PURBA update 2',	'Jaynagar Update 8',	'Jaynagar Update 3',	'Patharpratima update 2']
#target=['Bishnupur Update 2',	'Sonarpur Dakshin Update 1',	'Baduria Update 2',	'Purulia AC Update 1',	'Bandwan Update 1',	'Bandwan Update 2',	'Joypur update 1',	'Baghmundi Update 11',	'Balarampur update 1',	'Balarampur update 5',	'Para Update 2',	'Ranibandh Update 1',	'Ranibandh Update 1',	'Chhatna Update 2',	'INDAS UPDATE 2',	'INDAS UPDATE 2',	'Kotulpur Update 1',	'KHANAKUL UPDATE 1',	'KHANAKUL UPDATE 1',	'Bagnan Update 1',	'Uluberia Purba Update 1',	'Shyampur Update 1',	'Shyampur Update 1',	'Shyampur Update 2',	'Canning Purba Update 1',	'Canning Purba Update 1',	'Canning Paschim Update 1',	'Raidighi update 1',	'Bhabanipur Update 1',	'Bhabanipur Update 1',	'Kulpi Update 1',	'Jaynagar Update 3']
#target=['Chandipur AC update 1',	'Chandipur AC update 2',	'Chandipur Update 3',	'Uttar Kanthi Update 1',	'Uttar Kanthi Update 2',	'Uttar Kanthi Update 3',	'Bhagwanpur Update 2',	'Bhagwanpur Update 1',	'Khejuri update 6',	'Khejuri update 1',	'Khejuri update 5',	'Khejuri update 4',	'Khejuri update 2',	'Ramnagar update 4',	'Ramnagar update 5',	'Egra Update 1',	'Egra Update 2',	'Egra Update 6',	'Egra Update 4',	'Egra Update 5',	'Egra Update 3',	'RAJGANJ UPDATE 2',	'RAJGANJ UPDATE 1',	'Dabgram fulbari update 2',	'Dabgram fulbari update 1',	'DHUPGURI UPDATE 1','Dhupguri Update 2','Dhupguri Update 3',	'Nagrakata update 1',	'Nagrakata update 2',	'Mal Update 2',	'Mal Update 3',	'Mal Update 1',	'Jalpaiguri AC Update 1','Jalpaiguri AC Update 3',	'Jalpaiguri AC Update 2',	'Jalpaiguri AC Update 4',	'Jhargram AC Update 1',	'Jhargram AC Update 2',	'Nayagram Update 1',	'Gopiballavpur Update 1',	'Binpur Update 1',	'Gopiballavpur Update 2',	'Goghat Update 2',	'TARAKESWAR UPDATE 1',	'TARAKESWAR UPDATE 2',	'Goghat Update 3',	'Jangipara Update 1',	'Jangipara Update 2',	'Chanditala update 2',	'Chanditala update 1',	'Pursurah Update 3',	'Pursurah Update 2',	'Pursurah Update 4',	'Pursurah Update 1',	'Arambagh Update 4',	'Arambagh Update 3',	'Arambagh Update 1',	'Arambagh Update 2',	'Haripal Update 3',	'Haripal Update 1',	'Haripal Update 2',	'KHANAKUL UPDATE 3',	'KHANAKUL UPDATE 2',	'Goghat update 1',	'Champdani Update 1',	'Champdani Update 2',	'Champdani Update 3',	'Uttarpara Update 1',	'Uttarpara Update 2',	'Uttarpara Update 3',	'Saptagram Update 1',	'Saptagram Update 2',	'Serampore update 1',	'Serampore update 3',	'Serampore update 2',	'Chuchura Update 3',	'Chuchura Update 1',	'Chuchura Update 2',	'Singur Update 1',	'Singur Update 2',	'Pandua Update 3',	'Pandua Update 2',	'Pandua update 1',	'Pandua Update 4',	'Balagarh Update 1',	'Balagarh Update 2',	'Tamluk Update 1',	'Tamluk Update 2',	'Tamluk Update 3',	'Panskura Paschim update 1',	'Panskura Paschim update 2',	'Moyna Update 1',	'Moyna Update 2',	'HALDIA Update1',	'HALDIA Update 2',	'Gangarampur Update 1',	'Kumarganj Update 1',	'Tapan Update 1',	'Kushmandi Update 1',	'Tapan Update 2',	'Chandipur AC update 1',	'Chandipur AC update 2',	'Chandipur Update 3',	'Patashpur Update 1',	'Patashpur Update 2',	'Uttar Kanthi Update 1',	'Uttar Kanthi Update 2',	'Uttar Kanthi Update 3',	'Bhagwanpur Update 2',	'Bhagwanpur Update 1',	'Khejuri update 6',	'Khejuri update 1',	'Khejuri update 5',	'Khejuri update 4',	'Khejuri update 2',	'Ramnagar update 4',	'Ramnagar update 5',	'Ramnagar update 2',	'Ramnagar update 1',	'Egra Update 1',	'Egra Update 2',	'Egra Update 6',	'Egra Update 4',	'Egra Update 5',	'Egra Update 3',	'Patashpur Update 3',	'Howrah Uttar Update 1',	'Howrah Uttar Update 2',	'Howrah Uttar Update 3',	'Habibpur update 2',	'Habibpur update 1',	'Malatipur update 2',	'Maynaguri Update 1',	'Maynaguri Update 2',	'Maynaguri Update 3',	'Garhbeta Update 1','Chandrakona Update 1', 'Salboni Update 1','Kaliganj Update 3',	'Nakashipara Update 1',	'Nakashipara Update 2',	'Nakashipara Update 3',	'Chapra Update 1',	'Chapra Update 2',	'Chapra Update 3',	'Krishnagar Uttar Update 1',	'Krishnagar Uttar Update 2',	'Krishnagar Uttar Update 3',	'Santipur Update 1',	'Santipur Update 2',	'Santipur Update 3','Ghatal Update 1','Daspur Update 1','Sabang Update 1','Pingla Update 1','Debra Update 1','Keshpur Update 1','Kharagpur Update 1','Medinipur Update 1','Keshiary Update 1','Narayangarh Update 1','Nabadwip update 1',	'Nabadwip update 2',	'Krishnaganj Update 2',	'Krishnaganj Update 1',	'Krishnaganj Update 3',	'Chakdaha Update 1',	'Chakdaha Update 2',	'Kalyani Update 1',	'Kalyani Update 3',	'Kalyani Update 2',	'Haringhata Update 1',	'Haringhata Update 2'] 


#target=['Chandipur AC Update 1',	'Chandipur AC Update 2',	'Chandipur Update 3',	'Uttar Kanthi Update 1',	'Uttar Kanthi Update 2',	'Uttar Kanthi Update 3',	'Bhagwanpur Update 2',	'Bhagwanpur Update 1',	'Khejuri Update 6',	'Khejuri Update 1',	'Khejuri Update 5',	'Khejuri Update 4',	'Khejuri Update 2',	'Ramnagar Update 4',	'Ramnagar Update 5',	'Egra Update 1',	'Egra Update 2',	'Egra Update 6',	'Egra Update 4',	'Egra Update 5',	'Egra Update 3',	'RAJGANJ Update 2',	'RAJGANJ Update 1',	'Dabgram fulbari Update 2',	'Dabgram fulbari Update 1',	'DHUPGURI Update 1',	'Dhupguri Update 2','Dhupguri Update 3',	'Nagrakata Update 1',	'Nagrakata Update 2',	'Mal Update 2',	'Mal Update 3',	'Mal Update 1','Jalpaiguri AC Update 1','Jalpaiguri AC Update 3',	'Jalpaiguri AC Update 2',	'Jalpaiguri AC Update 4',	'Jhargram AC Update 1',	'Jhargram AC Update 2',	'Nayagram Update 1',	'Gopiballavpur Update 1',	'Binpur Update 1',	'Gopiballavpur Update 2',	'Goghat Update 2',	'TARAKESWAR Update 1',	'TARAKESWAR Update 2',	'Goghat Update 3',	'Jangipara Update 1',	'Jangipara Update 2',	'Chanditala Update 2',	'Chanditala Update 1',	'Pursurah Update 3',	'Pursurah Update 2',	'Pursurah Update 4',	'Pursurah Update 1',	'Arambagh Update 4',	'Arambagh Update 3',	'Arambagh Update 1',	'Arambagh Update 2',	'Haripal Update 3',	'Haripal Update 1',	'Haripal Update 2',	'KHANAKUL Update 3',	'KHANAKUL Update 2',	'Goghat Update 1',	'Champdani Update 1',	'Champdani Update 2',	'Champdani Update 3',	'Uttarpara Update 1',	'Uttarpara Update 2',	'Uttarpara Update 3',	'Saptagram Update 1',	'Saptagram Update 2',	'Serampore Update 1',	'Serampore Update 3',	'Serampore Update 2',	'Chuchura Update 3',	'Chuchura Update 1',	'Chuchura Update 2',	'Singur Update 1',	'Singur Update 2',	'Pandua Update 3',	'Pandua Update 2',	'Pandua Update 1',	'Pandua Update 4',	'Balagarh Update 1',	'Balagarh Update 2',	'Tamluk Update 1',	'Tamluk Update 2',	'Tamluk Update 3',	'Panskura Paschim Update 1',	'Panskura Paschim Update 2',	'Moyna Update 1',	'Moyna Update 2',	'HALDIA Update1',	'HALDIA Update 2',	'Gangarampur Update 1',	'Kumarganj Update 1',	'Tapan Update 1',	'Kushmandi Update 1',	'Tapan Update 2',	'Chandipur AC Update 1',	'Chandipur AC Update 2',	'Chandipur Update 3',	'Patashpur Update 1',	'Patashpur Update 2',	'Uttar Kanthi Update 1',	'Uttar Kanthi Update 2',	'Uttar Kanthi Update 3',	'Bhagwanpur Update 2',	'Bhagwanpur Update 1',	'Khejuri Update 6',	'Khejuri Update 1',	'Khejuri Update 5',	'Khejuri Update 4',	'Khejuri Update 2',	'Ramnagar Update 4',	'Ramnagar Update 5',	'Ramnagar Update 2',	'Ramnagar Update 1',	'Egra Update 1',	'Egra Update 2',	'Egra Update 6',	'Egra Update 4',	'Egra Update 5',	'Egra Update 3',	'Patashpur Update 3',	'Howrah Uttar Update 1',	'Howrah Uttar Update 2',	'Howrah Uttar Update 3',	'Habibpur Update 2',	'Habibpur Update 1',	'Malatipur Update 2',	'Maynaguri Update 1',	'Maynaguri Update 2',	'Maynaguri Update 3','Garhbeta Update 1','Chandrakona Update 1','Salboni Update 1','Kaliganj Update 3',	'Nakashipara Update 1',	'Nakashipara Update 2',	'Nakashipara Update 3',	'Chapra Update 1',	'Chapra Update 2',	'Chapra Update 3',	'Krishnagar Uttar Update 1',	'Krishnagar Uttar Update 2',	'Krishnagar Uttar Update 3',	'Santipur Update 1',	'Santipur Update 2',	'Santipur Update 3','Ghatal Update 1','Daspur Update 1','Sabang Update 1','Pingla Update 1','Debra Update 1','Keshpur Update 1','Kharagpur Update 1','Medinipur Update 1','Keshiary Update 1','Narayangarh Update 1','Nabadwip Update 1',	'Nabadwip Update 2',	'Krishnaganj Update 2',	'Krishnaganj Update 1',	'Krishnaganj Update 3',	'Chakdaha Update 1',	'Chakdaha Update 2',	'Kalyani Update 1',	'Kalyani Update 3',	'Kalyani Update 2',	'Haringhata Update 1',	'Haringhata Update 2']
#target=['Kanthi Uttar Update 2',	'RAJGANJ UPDATE 2',	'RAJGANJ UPDATE 1',	'Dabgram fulbari update 2',	'Dabgram fulbari update 1',	'DHUPGURI UPDATE 1',	'Nagrakata update 1',	'Nagrakata update 2',	'TARAKESWAR UPDATE 1',	'TARAKESWAR UPDATE 2',	'Chanditala update 1',	'KHANAKUL UPDATE 3',	'KHANAKUL UPDATE 2',	'Goghat update 1',	'Serampore update 1',	'Serampore update 2',	'Pandua update 1',	'Panskura Paschim update 1',	'Panskura Paschim update 2',	'Tapan update 1',	'TAPAN UPDATE 2',	'Kanthi Uttar Update 2',	'Habibpur update 2',	'Malatipur update 2',	'Nabadwip update 1']

target=['Kaliyaganj update 2',	'Bishnupur update 1',	'Bishnupur update 2']

string = "Message sent using Python!!!"

filename="WA_FIELD_WA_1908_WA_3.xlsx"    
workbook = xlsxwriter.Workbook(filename)
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 1000000)
worksheet.set_column('B:B', 1000000)
worksheet.set_column('C:C', 1000000)


row=0
colu=0
     

worksheet.write(row,colu, "SNO")
worksheet.write(row,colu+1, "Group Name")
worksheet.write(row,colu+2, "Phone Numbers")

row=1
colu=0
     
counter=0
stopc=0

time.sleep(30)
for i in range(3):
    time.sleep(1)
    driver.find_element_by_css_selector('''#side > div._2EoyP > div > label > div > div._3FRCZ.copyable-text.selectable-text''').send_keys(target[i])
    print(str((counter/763)*100)+" %")
    print("\n")
    print(str(counter)+" of 763 in process")
                                   
    try:
        time.sleep(1)
        try:
            driver.find_element_by_xpath('''//*[@id="pane-side"]/div[1]/div/div/div[2]''').click()
            #print(target[i])
            time.sleep(1)
            gname=driver.find_element_by_xpath('''//*[@id="main"]/header/div[2]/div[1]/div/span''').text
            #print(gname)
            time.sleep(1)
            if (gname==target[i]):
                print(target[i])
                driver.find_element_by_xpath("""//*[@id="main"]/header""").click()
                time.sleep(2)
                abc=driver.find_element_by_xpath('''//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[1]/div/div/div[1]/span''').text  
                print(abc)
                time.sleep(2)
                numbs=driver.find_element_by_xpath('''//*[@id="main"]/header/div[2]/div[2]/span''').text
                print(numbs)
                worksheet.write(row,colu, i+1)
                worksheet.write(row,colu+1, target[i])
                worksheet.write(row,colu+2, numbs)
                row=row+1
                print(stopc)
            else:
                print(target[i]+" NOT FOUND")
                worksheet.write(row,colu, i+1)
                worksheet.write(row,colu+1, target[i])
                worksheet.write(row,colu+2, "NO GROUP FOUND,NA")
                row=row+1
                time.sleep(1)
            driver.find_element_by_xpath('''//*[@id="side"]/div[1]/div/span/button''').click()
            counter=counter+1
            print(stopc)
        except Exception:
            # print(target[i])
            print("NOT FOUND")
            worksheet.write(row,colu, i+1)
            worksheet.write(row,colu+1, target[i])
            worksheet.write(row,colu+2, "NO GROUP FOUND,NA")
            row=row+1
            time.sleep(1)
            driver.find_element_by_xpath('''//*[@id="side"]/div[1]/div/span/button''').click()
            counter=counter+1
            print(stopc)
            pass
    except Exception:
        print("Internet Error-Stopping Because of Error at" + target[i])
        worksheet.write(row,colu, i+1)
        worksheet.write(row,colu+1, target[i])
        worksheet.write(row,colu+2, "Internet Error,NA")
        row=row+1
        counter=counter+1
        stopc=stopc+1
        print(stopc)
        #workbook.close()
        pass

       
workbook.close()
