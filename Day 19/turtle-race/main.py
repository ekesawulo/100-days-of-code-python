import turtle
from random import randint

screen = turtle.Screen()
screen.setup(width=500, height=400)


# Initially wanted to try this with random colours but quickly realised this wouldn't work.
# def random_colour():
#     """Returns a tuple of random int values used as rgb for turtle color method"""
#     return (
#         randint(0, 255),
#         randint(0, 255),
#         randint(0, 255),
#     )

colours = ["red", "orange", "yellow", "green", "blue", "purple"]


def initialise_turtles(available_colours):
    """
    Draws turtles and puts them at the start line

    Args:
        available_colours (list): List of colours to be used for the turtles

    Returns:
        list: List of generated turtle instances
    """
    turtles = [turtle.Turtle(shape="turtle") for _ in available_colours]
    for i, turt in enumerate(turtles):
        turt.color(available_colours[i])
        turt.penup()
        # dynamically set coordinates
        # spacing = 50
        # total_height = (len(available_colours) - 1) * spacing
        # start_y = total_height // 2
        turt.goto(-230, (130 - (i * 50)))
    return turtles


def turtle_race(turtle_colours):
    """Contains race logic"""

    while True:
        user_bet = screen.textinput(
            title="Make your bet",
            prompt="Which turtle will win the race? Enter a colour: ",
        )
        if user_bet and user_bet.lower() in turtle_colours:
            break
        screen.textinput(
            title="Invalid input",
            prompt=f"Try again. Valid colours: {', '.join(turtle_colours)}",
        )
    turtles = initialise_turtles(turtle_colours)
    is_racing = True
    while is_racing:
        for turt in turtles:
            turt.forward(randint(1, 10))
            if turt.xcor() > 230:
                is_racing = False
                winner = turt.pencolor()
                if user_bet.lower() == winner.lower():
                    print(f"You won! The {winner} turtle won the race.")
                else:
                    print(f"You lost. The {winner} turtle won the race.")


turtle_race(colours)
screen.exitonclick()
