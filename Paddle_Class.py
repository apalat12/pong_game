from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(x_pos, 0)
        # self.paddle.append(self)

    def move_up(self):
        pos = self.ycor()+20
        self.goto(self.xcor(),pos)

    def move_down(self):
        pos = self.ycor()-20
        self.goto(self.xcor(),pos)
