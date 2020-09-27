#  pythontutor.ru, 7 урок, четные элементы
print(' '.join([str(i) for i in [int(i) for i in input().split()] if i % 2 == 0]))
