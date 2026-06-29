from turtle import *
k = 100
left(90)
tracer(0)
screensize(10000, 10000)
begin_fill()
right(270)
for _ in range(2):
    forward(7 * k)
    right(120)
right(120)
for _ in range(2):
    right(120)
    forward(5 * k)
    right(240)
right(240)
for _ in range(2):
    forward(17 * k)
    right(120)
end_fill()
penup()
cnt = 0
canvas = getcanvas()
for x in range(-500, 500):
    for y in range(-500, 500):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            cnt += 1
print(cnt)
done()