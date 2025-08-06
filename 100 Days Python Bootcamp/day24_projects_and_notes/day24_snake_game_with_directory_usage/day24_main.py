#This code same as the Day 20-21. Just import names are different.

from turtle import Screen
from day24_food import Food
import day24_scoreboard as s
import time
from day24_snake import Snake


screen = Screen()
screen.setup(width=600, height=600)

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

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    #Detect collision with itself.
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()
    screen.update()
    time.sleep(0.1)




screen.exitonclick()