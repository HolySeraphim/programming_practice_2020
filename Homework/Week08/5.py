import numpy as np


def f1(b):
    if len(b.shape) == 1:
        s, c = 0, 0
        for i in b:
            if str(i) != str(np.nan):
                s += i
                c += 1
        return [s, c]
    else:
        s, c = 0, 0
        for i in b:
            m = f1(i)
            s += m[0]
            c += m[1]
        return [s, c]


def f2(a, c):
    if(len(a.shape)) == 1:
        for i in range(a.size):
            if str(a[i]) == str(np.nan):
                a[i] = c
    else:
        for i in a:
            f2(i, c)


def change(d):
    d = d.copy()
    c = f1(d)
    if c[1] != 0:
        c = c[0] / c[1]
    else:
        c = 0
    f2(d, c)
    return d


e = np.array([[[7, 1, 12], [12, np.nan, 4]], [[np.nan, 2, 2], [3, 2, np.nan]]])
print(e, '\n', change(e))
