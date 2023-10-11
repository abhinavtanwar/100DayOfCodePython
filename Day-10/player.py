import turtle

startingPosition = (0, -280)
moveDistance = 10
finishLine = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(startingPosition)
        self.setheading(90)

    def moveForward(self):
        self.forward(moveDistance)

    def LevelUpReset(self):
        self.goto(startingPosition)
        self.setheading(90)
