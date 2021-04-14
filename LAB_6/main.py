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
print(potega(2, 8))


