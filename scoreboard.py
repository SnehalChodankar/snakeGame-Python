from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def get_high_score(self):
        with open("data.txt", mode="r") as file:
            high_score = file.read()
            self.high_score = int(high_score)

    def reset(self):
        self.get_high_score()

        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()

        self.score = 0
        self.refresh_score()

    def set_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

