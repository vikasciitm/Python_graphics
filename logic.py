import turtle
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t1.speed(0)
turtle.bgcolor("black")
t1.color("red")
t2.speed(0)
t2.color("green")
t3.speed(0)
t3.color("pink")
turtle.speed(0)
turtle.color("white")
t1.goto(150,150)
t2.goto(-150,-150)
t3.goto(150,-150)
turtle.goto(-150,150)
for a in range(280):
    t1.left(121)
    t2.left(121)
    t3.left(121)
    turtle.left(121)
    t1.forward(a)
    t2.forward(a)
    t3.forward(a)
    turtle.forward(a)
