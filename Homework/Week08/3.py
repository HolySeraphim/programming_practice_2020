import numpy as np
from random import randint
A = np.array([randint(0, 10) for i in range(10)])
B = np.array([randint(0, 10) for i in range(10)])
print(np.delete(A, B))
# поиск пересечения множеств А-(A-B)