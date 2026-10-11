from turtle import *
k = 30
left(90)
tracer(0)
for _ in range(3):
    forward(7 * k)
    right(90)
forward(10 * k)
for i in range(3):
    left(90)
    forward(6 * k)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(k * x, k * y)
        dot(3)
done()
