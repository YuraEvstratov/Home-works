from turtle import *
left(90)
tracer(0)
k = 25
screensize(1000, 1000)
for _ in range(8):
    right(45)
    forward(8 * k)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(4)
done()