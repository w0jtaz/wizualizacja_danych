#Zadanie 1
A = [(1-x) for x in range(1,10)]
print(A)
B =  [(4)**x for x in range(1,8)]
print(B)
C =  [x for x in B if x%2 in [0,2,4,6,8]]
print(C)

#Zadanie 2
import random
lista1 = []
for x in range(10):
    lista1.append(random.randint(1, 100))
print(lista1)

lista1_parzysta = [x for x in lista1 if x%2 ==0]
print(lista1_parzysta)

#Zadanie 3
produkty = {"jabłka": "kilogramy",
            "batony": "sztuki",
            "mleko": "litry",
            "ciastka": "dekagramy",}
print(produkty)
produkty_odwrocone = {value: key for key, value in produkty.items()}
print(produkty_odwrocone)

#Zadanie 4
def czy_prostokatny(a, b, c):
    if a>b and a>c:
        if b**(2) + c**(2) == a**(2):
            print("Trójkąt jest prostokątny")
        else:
            print("Trójkąt nie jest prostokątny")
    if b>a and b>c:
        if a**(2) + c**(2) == b**(2):
            print("Trójkąt jest prostokątny")
        else:
            print("Trójkąt nie jest prostokątny")
    if c>b and c>a:
        if a**(2) + b**(2) == c**(2):
            print("Trójkąt jest prostokątny")
        else:
            print("Trójkąt nie jest prostokątny")
print(czy_prostokatny(3,4,5))

#Zadanie 5
def pole_trapezu(a=0, b=0, h=0):
    pole = ((a+b)*h)/2
    print("Pole trapezu wynosi:",pole)

pole_trapezu()
pole_trapezu(3,4,5)

#Zadanie 6

def iloczyn_ciagu(a=1, b=4, ile=10):
    ciag = []
    for x in range(a-1,ile):
        ciag.append(a*b**(x))
    print(ciag)
    return ciag[x-9]*ciag[x-8]*ciag[x-7]*ciag[x-6]*ciag[x-5]*ciag[x-4]*ciag[x-3]*ciag[x-2]*ciag[x-1]*ciag[x]

print(iloczyn_ciagu(1,4,10))

#Zadanie 7


#Zadanie 8
def zakupy(**koszyk):
    przedmioty = len(koszyk)
    if przedmioty != 0:
        suma = 0
        ceny = [cena for cena in koszyk.values() if isinstance(cena, float) == True or isinstance(cena, int) == True]
        for x in range (len(ceny)):
            suma+=float(ceny[x])
    else:
        return "Nie wprowadzono zakupów"

    print(suma,"zł")
    return len(koszyk)

print(zakupy(cola = 4, piwo= 3.5, chipsy = 4, gumy = 2, gazeta = 5))

#Zadanie 9
from ciagi import *