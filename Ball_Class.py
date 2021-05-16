from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        # self.speed('fastest')
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        self.xpos = self.xcor() + self.xmove
        self.ypos = self.ycor() + self.ymove
        self.goto(self.xpos, self.ypos)

    def bounce(self):
        self.ymove *= -1

    def bounce_back(self):
        self.xmove *= -1

    def ball_reset(self):
        self.goto(0, 0)
