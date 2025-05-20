from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Slippy The Snake")
screen.tracer(0)

slippy = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(slippy.up, "w")
screen.onkey(slippy.down, "s")
screen.onkey(slippy.left, "a")
screen.onkey(slippy.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    # raise for slower game, lower for faster
    time.sleep(0.05)
    slippy.move()

    # collision detection
    if slippy.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        scoreboard.update_scoreboard()


# this doesn't actually work at the moment, you'll need to close the window.
screen.exitonclick()
