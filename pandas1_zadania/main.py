import numpy as np
import pandas as pd
import xlrd
import openpyxl

#Zadanie 1
xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

#Zadanie 2