from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.__body = []
        self.build_snake()

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
            self.__body[seg_num].goto(front_segment_pos)

        self.__body[0].forward(20)

    def up(self):
        self.__body[0].setheading(90)

    def down(self):
        self.__body[0].setheading(270)

    def left(self):
        self.__body[0].setheading(180)

    def right(self):
        self.__body[0].setheading(0)