from turtle import *
tracer(0)
left(90)
k = 10
screensize(10000, 10000)
for _ in range(9):
    forward(66 * k)
    left(90)
    forward(100 * k)
    left(90)
penup()
forward(27 * k)
left(90)
forward(41 * k)
right(90)
pendown()
for _ in range(9):
    forward(120 * k)
    right(90)
    forward(99 * k)
    right(90)
penup()
for x in range(-150, 150):
    for y in range(-150, 150):
        goto(x * k, y * k)
        dot(3)
done()