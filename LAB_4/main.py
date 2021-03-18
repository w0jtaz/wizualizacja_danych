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
