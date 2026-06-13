from turtle import *
k = 30
tracer(0)
left(90)
for _ in range(4):
    forward(10 * k)
    right(90)
right(30)
for _ in range(5):
    forward(6 * k)
    right(60)
    forward(6 * k)
    right(120)
penup()
for x in range(-80, 80):
    for y in range(-80, 80):
        goto(x * k, y * k)
        dot(2)
done()