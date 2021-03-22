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

    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)
    def ile_produktu(self):
        print(str(self.ilosc) + " " + self.jednostka_miary)
    def ile_kosztuje(self):
        kwota = self.cena_jed * self.ilosc
        print(kwota)

produkt = NaZakupy("Banany", 2, "Kg", 5.99)
produkt.wyswietl_produkt()
produkt.ile_produktu()
produkt.ile_kosztuje()

#Zadanie 5

#Zadanie 6