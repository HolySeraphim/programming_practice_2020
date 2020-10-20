# Input count of pairs
n = int(input())
a = []
# Input pairs separated by space
for i in range(n):
    a, b = [int(x) for x in input().split()]
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)
