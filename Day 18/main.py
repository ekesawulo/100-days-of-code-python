import turtle
from random import randint, choice

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("coral")
screen = turtle.Screen()


def random_colour():
    """Returns a tuple of random int values used as rgb for turtle color method"""
    return (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
    )


def square():
    """draws a square"""
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)


def dashed_line():
    """draws a dashed line"""
    for _ in range(10):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def polygons():
    """draws polygons with increasing number of sides along the same plane"""
    turtle.colormode(255)
    timmy.pensize(5)
    timmy.speed("fastest")
    for n in range(3, 11):
        timmy.color(random_colour())
        for _ in range(n):
            timmy.forward(100)
            timmy.right(360 / n)


def random_walk():
    """generates a random walk"""
    turtle.colormode(255)
    timmy.pensize(5)
    timmy.speed("fastest")
    direction = [0, 90, 180, 270]
    for _ in range(200):
        timmy.color(random_colour())
        timmy.setheading(choice(direction))
        timmy.forward(20)


def spirograph(gap, radius):
    """Draws a spirograph

    Args:
        gap (int): Specifies the gap between circles
        radius (int): Specifies the radius of the generated circles
    """
    turtle.colormode(255)
    timmy.speed("fastest")
    for angle in range(0, 360, gap):
        timmy.setheading(angle)
        timmy.color(random_colour())
        timmy.circle(radius)


spirograph(5, 75)
screen.exitonclick()
