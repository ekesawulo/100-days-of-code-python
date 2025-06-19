from turtle import Turtle


class Ball(Turtle):
    """
    Creates the ball object
    Inherits turtle
    """

    def __init__(self) -> None:
        """
        Initialises ball shape, size and colour, also gives distance it moves
        """
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_move = 4
        self.y_move = 4

    def move(self) -> None:
        """
        Controls the movements of the ball
        """
        # self.setheading(45)
        # self.forward(5)
        # if self.ycor() > 280 or self.ycor() < -280:
        #     self.setheading(360 - self.heading())
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self) -> None:
        """
        Controls the ricochet of ball on hitting a horizontal obstacle
        """
        self.y_move *= -1

    def bounce_x(self) -> None:
        """
        Controls the ricochet of ball on hitting a vertical obstacle
        """
        self.x_move *= -1

    def reset(self) -> None:
        """
        Resets the ball to the centre of the screen
        """
        self.home()
        self.bounce_x()
        self.move()
