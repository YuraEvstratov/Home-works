from turtle import *
k = 15
left(90)
tracer(0)
screensize(10000, 10000)
right(180)
for _ in range(9):
    forward(59 * k)
    left(90)
    forward(84 * k)
    left(90)
penup()
forward(18 * k)
left(90)
forward(38 * k)
right(90)
pendown()
for _ in range(9):
    forward(120 * k)
    right(90)
    forward(99 * k)
    right(90)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(4)
done()