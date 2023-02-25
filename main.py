import turtle
import paddle
import ball
import time
import score


screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = paddle.Paddle("right")
l_paddle = paddle.Paddle("left")
ball = ball.Ball()
score = score.Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 285 or ball.ycor() < - 285:
        ball.collide_wall()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.collide_paddle()

    if ball.xcor() > 390:
        ball.center()
        ball.collide_paddle()
        score.l_point()
    if ball.xcor() < - 390:
        ball.center()
        ball.collide_paddle()
        score.r_point()

screen.exitonclick()
