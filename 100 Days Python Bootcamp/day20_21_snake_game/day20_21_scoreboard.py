from idlelib.pyshell import restart_line
from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Pixelify Sans",20,"normal")
WARNING_FONT = ("Pixelify Sans",40,"normal")
ENDING_POSITIONS = [(0, 150), (0, 50), (0, -50), (0, -150),(0,-250)]

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.player_score = 0
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.player_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.player_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.color("red")
        for position in ENDING_POSITIONS:
            self.goto(position)
            self.write(f"GAME OVER!",align=ALIGNMENT,font=WARNING_FONT)



