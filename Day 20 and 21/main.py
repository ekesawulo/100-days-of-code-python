import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialise object instances
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Screen key-mapping
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


def snake_game():
    """
    Game logic, detects food, walls, collisions with itself and allows the snake grow
    """
    while True:
        screen.update()
        time.sleep(0.1)
        snake.move()
        # Detect food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.update()
            snake.grow()
        # Detect walls
        if (
            snake.head.xcor() > 280
            or snake.head.ycor() > 275
            or snake.head.xcor() < -280
            or snake.head.ycor() < -280
        ):
            scoreboard.game_over()
            break
        # Detect collision with body
        for turt in snake.turtles[1:]:
            if snake.head.distance(turt) < 10:
                scoreboard.game_over()
                break


snake_game()
screen.exitonclick()
