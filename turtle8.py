import turtle
turtle.hideturtle()
turtle.right(90)
turtle.bgcolor("black")
turtle.color("red")
turtle.forward(100)
turtle.left(90)
turtle.speed(0)
for a in range(300):
    turtle.circle(a)
    turtle.forward(3)
    if a%2==0:
        turtle.left(1)

