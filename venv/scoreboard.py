import turtle

from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')
GAME_OVER_FONT = ('Courier', 40, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)

        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"   GAME OVER\n Final Score: {self.score} ", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)