from turtle import *

left(90)
tracer(0)
screensize(10000,10000)
k = 30
for _ in range(8):
    right(45)
    forward(8 * k)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()