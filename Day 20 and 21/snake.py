from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

STARTING_TURTLES = 3


class Snake:
    """
    Forms the snake object. It contains a constructor and 9 methods
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

    def grow(self) -> None:
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

    def reset(self) -> None:
        """
        Resets the snake (turtles) to start position
        """
        for turt in self.turtles:
            turt.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def move(self) -> None:
        """
        Moves the snake forward. Each segment follows the segment in front of it.
        The head moves forward according to its current heading.
        """
        # Iterates from last turtle to the second
        for i in range(len(self.turtles) - 1, 0, -1):
            new_position = self.turtles[i - 1].pos()
            self.turtles[i].goto(*new_position)
        self.head.forward(MOVE_DISTANCE)

    def _set_direction(self, new_direction, opposite_direction) -> None:
        """
        Sets the direction of the head turtle and encapsulates the opposite direction change logic

        Args:
            new_direction (int): intended new direction of the turtle head
            opposite_direction (int): opposite of intended direction
        """
        if self.head.heading() != opposite_direction:
            self.head.setheading(new_direction)

    def up(self) -> None:
        """
        Sets the direction of the head turtle upwards, subsequent turtles follow thanks to the logic of self.move()
        """
        self._set_direction(UP, DOWN)

    def down(self) -> None:
        """
        Sets the direction of the head turtle downwards, subsequent turtles follow thanks to the logic of self.move()
        """
        self._set_direction(DOWN, UP)

    def right(self) -> None:
        """
        Sets the direction of the head turtle to the right, subsequent turtles follow thanks to the logic of self.move()
        """
        self._set_direction(RIGHT, LEFT)

    def left(self) -> None:
        """
        Sets the direction of the head turtle left, subsequent turtles follow thanks to the logic of self.move()
        """
        self._set_direction(LEFT, RIGHT)
