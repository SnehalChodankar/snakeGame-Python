import random
from turtle import Turtle

colors = ["green", "white", "orange", "yellow", "blue", "red"]

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POS:
            new_seg = Turtle("square")
            new_seg.penup()
            new_seg.color(random.choice(colors))
            new_seg.setpos(pos)
            self.snake.append(new_seg)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)

        self.snake[0].forward(SPEED)
