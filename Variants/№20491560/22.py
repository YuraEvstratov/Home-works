from turtle import *
tracer(0)
left(90)
k = 25
right(270)
for _ in range(2):
    forward(7 * k)
    right(120)
right(120)
for _ in range(2):
    right(120)
    forward(5 * k)
    right(240)
right(240)
for _ in range(2):
    forward(17 * k)
    right(120)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()