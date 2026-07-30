from turtle import *
k = 3
left(90)
tracer(0)
begin_fill()
for _ in range(5):
    right(36)
    forward(10 * k)
    right(36)
end_fill()
penup()
k = 0
canvas = getcanvas()
for x in range(-70, 70):
    for y in range(-70, 70):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) != ():
            k += 1
done()
print(k)
