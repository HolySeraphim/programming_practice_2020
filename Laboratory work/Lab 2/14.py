import turtle as t
t.shape('turtle')

def f(n):
    for i in range(n):
        t.forward(300)
        t.left(180+180/n)


f(11)

t.penup()
t.goto(-310, 0)
t.pendown()

f(5)
