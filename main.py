import turtle
import time
from paddle import Paddle
from ball import Ball
from score import Score
from line import Line
import random

# create a screen.
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Pong")# set the title of the screen.
screen.bgcolor("black")# set the background color.
screen.tracer(0)

left_paddle = Paddle(-390) # create a paddle on the left side of the screen.
right_paddle = Paddle(386) # create a paddle on the right side of the screen.

screen.listen()
screen.onkeypress(left_paddle.go_up, "w") # w is the key to move the left paddle up.
screen.onkeypress(left_paddle.go_down, "s") # s is the key to move the left paddle down.
screen.onkeypress(right_paddle.go_up, "Up") # Up is the key to move the right paddle up.
screen.onkeypress(right_paddle.go_down, "Down") # Down is the key to move the right paddle down.

# create ball
ball = Ball()
score = Score()
line = Line()


# start the game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    # move the ball
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -360 or ball.distance(right_paddle) < 50 and ball.xcor() > 360:
        ball.bounce_x()
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()

    # check if any players score has reached 10
    if score.l_score == 10 or score.r_score == 10:
        game_is_on = False
        score.game_over()
        screen.onkeypress(score.reset, "r")

screen.exitonclick()