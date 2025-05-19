from turtle import Screen
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Slippy The Snake")
screen.tracer(0)

slippy = Snake()
food = Food()

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
        print("nom nom nom")

# this doesn't actually work at the moment, you'll need to close the window.
screen.exitonclick()
