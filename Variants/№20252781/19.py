from turtle import *
k = 30
tracer(0)
left(90)
screensize(1000,1000)
for _ in range(4):
    forward(12 * k)
    right(90)
for _ in range(5):
    forward(4 * k)
    right(45)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()