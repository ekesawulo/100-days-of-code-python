from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        self.turtles = [Turtle(shape="square") for i in range(3)]
        for i, turt in enumerate(self.turtles):
            turt.color("white")
            turt.penup()
            turt.goto((-20 * i), 0)

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            new_position = self.turtles[i - 1].pos()
            self.turtles[i].goto(*new_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
