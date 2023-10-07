import turtle
import random


def makeSpirograph(tim):
    angle = 0
    tim.speed("fastest")
    tim.pensize(1.5)
    for _ in range(360):
        tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tim.circle(100)
        tim.setheading(angle)
        angle += 2


def makeDonut(tim):
    tim.setheading(270)
    tim.penup()
    tim.forward(25)
    tim.setheading(0)
    tim.pendown()
    tim.circle(50)
    tim.pensize(50)
    tim.setheading(270)
    tim.penup()
    tim.forward(25)
    tim.setheading(0)
    tim.pendown()
    tim.circle(50)
    pass

timmy = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
#makeSpirograph(timmy)
makeDonut(timmy)
screen.exitonclick()