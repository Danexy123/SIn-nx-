import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi, 0.1)
y1 = np.sin(x)
y2 = np.sin(2*x)
y3 = np.sin(3*x)
y4 = np.sin(4*x)

plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='sin(2x)')
plt.plot(x, y3, label='sin(3x)')
plt.plot(x, y4, label='sin(4x)')

plt.title('Графики sin(nx) для n=[1, 2, 3, 4]')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()