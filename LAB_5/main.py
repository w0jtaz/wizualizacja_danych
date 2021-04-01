#Zadanie 1

class Material():
    rodzaj = None
    dlugosc = None
    szerokosc = None

    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self. szerokosc = szerokosc

    def wyswietl_nazwe(self, nazwa):
        self.nazwa = nazwa
        print("Nazwa: "+nazwa)

class Ubrania(Material):
    rozmiar = None
    kolor = None
    dla_kogo = None

    def wyswietl_dane(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo
        print("Rozmiar: "+str(rozmiar)+", Kolor: "+str(kolor)+", Dla kogo: "+dla_kogo)

class Sweter(Ubrania):
    rodzaj_swetra = None

    def wyswietl_dane(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra
        print("Rodzaj: "+rodzaj_swetra)

material = Material("bawełna", 60, 40)
material.wyswietl_nazwe("bawełna")
spodnie = Ubrania("spodnie", 80, 40)
spodnie.wyswietl_dane("L", "czarny", "dla mamy")
sweterek = Sweter("swetr", 60, 42)
sweterek.wyswietl_dane("rozpinany")


cieply_sweter = Sweter("ciepły", 60, 45)
cieply_sweter.wyswietl_dane("ciepły")
cieply_sweter.wyswietl_nazwe("Cieplutki sweterek")
cieply_sweter.kolor = "niebieski"
cieply_sweter.dla_kogo = "dla taty"
print(cieply_sweter.kolor)
print(cieply_sweter.dla_kogo)

#Zadanie 2
class Kwadrat():

    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return "Kwadrat o długości boku równej {}".format(self.x)

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, tekst):
        self.opis = tekst

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik

    def __add__(self, other):
       return self.pole() + self.obwod()

kwadrat = Kwadrat(5)
print(kwadrat)

kwadrat2 = Kwadrat(kwadrat.pole()+kwadrat.obwod())
print(kwadrat2)