#Zadanie 1
lista_filmow = ["Piraci z Karaibów", "Kogel Mogel", "Oszukać przeznaczenie", "LOST", "Droga bez powrotu"]
lista_filmow.reverse()
lista_filmow.insert(5, "Jumanji")
lista_filmow.insert(6, "Chłopaki nie płaczą")
lista_filmow.insert(7, "Harry Potter")
lista_filmow.insert(8, "Epoka Lodowcowa")
lista_filmow.insert(9, "Poranek Kojota")
print(lista_filmow)
print(len(lista_filmow))

#Zadanie 2
filmy = {"przygodowy1": "Piraci z Karaibów", "komedia1": "Kogel Mogel", "fabularny": "Oszukać przeznaczenie", "serial": "LOST", "horror": "Droga bez powrotu", "przygodowy2": "Jumanji", "komedia2": "Chłopaki nie płaczą", "fantastyczny": "Harry Potter", "animowany": "Epoka Lodowcowa", "komedia3": "Poranek Kojota"}
print(filmy)

#Zadanie 3
przedmioty = {"CKWP": "CAD Komputerowe wspomaganie projektowania", "AMDI": "Analiza matematyczna dla informatyków", "JI": "Język angielski", "MDDI": "Matematyki dyskretna dla informatyków", "WOT": "Wiedza o teatrze", "PS": "Programowanie strukturalne", "WD": "Wizualizacja danych"}
print(przedmioty)
print(przedmioty.keys())
print(przedmioty.values())
print("Liczba elementów w słowniku przedmioty:",len(przedmioty))

#Zadanie 4
liczba = input("Podaj liczbe: ")
liczba = float(liczba)**(float(liczba))
print(liczba)

#Zadanie 5
import sys as system
system.stdout.write("Podaj dowolny ciąg znaków: ")
ciag_znakow = system.stdin.readline()
ilosc_wystapien = ciag_znakow.count("a")
system.stdout.write("Ilość wystąpień litery a: "+str(ilosc_wystapien)+"\n")

#Zadanie 6
a = int(input("Podaj liczbę: "))
b = int(input("Podaj liczbę: "))
c = int(input("Podaj liczbę: "))

if(a%2 == 0):
    print("Liczba a jest parzysta")
    if(b > c):
        print("Liczba b jest większa od c")
else:
    print("Liczba a nie jest parzysta lub liczba b jest mniejsza od c")

#Zadanie 7
liczby = [1, 2, 3.5, 5, 6.2, 7.1, 8, 9.4, 10, 11.9]
for x in range(0, len(liczby)-1):
    suma = liczby[x] + liczby[x+1]
    print(suma)

#Zadanie 8
licznik = 0
lista_liczb = []
while licznik < 10:
    licznik += 1
    liczba = int(input("Podaj liczbe: "))
    if liczba %2 == 0:
        lista_liczb.insert(licznik, liczba)
print(lista_liczb)

#Zadanie 9
for i in range(6):
    for j in range(6):
        if (i == 0 or i == 5) or (j == 0 or j == 5):
            if j == 5:
                print('O')
            else:
                print('O', end='')
        else:
            print(' ', end='')

#Zadanie 10
x = input("Podaj liczbę: ")
try:
    liczba = float(x)
    print(liczba)
except ValueError:
    print("Wprowadzono literę zamiast liczby!")