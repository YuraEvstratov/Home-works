from turtle import *
k = 30
left(90)
tracer(0)
screensize(10000, 10000)
begin_fill()
for _ in range(4):
    forward(18 * k)
    right(90)
    forward(18 * k)
    left(90)
    forward(18 * k)
    right(90)
end_fill()
penup()
k = 0
canvas = getcanvas()
for x in range(-100, 100):
    for y in range(-100, 100):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            k += 1
print(k)
done()
