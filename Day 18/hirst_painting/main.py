import colorgram
import random
import turtle

turtle.colormode(255)

timmy = turtle.Turtle()
timmy.speed("fastest")
screen = turtle.Screen()


def extract_colours(image_path, num_colours=9):
    """Extracts a specified number of colours from an image using colorgram module

    Args:
        image_path (string): path of the image
        num_colours (int, optional): Number of colours to extract. Defaults to 9.

    Returns:
        list of tuples: A list of rgb tuples of the extracted colours
    """
    extracted_colours = colorgram.extract(image_path, num_colours)
    return [(colour.rgb.r, colour.rgb.g, colour.rgb.b) for colour in extracted_colours]


# def random_colour(colours_list):
#     """Selects a random colour tuple from the extracted list of colours

#     Args:
#         colours_list (List): A list of rgb tuples

#     Returns:
#         tuple: Returns an rgb tuple
#     """
#     return random.choice(colours_list)


def dot_painting(colours, dot_size, spacing, grid_size):
    """Draws a hirst-like dot painting

    Args:
        colours (list): List of extracted colours
        dot_size (int): Size of the dot
        spacing (int): Space between dots
        grid_size (int): Grid size
    """
    # timmy.setheading(225)
    # timmy.forward(300)

    for y in range(0, grid_size * spacing, spacing):
        timmy.hideturtle()
        timmy.goto(0, y)
        timmy.setheading(0)
        timmy.showturtle()
        for _ in range(grid_size):
            timmy.dot(dot_size, random.choice(colours))
            timmy.penup()
            timmy.forward(spacing)
    timmy.hideturtle()


colours_list = extract_colours("Day 18/hirst_painting/image.Jpeg", num_colours=12)
dot_painting(
    colours=colours_list,
    dot_size=20,
    spacing=50,
    grid_size=10,
)
screen.exitonclick()
