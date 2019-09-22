import turtle
import math

def n_ugolnik(n, x):
    turtle.left(180-180*(n-2)/n/2)
    turtle.forward(2*x*math.sin(math.pi/n))
    for y in range (n-1):
        turtle.left(360/n)
        turtle.forward(2*x*math.sin(math.pi/n))

turtle.shape('turtle')
turtle.penup()
turtle.forward(30)
turtle.pendown()
x=20
for i in range(3,360,1):
    x=x+25
    n_ugolnik(i,x)
    turtle.right(180*(i-2)/i/2)
    turtle.penup()
    turtle.forward(25) 
    turtle.pendown()
