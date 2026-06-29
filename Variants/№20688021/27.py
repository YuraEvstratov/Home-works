from turtle import *
k = 10
left(90)
tracer(0)
screensize(10000, 10000)
begin_fill()
right(180)
forward(5 * k)
right(90)
forward(50 * k)
right(90)
forward(5 * k)
for _ in range(5):
    seth(90)
    circle(-5 * k, 180)
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