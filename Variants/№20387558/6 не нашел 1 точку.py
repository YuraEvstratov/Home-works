from turtle import *
left(90)
screensize(10000,10000)
tracer(0)
k = 30
for _ in range(4):
    forward(8 * k)
    right(90)
for _ in range(3):
    forward(12 * k)
    right(120)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(1)

done()
