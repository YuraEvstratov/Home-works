from turtle import *
left(90)
tracer(0)
k = 25
for _ in range(2):
    forward(8 * k)
    left(270)
    back(6 * k)
    right(90)
penup()
forward(5 * k)
right(90)
back(3 * k)
left(90)
pendown()
for _ in range(2):
    forward(7 * k)
    right(90)
    forward(2 * k)
    right(90)
penup()
forward(3 * k)
right(180)
back(1 * k)
pendown()
for _ in range(2):
    forward(5 * k)
    right(90)
    forward(5 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(4)
done()