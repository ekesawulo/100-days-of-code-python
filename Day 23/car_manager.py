from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_START_RANGE = (-250, 250)
X_START = 300


class CarManager:
    """
    Car Manager object, creates new cars and controls their movement
    """

    def __init__(self) -> None:
        """
        Creates a list that will hold individual car turtles and also holds their move distance
        """
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self) -> None:
        """
        Creates a new car at a random Y position as an instance of Turtle
        """
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(COLORS))
        random_y = random.randint(*Y_START_RANGE)
        car.goto(X_START, random_y)
        self.cars.append(car)

    def move(self) -> None:
        """
        Move cars along the window from right to left
        """
        for car in self.cars:
            car.backward(self.move_distance)

    def increase_speed(self) -> None:
        """
        Increase the speed of the cars after completing a level
        """
        self.move_distance += MOVE_INCREMENT
