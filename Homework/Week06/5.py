import matplotlib.pyplot as plt


def f(x):
    if -5 <= x <= 5:
        return x**2
    elif x < -5:
        return 2 * (x if x >= 0 else -x) - 1
    else:
        return 2 * x


y = []
for i in range(-10, 11, 1):
    y.append(f(i))

plt.plot(range(-10, 11, 1), y)
plt.show()

