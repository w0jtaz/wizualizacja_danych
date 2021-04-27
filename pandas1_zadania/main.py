import numpy as np
import pandas as pd
import xlrd
import openpyxl

#Zadanie 1
xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
# print(df)

#Zadanie 2
# print(df[df['Liczba'] < 1000])
# print(df[df['Imie'] == 'WOJCIECH'])
# print(df.agg({'Liczba':['sum']}))
# print(df[((df['Rok'] >= 2005) & (df['Rok'] <= 2010))].agg({'Liczba':['sum']}))
# print(df[((df['Rok'] >= 2000) & (df['Plec'] == 'M'))].agg({'Liczba':['sum']}))
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())
# print(df.groupby(['Plec', 'Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'), ascending=False).iloc[[0, 1]])

