#  pythontutor.ru, 7 урок, четные индексы
lst = [int(i) for i in input().split()]
print(' '.join([str(lst[i]) for i in range(0, len(lst), 2)]))
