import random
from turtle import Turtle

colors = ["green", "white", "orange", "yellow", "blue", "red"]

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color(random.choice(colors))
        new_seg.setpos(pos)
        new_seg.heading()
        self.snake.append(new_seg)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)

        self.snake[0].forward(SPEED)

    def up(self):
        curr_heading = self.head.heading()
        if curr_heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        curr_heading = self.head.heading()
        if curr_heading != UP:
            self.head.setheading(DOWN)

    def left(self):
        curr_heading = self.head.heading()
        if curr_heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        curr_heading = self.head.heading()
        if curr_heading != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]