from turtle import *
k = 30
left(90)
tracer(0)
screensize(10000, 10000)
for _ in range(9):
    forward(22 * k)
    right(90)
    forward(6 * k)
    right(90)
penup()
forward(1 * k)
right(90)
forward(5 * k)
left(90)
pendown()
for _ in range(9):
    forward(53 * k)
    right(90)
    forward(75 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()
