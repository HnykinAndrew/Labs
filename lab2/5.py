import turtle

turtle.shape('turtle')
turtle.penup()
for i in range(2):
    turtle.right(90)
    turtle.forward(25)
turtle.right(180)
turtle.pendown()
for x in range(50,300,25):
    for i in range(3):
        turtle.forward(x)
        turtle.left(90)
    turtle.forward(x)
    turtle.penup()
    turtle.forward(25/2)
    turtle.right(90)
    turtle.forward(25/2)
    turtle.right(180)
    turtle.pendown()