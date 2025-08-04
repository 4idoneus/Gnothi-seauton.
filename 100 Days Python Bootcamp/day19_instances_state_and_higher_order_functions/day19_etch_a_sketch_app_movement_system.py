
def move_forwards(turtle_name):
    turtle_name.forward(10)
def move_backwards(turtle_name):
    turtle_name.backward(10)
def turn_right(turtle_name):
    heading = turtle_name.heading()
    turtle_name.setheading(heading+10)
def turn_left(turtle_name):
    heading = turtle_name.heading()
    turtle_name.setheading(heading - 10)