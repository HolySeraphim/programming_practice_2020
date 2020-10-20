import math


def Circle():
    r = float(input('Input radius '))
    return 2 * math.pi * r**2


def Square():
    a, b = [float(x) for x in input('Input sides ').split()]
    return a * b


def Triangle():
    a, b, c = [float(x) for x in input('Input sides ').split()]
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


answer = {'Circle': Circle, 'Square': Square, 'Triangle': Triangle}

print(answer[input()]())
