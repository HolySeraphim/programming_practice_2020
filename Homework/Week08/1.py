#  y scale = log

import numpy as np
from random import random as rand
from time import time as current_time
import matplotlib.pyplot as plt


def np_1(n):
    t_start = current_time()
    x, y = [np.random.sample(n) for i in range(2)]
    z = 2 * x**2 + 4 * y
    return current_time() - t_start


def py_1(n):
    t_start = current_time()
    x, y = [[rand() for i in range(n)] for j in range(2)]
    z = []
    for i, j in zip(x, y):
        z.append(2*i**2 + 4*j)
    return current_time() - t_start


def np_2(n):
    t_start = current_time()
    x, y = [np.random.sample((n,n)) for i in range(2)]
    z = np.dot(x, y)
    return current_time() - t_start


def py_2(n):
    t_start = current_time()
    x, y = [[[rand() for i in range(n)] for j in range(n)] for k in range(2)]
    z = []
    for i in range(n):
        t1 = []
        for j in range(n):
            t1.append(sum([x[i][s] * y[s][j] for s in range(n)]))
        z.append(t1)
    return current_time() - t_start


def research(n1, n2, step, m):
    res_np_1, res_np_2, res_py_1, res_py_2 = [], [], [], []
    for i in range(1, n1, step):
        s_np, s_py = 0, 0
        for ep in range(m):
            s_np += np_1(i)
            s_py += py_1(i)
        res_np_1.append(s_np / m)
        res_py_1.append(s_py / m)

    for i in range(1, n2, step):
        s_np, s_py = 0, 0
        for ep in range(m):
            s_np += np_2(i)
            s_py += py_2(i)
        res_np_2.append(s_np / m)
        res_py_2.append(s_py / m)

    plt.subplot(121)
    plt.yscale('log')
    plt.plot(range(1, n1, step), res_np_1, color='b')
    plt.plot(range(1, n1, step), res_py_1, color='r')

    plt.subplot(122)
    plt.yscale('log')
    plt.plot(range(1, n2, step), res_np_2, color='b')
    plt.plot(range(1, n2, step), res_py_2, color='r')
    plt.show()


research(1000, 100, 10, 50)