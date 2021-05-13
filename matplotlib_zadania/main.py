import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# #Zadanie 1
#
# x = np.linspace(1, 21, 20)
# plt.plot(x, 1/x, label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Wykres funkcji f(x) dla x [1,20]')
# plt.legend()
# plt.show()
#
# #Zadanie 2
# x = [1/x for x in range(1, 21)]
# plt.axis([0, 20, 0, 1])
# plt.plot(x, 'g^--', label='f(x)=1/x')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Wykres funkcji f(x)= 1/x w przedziale [1,20]')
# plt.show()

# #Zadanie 3
# x = np.arange(0.0, 30.0, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# plt.subplot(3, 2, 1)
# plt.plot(x, y1, '-')
# plt.title('Wartość sinusa')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(3, 2, 5)
# plt.plot(x, y2, 'r-')
# plt.title('Wartość cosinusa')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.show()

#Zadanie 4
x = np.arange(0, 30, 0.1)
y1 = np.sin(-x)
y2 = np.sin(x)+2

plt.plot(x, y1, '-',  label='sin(x)')
plt.plot(x, y2, '-',  label='sin(x)')
plt.title('Wartość sin(x), sin(x)')
plt.legend(loc=6)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()

