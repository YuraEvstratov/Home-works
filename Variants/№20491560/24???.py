from turtle import *
tracer(0)
left(90)
k = 25
screensize(10000,10000)
for _ in range(2):
    for _ in range(2):
        forward(180 * k)
        right(120)
    right(120)
right(150)
forward(15 * k)
right(90)
forward(360 * k)
right(90)
forward(15 * k)
right(30)
forward(74 * k)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()
# КАК СЧИТАТЬ????????