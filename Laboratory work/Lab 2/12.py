import turtle

turtle.shape('turtle')
turtle.left(90)


def f(a):
    for i in range(90):
        turtle.forward(2)
        turtle.right(2)


def g(a):
    for i in range(90):
        turtle.forward(0.5)
        turtle.right(2)


for i in range(10):
    f(0)
    g(0)
