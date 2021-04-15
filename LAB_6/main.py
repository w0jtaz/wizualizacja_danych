import numpy as np

#Zadanie 1
ile = (4*20+1)
a = np.arange(4,ile, 4)
print(a)

#Zadanie 2
lista = np.array([0.2, 1.3, 2.4])
print(lista)
print(lista.dtype)

lista2 = lista.astype('int32')
print(lista2)
print(lista2.dtype)

#Zadanie 3
def tablica(n):
    a = [2**x for x in range(n*n)]
    return np.array(a).reshape(n,n)

print(tablica(4))

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
malina = np.array(list('malina'))
mrowka = np.array(list('mrówka'))
armata = np.array(list('armata'))
wykreslanka = np.diag(mrowka)
wykreslanka[:, 0] = malina
wykreslanka[5,::-1] = armata
wykreslanka[5,:] = armata
print(wykreslanka)

#Zadanie 7
def foo7(n):
    macierz = np.diag([2 for _ in range(n)])
    for indeks in range(1,n):
        vec = [2+(2*indeks) for _ in range(n-indeks)]
        macierz += np.diag(vec, indeks)
        macierz += np.diag(vec, -indeks)
    print(macierz)

foo7(4)

#Zadanie 8
def zad8(tab, kierunek='poziomo'):
    print(tab)
    if kierunek == 'poziomo':
        # nieparzysta liczba wierszy
        if tab.shape[0] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę wierszy")
            return
        p1 = tab[0:int(tab.shape[0]/2), :]
        p2 = tab[int(tab.shape[0]/2):, :]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)
    elif kierunek == "pionowo":
        if tab.shape[1] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę kolumn")
            return
        p1 = tab[:, 0:int(tab.shape[1]/2)]
        p2 = tab[:, int(tab.shape[1] / 2):]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)

zad8(np.arange(36).reshape((6,6)), kierunek='pionowo')

#Zadanie 9
def ciag_arytmetyczny(a, r, n=25):
    lista = []
    lista.append(a)
    index = 1
    while index != n:
        a = a + r
        lista.append(a)
        index += 1
    return lista

macierz = np.array(ciag_arytmetyczny(2,3)).reshape((5,5))
print(macierz)