from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def snake_hits_wall():
    if slippy.head.xcor() > 270 or slippy.head.xcor() < -280 or slippy.head.ycor() > 280 or slippy.head.ycor() < -270:
        return True


def snake_hits_tail():
    for body in slippy.body[2:]:
        if slippy.head.distance(body) < 10:
            return True


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
    # snake movement
    slippy.move()

    # collision with food
    if slippy.head.distance(food) < 15:
        food.refresh()
        slippy.extend()
        scoreboard.add_score()

    # collision with wall or tail
    if snake_hits_wall() or snake_hits_tail():
        game_is_on = False

    if game_is_on:
        scoreboard.update_scoreboard()
    else:
        scoreboard.game_over()

    # update screen to draw all changes for current frame
    screen.update()

    # game speed control
    if game_is_on: # only sleep if game is still running
        time.sleep(0.07)
    else:
        pass


# screen.exitonclick() will keep window with last drawn frame
screen.exitonclick()
