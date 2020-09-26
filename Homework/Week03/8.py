#pythontutor.ru, занятие 11, «Словарь синонимов»
n = int(input())
d = {}

for i in range(n):
    a = input().split()
    d.update({a[0]: a[1], a[1]: a[0]})

print(d[input()])
