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
        with open("Day 20 and 21/data.txt") as file:
            contents = int(file.read())
        self.high_score = contents
        self.speed("fastest")
        self.color("white")
        self.teleport(0, 275)
        self.hideturtle()
        self._update_score()

    def _update_score(self) -> None:
        """
        Displays the scoreboard text
        """
        self.clear()
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self) -> None:
        """
        Increments score by one and updates the new score after the snake eats food
        """
        self.score += 1
        self._update_score()

    def reset(self) -> None:
        """
        Displays the new high score (if any) and resets the current score
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day 20 and 21/data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self._update_score()
