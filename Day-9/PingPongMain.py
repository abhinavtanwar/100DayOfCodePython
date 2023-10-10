# Ping Pong Game
import turtle
import paddle
import ball
import time
import score


screen = turtle.Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)

p1 = paddle.Paddle((350, 0))
p2 = paddle.Paddle((-350, 0))
ball = ball.Ball()
scoreboard = score.Score()
screen.listen()
screen.onkeypress(key="i", fun=p1.moveForward)
screen.onkeypress(key="k", fun=p1.moveBackward)
screen.onkeypress(key="w", fun=p2.moveForward)
screen.onkeypress(key="s", fun=p2.moveBackward)

gameOn = True
while gameOn:
    time.sleep(ball.move_speed)
    screen.update()
    ball.moveBall()

    # detecting collision with top walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceWall()
        pass

    # detecting collision with paddle
    if ball.distance(p1) < 50 and ball.xcor() > 330 or ball.distance(p2) < 50 and ball.xcor() < -330:
        ball.paddleCollide()

    # detecting collision with walls behind paddles
    if ball.xcor() > 382:
        print("Game Over for p1")
        scoreboard.p2Scores()
        ball.resetPosition()
        sleepTime = 0.1

    if ball.xcor() < -382:
        print("Game Over for p2")
        scoreboard.p1Scores()
        ball.resetPosition()

    if scoreboard.p2Score >= 3 or scoreboard.p1Score >= 3:
        scoreboard.gameOver()
        gameOn = False

screen.exitonclick()
