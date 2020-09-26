#pythontutor.ru, занятие 10, «Пересечение множеств»
l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]

a = []
for i in l1:
    if l2.count(i) != 0:
        a.append(i)
a.sort()

print(" ".join(str(i) for i in a))
