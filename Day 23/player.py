from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    Creates player object which is controlled by the user
    """

    def __init__(self) -> None:
        """
        Initialises the player object with a turtle shape at the bottom of the screen
        """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(*STARTING_POSITION)
        self.setheading(90)

    def move(self) -> None:
        """
        Moves the turtle upwards
        """
        self.forward(MOVE_DISTANCE)

    def reset(self) -> None:
        """
        Moves turtle back to starting point upon completion of a level
        """
        self.teleport(*STARTING_POSITION)

    def at_finish_line(self) -> bool:
        """
        Checks if turtle has reached the finish line

        Returns:
            bool: Returns a boolean value based on the turtle's current position on the Y-axis
        """
        return self.ycor() >= FINISH_LINE_Y
