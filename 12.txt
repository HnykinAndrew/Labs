import turtle
import math

def circle(r, angle):
    for i in range(angle):
        turtle.right(1)
        turtle.forward(r*2*math.pi/360)

turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)
for x in range(1000):
    circle(60, 180)
    circle(12, 180)