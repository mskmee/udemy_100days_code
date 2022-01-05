import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_forward, 'Up')
screen.onkey(player.move_back, 'Down')
screen.onkey(player.move_left, 'Left')
screen.onkey(player.move_right, 'Right')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.lose_board()

    if player.finish():
        scoreboard.new_round()
        time.sleep(1)
        scoreboard.appended_score()
        car_manager.level_up()


screen.exitonclick()
