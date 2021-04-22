import numpy as np
import pandas as pd
import xlrd
import openpyxl

#series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s = pd.Series([10, 13, 8, 14], index=['Liczba1', 'Liczba2', 'Liczba3', 'Liczba4'])
print(s)

#dataframe
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [111232323, 32333232, 3232323]}
df = pd.DataFrame(data)
print(df)
#data frame przechowuje typ dla każdej z kolumn i możemy go sprawdzić następująco
print(df.dtypes)

#możemy stworzyć serie danych
daty = pd.date_range('20210422', periods=5)
print(daty)
df = pd.DataFrame(np.random.randn(5,4), index=daty, columns=list('ABCD'))
print(df)

#pandas umożliwia tworzenie dataframe z zewnętrznych źródeł np plik.csv
df = pd.read_csv('wyniki.csv', header=0, sep=';')
print(df)
df.to_csv('wyniki2.csv', index=False)

xlsx = pd.ExcelFile('wyniki.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
df.to_excel('plik.xlsx', sheet_name='arkusz pierwszy')

s = pd.Series([10, 13, 8, 14], index=['Liczba1', 'Liczba2', 'Liczba3', 'Liczba4'])
print(s)

#dataframe
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [111232323, 32333232, 3232323]}
df = pd.DataFrame(data)
#pobieranie elementów z serii
print(s['Liczba1'])
print(s.Liczba1)
#pojedynczy elment z ramki danych
print(df[0:1])
print(df['Populacja'])
print(df.iloc[[0][0]])
print(df.loc[[0],['Kraj']])
print(df.at[0, 'Kraj'])
print('kraj: ' + df.Kraj)

#mamy też możliwość losowego pobierania elementów z ramki danych lub w odniesieniu do procentowej wartości całego zbioru
#jeden element losowy z dataframe
print(df.sample())
print(df.sample(2))
print(df.sample(frac=0.5))
print("")
print(df.sample(n=10, replace=True))
#wyświetlanie wierszy od początku
print(df.head())
print(df.head(2))
#wyświetlanie wierszy od końca
print(df.tail(1))

print(df.describe())
print(df.T)

print(s[s>9])
print(s.where(s>10, 'za duże'))
seria = s.copy()
seria.where(s>10, 'za duże', inplace=True)
print(seria)

print(s[~(s>10)])
print(s[(s>8) & (s<14)])

s['Liczba2'] = 15
print(s)

#dodawanie kolejnego indeksu, trafia na koniec
s['Liczba5'] = 16
print(s)

print(df[df['Populacja']>12000000])
print(df[((df.Populacja)>1000000) & (df.index.isin([0,2]))])

szukaj = ['Belgia', 'Brasilia']
print(df.isin(szukaj))

df.loc[3] = 'dodana'
print(df)

#dodawanie elementu do ramki danych
df.loc[4] = ['Polska', 'Warszawa', 1765467]
print(df)

#usuwanie elementu na kopi
new_df = df.drop([3])
print(new_df)
#usuwanie elementu na oryginale
df.drop([3], inplace=True)
print(df)


df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
print(df.sort_values(by='Kraj')) #sortowanie
#grupowanie
grouped = df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))

print(df.groupby(['Kontynent']).agg({'Populacja' : ['sum']}))
