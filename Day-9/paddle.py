import turtle


class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def moveForward(self):
        if self.ycor() < 250:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def moveBackward(self):
        if self.ycor() > -250:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)
