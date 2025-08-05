from turtle import Turtle
import time
DISTANCE_BETWEEN_LINES = 20
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1200
BORDER_PADDING = 10
FONT = ("Pixelify Sans",20,"normal")
W_FONT = ("Pixelify Sans",50,"normal")
GO_FONT = ("Pixelify Sans",30,"normal")
GO_ENDING_POSITIONS = [(0, 200), (0, 100), (0, -100), (0, -200)]
GG_ENDING_POSITIONS = [(0, 250),(0, 150), (0, 50), (0, -50), (0, -150),(0, -250)]

def draw_game_border(turtle, width, height):
    turtle.hideturtle()
    turtle.color("white")
    turtle.penup()
    top_left_x = -width // 2
    top_left_y = height // 2

    turtle.goto(top_left_x, top_left_y)
    turtle.pendown()

    # Draw 4 sides
    turtle.goto(width // 2, top_left_y)  # Top side
    turtle.goto(width // 2, -height // 2)  # Right side
    turtle.goto(-width // 2, -height // 2)  # Bottom side
    turtle.goto(top_left_x, top_left_y)  # Left side

def write_game_title(turtle, screen_width, screen_height):
    turtle.hideturtle()
    turtle.color("white")
    turtle.penup()
    font = ("Courier", 20, "bold")

    # Top title
    turtle.goto(0, (screen_height // 2) + BORDER_PADDING)
    turtle.write("Lethe's Pong Game", align="center", font=font)

    # Bottom title
    turtle.goto(0, -(screen_height // 2) - 30)
    turtle.write("Lethe's Pong Game", align="center", font=font)

def draw_center_line(turtle, height):
    turtle.hideturtle()
    turtle.color("white")
    turtle.teleport(0, (height // 2) - 5)
    turtle.setheading(270)

    steps = height // (DISTANCE_BETWEEN_LINES * 2)
    for _ in range(steps):
        turtle.forward(DISTANCE_BETWEEN_LINES)
        turtle.penup()
        turtle.forward(DISTANCE_BETWEEN_LINES)
        turtle.pendown()

def screen_setting(screen,center_line_turtle):
    screen.setup(width=1225, height=625)
    screen.listen()
    screen.title("PONG")
    screen.tracer(0)
    screen.bgcolor("black")
    draw_center_line(center_line_turtle,SCREEN_HEIGHT)

    draw_game_border(center_line_turtle, SCREEN_WIDTH, SCREEN_HEIGHT)
    draw_center_line(center_line_turtle, SCREEN_HEIGHT)
    write_game_title(center_line_turtle, SCREEN_WIDTH, SCREEN_HEIGHT)

def restart_game(screen):
    time.sleep(5)
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
        self.color("white")
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.penup()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(x= 100, y= 270)
        self.write(f"P1: {self.player1_score}", align="right", font=FONT)
        self.goto(x= -100, y= 270)
        self.write(f"P2: {self.player2_score}", align="left", font=FONT)

    def increase_score(self,player_name):
        if player_name == "Right":
            self.player1_score += 1
        else:
            self.player2_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.color("white")
        self.goto(0,0)
        if self.player1_score > self.player2_score:
            self.write(f"Winner is Player 1 with {self.player1_score}.",align="center",font=W_FONT)
        elif self.player1_score < self.player2_score:
            self.write(f"Winner is Player 2 with {self.player2_score}.",align="center",font=W_FONT)
        else:
            self.write(f"It's a DRAW. When is the rematch?",align="center",font=W_FONT)
        self.color("red")
        for position in GO_ENDING_POSITIONS:
            self.goto(position)
            self.write(f"GAME OVER!",align="center",font=GO_FONT)
        self.color("blue")
        for position in GG_ENDING_POSITIONS:
            self.goto(position)
            self.write(f"GG! GG! GG!", align="center", font=FONT)






