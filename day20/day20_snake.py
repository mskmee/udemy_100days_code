import time
import turtle
from turtle import Turtle, Screen
from day20_snake_class import Snake

game_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)


snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
screen.exitonclick()


