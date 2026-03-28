from turtle import *
tracer(0)
k = 85
left(90)
screensize(10000,10000)
for _ in range(2):
    forward(14 * k)
    right(90)
    forward(18 * k)
    right(90) 
penup()
forward(3 * k)
right(90)
forward(7 * k)
left(90)
pendown()
for _ in range(2):
    forward(74 * k)
    right(90)
    forward(92 * k)
    right(90) 
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(6)
done()
# НЕ ПОЛУЧИЛОСЬ