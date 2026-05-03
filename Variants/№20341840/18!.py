from turtle import *

left(90)
tracer(0)
k = 30
screensize(1000000)

for _ in range(4):
    forward(28 * k)
    right(90)
    forward(26 * k)
    right(90)
penup()
forward(8 * k)
right(90)
forward(7 * k)
left(90)
pendown()
for _ in range(4):
    forward(67 * k)
    right(90)
    forward(98 * k)
    right(90)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()