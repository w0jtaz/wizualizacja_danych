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
