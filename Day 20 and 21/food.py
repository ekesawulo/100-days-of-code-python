from random import randint
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("coral")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.teleport(randint(-280, 280), randint(-280, 270))
