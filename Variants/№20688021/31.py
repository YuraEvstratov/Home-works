from turtle import *
k = 15
left(90)
tracer(0)
screensize(10000, 10000)
begin_fill()
for _ in range(12):
    right(60)
    forward(2 * k)
    right(60)
    forward(2 * k)
    right(270)
penup()
end_fill()
cnt = 0
canvas = getcanvas()
for x in range(-100, 100):
    for y in range(-100, 100):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            cnt += 1
print(cnt)
done()