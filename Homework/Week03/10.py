#pythontutor.ru, занятие 11, «Продажи»
a = {}

#input
while True:
    try:
        x = input().split()
        x[2]=int(x[2])
        a[x[0]]=a.get(x[0],{})
        a[x[0]][x[1]]=a[x[0]].get(x[1],0) + x[2]
    except ValueError:
        break

#result
for k in sorted(a.keys()):
    print(k+':')
    for l in sorted(a[k].keys()):
        print(l,' ',a[k][l])