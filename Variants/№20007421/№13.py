from turtle import *
tracer(0)
k = 30
left(90)
for _ in range(8):
    right(45)
    forward(6 * k)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()
# РЕШЕНО ВЕРНО