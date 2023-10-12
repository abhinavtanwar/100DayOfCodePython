import turtle


with open("100DayOfCodePython\Day-8\storage.txt", mode="r") as file:
    allTime_highscore = file.read()
    allTime_highscore = int(allTime_highscore)


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.penup()
        self.highscore = allTime_highscore
        self.goto(0, 280)
        self.write(arg=f"Current score: {self.score}, HighScore: {self.highscore}", move=False, align="center")

    def refreshScore(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Current score: {self.score}, HighScore: {self.highscore}", move=False, align="center")

    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        if self.score > self.highscore:
            self.highscore = self.score
        self.write(arg=f"Game Over. Final Score: {self.score}, HighScore: {self.highscore}", align="center",
                   font=("Arial", 20, "normal"))
        with open("100DayOfCodePython\Day-8\storage.txt", mode="w") as myfile:
            myfile.write(f"{self.highscore}")