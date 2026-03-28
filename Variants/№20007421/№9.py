from turtle import *
tracer(0)
k = 30
left(90)
for _ in range(4):
    forward(6 * k)
    right(150)
    forward(6 * k)
    right(30)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()
#12