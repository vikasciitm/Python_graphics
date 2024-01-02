import turtle
turtle.bgcolor("black")
turtle.speed(0)
for i in range(900):
    turtle.color("red")
    if i%2==0:
        turtle.color("green")
    turtle.left(91)
    turtle.forward(i)
