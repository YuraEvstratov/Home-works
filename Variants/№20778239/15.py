from turtle import *
k = 30 
left(90)
tracer(0)
for _ in range(8):
    forward(6 * k)
    right(120)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(4)
done()