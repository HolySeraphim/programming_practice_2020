#pythontutor.ru, занятие 7, «Переставить min и max»
l = [int(i) for i in input().split()]

posmax = l.index(max(l))
posmin = l.index(min(l))
max = max(l)
l[posmax] = min(l)
l[posmin] = max

print(" ".join(map(str, l)))
