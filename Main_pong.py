from turtle import Screen, Turtle
from Paddle_Class import Paddle
from Score import Scores
from Ball_Class import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1500, height=800)
screen.title('Abhi\'s Beer Pong')
screen.tracer(0)

partition= Turtle()
partition.penup()
partition.color('white')
partition.goto(0,400)
partition.setheading(270)
for _ in range(90):
    partition.pendown()
    partition.fd(5)
    partition.penup()
    partition.fd(5)


player1 = Paddle(700)
# player1.player_one_paddle(730)
player2 = Paddle(-710)
# player2.player_one_paddle(-740)

p1_score = Scores(40, 300)
p2_score = Scores(-40, 300)

ball = Ball()

screen.listen()
screen.onkeypress(fun=player1.move_up, key='Up')
screen.onkeypress(fun=player1.move_down, key='Down')
screen.onkeypress(fun=player2.move_up, key='w')
screen.onkeypress(fun=player2.move_down, key='s')

GAME_ON = True
delay=0.05
while GAME_ON:
    screen.update()
    time.sleep(delay)
    ball.move()
    if ball.ycor() >= 390 or ball.ycor() <= -390:
        ball.bounce()


    # Detect ball collision with player1
    if ball.distance(player1.pos()) <= 50 and ball.xcor() > 690:
        ball.bounce_back()
        if delay<0:
            delay=0
        else:
            delay*=0.9


    # Detect ball collision with player2
    if ball.distance(player2.pos()) <= 50 and ball.xcor() < -690:
        ball.bounce_back()
        if delay<0:
            delay=0
        else:
            delay*=0.9

    if ball.xcor() > 700:
        p2_score.keep_score()
        # ball.reset()
        ball.goto(0,0)
        delay=0.1
        ball.bounce_back()

    if ball.xcor() <= -710:
        p1_score.keep_score()
        ball.goto(0,0)
        delay=0.1
        ball.bounce_back()



screen.exitonclick()
