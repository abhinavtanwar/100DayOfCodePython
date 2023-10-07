import turtle
import random
import colorgram


# def getColor():
#     colors = colorgram.extract("100DayOfCodePython\Day-6\HirstSpotPainting.webp", 50)
#     color = colors[random.randint(0, len(colors))].rgb
#     newcolor = (color[0], color[1], color[2])
#     return newcolor

colors = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203),
              (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67),
              (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165),
              (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187),
              (169, 206, 172), (219, 182, 169)]

# def paint(tim):
#     tim.setheading(180)
#     tim.penup()
#     tim.forward(75)
#     tim.setheading(270)
#     tim.forward(100)
#     tim.setheading(0)
#     print(tim.pos())
#     for i in range(15):
#         for j in range(20):
#             tim.pendown()
#             tim.dot(2)
#             tim.penup()
#             tim.forward(10)
#         tim.goto(-75, -100+(i*10))
#     pass


def painting(tim):
    tim.hideturtle()
    tim.speed("fastest")
    tim.setheading(225)
    tim.penup()
    tim.forward(300)
    tim.setheading(0)
    tim.pendown()
    x = tim.xcor()
    y = tim.ycor()
    for j in range(10):
        for i in range(10):
            tim.pendown()
            tim.dot(20, random.choice(colors))
            tim.penup()
            tim.forward(50)
        y = y+50
        tim.goto(x, y)
        

timmy = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
painting(timmy)
# paint(timmy)
# print(getColor())
screen.exitonclick()