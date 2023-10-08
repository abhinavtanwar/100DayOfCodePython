import turtle


def tiltLeft():
    # tim.tilt(5)
    tim.left(5)


def moveForward():
    # tim.setheading(90)
    tim.forward(10)


def moveBackward():
    # tim.setheading(270)
    tim.backward(10)


def tiltRight():
    tim.right(5)


def clearUp():
    screen.reset()
    tim.goto(0, 0)


tim = turtle.Turtle()
screen = turtle.Screen()

screen.listen()
# if we add () after the function will passing then it will execute the function then and there without listening
screen.onkeyrelease(key="d", fun=tiltRight)
screen.onkeyrelease(key="w", fun=moveForward)
screen.onkeyrelease(key="a", fun=tiltLeft)
screen.onkeyrelease(key="s", fun=moveBackward)
screen.onkey(key="c", fun=clearUp)

screen.exitonclick()
