import numpy as np
a = np.array([i for i in range(2, 76)])
print([a[i] for i in range(1, 75, 2)])
for i in range(1, 75, 2):
    a[i] = -1
