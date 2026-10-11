from turtle import *
k = 30
left(90)
tracer(0)
for _ in range(6):
    forward(13 * k)
    right(120)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(k * x, k * y)
        dot(3)
done()
