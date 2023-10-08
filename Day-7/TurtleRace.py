import turtle
import random

# To color the Turtles
Rainbowcolors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


# Making the finish line
def makeFinishLine():
    finishLine.hideturtle()
    finishLine.penup()
    finishLine.speed("fastest")
    finishLine.goto(200, -160)
    finishLine.pensize(5)
    finishLine.setheading(90)
    finishLine.pendown()
    finishLine.forward(300)


# setting every turtle to the starting location
def setup(tim, c, pos):
    x = -200
    y = -150
    tim.color(c)
    tim.penup()
    tim.goto(x, y + (40 * pos))


# making turtles to move random steps forward
def moveForward():
    t1.forward(random.randint(5, 20))
    t2.forward(random.randint(5, 20))
    t3.forward(random.randint(5, 20))
    t4.forward(random.randint(5, 20))
    t5.forward(random.randint(5, 20))
    t6.forward(random.randint(5, 20))
    t7.forward(random.randint(5, 20))


# main function to start the race
def startRace():

    while True:
        moveForward()
        if t1.xcor() >= 200:
            return t1
        elif t2.xcor() >= 200:
            return t2
        elif t3.xcor() >= 200:
            return t3
        elif t4.xcor() >= 200:
            return t4
        elif t5.xcor() >= 200:
            return t5
        elif t6.xcor() >= 200:
            return t6
        elif t7.xcor() >= 200:
            return t7


# screen setup
screen = turtle.Screen()
screen.setup(width=600, height=400)

# Turtle to make finish line
finishLine = turtle.Turtle()

# Declaring the turtles and calling the setup function
t1 = turtle.Turtle()
setup(t1, Rainbowcolors[0], 0)
t2 = turtle.Turtle()
setup(t2, Rainbowcolors[1], 1)
t3 = turtle.Turtle()
setup(t3, Rainbowcolors[2], 2)
t4 = turtle.Turtle()
setup(t4, Rainbowcolors[3], 3)
t5 = turtle.Turtle()
setup(t5, Rainbowcolors[4], 4)
t6 = turtle.Turtle()
setup(t6, Rainbowcolors[5], 5)
t7 = turtle.Turtle()
setup(t7, Rainbowcolors[6], 6)

# calling function to make finish line
makeFinishLine()

# asking user for bet
chosenTurtle = screen.textinput(title="Make a BET!!!", prompt="Enter the the color you wanna gamble upon:")

# starting the race
winner = startRace()

# getting the winning color
# winner.color() prints = ('red', 'red') that's y we need to access first element in the tuple
# color() will give pencolor and fillcolor
winingcolor = winner.color()[0]
print(f"You choose {chosenTurtle} turtle and", end=" ")
if chosenTurtle == winner.color()[0]:
    print("You Win!!!")
else:
    print(f"You Lose!!! The winner is {winingcolor}")
screen.exitonclick()
