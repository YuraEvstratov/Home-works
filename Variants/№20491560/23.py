from turtle import *
tracer(0)
left(90)
k = 25
for _ in range(7):
    forward(10 * k)
    right(120)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()