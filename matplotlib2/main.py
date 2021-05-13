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
x = np.sin(t)*np.cos(t)
y = np.tan(t)
ax.plot(x,y,z, label='Pierwszy przykład')
ax.legend()
plt.show()

#wykres 3d punktowy
np.random.seed(19680801)
def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100
for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)
ax.set_xlabel('oś x')
ax.set_ylabel('oś y')
ax.set_zlabel('oś z')
plt.show()

#wykres powierzchniowy 3d
fig = plt.figure()
ax = fig.gca(projection='3d')
#generujemy dane
x= np.arange(-5, 5, 0.25)
y= np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)
surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.2f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

#wykres kolumnowy 3d
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x+y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax1.set_title('Wykres zacieniony')
ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
ax2.set_title('Wykres niezacieniony')
plt.show()

#wiele wykresów w jednym wywołaniu
fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(121, projection='3d')
x= np.arange(-5, 5, 0.25)
y= np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)
surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
fig.colorbar(surf, shrink=0.5, aspect=5)
ax = fig.add_subplot(122, projection='3d')
x, y, z = get_test_data()
ax.plot_wireframe(x, y, z, rstride=10, cstride=10)
plt.show()


#
fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.linspace(0, 1, 100)
y = np.sin(x * 2* np.pi)/2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='curve in (x,y')
colors = ('r', 'g', 'b', 'k')
np.random.seed(198680801)
x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
c_list = []
for c in colors:
    c_list.extend([c] * 20)
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x,z)')
ax.legend()
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_zlim(0,1)
ax.set_xlabel('oś x')
ax.set_xlabel('oś x')
ax.set_ylabel('oś y')
ax.set_zlabel('oś z')
ax.view_init(elev=20., azim=-35)
plt.show()
