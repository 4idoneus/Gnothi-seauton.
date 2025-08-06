#This code same as the Day 20-21.


from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Head, Body1, Body2
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segment) - 1 , 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self,position):
        # Add a new segment to sneak.
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segment.append(segment)

    def reset(self):
        for seg in self.segment:
            seg.goto(2000,2000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def extend(self):
        # Add a new segment to sneak when it eats food.
        self.add_segment(self.segment[-1].position())
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
