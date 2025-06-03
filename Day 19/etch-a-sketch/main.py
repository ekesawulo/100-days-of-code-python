from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()
screen.setup(500, 400)
timmy.speed("fastest")


def move_forward():
    """Moves timmy forward"""
    timmy.forward(10)


def move_backward():
    """Moves timmy backwards"""
    timmy.backward(10)


def turn_right():
    """Rotates timmy clockwise"""
    timmy.setheading(timmy.heading() - 10)


def turn_left():
    """Rotates timmy anticlockwise"""
    timmy.setheading(timmy.heading() + 10)


def clear_screen():
    """Clears drawings and returns timmy to home"""
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


def toggle_pen():
    """Toggles pen state (up/down)"""
    if timmy.isdown():
        timmy.penup()
    else:
        timmy.pendown()


def etch_a_sketch():
    """Etch a sketch program"""
    screen.listen()
    screen.onkey(move_forward, "w")
    screen.onkey(move_backward, "s")
    screen.onkey(turn_right, "d")
    screen.onkey(turn_left, "a")
    screen.onkey(clear_screen, "c")
    screen.onkey(toggle_pen, "p")


etch_a_sketch()
screen.exitonclick()
