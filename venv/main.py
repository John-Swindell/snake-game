from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

slippy = Snake()

screen.listen()
screen.onkey(slippy.up, "w")
screen.onkey(slippy.down, "s")
screen.onkey(slippy.left, "a")
screen.onkey(slippy.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    slippy.move()

# this doesn't actually work at the moment, you'll need to close the window.
screen.exitonclick()
