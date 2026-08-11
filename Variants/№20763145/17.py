from turtle import *
k = 30
left(90)
tracer(0)
screensize(10000, 10000)
for _ in range(4):
    forward(9 * k)
    right(90)
    forward(7 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()
