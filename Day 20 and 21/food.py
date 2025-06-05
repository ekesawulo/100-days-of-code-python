from random import randint
from turtle import Turtle

X_LIMIT = 280
UPPER_Y_LIMIT = 270
LOWER_Y_LIMIT = -280
FOOD_SIZE = 0.5


class Food(Turtle):
    """
    Represents the food item in the Snake game.
    It appears at random locations on the screen.
    Inherits from the Turtle class.
    """

    def __init__(self) -> None:
        """
        Initialises the food object with a specific shape, size, and position.
        """
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=FOOD_SIZE, stretch_len=FOOD_SIZE)
        self.color("coral")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self) -> None:
        """
        Controls the random reappearance of food once the previous instance has been eaten
        """
        self.teleport(randint(-X_LIMIT, X_LIMIT), randint(LOWER_Y_LIMIT, UPPER_Y_LIMIT))
