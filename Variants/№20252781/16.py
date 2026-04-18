from turtle import *
k = 30
tracer(0)
left(90)
for _ in range(5):
    forward(9 * k)
    right(90)
    forward(3 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()