import numpy as np
from random import randint
A = np.array([[randint(0, 10) for i in range(randint(1, 20))]]*randint(1, 20))
B = randint(0, 10)
D = randint(0, 10)
print(A, '\n', B, D)


def ret(a, b, d):
    for i in range(len(a[0])):
        a[0][i] = b
    for i in range(len(a[len(a)-1])):
        a[len(a)-1][i] = b
    for i in range(len(a)):
        a[i][0] = b
        a[i][len(a[i])-1] = b
    for i in range(1, len(a)-1):
        for j in range(1, len(a[0])-1):
            a[i][j] = d


ret(A, B, D)
print('\n', A)

