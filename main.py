import random
import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
colors = ["green", "white", "orange", "yellow", "blue", "red"]

snake = []

for pos in starting_pos:
    new_seg = Turtle("square")
    new_seg.penup()
    new_seg.color(random.choice(colors))
    new_seg.setpos(pos)
    snake.append(new_seg)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Move last segment to second last position
    for seg_num in range(2, 0, -1):
        new_x = snake[seg_num - 1].xcor()
        new_y = snake[seg_num - 1].ycor()
        snake[seg_num].goto(new_x, new_y)

    snake[0].forward(20)

screen.exitonclick()
