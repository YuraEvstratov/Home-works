from turtle import *
k = 30
left(90)
tracer(0)
for _ in range(10):
    forward(9 * k)
    right(90)
    forward(2 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()