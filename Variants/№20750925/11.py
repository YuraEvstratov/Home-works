from turtle import *
k = 30
left(90)
tracer(0)
screensize(10000, 10000)
for _ in range(2):
    forward(7 * k)
    left(270)
    back(5 * k)
    right(90)
penup()
forward(6 * k)
right(90)
back(4 * k)
left(90)
pendown()
for _ in range(2):
    forward(9 * k)
    right(90)
    forward(4 * k)
    right(90)
penup()
forward(4 * k)
right(180)
back(2 * k)
pendown()
for _ in range(2):
    forward(7 * k)
    right(90)
    forward(7 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()



