import numpy as np
from random import randint


def norm(m):
    mmax = m.max()
    mmin = m.min()
    a = m.shape
    b = m.copy()
    b = b.reshape(np.sum(a))
    for i in range(len(b)):
        b[i] = (b[i] - mmin) / (mmax - mmin)
    b = b.reshape(a)
    return b


n = np.array([float(randint(0, 10)) for i in range(10)])
print(n)
print(norm(n))
