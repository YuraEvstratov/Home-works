from turtle import *
k = 40
tracer(0)
left(90)
for _ in range(4):
    forward(9 * k)
    right(90)
for _ in range(3):
    forward(9 * k)
    right(120)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(1)
done()