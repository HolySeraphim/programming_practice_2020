#pythontutor.ru, занятие 7, «Количество совпадающих пар»
import math
l = [int(i) for i in input().split()]

a = 0 #counter
for i in l:
    a += l.count(i)-1
print(a//2)
