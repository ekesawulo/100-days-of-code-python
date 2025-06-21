import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")


def turtle_crossing() -> None:
    """
    Game logic, controls the generation of new cars, detects crashes and finishes a level
    """
    game_is_on = True
    counter = 0
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        if counter % 6 == 0:
            car_manager.create_car()
        car_manager.move()
        # Finish level
        if player.at_finish_line():
            scoreboard.increase_level()
            car_manager.increase_speed()
            player.reset()
        counter += 1

        # Detect crash
        for car in car_manager.cars:
            if player.distance(car) < 20:
                game_is_on = False
                scoreboard.game_over()


turtle_crossing()

screen.exitonclick()
