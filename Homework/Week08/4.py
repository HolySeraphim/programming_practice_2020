import numpy as np
from random import randint
a = randint(10, 100)
m = np.random.random((a, a))
print(m.max(), m.sum())
a = m.max()
for i in m:
    for j in i:
        j /= a
for i in m:
    a = i.mean()
    for j in i:
        j -= a
a = m.max()
for i in m:
    for j in i:
        if j == a:
            j = -1
