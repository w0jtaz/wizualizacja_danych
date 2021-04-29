import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zadanie 1
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# grupa = df.groupby(['Rok']).agg({'Liczba': ['sum']})
# print(grupa)
# grupa.plot()
# plt.title('Liczba urodzeń')
# plt.show()

#Zadanie 2
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# grupa = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# print(grupa)
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Płeć')
# wykres.set_ylabel('Mld')
# wykres.legend()
# plt.xticks(rotation=0)
# plt.title('Liczba urodzeń z podziałem na płeć')
# plt.legend(loc='upper left')
# plt.show()