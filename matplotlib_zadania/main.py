import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zadanie 1

# x = np.linspace(1, 21, 20)
# plt.plot(x, 1/x, label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Wykres funkcji f(x) dla x [1,20]')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.show()

#Zadanie 2
# x = [1/x for x in range(1, 21)]
# plt.axis([0, 20, 0, 1])
# plt.plot(x, 'g^--', label='f(x)=1/x')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Wykres funkcji f(x)= 1/x w przedziale [1,20]')
# plt.show()

# #Zadanie 3
# x = np.arange(0.0, 30.0, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# plt.subplot(3, 2, 1)
# plt.plot(x, y1, '-')
# plt.title('Wartość sinusa')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(3, 2, 5)
# plt.plot(x, y2, 'r-')
# plt.title('Wartość cosinusa')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.show()

# #Zadanie 4
# x = np.arange(0, 30, 0.1)
# y1 = np.sin(-x)
# y2 = np.sin(x)+2
#
# plt.plot(x, y1, '-',  label='sin(x)')
# plt.plot(x, y2, '-',  label='sin(x)')
# plt.title('Wartość sin(x), sin(x)')
# plt.legend(loc=6)
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.show()

# #Zadanie 5
# df = pd.read_csv("iris.data", names=["sepal len", "sepal wid", "petal len", "petal wid", "class"])
# df = pd.DataFrame(df)
# df = df[["sepal len", "sepal wid", "class"]]
# plt.xlabel("sepal length")
# plt.ylabel("sepal width")
# data = {"a": df["sepal len"], "b": df["sepal wid"], "c": np.random.randint(0, 150, 150)}
# data["d"] = np.abs(data["a"]-data["b"])*5
# plt.scatter("a", "b", c="c", s="d", data=data)
# plt.title("Iris sepal length and width")
# plt.show()

#Zadanie 6
data = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(data, header=0)
print(df)
plt.subplot(1, 3, 1)
grouped = df.groupby('Plec').agg({'Liczba': ['sum']}).unstack()
grouped.plot.bar(color=['r', 'g'])
plt.xlabel('Płeć')

# wykres 2
plt.subplot(1, 3, 2)
x = df['Rok'].unique()
kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
plt.plot(x, kobiety, label="Kobiety")
plt.plot(x, mezczyzni, label="Mężczyźni")
plt.ylabel('Liczba narodzonych dzieci')

# wykres 3
plt.subplot(1, 3, 3)
x = df['Rok'].unique()
# bez funkcji flatten matplotlib wyrzuca wyjątek, który informuje nas, że nie można
# przekazywać parametru jako tablicy wielowymiarowej a w takiej postaci w tym przypadku
# zwracany jest wektor y, korzystamy więc z flatten() poznanej przy okazji omawiania biblioteki numpy
y = df.groupby('Rok').agg({'Liczba':['sum']}).values.flatten()

plt.bar(x, y)

# wyświetlamy cały wykres
plt.show()

#Zadanie 7
df = pd.read_csv('zamowienia.csv', sep=';')
policzone = df.groupby('Sprzedawca')['Utarg'].sum()
# explode
explode = [0.0 for n in range(len(policzone.index))]
# określamy które kawałki i o ile wysunąć, tu losujemy jeden
explode[np.random.randint(0, len(policzone.index))] = 0.2
policzone.plot.pie(subplots=True, autopct='%.2f %%', fontsize=8, explode=explode, shadow=True)
plt.title("Procentowy udział kwot zamówień sprzedawców")
plt.show()