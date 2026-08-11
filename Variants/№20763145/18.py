from turtle import *
k = 30
left(90)
tracer(0)
screensize(10000, 10000)
right(90)
for _ in range(7):
    right(45)
    forward(11 * k)
    right(45)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()
