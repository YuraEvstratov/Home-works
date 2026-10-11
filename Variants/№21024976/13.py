from turtle import *
k = 30
left(90)
tracer(0)
for _ in range(4):
    forward(12 * k)
    right(90)
for _ in range(3):
    forward(12 * k)
    right(120)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(k * x, k * y)
        dot(3)
done()
