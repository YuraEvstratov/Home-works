from turtle import *
tracer(0)
left(90)
k = 25
for _ in range(4):
    forward(12 * k)
    right(90)
for _ in range(3):
    forward(12 * k)
    right(120)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()