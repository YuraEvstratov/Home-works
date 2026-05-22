from turtle import *
left(90)
tracer(0)
k = 25
for _ in range(2):
    forward(3 * k)
    left(90)
    back(10 * k)
    left(90)
penup()
back(10 * k)
right(90)
forward(8 * k)
left(90)
pendown()
for _ in range(2):
    forward(16 * k)
    right(90)
    forward(8 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(4)
done()