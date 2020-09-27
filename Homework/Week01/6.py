#  pythontutor.ru, 6 урок, второй максимум
m = []
a = int(input())
while a != 0:
    m.append(a)
    a = int(input())
m.sort()
print(m[-2])
