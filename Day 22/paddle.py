from turtle import Turtle

# Constants
PADDLE_SIZE = (1, 5)
PADDLE_START_LOCATION = (350, 0)
UP = 90
DOWN = 270
PADDLE_MOVE_DISTANCE = 20


class Paddle(Turtle):
    """
    Forms the paddle object for the pong game which is controlled by the user

    """

    def __init__(self, *paddle_position: tuple) -> None:
        """
        Initialises the Paddle object with shape, size and position
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(*PADDLE_SIZE)
        self.penup()
        self.speed("fastest")
        self.setheading(UP)
        self.teleport(*paddle_position)

    def _move_paddle(self, direction: int) -> None:
        """
        Moves the paddle in a given direction

        Args:
            direction (int): Chosen heading
        """
        self.setheading(to_angle=direction)
        self.forward(PADDLE_MOVE_DISTANCE)

    def up(self) -> None:
        """
        Moves paddle upwards
        """
        self._move_paddle(UP)

    def down(self) -> None:
        """
        Moves paddle downwards
        """
        self._move_paddle(DOWN)
