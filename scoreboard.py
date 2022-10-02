from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24 , "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x= 0, y=268)
        self.hideturtle()
        self.update_score()

        
    def update_score(self):
        self.write(f"Score: {self.score}",align= ALIGNMENT,font = FONT)


### HERO FUNCTION for SCOREBOARD
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write('GAME OVER', font = FONT, align=ALIGNMENT)