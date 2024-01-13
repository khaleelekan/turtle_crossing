import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

crosser = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
level = Scoreboard()
car = CarManager()
screen.onkey(crosser.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_car()
    if crosser.ycor() == 280:
        crosser.next_level()
        level.level_up()
        car.increase_speed()

    for each in car.all_cars:
        if each.distance(crosser) < 20:
            game_is_on = False
            level.game_over()
screen.exitonclick()

