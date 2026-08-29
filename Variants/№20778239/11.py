from turtle import *
k = 30
left(90)
tracer(0)
for _ in range(7):
    forward(17 * k)
    right(90)
    forward(26 * k)
    right(90)
penup()
forward(4 * k)
right(90) 
forward(6 * k)
left(90)
pendown()
for _ in range(7):
    forward(278 * k)
    right(90)
    forward(345 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(4)
done()
