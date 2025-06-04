from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.color("green")
timmy.goto(0, 200)
timmy.write("Hello", False, "center", ("Calibri", 20, "underline"))
timmy.hideturtle()
screen.exitonclick()
