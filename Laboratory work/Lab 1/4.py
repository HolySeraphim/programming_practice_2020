import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10, 10.01, 0.01)
func = input()
with plt.xkcd():
    plt.plot(x, eval(func))
    plt.show()
