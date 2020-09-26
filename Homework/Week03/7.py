#pythontutor.ru, занятие 10, «Количество слов в тексте»
k = []
a = 0 #counter

for i in range(int(input())):
    m = [i for i in input().split()]

    for i in m:
        if k.count(i) == 0:
            a += 1
        k.append(i)

print(a)
