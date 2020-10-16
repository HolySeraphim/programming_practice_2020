from random import randint
import turtle

turtle.penup()
turtle.goto(-250, 250)
turtle.pendown()
turtle.goto(250, 250)
turtle.goto(250, -250)
turtle.goto(-250, -250)
turtle.goto(-250, 250)


number_of_turtles = 5
steps_of_time_number = 100

a_Turtle = []
for i in range(number_of_turtles):
    a_Turtle.append(randint(-180, 180))

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for i in range(0, number_of_turtles):
    pool[i].penup()
    pool[i].speed(50)
    pool[i].goto(randint(-200, 200), randint(-200, 200))
    pool[i].left(a_Turtle[i])


while True:
    for i in range(0, number_of_turtles):
        pool[i].forward(2)
        if abs(pool[i].xcor()) >= 250:
            pool[i].left(180-2*a_Turtle[i])
            a_Turtle[i] = 180-a_Turtle[i]
        if abs(pool[i].ycor()) >= 250:
            pool[i].left(-2*a_Turtle[i])
            a_Turtle[i] = 180-a_Turtle[i]
