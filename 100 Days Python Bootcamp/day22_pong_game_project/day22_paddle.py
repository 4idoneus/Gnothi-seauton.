from turtle import Turtle
MOVE_DISTANCE = 10

class Paddle(Turtle):

    def __init__(self,starting_positions, color="white"):
        super().__init__()
        self.segment = []
        self.starting_positions = starting_positions
        self.color = color
        self.create_paddle()

    def create_paddle(self):
        for position in self.starting_positions:
            #Create a paddle that has 5 square turtles
            segment = Turtle("square")
            segment.color(self.color)
            segment.penup()
            segment.goto(position)
            self.segment.append(segment)

    def move(self,move_distance):
        top_y = self.segment[0].ycor()
        bottom_y = self.segment[-1].ycor()
        if (top_y + move_distance) <= 280 and (bottom_y + move_distance) >= -280:
            for segment in self.segment:
                segment.sety(segment.ycor() + move_distance)
    def up(self):
        move_distance = MOVE_DISTANCE
        self.move(move_distance)
    def down(self):
        move_distance = - MOVE_DISTANCE
        self.move(move_distance)

    def detect_collision(self, ball):
        for i, segment in enumerate(self.segment):
            if 19 < ball.distance(segment) < 30:
                return i
        return None