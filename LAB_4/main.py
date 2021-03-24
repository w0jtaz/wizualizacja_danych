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
class CiagiArytmetyczne():
    a1 = 0
    n = 0
    r = 0
    an = a1+(n-1)*r
    ciag = [a1]
    suma = 0

    def wyswietl_dane(self):
        print(self.ciag)

    def pobierz_elementy(self, *n):
        pobrane_elementy = []
        for x in n:
            pobrane_elementy.append(self.ciag[x-1])
        print(pobrane_elementy)

    def pobierz_parametry(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n

    def policz_sume(self):
        for x in self.ciag:
            self.suma +=x
        print(self.suma)

    def policz_elementy(self):
        if self.r != 0:
            a1 = self.a1
            zakres = self.n-1
            for x in range(zakres):
                an = a1 + self.r
                self.ciag.append(an)
                self.ciag[0] = self.a1
                a1= an

ciag = CiagiArytmetyczne()
ciag.pobierz_parametry(10, 2, 10)
ciag.policz_elementy()
ciag.pobierz_elementy(2, 3, 10)
ciag.policz_sume()
ciag.wyswietl_dane()


#Zadanie 6