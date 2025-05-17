from turtle import Turtle

# tuples passed to goto turtle function on spawn.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20
# turtle graphics default directions.
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.__body = []
        self.build_snake()
        self.__head = self.__body[0]

    def build_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.__body.append(new_segment)

    def move(self):
        for seg_num in range(len(self.__body) - 1, 0, -1):
            front_segment_pos = self.__body[seg_num - 1].pos()
            # previous segment goes to next segment position
            self.__body[seg_num].goto(front_segment_pos)

        self.__head.forward(MOVE_DISTANCE)


    # each method sets heading (direction) if the snake is not currently moving in the opposite direction.
    def up(self):
        if self.__head.heading() != DOWN:
            self.__head.setheading(UP)

    def down(self):
        if self.__head.heading() != UP:
            self.__head.setheading(DOWN)

    def left(self):
        if self.__head.heading() != RIGHT:
            self.__head.setheading(LEFT)

    def right(self):
        if self.__head.heading() != LEFT:
            self.__head.setheading(RIGHT)