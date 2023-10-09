# Snake Game
# inheritance, slicing
import turtle
import time
import snake
import food
import scoreboard

# setting up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# turning off animations
screen.tracer(0)

# creating a snake object
mysnake = snake.Snake()
food = food.Food()
score = scoreboard.Scoreboard()
screen.update()

screen.listen()
screen.onkey(key="w", fun=mysnake.up)
screen.onkey(key="a", fun=mysnake.left)
screen.onkey(key="s", fun=mysnake.down)
screen.onkey(key="d", fun=mysnake.right)
gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.08)
    mysnake.moveSnake()

    # detecting collision with food
    if mysnake.snakehead.distance(food) < 15:
        # print("nom nom nom")
        score.refreshScore()
        food.refreshFood()
        mysnake.grow()

    # detecting collision with tail
    for i in mysnake.mysnake[1:]:
        if mysnake.snakehead.distance(i) < 10:
            score.gameOver()
            gameOn = False

    # detecting collision with walls
    if mysnake.snakehead.xcor() > 290 or mysnake.snakehead.xcor() < -290 or mysnake.snakehead.ycor() > 290 or mysnake.snakehead.ycor() < -290:
        score.gameOver()
        gameOn = False

screen.exitonclick()
