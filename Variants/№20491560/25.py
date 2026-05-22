from turtle import *
tracer(0)
left(90)
k = 25
for _ in range(10):
    forward(5 * k)
    right(60)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()