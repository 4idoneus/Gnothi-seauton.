from turtle import Turtle
from day23_cars_manager import CarManager
from day23_screen_details_and_scoreboard import Scoreboard

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("maroon")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.teleport(0,-290)

    def move(self):
        self.forward(10)

class Level:
    def __init__(self,player,screen):
        self.game_level = 1
        self.car_manager = CarManager()
        self.scoreboard = Scoreboard()
        self.player = player
        self.screen = screen

    def play_game(self):
        level = self.game_level
        self.scoreboard.update_scoreboard(level)
        car_manager = self.car_manager
        car_manager.generate_cars(level)
        player_cord = (self.player.xcor(),self.player.ycor())
        is_collision = car_manager.move_cars(level,player_cord)
        if is_collision:
            self.screen.clear()
            self.scoreboard.game_over()
            return False
        else:
            if self.player.ycor() > 270:
                self.game_level += 1
                self.scoreboard.update_scoreboard(self.game_level)
                self.player.teleport(0,-290)

            return True


