def power(a, n):
    res = 1
    if a == 0 and n < 1:
        return None
    elif n > 0:
        for i in range(n):
            res *= a
        return res
    else:
        for i in range(-n):
            res /= a
        return res
