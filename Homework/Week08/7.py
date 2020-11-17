import numpy as np
from random import randint


def write_to_file(file, mass):
    file = open(f'{file}.txt', 'w')
    file.write(f'{mass.shape}')
    a = mass.copy()
    a = a.reshape(np.prod(mass.shape))
    for i in a:
        file.write(f'\n{i}')
    file.close()


def read_from_file(file):
    file = open(f'{file}.txt', 'r')
    shape = file.readline().rstrip()
    data = np.array([x.rstrip() for x in file.readlines()])
    data = data.reshape(eval(shape))
    return data


A = np.array([[[randint(0, 10) for i in range(10)]]])
write_to_file(1, A)
A = read_from_file(1)
