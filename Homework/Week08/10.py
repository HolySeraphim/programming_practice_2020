import numpy as np
from random import randint
A = np.array([[randint(0, 10) for i in range(10)] for i in range(10)])
B = randint(0, 9)
print(A, '\n', B)


def s(a, b):
    for j in range(len(a)-1):
        for i in range(0, len(a)-1):
            if a[i][b] < a[i+1][b]:
                c = a[i].copy()
                a[i] = a[i+1]
                a[i+1] = c
    print('\n', a)


s(A, B)
