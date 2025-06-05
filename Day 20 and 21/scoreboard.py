from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    """
    Manages and displays the game score and game over message.
    Inherits from Turtle
    """

    def __init__(self) -> None:
        """
        Sets up the scoreboard object, giving it its position
        """
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("white")
        self.teleport(0, 275)
        self.hideturtle()
        self._display_score()

    def _display_score(self) -> None:
        """
        Displays the scoreboard text
        """
        self.write(
            arg=f"Score: {self.score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self) -> None:
        """
        Increments score by one and updates the new score after the snake eats food
        """
        self.clear()
        self.score += 1
        self._display_score()

    def game_over(self) -> None:
        """
        Displays game over text at the centre of the screen
        """
        self.teleport(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
