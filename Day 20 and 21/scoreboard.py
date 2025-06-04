from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("white")
        self.teleport(0, 275)
        self.hideturtle()
        self.display()

    def display(self):
        self.write(
            arg=f"Score: {self.score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def update(self):
        self.clear()
        self.score += 1
        self.display()

    def game_over(self):
        self.teleport(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
