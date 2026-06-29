from turtle import *
k = 30
left(90)
tracer(0)
for _ in range(5):
    forward(9 * k)
    right(120)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(2, "blue")
done()