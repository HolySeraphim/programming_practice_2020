import matplotlib.pyplot as plt
from numpy import array
from time import sleep
from random import choice

k = 5
skip = 1
width = 19 * k
height = 10 * k
delay = 0

print('Enter Your rule, please:(B3678/S34678 by default)')
rule = input()
if rule == '':
    rule = 'B3678/S34678'

rules = [[], []]
j = 0
for i in rule:
    if i.isdigit():
        rules[j].append(int(i))
    elif i == "/":
        j += 1
rule = [set(rules[0]), set(rules[1])]

plt.ion()
palette = array([[255, 255, 255], [0, 0, 0]])
image = array([[choice([0, 1]) for i in range(width)] for j in range(height)])
plt.imshow(palette[image])
plt.gcf().canvas.flush_events()
sleep(delay)

f = 1
while f:
    f = 0
    plt.clf()
    for l in range(skip):
        newim = image.copy()
        for i in range(height):
            for j in range(width):
                neighbors = array([image[(i + 1) % height][j - 1],
                                   image[(i + 1) % height][j],
                                   image[(i + 1) % height][(j + 1) % width],
                                   image[i][j - 1],
                                   image[i][(j + 1) % width],
                                   image[i - 1][j - 1],
                                   image[i - 1][j],
                                   image[i - 1][(j + 1) % width]])
                if image[i][j] == 1:
                    if neighbors.sum() not in rule[1]:
                        f = 1
                        newim[i][j] = 0
                else:
                    if neighbors.sum() in rule[0]:
                        f = 1
                        newim[i][j] = 1
        image = newim
    plt.imshow(palette[image])
    plt.gcf().canvas.flush_events()
    sleep(delay)
plt.ioff()
plt.show()
