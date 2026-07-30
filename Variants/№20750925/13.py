from turtle import * 
k = 30
left(90)
tracer(0)
screensize(10000, 10000)
for _ in range(4):
    for _ in range(4):
        forward(8 * k)
        right(90)
    forward(13 * k)
    right(90)
    forward(4 * k)
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()