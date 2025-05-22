import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Mondrian-Style Art")

# Turtle setup
pen = turtle.Turtle()
pen.speed("fastest")
pen.pensize(5)

# Colors used by Mondrian
colors = ["red", "blue", "yellow", "white"]


# Function to draw a filled rectangle
def draw_rectangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()


# Draw the grid
def draw_mondrian_art():
    start_x, start_y = -200, 200
    row_heights = [random.randint(50, 150) for _ in range(4)]
    col_widths = [random.randint(50, 150) for _ in range(4)]

    y = start_y
    for height in row_heights:
        x = start_x
        for width in col_widths:
            color = random.choice(colors)
            draw_rectangle(x, y, width, height, color)
            x += width
        y -= height

    # Draw grid lines
    pen.color("black")
    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()
    y = start_y
    for height in row_heights:
        x = start_x
        for width in col_widths:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            for _ in range(2):
                pen.forward(width)
                pen.right(90)
                pen.forward(height)
                pen.right(90)
            x += width
        y -= height


draw_mondrian_art()
pen.hideturtle()
screen.mainloop()
