from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        if position == "left":
            self.goto(-350, 0)
        else:
            self.goto(350, 0)
        self.shapesize(5, 1)
        self.color("white")

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 30)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 30)
