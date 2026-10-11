from turtle import *
k = 30
left(90)
tracer(0)
for _ in range(4):
    forward(14 * k)
    left(270)
    back(12 * k)
    right(90)
penup()
forward(9 * k)
right(90)
back(7 * k)
left(90)
pendown()
for i in range(2):
    forward(1 * k)
    right(90)
    forward(6 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(k * x, k * y)
        dot(3)
done()
