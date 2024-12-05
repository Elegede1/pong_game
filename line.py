from turtle import Turtle

# drawing a line across the center of the canvas
class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        # self.goto(0, 0)
        # self.pendown()
        self.goto(0, 380)
        self.setheading(270)
        self.hideturtle()
        # self.goto(0, -380)
        self.width(5)
        self.draw_dashed_line()

    def draw_dashed_line(self):
        while self.ycor() > -380:  # Loop until reaching the bottom
            self.pendown()
            self.forward(20)     # Draw a 20-pixel line segment
            self.penup()         
            self.forward(20)