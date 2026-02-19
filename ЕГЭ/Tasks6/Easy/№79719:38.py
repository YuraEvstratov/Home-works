from turtle import *
import turtle
screen = turtle.Screen()

screen.cv._rootwindow.resizable(True, True)

tracer(0)
left(90)
screensize(100000,10000)
k = 100
for _ in range(2):
    forward(14* k)
    right(90)
    forward(18*k)
    right(90)
penup()
forward(3*k)
right(90)
forward(7*k)
left(90)
pendown()
for _ in range(2):
    forward(74* k)
    right(90)
    forward(92*k)
    right(90)
penup()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x * k, y* k)
        dot(4)
done()