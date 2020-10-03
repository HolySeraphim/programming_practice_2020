import turtle

turtle.shape('turtle')
for i in range(0, 160, 16):
    turtle.penup()
    turtle.forward(8)
    turtle.right(90)
    turtle.forward(8)
    turtle.right(-90)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50+i)
    turtle.left(90)
    turtle.forward(50+i)
    turtle.left(90)
    turtle.forward(50+i)
    turtle.left(90)
    turtle.forward(50+i)


