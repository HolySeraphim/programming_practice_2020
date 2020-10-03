import turtle as t
import math

t.shape('turtle')
def f(a):
    for i in range(3, 11):
        t.penup()
        t.forward(20)
        t.pendown()
        t.left(90*(i-2)/i)
        for j in range(0, i):
            t.left(360/i)
            t.forward((math.sin(math.pi/i))*2*(i-2)*20)
        t.right(90 * (i - 2) / i)

f(0)
