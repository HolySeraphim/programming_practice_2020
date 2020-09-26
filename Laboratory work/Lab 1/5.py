import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
plt.errorbar(x, y, xerr=0.05, yerr=0.1)


p, v = np.polyfit(x, y, deg=1, cov=True)
p_f = np.poly1d(p)

p1, v1 = np.polyfit(x, y, deg=2, cov=True)
p_f1 = np.poly1d(p1)

plt.plot(x, y, 'o--', x, p_f(x), x, p_f1(x))

plt.grid()
plt.show()
