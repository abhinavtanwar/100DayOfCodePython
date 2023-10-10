import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.p1Score = 0
        self.p2Score = 0
        self.printScores()

    def printScores(self):
        self.goto(-50, 250)
        self.write(arg=f"P2: {self.p2Score}", align="center", font=20)
        self.goto(50, 250)
        self.write(arg=f"P1: {self.p1Score}", align="center", font=20)

    def p1Scores(self):
        self.p1Score += 1
        self.clear()
        self.printScores()

    def p2Scores(self):
        self.p2Score += 1
        self.clear()
        self.printScores()

    def gameOver(self):
        self.goto(0, 0)
        self.clear()
        self.write(arg=f"Game Over p1 = {self.p1Score} and p2 = {self.p2Score}", align="center", font=30)