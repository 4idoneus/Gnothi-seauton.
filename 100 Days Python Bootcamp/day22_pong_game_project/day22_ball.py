from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self,move_distance):
        super().__init__()
        self.heading = 0
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_distance = move_distance
        self.y_move = self.move_distance
        self.x_move = self.move_distance


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_from_paddle(self, segment_index: int, paddle_side: str,max_speed=6):
        """
        Changes the direction (angle) of the ball based on paddle segment hit.
        Speed remains unchanged. No math module used.
        """

        # Predefined unit-like direction vectors (x %, y %) for movement direction
        direction_vectors = {
            0: (0.5, 1),  # steep upward
            1: (0.8, 0.5),  # slight upward
            2: (1, 0),  # straight
            3: (0.8, -0.5),  # slight downward
            4: (0.5, -1),  # steep downward
        }

        x_percent, y_percent = direction_vectors.get(segment_index, (1, 0))

        # Normalize based on current speed magnitude

        speed = (abs(self.x_move) ** 2 + abs(self.y_move) ** 2) ** 0.5
        if speed > max_speed:
            speed = max_speed
        # Reverse x direction depending on which paddle
        x_direction = -1 if paddle_side == "right" else 1

        self.x_move = x_direction * x_percent * speed
        self.y_move = y_percent * speed

        # Optional: clamp to avoid too slow movement
        if abs(self.x_move) < 1:
            self.x_move = self.move_distance if self.x_move > 0 else -self.move_distance
        if abs(self.y_move) < 1:
            self.y_move = self.move_distance if self.y_move > 0 else -self.move_distance

    def refresh_ball(self):
        random_y = random.randint(-250,250)
        self.teleport(0,random_y)

    def need_for_speed(self, scoreboard):
        total_score = scoreboard.player1_score + scoreboard.player2_score
        if total_score in (5, 10):
            self.speed_up()

    def speed_up(self, factor=1.3, max_speed=6):
        # Increase base speed but cap it
        self.move_distance = min(self.move_distance * factor, max_speed)

        # Calculate current speed magnitude (pythagorean)
        current_speed = (self.x_move ** 2 + self.y_move ** 2) ** 0.5

        # Calculate ratio to scale current x_move and y_move to new speed_distance
        if current_speed == 0:
            # Avoid division by zero; set to base speed moving right
            self.x_move = self.move_distance
            self.y_move = 0
        else:
            scale = self.move_distance / current_speed
            self.x_move *= scale
            self.y_move *= scale


