#pythontutor.ru, занятие 11, «Самое частое слово»
d = {}
n = int(input())

#dict creation
for i in range(0,n):
    b = input().split()
    for j in b:
        if d.get(j,'0') != '0':
            d[j] = d[j] + 1
        else:
            d[j] = 1

#dict converting
dlist = list(d.items())
dlist.sort()
d = {dlist[i][0]: dlist[i][1] for i in range(len(dlist)-1, -1,-1)}
max = max(d.values())

#dict max_key founder
for key in d:
    if d[key] == max:
        print(key)
        break
