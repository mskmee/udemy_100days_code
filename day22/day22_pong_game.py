import time
from turtle import Screen
from day22_score import Score
from day22_paddle import Paddle
from day22_ball import Ball


screen = Screen()
screen.title('Pong')
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')

score = Score()

score.left_player()
score.right_player()

left_paddle = Paddle()
right_paddle = Paddle()
right_paddle.goto(270, 0)

speed = 1


screen.listen()
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')
screen.onkey(left_paddle.move_up, 'a')
screen.onkey(left_paddle.move_down, 's')

ball = Ball()
game_on = True
round_on = True

while game_on:
    screen.update()
    screen.tracer(1)

    ball.start_ball()

    #detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce()
    #detect collision with the paddle
    if right_paddle.distance(ball) < 50 and ball.xcor() > 250:
        ball.ball_bounce_paddle()
        speed += 0.3
        ball.speed(speed)

    elif left_paddle.distance(ball) < 50 and ball.xcor() < -250:
        ball.ball_bounce_paddle()
        speed += 0.3
        ball.speed(speed)

    if ball.xcor() > 280:
        score.update_score('left_player')
        ball.reset_position()
    elif ball.xcor() < -280:
        score.update_score('right_player')
        ball.reset_position()

    if score.right_player_score == 3:
        score.end_game('Right player')
        game_on = False
    elif score.left_player_score == 3:
        score.end_game('Left player')
        game_on = False

screen.exitonclick()
