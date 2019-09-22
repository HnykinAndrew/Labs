import turtle
import math


def circle(r, angle):
    for i in range(angle):
        turtle.right(1)
        turtle.forward(r*2*math.pi/360)

turtle.shape('turtle')
turtle.speed(10)
turtle.right(90)
for x in range(60, 1000, 10):
    circle(x, 360)
    turtle.right(180)
    circle(x, 360)