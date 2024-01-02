import turtle
turtle.speed(0)
turtle.bgcolor("black")
turtle.color("red")
turtle.backward(630)
turtle.left(90)
turtle.forward(320)
turtle.right(135)
for i in range(0,500,2):
    turtle.forward(10)
    if i==100:
        turtle.right(90)
    turtle.circle(20)