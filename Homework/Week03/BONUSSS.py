#special task for professional firework riders

d = {}

for j in input().split():
    if d.get(j, '0') != '0':
        d[j] = d[j] + 1
    else:
        d[j] = 1

print(d)
