from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.8, 0.8)
        self.speed("slow")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def collide_wall(self):
        """ to check the collision with the upper and lower edges of the screen, the ball should bounce """
        self.y_move *= -1

    def collide_paddle(self):
        """ to check the collision with the paddles, the ball should bounce """
        self.x_move *= -1
        self.move_speed *= 0.9

    def center(self):
        self.goto(0, 0)
        self.move_speed = 0.08
