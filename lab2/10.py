import turtle
import math

def circle(r, angle):
    for i in range(angle):
        turtle.right(1)
        turtle.forward(r*2*math.pi/360)

turtle.shape('turtle')
for x in range(6):
    circle(50, 360)
    turtle.right(60)


