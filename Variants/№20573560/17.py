from turtle import *
k = 30
tracer(0)
left(90)
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
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x * k, y * k, x *k, y*k) == (5,):
            cnt += 1
done()
print(cnt)