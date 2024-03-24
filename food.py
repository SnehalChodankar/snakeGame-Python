import random
from turtle import Turtle

colors = ["green", "white", "orange", "yellow", "blue", "red"]


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color(random.choice(colors))

        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        self.goto(random_x, random_y)

    def refresh_loc(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        self.goto(random_x, random_y)