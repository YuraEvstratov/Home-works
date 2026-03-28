from turtle import *
tracer(0)
k = 30
n = 15
left(90)
for _ in range(4):
    forward(n * k)
    right(90)
    forward(n * k)
    left(90)
    forward(n * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()
# 15