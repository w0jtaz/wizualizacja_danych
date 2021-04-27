import numpy as np
import pandas as pd
import xlrd
import openpyxl

#Zadanie 1
xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

#Zadanie 2
print(df[df['Liczba'] < 1000])
print(df[df['Imie'] == 'WOJCIECH'])
print(df.agg({'Liczba':['sum']}))
print(df[((df['Rok'] >= 2005) & (df['Rok'] <= 2010))].agg({'Liczba':['sum']}))
print(df[((df['Rok'] >= 2000) & (df['Plec'] == 'M'))].agg({'Liczba':['sum']}))
print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())
print(df.groupby(['Plec', 'Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'), ascending=False).iloc[[0, 1]])

#Zadanie 3
df = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';')
print(df)
print(set(df['Sprzedawca']))
print(df.sort_values(by='Utarg', ascending=False)[0:5])
print(df.groupby(['Sprzedawca']).size())
print(df.groupby(['Kraj']).agg({'Utarg':['sum']}))
print(df[((df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31') & (df['Kraj'] == 'Polska'))].agg({'Utarg':['sum']}))
print(df[((df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))].agg({'Utarg': ['mean']}))
rok_2004 = df[((df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
rok_2005 = df[((df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31'))]
rok_2004.to_csv("zamowienia_2004.csv", index=False, sep=';')
rok_2005.to_csv("zamowienia_2005.csv", index=False, sep=';')
