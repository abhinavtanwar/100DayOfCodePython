import turtle

font = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-150, 260)
        self.write(arg=f"Level: {self.level}", align="center", font=font)

    def levelUp(self):
        self.level += 1
        self.clear()
        self.goto(-150, 260)
        self.write(arg=f"Level: {self.level}", align="center", font=font)

    def gameOver(self):
        self.clear()
        self.goto(0, 260)
        self.write(arg="Game Over!!!!", align="center", font=font)
