import turtle

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 240)
        self.score = 0
        self.write(f"Current Score: {self.score}", move=False, align='center', font=('Sans Serif', 25, 'normal'))

    def addScore(self):
        self.clear()
        self.score += 1
        self.write(f"Current Score: {self.score}", move=False, align='center', font=('Sans Serif', 25, 'normal'))