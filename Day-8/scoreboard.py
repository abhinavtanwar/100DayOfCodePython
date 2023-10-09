import turtle


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.write(arg=f"Current score: {self.score}", move=False, align="center")

    def refreshScore(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Current score: {self.score}", move=False, align="center")

    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over. Final Score: {self.score}", align="center", font=("Arial", 20, "normal"))