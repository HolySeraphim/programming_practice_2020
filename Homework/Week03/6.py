#pythontutor.ru, занятие 10, «Встречалось ли число раньше»
l = [int(i) for i in input().split()]

m = [] #checklist
for i in l:
    if m.count(i) == 0:
        print('NO')
    else:
        print('YES')
    m.append(i)
