import turtle as t
t.shape('turtle')

#  smile
t.begin_fill()
for i in range(180):
    t.forward(3)
    t.left(2)
t.color('yellow')
t.end_fill()

#  l.eye
t.color('black')
t.penup()
t.goto(-25, 110)
t.pendown()
t.begin_fill()
for i in range(180):
    t.forward(0.4)
    t.left(2)
t.color('blue')
t.end_fill()

#  r.eye
t.color('black')
t.penup()
t.goto(25, 110)
t.pendown()
t.begin_fill()
for i in range(180):
    t.forward(0.4)
    t.left(2)
t.color('blue')
t.end_fill()

t.color('black')
t.penup()
t.goto(0, 90)
t.pendown()
t.right(90)
t.pensize(10)
t.forward(40)

t.color('red')
t.penup()
t.goto(30, 45)
t.pendown()
for i in range(90):
    t.forward(1)
    t.right(2)
