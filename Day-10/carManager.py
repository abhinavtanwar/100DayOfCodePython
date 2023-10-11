import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]



class CarManager:
    def __init__(self):
        self.all_cars = []
        self.moveDistance = 5
        self.moveIncrement = 3

    def createCar(self):
        # to slow down car formation
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = turtle.Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def moveCars(self):
        for car in self.all_cars:
            car.backward(self.moveDistance)

    def levelUp(self):
        self.moveDistance += self.moveIncrement
