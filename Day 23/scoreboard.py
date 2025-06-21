from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-270, 250)


class Scoreboard(Turtle):
    """
    Creates the scoreboard object which keeps track of the current level
    """

    def __init__(self) -> None:
        """
        Creates the scoreboard and initialises the current level
        """
        super().__init__()
        self.current_level = 1
        self.penup()
        self.hideturtle()
        self.goto(*SCOREBOARD_POSITION)
        self._display_level()

    def _display_level(self) -> None:
        """
        Writes the current level on the screen
        """
        self.clear()
        self.write(arg=f"Level: {self.current_level}", font=FONT)

    def increase_level(self) -> None:
        """
        Increments level by one and updates the new level after turtle completes a level
        """
        self.clear()
        self.current_level += 1
        self._display_level()

    def game_over(self) -> None:
        """
        Displays game over text at the centre of the screen
        """
        self.teleport(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)
