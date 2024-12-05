from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, 0)

    def go_up(self):
        y = self.ycor() + 20
        self.sety(y)

    def go_down(self):
        y = self.ycor() - 20
        self.sety(y)


