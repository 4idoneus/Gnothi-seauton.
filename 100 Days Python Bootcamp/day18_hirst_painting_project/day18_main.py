from turtle import Turtle, Screen
def move_square(turtle,angle):
    turtle.setheading(angle)
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    for i in range(4):
        turtle.left(180)
        turtle.forward(100)
        turtle.left(90)
    for i in range(4):
        turtle.right(180)
        turtle.forward(100)
        turtle.right(90)
    for i in range(4):
        turtle.left(45)
        turtle.forward(141.42135623730950488016887242097)
        turtle.right(135)
        turtle.forward(100)
        turtle.right(45)
        turtle.forward(141.42135623730950488016887242097)
        turtle.right(135)
        turtle.forward(100)
ai = Turtle()
lethe = Turtle()
philip = Turtle()
ui = Turtle()

ai.color("dark green")
lethe.color("dark red")
philip.color("midnight blue")
ui.color("indigo")

ai.speed(10)
lethe.speed(10)
philip.speed(10)
ui.speed(10)
for _ in range(1,86,4):
    move_square(ai,_)
    move_square(lethe,_ + 1)
    move_square(philip,_ + 2)
    move_square(ui,_ + 3)



#This code snippet should happen on the bottom of the code
screen = Screen()
screen.exitonclick()