import numpy as np
import matplotlib.pyplot as plt

#  init func
x = np.arange(-2, 2, 0.001)
print('Введите нечетное число a, не равное 1')
a = float(input())
print('Введите 0<b<1')
b = float(input())
print('Введите число итераций n')
n = int(input())
s = float(0)

#  drawing
for i in range(0, n+1):
    s += b**i * np.cos(a**i * np.pi * x)
plt.plot(x, s)
plt.show()
