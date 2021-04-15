import numpy as np
#inicjalizacja danych
a = np.array([20,30,40,50])
b = np.arange(4)

print(a)
print(b)
#wykonane będzie działanie i zapisane do nowej zmiennej
c = a-b
print(c)
#wykonanie operacji kwadrat zawartości
print(b**2)

# a += b
# print(a)
a -= b
print(a)

a = np.arange(12).reshape(3,4)
print(a)
#suma całej macierzy
print(a.sum())
#suma każdej z kolumn
print(a.sum(axis=0))
#wartość minimalna dla każdego z wierszy
print(a.min(axis=1))
#suma skumulowana dla wierszy
print(a.cumsum(axis=1))

#mnożenie
a = np.arange(3)
b = np.arange(3)
print(a)
print(b)
print(a.dot(b))
print(np.dot(a,b))

a = np.array([[2,1,3], [-1,2,4]])
b = np.array([[1,3], [2,-2], [-1,4]])
print(a)
print(b)
print(a.dot(b))


a = np.ones(3, dtype='int32')
print(a)
print(a.dtype)
b = np.linspace(0, np.pi, 3)
print(b)
print(b.dtype)

c = a + b
print(c)
print(c.dtype)

d = np.exp(c*1j)
print(d)
print(d.dtype)

b = np.arange(3)
print(b)
print(np.exp(b))
print(np.sqrt(b))

c = np.array([2., -1., 4.])
print(np.add(b,c))


a = np.arange(6).reshape(3,2)
print(a)
for b in a:
    print(b)
    print("")

a = np.arange(6).reshape(3, 2)
print(a)
for b in a.flat:
    print(b)
    print("")

#rozmiary macierzy 1x6, 1xilość elementów w tablicy 1wymiarowej
a = np.arange(6)
print(a)
print(a.shape)
#zmiana rozmiaru macierzy na 3x2
b = a.reshape((3,2))
print(b)
print(b.shape)
print("")
c = a.reshape((2,3))
print(c)
print(c.shape)
#spłaszczanie macierzy
d = c.ravel()
print(d)

#transpozycja
e = c.T
print(e)
print(e.shape)