from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    """

    Forms the scoreboard object of the paddle game

    """

    def __init__(self) -> None:
        """
        Initialises the scoreboard and the left and right score at the beginning of the game
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """
        Updates the scoreboard
        """
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 240)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self) -> None:
        """
        Increments the left paddle's score when the right paddle misses the ball
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self) -> None:
        """
        Increments the right paddle's score when the left paddle misses the ball
        """
        self.r_score += 1
        self.update_scoreboard()
