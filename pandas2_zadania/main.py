import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zadanie 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
grupa = df.groupby(['Rok']).agg({'Liczba': ['sum']})
print(grupa)
grupa.plot()
plt.title('Liczba urodzeń')
plt.show()

#Zadanie 2
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
grupa = df.groupby(['Plec']).agg({'Liczba': ['sum']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_xlabel('Płeć')
wykres.set_ylabel('Mld')
wykres.legend()
plt.xticks(rotation=0)
plt.title('Liczba urodzeń z podziałem na płeć')
plt.legend(loc='upper left')
plt.show()

#Zadanie 3
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
grupa = df.groupby(['Plec']).agg({'Liczba': ['sum']})
print(grupa)
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6,6), legend=(0,0))
plt.legend(loc='lower right')
plt.title('Liczba urodzeń z podziałem na płeć')
plt.show()

#Zadanie 4
dane = pd.read_csv("zamowienia.csv",sep=';')
suma =  dane.groupby('Sprzedawca').agg({'Utarg':['sum']})
suma.plot.bar()
plt.xticks(rotation=0)
plt.show()