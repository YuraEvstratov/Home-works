from turtle import *
tracer(0)
left(90)
k = 10
screensize(10000, 10000)
for _ in range(2):
    forward(27 * k)
    right(90)
    forward(8 * k)
    right(90)
penup()
forward(4 * k)
right(90)
forward(2 * k)
left(90)
pendown()
for _ in range(2):
    forward(17 * k)
    right(90)
    forward(7 * k)
    right(90)
penup()
for x in range(-150, 150):
    for y in range(-150, 150):
        goto(x * k, y * k)
        dot(3)
done()