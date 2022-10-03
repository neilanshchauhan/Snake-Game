# Hello Neilansh 😁 .........
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Green")
        self.speed("fastest")
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.penup()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270,270)
        random_y = random.randint(-270,270)
        self.goto(random_x, random_y)
    