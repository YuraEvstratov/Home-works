from turtle import *
tracer(0)
left(90)
k = 20
for _ in range(2):
    forward(9 * k)
    right(90)
    forward(15 * k)
    right(90)
penup()
forward(12 * k)
right(90)
pendown()
for _ in range(2):
    forward(6 * k)
    right(90)
    forward(12 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(4)
done()