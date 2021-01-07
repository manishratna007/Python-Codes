# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:54:51 2020

@author: user
"""


import os

counter = 0
print("If you want all the excel file, for example write .xlsx")
inp = input("What are you looking for?:> ")
thisdir = os.getcwd()
files=[]
for r, d, f in os.walk(r"C:\Users\user\Desktop\Jb Letter-GR-V7-3010.xlsx"): # change the hard drive, if you want
    for file in f:
        filepath = os.path.join(r, file)
        if inp in file:
        	counter += 1
        	files.append(inp)
        	print(os.path.join(r, file))
print(f"trovati {counter} files.")
#print(counter)

import pandas as pd
df = pd.DataFrame(files)
df.to_excel('Dummy_1610.xlsx',index=False)