from turtle import Turtle,Screen
from prettytable import PrettyTable
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

my_table = PrettyTable()
my_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
my_table.add_column("Type", ["Electric", "Water", "Fire"])
my_table.align="l"
print(my_table)
