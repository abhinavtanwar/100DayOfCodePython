import pandas
import turtle


class WriteNames(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def writeName(self, state, x, y):
        self.goto(x, y)
        self.write(state)


data = pandas.read_csv("100DayOfCodePython\Day-11\State_Coordinate_Data.csv")
states = data["states"].tolist()
# print(type(states))
# print(states)

t = WriteNames()

screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.title("India State Guess")

# setting image
img = "100DayOfCodePython\Day-11\IndiaMap.gif"
screen.addshape(img)
turtle.shape(img)


count = 0
while count < 29:
    ans = screen.textinput(title="Guess the State", prompt="Write the state's name")
    if ans in states:
        count += 1
        new_x = data[data.states == ans]["x coords"].tolist()
        new_y = data[data.states == ans]["y coords"].tolist()
        t.writeName(ans, new_x[0], new_y[0])

print(count)
turtle.mainloop()