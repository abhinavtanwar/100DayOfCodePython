import turtle
pos = [(0, 0), (-20, 0), (-40, 0)]
moveDistance = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    # constructor initializing the snake body by creating 3 turtles
    def __init__(self):
        self.mysnake = []
        self.createSnake()
        self.snakehead = self.mysnake[0]

    def createSnake(self):

        for i in pos:
            newTurtle = turtle.Turtle(shape="square")
            newTurtle.color("white")
            newTurtle.penup()
            self.mysnake.append(newTurtle)
            newTurtle.goto(i)

    def moveSnake(self):
        for i in range(len(self.mysnake)-1, 0, -1):
            newx = self.mysnake[i-1].xcor()
            newy = self.mysnake[i-1].ycor()
            self.mysnake[i].goto(newx, newy)
        self.snakehead.forward(moveDistance)

    def up(self):
        if self.snakehead.heading() != DOWN:
            self.snakehead.setheading(UP)

    def down(self):
        if self.snakehead.heading() != UP:
            self.snakehead.setheading(DOWN)

    def right(self):
        if self.snakehead.heading() != LEFT:
            self.snakehead.setheading(RIGHT)

    def left(self):
        if self.snakehead.heading() != RIGHT:
            self.snakehead.setheading(LEFT)

    def grow(self):
        newTurtle = turtle.Turtle(shape="square")
        newTurtle.color("white")
        newTurtle.penup()
        newTurtle.goto(self.mysnake[-1].xcor(), self.mysnake[-1].ycor())
        self.mysnake.append(newTurtle)

