#pythontutor.ru, занятие 7, «Больше своих соседей»
list=[int(i) for i in input().split()]

a = 0 #counter

for i in range(1, len(list)-1):
    if list[i] > list[i-1] and list[i] > list[i+1]:
        a += 1

print(a)
