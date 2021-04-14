import numpy as np

#Zadanie 1
ile = (4*20)
a = np.arange(0,ile, 4)
print(a)

#Zadanie 2
lista = np.array([0.2, 1.3, 2.4])
print(lista)
print(lista.dtype)

lista2 = lista.astype('int32')
print(lista2)
print(lista2.dtype)

#Zadanie 3
def tablica(n : int):
    a = 2**np.mgrid[1:n+1, 1:n+1]
    return a

print(tablica(20))

#Zadanie 4
def potega(n, m):
    a = np.logspace(start=1,num=m, stop=m, base=n, dtype='int')
    return a
print(potega(2, 4))

#Zadanie 5
def wektor(dlugosc):
    macierz = np.diag([x for x in range(dlugosc, 0, -1)], 2)
    return macierz

print(wektor(8))

#Zadanie 6
tab = np.array([['P', 'I', 'W', 'O'], ['O', 'I', 'E', 'K'], ['L', 'A', 'E', 'A'], ['E', 'L', 'K', 'S']])
print(tab)

#Zadanie 7

#Zadanie 8

#Zadanie 9
ciag = np.arange(1, 125, 5)
ciag = ciag.reshape((5,5))
print(ciag)
