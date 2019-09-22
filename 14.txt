import turtle

def n_star(n, size):
    for i in range(n):
        turtle.left(180-180/n)
        turtle.forward(100)
turtle.shape('turtle')
turtle.left(180)
n_star(5, 100)															
turtle.left(180)
turtle.penup()
turtle.forward(150)
turtle.left(180)
turtle.pendown()
n_star(11, 100)	

