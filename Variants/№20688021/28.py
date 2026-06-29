from turtle import *
k = 30
left(90)
tracer(0)
screensize(10000, 10000)
for _ in range(2):
    forward(9 * k)
    right(90)
    forward(15 * k)
    right(90)
penup()
forward(12 * k)
right(90)
pendown()
for _ in range(2):
    forward(6 * k)
    right(90)
    forward(12 * k)
    right(90)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(4)

done()