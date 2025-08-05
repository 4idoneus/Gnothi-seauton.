from turtle import Turtle
import time
WARNING_FONT = ("Pixelify Sans",40,"normal")
ENDING_POSITIONS = [(0, 150), (0, 50), (0, -50), (0, -150),(0,-250)]
BORDER_PADDING = 20
FONT = ("Pixelify Sans",20,"normal")
FONT2 = ("Pixelify Sans",18,"bold")

def draw_square(turtle, x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def draw_checkerboard(turtle, x_min, x_max, y_min, y_max, tile_size):
    turtle.speed("fastest")
    colors = ["black", "white"]

    # Ensure x_min < x_max and y_min < y_max
    if x_min > x_max:
        x_min, x_max = x_max, x_min
    if y_min > y_max:
        y_min, y_max = y_max, y_min

    # Calculate hole area (centered 8x2 tiles)
    total_width = x_max - x_min
    total_height = y_max - y_min

    hole_width = tile_size * 8
    hole_height = tile_size * 2

    hole_x_min = x_min + (total_width - hole_width) / 2
    hole_x_max = hole_x_min + hole_width
    hole_y_min = y_min + (total_height - hole_height) / 2
    hole_y_max = hole_y_min + hole_height

    # Start from top-left
    y = y_max
    row = 0
    while y - tile_size >= y_min:
        x = x_min
        col = 0
        while x + tile_size <= x_max:
            # Skip tiles in the hole area
            tile_center_x = x + tile_size / 2
            tile_center_y = y - tile_size / 2

            if not (hole_x_min <= tile_center_x <= hole_x_max and
                    hole_y_min <= tile_center_y <= hole_y_max):
                color_index = (row + col) % 2
                draw_square(turtle, x, y, tile_size, colors[color_index])
            x += tile_size
            col += 1
        y -= tile_size
        row += 1

    # Draw border after filling tiles
    turtle.penup()
    turtle.goto(x_min, y_max)
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor("black")

    for _ in range(2):
        turtle.forward(x_max - x_min)
        turtle.right(90)
        turtle.forward(y_max - y_min)
        turtle.right(90)

    turtle.pensize(1)

def draw_game_border(turtle, width, height):
    turtle.penup()
    turtle.goto(-width // 2, (height // 2 + 20))
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def write_game_title(turtle, screen_height):
    turtle.penup()
    turtle.goto(0, screen_height // 2 - 20)
    turtle.write("Aidoneus's Crossing", align="center", font=FONT)

def draw_lines(turtle,line_name):

    if line_name == "Start":
        draw_checkerboard(turtle, x_min=-300, x_max=300, y_min=-280, y_max=-260, tile_size=10)
        turtle.penup()
        turtle.color("red")
        turtle.goto(0, -285)
        turtle.write("Start", align="center", font=FONT2)
    else:
        draw_checkerboard(turtle, x_min=-300, x_max=300, y_min=260, y_max=280, tile_size=10)
        turtle.penup()
        turtle.color("red")
        turtle.goto(0, 255)
        turtle.write(line_name, align="center", font=FONT2)

def screen_setting(screen, screen_width=600, screen_height=600):
    screen.setup(width=610, height=625)
    screen.listen()
    screen.title("Turtle Crossing")
    screen.tracer(0)
    screen.bgcolor("white")
    screen_detail_turtle = Turtle()
    screen_detail_turtle.hideturtle()
    draw_game_border(screen_detail_turtle, screen_width, screen_height)
    write_game_title(screen_detail_turtle, screen_height)
    draw_lines(screen_detail_turtle,"Finish")
    draw_lines(screen_detail_turtle,"Start")

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
        self.hideturtle()
        self.penup()
        self.color("red")


    def update_scoreboard(self,game_level):
        self.goto(x= -280, y= 280)
        self.write(f"Level {game_level}", align="left", font=FONT)

    def game_over(self):
        self.color("red")
        for position in ENDING_POSITIONS:
            self.goto(position)
            self.write(f"GAME OVER!",align="center",font=WARNING_FONT)
