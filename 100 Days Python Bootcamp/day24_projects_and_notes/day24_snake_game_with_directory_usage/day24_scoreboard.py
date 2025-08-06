

from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Pixelify Sans",20,"normal")
WARNING_FONT = ("Pixelify Sans",40,"normal")
ENDING_POSITIONS = [(0, 150), (0, 50), (0, -50), (0, -150),(0,-250)]


def restart_game(screen):
    answer = screen.textinput("Restart", "Do you want to play again?\nType y/yes or n/no").lower()
    if answer and answer in ("y", "yes"):
        # If player wants to continue clears the screen.
        screen.clear()
        return True
    # If player wants to exit.
    elif answer in ("n", "no"):
        return False
    #If player's answer is not supported
    else:
        return False

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("day24_data.txt") as data:
            self.high_score = int(data.read())
        self.player_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()   #Different from 20-21
        self.write(f"Score: {self.player_score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self): #Different from 20-21
        if self.player_score > self.high_score:
            self.high_score = self.player_score
            with open("day24_data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.player_score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.player_score += 1
        self.update_scoreboard()




