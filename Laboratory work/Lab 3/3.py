import turtle as t

#  input
inp = input()

# turtle
t.shape('turtle')
t.color('blue')

#  window size
t.Screen().setup(1300, 650, 0, 0)

#  reading from file
f = open('numbers.txt', 'r')
data = [x.rstrip() for x in f.readlines()]
f.close()

#  second massive making
data = [x.split('|') for x in data]
data1 = []
for i in data:
    data1.append([j.split() for j in i])

#  third massive making + drawing
x0 = 250
for i in range(len(inp)):
    t.penup()
    t.goto(i*75-x0, 0)
    t.pendown()
    for c in range(len(data1[int(inp[i])]) - 1):
        t.goto((int(data1[int(inp[i])][c][0]) + i*75 - x0), int(data1[int(inp[i])][c][1]))

#  final location
t.penup()
t.goto(len(inp)*75 + 75 - x0, 0)
input()
