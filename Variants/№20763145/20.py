from turtle import *
k = 30
left(90)
tracer(0)
screensize(10000, 10000)
right(270)
for _ in range(2):
    forward(8 * k)
    right(120)
right(120)
for _ in range(2):
    right(120)
    forward(3 * k)
    right(240)
right(240)
for _ in range(2):
    forward(14 * k)
    right(120)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()
