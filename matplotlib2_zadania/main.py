import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data

fig = plt.figure()
ax = fig.gca(projection='3d')
t = np.linspace(0, 2*np.pi, 100)
z = t
x = np.sin(z)
y = 2*np.cos(z)
ax.plot(x,y,z, label='Wykres liniowy 3d')
ax.legend()
plt.show()

