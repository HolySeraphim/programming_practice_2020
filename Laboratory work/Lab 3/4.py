import turtle as t

t.speed(1000)
# turtle
t.shape('turtle')

xt = 0
yt = 0
vx = 10
vy = 10
ay = 1
dt = 0.1
for t1 in range(20000):
    t.goto(xt/2, 2*yt)
    xt += vx*dt
    yt += vy*dt
    vy -= ay*dt
    vx -= 0.001*vx*vx*dt
    if yt < 0:
        vy = -vy*0.9
        yt = 0
