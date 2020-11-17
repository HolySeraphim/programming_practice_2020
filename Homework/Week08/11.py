import numpy as np


def ch(a, b):
    m = np.full((a, b), 0)
    for i in range(0, a):
        for j in range(0, b):
            if i % 2 + j % 2 == 1:
                m[i][j] = 1
    print(m)


A = int(input())
B = int(input())
ch(A, B)
