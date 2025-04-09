# this creats the turtle
import turtle 

turtle.Screen().bgcolor("black")

t = turtle.Turtle()
#this changes the speed
t.speed(60)

t.goto(0,0)
t.color("yellow")

for i in range(25):
    t.forward(89)
    t.left(165)


t.penup()
t.goto(-100,0)
t.color( "pink" )
t.pendown()
#this makes a firework shape
for i in range(25):
    t.forward(89)
    t.left(165)



t.penup()
t.goto(-100,100)
t.color( "cyan" )
t.pendown()

for i in range(25):
    t.forward(89)
    t.left(165)

turtle.exitonclick()
