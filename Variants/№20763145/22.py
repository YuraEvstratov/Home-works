from turtle import *
k = 30
left(90)
tracer(0)
screensize(10000, 10000)
for _ in range(2):
    forward(21 * k)
    right(90)
    forward(27 * k)
    right(90)
penup()
forward(9 * k)
right(90)
forward(10 * k)
left(90)
pendown()
for _ in range(2):
    forward(86 * k)
    right(90)
    forward(47 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()
