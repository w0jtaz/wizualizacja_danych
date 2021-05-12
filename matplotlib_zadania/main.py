import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zadanie 1

x = np.linspace(1, 21, 20)
plt.plot(x, 1/x, 'g^', label='f(x) = 1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x) dla x [1,20]')
plt.legend()
plt.show()