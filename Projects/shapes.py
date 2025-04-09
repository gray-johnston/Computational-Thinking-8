import turtle

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("green")
t.pendown()

for i in range(1000):
    t.forward(35)
    t.left(-150)
    t.right(100)


turtle.exitonclick()