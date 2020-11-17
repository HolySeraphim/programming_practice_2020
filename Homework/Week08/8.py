import numpy as np
from random import randint
A = np.array([[randint(0, 10) for i in range(10)]])
B = randint(0, 10)
print(A, B)
c = A.copy()
c = c.reshape(np.prod(A.shape))
for i in range(len(c)):
    c[i] -= B
d = c.copy()
for i in range(len(d)):
    d[i] = abs(d[i])
print(c[d.argmin()]+B)
