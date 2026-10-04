from turtle import *
k = 30
left(90)
tracer(0)
screensize(10000, 10000)
for _ in range(11):
    forward(36 * k)
    right(72)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()
