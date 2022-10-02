from turtle import Turtle
STARTIN_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTIN_POSITION:
            self.add_segment(position)

    
    def add_segment(self, position):
            new_square = Turtle("circle")
            new_square.penup()
            new_square.color("orange")
            new_square.goto(position)
            self.segment.append(new_square)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    
    
    def move(self):
        for seg_num in range(len(self.segment) - 1 , 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.segment[0].setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(LEFT)
    
