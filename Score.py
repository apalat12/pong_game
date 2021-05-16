from turtle import Turtle



class Scores(Turtle):

    def __init__(self,posx,posy):
        super().__init__()
        self.color('white')
        self.score=0
        self.penup()
        self.goto(posx,posy)
        self.write("{}".format(self.score), move=False, align="center", font=("Courier", 50, "bold"))
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write("{}".format(self.score), move=False, align="center", font=("Courier", 50, "bold"))

    def keep_score(self):
        self.score+=1
        self.update_scoreboard()
