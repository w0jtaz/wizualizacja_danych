#Zadanie 1
liczba_calkowita1 = 7
liczba_calkowita2 = 20
print("Liczby całkowite (typ int): ", liczba_calkowita1,",", liczba_calkowita2)
print(type(liczba_calkowita1))

liczba_rzeczywista1 = 7.5
liczba_rzeczywista2 = 6.9
print("Liczby rzeczywiste (typ float): ", liczba_rzeczywista1,",", liczba_rzeczywista2)
print(type(liczba_rzeczywista1))

liczba_zespolona1 = 3 + 5j
liczba_zespolona2 = 9 + 2j
print("Liczby zespolone (typ complex): ", liczba_zespolona1,",", liczba_zespolona2)
print(type(liczba_zespolona1))

napis1 = "Python"
napis2 = "Java"
print("Napisy (typ string): ", napis1,",", napis2)
print(type(napis1))

#Zadanie 2
a = input("Podaj liczbe: ")
b = input("Podaj liczbe: ")
operator = input("Podaj operator: ")
if operator == "+": print(float(a) + float(b))
if operator == "-": print(float(a) - float(b))
if operator == "*": print(float(a) * float(b))
if operator == "/" : print(float(a) / float(b))
if operator == "**": print(float(a) ** float(b))
if operator == "%": print(float(a) % float(b))

#Zadanie 3
a = 5
a += 5
print(a)

a = 5
a -= 5
print(a)

a = 5
a *= 5
print(a)

a = 5
a /= 5
print(a)

a = 5
a **= 5
print(a)

a = 5
a %= 5
print(a)

#Zadanie 4
import math
przyklad1 = print(math.e ** 10)
przyklad2 = print(math.log (5 + (math.sin(2))*8)**1/6)
przyklad3 = print(math.floor(3.55))
przyklad4 = print(math.ceil(4.80))

#Zadanie 5
imie = "WOJTEK"
nazwisko = "KOWALCZYK"
print(imie.capitalize(), nazwisko.capitalize())

#Zadanie 6
tekst = "Ty co nie lubisz traw pif paf, pif pif paf"
print("Wystąpienia słowa paf w tekście: ",tekst.count("pif"))

#Zadanie 7
zmienna = "europarlamentarzysta"
print("Druga litera to: ",zmienna[1]+"\n""Ostatnia litera to: ", zmienna[int(len(zmienna)-1)])

#Zadanie 8
tekst = "Ty co nie lubisz traw pif paf, pif pif paf"
print(tekst.split())

#Zadanie 9
zmienna1 = "pechowa liczba"
zmienna2 = 5.0
zmienna3 = "4F9"
print("Powszechnie znana %s to 13" %(zmienna1))
print(u"Średnia %.1f to marzenie każdego studenta" %(zmienna2))
print("Liczba dziesiętna 1273 w postaci szesnastkowej jest równa: %s" %(zmienna3))






