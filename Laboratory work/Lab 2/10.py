import turtle

turtle.shape('turtle')


def f(a):
    turtle.left(60)
    for j in range(180):
        turtle.forward(2)
        turtle.left(2)


for i in range(0, 6):
    f(i)
