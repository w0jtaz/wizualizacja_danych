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

