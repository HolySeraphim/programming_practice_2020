#pythontutor.ru, занятие 7, «Уникальные элементы»
l = [int(i) for i in input().split()]

a = []
for i in l:
    if l.count(i) == 1:
        a.append(i)

print(" ".join(str(i) for i in a))
