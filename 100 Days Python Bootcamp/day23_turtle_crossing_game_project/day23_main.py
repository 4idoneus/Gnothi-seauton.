# Turtle Crossing Game
# A simple game where the player controls a turtle to cross a road filled with obstacles.
# The player levels up by crossing the road successfully.
# Each level increases the difficulty with more obstacles.
import time
from turtle import Turtle, Screen
import day23_screen_details_and_scoreboard as s
from day23_level_manager import Level,Player

screen = Screen()

while True:

    s.screen_setting(screen)
    player = Player()
    screen.onkeypress(player.move, "Up")
    screen.onkeypress(player.move, "w")
    screen.onkey(screen.bye, "q")  # Press 'q' to quit immediately
    level_manager = Level(player, screen)

    play_game = True
    while play_game:

        play_game= level_manager.play_game()
        screen.update()
        time.sleep(0.05)
        
    # Restart the game or end the game method
    if not s.restart_game(screen):
        break
screen.exitonclick()
