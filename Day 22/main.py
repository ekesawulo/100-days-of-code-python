from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
screen.update()

ball = Ball()
scoreboard = Scoreboard()
screen.tracer(1)
screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")


def pong() -> None:
    """
    Game logic, detects wall and paddle collisions and increments scores when ball goes out of bounds
    """
    is_playing = True
    while is_playing:
        ball.move()
        # Detect horizontal wall collision
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        # Detect paddle collisions
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (
            ball.distance(l_paddle) < 50 and ball.xcor() < -330
        ):
            ball.bounce_x()
        # Detect ball going out of bounds
        if ball.xcor() > 380:
            scoreboard.l_point()
            scoreboard.update_scoreboard()
            ball.reset()
        if ball.xcor() < -380:
            scoreboard.r_point()
            scoreboard.r_score += 1
            ball.reset()


pong()
screen.exitonclick()
