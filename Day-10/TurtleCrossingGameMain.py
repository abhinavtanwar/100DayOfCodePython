# Turtle Crossing game
import random
import time
import turtle
import carManager
import player
import scoreBoard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# initializing player, score and cars
player = player.Player()
scoreboard = scoreBoard.Scoreboard()
carManager = carManager.CarManager()

screen.listen()
screen.onkey(key="w", fun=player.moveForward)

gameOn = True
while gameOn:
    time.sleep(0.1)
    screen.update()
    carManager.createCar()
    carManager.moveCars()

    # checking Whether turtle reached finishLine
    if player.ycor() > 275:
        scoreboard.levelUp()
        player.LevelUpReset()
        carManager.levelUp()

    # checking collision of turtle and car
    for car in carManager.all_cars:
        if car.distance(player) < 25:
            scoreboard.gameOver()
            gameOn = False

screen.exitonclick()
