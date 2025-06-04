from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

STARTING_TURTLES = 3


class Snake:
    """
    Forms the snake object. It contains a constructor and 8 methods
    """

    def __init__(self) -> None:
        """Class constructor"""
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self) -> None:
        """
        Creates the snake which comprises 3 square turtles
        """
        self.turtles = [Turtle(shape="square") for i in range(STARTING_TURTLES)]
        for i, turt in enumerate(self.turtles):
            turt.color("white")
            turt.penup()
            turt.goto((-MOVE_DISTANCE * i), 0)

    def grow(self):
        """
        Adds a new turtle so the snake grows longer when it eats food.
        The new segment is positioned at the current location of the last segment
        """
        tail = self.turtles[-1]
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(tail.position())
        self.turtles.append(new_segment)

    def move(self):
        """
        Moves the snake forward. Each segment follows the segment in front of it.
        The head moves forward according to its current heading.
        """
        # Iterates from last turtle to the second
        for i in range(len(self.turtles) - 1, 0, -1):
            new_position = self.turtles[i - 1].pos()
            self.turtles[i].goto(*new_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Sets the direction of the head turtle upwards, subsequent turtles follow thanks to the logic of self.move()
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Sets the direction of the head turtle downwards, subsequent turtles follow thanks to the logic of self.move()
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """
        Sets the direction of the head turtle to the right, subsequent turtles follow thanks to the logic of self.move()
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """
        Sets the direction of the head turtle left, subsequent turtles follow thanks to the logic of self.move()
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
