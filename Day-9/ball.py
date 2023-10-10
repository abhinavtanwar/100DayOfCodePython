import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed(1.5)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def moveBall(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def paddleCollide(self):
        self.x_move *= -1
        if self.move_speed > 0.02:
            self.move_speed *= 0.9

    def bounceWall(self):
        self.y_move *= -1

    def resetPosition(self):
        self.goto(0, 0)
        self.paddleCollide()
        self.move_speed = 0.1