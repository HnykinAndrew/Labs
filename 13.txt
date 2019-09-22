import turtle
import math
from time import sleep

def circle(r, angle):
    for i in range(angle):
        turtle.right(1)
        turtle.forward(r*2*math.pi/360)

turtle.shape('turtle')

turtle.right(180)
turtle.fillcolor('Yellow')
turtle.begin_fill()
circle (115,360)
turtle.end_fill()

turtle.right(90)
turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.forward(45)
turtle.pendown()

turtle.fillcolor('Blue')
turtle.begin_fill()
circle(17,360)
turtle.end_fill()

turtle.left(180)
turtle.penup()
turtle.forward(90)
turtle.pendown()

turtle.left(180)
turtle.begin_fill()
circle(17,360)
turtle.end_fill()

turtle.penup()
turtle.forward(45)
turtle.left(90)
turtle.forward(25)
turtle.pendown()
turtle.width(8)
turtle.forward(25)
turtle.penup()
turtle.forward(5)
turtle.left(90)
turtle.forward(60)
turtle.right(90)
turtle.pendown()
turtle.color('Red')
circle(60,180)
sleep(50)