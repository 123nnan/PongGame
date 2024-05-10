from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.tracer(0)
ball = Ball()

# Scoreboard
scoreboard = Scoreboard()

# Key Binds
screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

# Screen Set-up
screen.setup(800,600)
screen.title("Pong Game")
screen.bgcolor("black")

# Game
game_on = True
while game_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()

    # Detection of collision against top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce
        ball.bounce_y()

    # Detection of collision with the paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() == 330 or ball.distance(l_paddle) < 60 and ball.xcor() == -330:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_pos()
        scoreboard.increase_l_score()

    if ball.xcor() < -400:
        ball.reset_pos()
        scoreboard.increase_r_score()

    if scoreboard.l_score >= 10 or scoreboard.r_score >= 10:
        scoreboard.game_over()
        game_on = False
screen.exitonclick()