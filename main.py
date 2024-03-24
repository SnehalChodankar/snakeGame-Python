import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
colors = ["green", "white", "orange", "yellow", "blue", "red"]

for pos in starting_pos:
    new_seg = Turtle("square")
    new_seg.penup()
    new_seg.color(random.choice(colors))
    new_seg.setpos(pos)



screen.exitonclick()
