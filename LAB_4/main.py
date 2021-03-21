#Zadanie 1
import random
liczby = []
for x in range(10):
    liczby.append(random.randint(0, 30))
    liczby[x] = liczby[x] * 2
print(liczby)
plik = open('liczby.txt', 'w+')
plik.write(str(liczby))
plik.close()

#Zadanie 2
plik = open('liczby.txt', 'r')
print(plik.readlines())

#Zadanie 3
with open('python.txt', 'r') as plik:
    for linia in plik:
        print(linia, end='')

#Zadanie 4
class NaZakupy():
    nazwa_produktu = ""
    ilosc = 0
    jednostka_miary = ""
    cena_jed = 0
    produkt = NaZakupy()
    def wyswietl_produkt(self):
        return produkt.nazwa_produktu
    def ile_produktu(self):
        return produkt.ilosc, produkt.jednostka_miary
    def ile_kosztuje(self):
        return produkt.cena_jed * produkt.ilosc

