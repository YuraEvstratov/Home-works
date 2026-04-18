from turtle import *
k = 30
tracer(0)
left(90)
screensize(1000,1000)
for _ in range(4):
    forward(14 * k)
    right(120)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()