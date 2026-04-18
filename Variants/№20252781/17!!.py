from turtle import *
k = 30
tracer(0)
left(90)
for _ in range(7):
    forward(15 * k)
    right(90)
    forward(23 * k)
    right(90)
penup()
forward(3 * k)
right(90)
forward(5 * k)
left(90)
pendown()
for _ in range(7):
    forward(251 * k)
    right(90)
    forward(398 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()