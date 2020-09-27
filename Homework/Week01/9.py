#  pythontutor.ru, 8 урок, длина отрезка
def distance(x1, y1, x2, y2):
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return dist


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))
