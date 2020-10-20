def count(a, t):
    if t == 'main':
        c = 0
        for i in range(len(a)):
            c += a[i][i]
        return c
    else:
        c = 0
        for i in range(len(a)):
            c += a[i][len(a) - 1 - i]
        return c


qwe = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(count(qwe, 'main'))
print(count(qwe, 'not main'))
