import time
from turtle import Turtle, Screen
from day22_paddle import Paddle
from day22_ball import Ball
import day22_scoreboard as s
import day22_paddle_movement_system as movement
PADDLE1_STARTING_POSITIONS = [(580,40), (580,20), (580, 0), (580,-20), (580,-40)]
PADDLE2_STARTING_POSITIONS = [(-580,40), (-580,20), (-580, 0), (-580,-20), (-580,-40)]

screen = Screen()
center_line= Turtle()


game_is_on = True
while game_is_on:

    s.screen_setting(screen, center_line)

    paddle1 = Paddle(PADDLE1_STARTING_POSITIONS, "red")
    paddle2 = Paddle(PADDLE2_STARTING_POSITIONS, "blue")

    scoreboard = s.Scoreboard()

    #Paddle1 movement control system
    screen.onkeypress(movement.paddle1_up_press, "Up")
    screen.onkeyrelease(movement.paddle1_up_release, "Up")

    screen.onkeypress(movement.paddle1_down_press, "Down")
    screen.onkeyrelease(movement.paddle1_down_release, "Down")

    # Paddle2 movement control system
    screen.onkeypress(movement.paddle2_up_press, "w")
    screen.onkeyrelease(movement.paddle2_up_release, "w")

    screen.onkeypress(movement.paddle2_down_press, "s")
    screen.onkeyrelease(movement.paddle2_down_release, "s")
    ball = Ball(3)
    ball.hideturtle()
    in_game = True

    while in_game:
        ball.showturtle()
        ball.move()

        #Flag system trigger for smooth movement of paddle
        if movement.paddle1_up:
            paddle1.up()
        if movement.paddle1_down:
            paddle1.down()
        if movement.paddle2_up:
            paddle2.up()
        if movement.paddle2_down:
            paddle2.down()

        #Detection collusion with wall for ball
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        # Detection collusion with paddle1 for ball
        index = paddle1.detect_collision(ball)
        if index is not None and ball.xcor() > 561:
            ball.bounce_from_paddle(index, paddle_side="right")

        index = paddle2.detect_collision(ball)
        if index is not None and ball.xcor() < -561:
            ball.bounce_from_paddle(index, paddle_side="left")

        if ball.xcor() < -590 or ball.xcor() > 590:
            if ball.xcor() > 590:
                print("Player2 won a point")
                scoreboard.increase_score("Left")
            elif ball.xcor() < -590:
                print("Player1 won a point")
                scoreboard.increase_score("Right")

            ball.refresh_ball()

        ball.need_for_speed(scoreboard)
        if scoreboard.player1_score + scoreboard.player2_score >= 20:
            scoreboard.game_over()
            ball.hideturtle()
            in_game = False

        # Refresh rate of the screen
        screen.update()
        time.sleep(0.01)

    # Restart the game mechanic.

    game_is_on = s.restart_game(screen)

screen.exitonclick()