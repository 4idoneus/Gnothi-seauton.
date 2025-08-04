from turtle import Turtle,Screen
import day19_etch_a_sketch_app_movement_system as ms

screen = Screen()
screen.colormode(255)

ai = Turtle()

def clear_drawing():
    screen.resetscreen()

screen.listen()
screen.onkey(lambda: ms.move_forwards(ai), key="w")
screen.onkey(lambda: ms.move_backwards(ai),key="s")
screen.onkey(lambda: ms.turn_right(ai),key="d")
screen.onkey(lambda: ms.turn_left(ai),key="a")
screen.onkey(key="c",fun=clear_drawing)

screen.exitonclick()


