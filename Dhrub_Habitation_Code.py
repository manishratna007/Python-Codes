import openpyxl
import os 
import xlsxwriter
from string import ascii_uppercase
import itertools
import os
import re

def iter_all_strings():
    for size in itertools.count(1):
        for s in itertools.product(ascii_uppercase, repeat=size):
            yield "".join(s)
workbook = xlsxwriter.Workbook(r'D:\Dhrub\New_Solution\Revised_Excel_Part_5544.xlsx') 
worksheet = workbook.add_worksheet()
path= r'D:\Dhrub\Test_4'
d='.'
count=0
j=2
vision_length2=2
try:
    for o in os.listdir(path):
        #print(o)
        for filename in os.listdir(os.path.join(path,o)):
            #print("URGENTTTT" + os.path.join(path,o,filename))
            ps = openpyxl.load_workbook(os.path.join(path,o,filename))
            #xls = pd.ExcelFile('Hooghly_Balagarh_Habitation Report.xlsx')
            #for f in range(0,20):
            #   sheet = pd.read_excel(xls, sheet_name=f, na_values='n/a')
            
            ascii=65
            random=1

            for sheet in ps:
                check=0
                t=0
                k=0
                new_sheet_length=vision_length2
                iter_sheet= ps[sheet.title]
                #print ('here too')

                if iter_sheet['A1'].value!=None :
                    print("inside")
                    if iter_sheet['B3'].value!=None and iter_sheet['B5'].value!=None:
                        print(str(iter_sheet['B3'].value) + '_' + str(iter_sheet['B5'].value) + '_' + str(iter_sheet['B8'].value))
                    elif iter_sheet['B3'].value!=None:
                        print(iter_sheet['B3'].value)
                    elif iter_sheet['B5'].value!=None:
                        print(iter_sheet['B5'].value)

                    #print("new_sheet_length " + str(new_sheet_length))
                    #print("vision_length_2 " + str(vision_length2))
                    #print("vision_length1 " + str(vision_length1))
                    list=[]
                    code=0
                    ascii=65
                    value=0

                    for row in range(3, 9):
                        worksheet.write(chr(ascii) + str(new_sheet_length),iter_sheet['B' + str(row)].value)
                        ascii=ascii+1

                    for c,d,e,f,g,h in zip(iter_sheet["A1:A200"],iter_sheet["B1:B200"],iter_sheet["C1:C200"],iter_sheet["D1:D200"],iter_sheet["E1:E200"],iter_sheet["F1:F200"]):
                        value=value+1

                        if c[0].fill.fgColor.rgb =='FFD6DCE4' and d[0].fill.fgColor.rgb =='FFD6DCE4' and e[0].fill.fgColor.rgb =='FFD6DCE4' and f[0].fill.fgColor.rgb =='FFD6DCE4' and g[0].fill.fgColor.rgb =='FFD6DCE4' and  h[0].fill.fgColor.rgb =='FFD6DCE4'and code==1:
                            check=check+1
                            #print("check" + str(check))
                            if check ==11:
                                #print('this isnt possible')
                                for x in iter_all_strings():
                                    k=value+t+1  
                                    vision_length1= new_sheet_length

                                    if x=='G':
                                        break
                                    #print(x)



                                    while type(iter_sheet[x + str(k)]).__name__ != 'MergedCell'  :

                                        if x=='A' and iter_sheet[x + str(k)].fill.fgColor.rgb=='FF2F5496':
                                            #print('break')
                                            break
                                        #print("Master Excel cell")
                                        #print(chr(ascii) + str(new_sheet_length))

                                        worksheet.write(chr(ascii) + str(new_sheet_length),iter_sheet[x + str(k)].value)

                                        #print('eureka')
                                        k=k+1

                                        #print(x + str(k))
                                        new_sheet_length=new_sheet_length+1

                                    vision_length2=new_sheet_length
                                    new_sheet_length=vision_length1
                                    ascii=ascii+1

                                        #
                                ascii=65  
                                random=2

                        elif c[0].fill.fgColor.rgb =='FF2F5496':
                            #print("danger")
                            code=1
                        else:
                            code=0
                else:
                    continue
except:
    print("Not a directory error")
workbook.close()
