def element_n_ciagu_geometrycznego(a1, q, n):
    return a1 * q ** (n - 1)

def suma_ciagu_geometrycznego(a1, n, q = 1):
    if(q == 1):
        return n * a1
    return a1 * ((1 - q ** n) / (1 - q))

def wyraz_srodkowy_ciagu_geometrycznego(a, b):
    return sqrt(a * b)