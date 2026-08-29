from turtle import *
k = 30 
left(90)
tracer(0)
for _ in range(4):
    forward(10 * k)
    right(270)
penup()
forward(3 * k)
right(270)
forward(5 * k)
right(90)
pendown()
for _ in range(2):
    forward(10 * k)
    right(270)
    forward(12 * k)
    right(270)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(4)
done()