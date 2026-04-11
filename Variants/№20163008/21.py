from turtle import *
left(90)
k = 30
tracer(0)
for _ in range(4):
    forward(5 * k)
    right(90)
    forward(10 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()
#66