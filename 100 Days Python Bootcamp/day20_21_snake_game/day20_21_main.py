from turtle import Screen
from day20_21_food import Food
import day20_21_scoreboard as s
import time
from day20_21_snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
play_game = True

while play_game:

    screen.listen()
    screen.title("SNAKE GAME")
    screen.tracer(0)
    screen.bgcolor("black")
    snake = Snake()
    food = Food()
    scoreboard = s.Scoreboard()



    screen.onkey(snake.up,"w")
    screen.onkey(snake.up,"Up")

    screen.onkey(snake.down,"s")
    screen.onkey(snake.down,"Down")

    screen.onkey(snake.right,"d")
    screen.onkey(snake.right,"Right")

    screen.onkey(snake.left,"a")
    screen.onkey(snake.left,"Left")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            snake.extend()
            scoreboard.increase_score()
            food.refresh()

        #Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        #Detect collision with itself.
        for segment in snake.segment[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    #Restart the game mechanic.
    play_game = s.restart_game(screen)

screen.exitonclick()