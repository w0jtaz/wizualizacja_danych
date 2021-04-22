import numpy as np

#Zadanie 1
a = np.array([2,3,4,5])
b = np.array([12,1,-7,2])
c = a*b
print(c)

#Zadanie 2
a = np.array([[2,1,3], [-1,2,4], [-8,4,5]])
b = np.array([[-2,-1,-3,7], [-1,2,4,5], [8,4,5,12], [1,2,3,4]])

print('minimalne wartosci dla kolumn',a.min(axis=0))
print('minimalne wartosci dla wierszy',a.min(axis=1))

print('minimalne wartosci dla kolumn',b.min(axis=0))
print('minimalne wartosci dla wierszy',b.min(axis=1))

#Zadanie 3
a = np.array([2,3,4,5])
b = np.array([12,1,-7,2])
print(np.dot(a,b))

#Zadanie 4
e = np.array([1, 5, 10])
f = np.array([5.5, 6.6, 7.7])
print(e*f)

#Zadanie 5
g = np.array([[4, 8, 12], [6, 4, 0]])
a5 = np.sin(g)
print(a5)

#Zadanie 6
h = np.array([[10, 15, 0], [1, 0, 33]])
b6 = np.cos(h)
print(b6)

#Zadanie 7
print(np.add(a5,b6))

#Zadanie 8
i = np.arange(0, 50, 6).reshape(3, 3)

for x in i:
    print(x)

#Zadanie 9
j = np.arange(50, 150, 12).reshape(3, 3)

for x in j.flat:
    print(x)

#Zadanie 10
k = np.arange(81).reshape(9, 9)
print(k)
print(k.reshape(81, 1))
print(k.reshape(1, 81))
