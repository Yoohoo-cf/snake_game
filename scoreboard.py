from turtle import Turtle

FONT = ('Arial', 12, 'normal')
ASSIGNMENT = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 280)
        self.write(f"Score: {self.score}", align=ASSIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ASSIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align=ASSIGNMENT, font=FONT)



