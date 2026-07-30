from turtle import *
k = 30
tracer(0)
screensize(10000, 10000)
left(90)
for _ in range(2):
    forward(24 * k)
    right(90)
    forward(10 * k)
    right(90)
forward(3 * k)
left(90)
forward(13 * k)
right(90)
for _ in range(2):
    forward(9 * k)
    right(90)
    forward(32 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()
