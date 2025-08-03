```
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

```
This is the first edition code of using Turtle on Python. It creates circle from 4 squares rotation.
##### Dashed line Code
```
for _ in range(20):
    ai.forward(10)
    ai.penup()
    ai.forward(10)
    ai.pendown()
```

##### Draw triangle to decagon
```
colours = ["dark green","cyan","red","magenta","gold","blue","black","orange"]
for i in range(3, 11, 1):
    colour = r.choice(colours)
    ai.color(colour)
    for _ in range(i):
        ai.left(360/i)
        ai.forward(100)
> You can turn the second for loop into a function.

def draw_gon(number_of_sides):
    angle = 360/number_of_sides
    for _ in range(number_of_sides):
        ai.left(angle)
        ai.forward(100)
```
##### Random Walk Code
```
colours = ["dark green","cyan","red","magenta","gold","blue","black","orange"]
directions = [0, 90, 180, 270]

a = 1
for _ in range(100):
    ai.color(r.choice(colours))
    ai.forward(30)
    ai.setheading(r.choice(directions))
    ai.pensize(a) #For every loop it will increase the the pen size
    if a > 10: #In turtle max speed is 10(don't count the 0 because lack of animation) so if the a is more than 10 it makes the speed 10
        ai.speed(10)
    else:
        ai.speed(a) #For every loop it will increase the the speed
    a += 0.1
```
##### Random Walk with RGB Colour Randomizing
```
directions = [0, 90, 180, 270]
screen = Screen()
screen.colormode(255)

ai = Turtle()
a = 1
for _ in range(200):
    ai.color((r.randint(0,255),r.randint(0,255),r.randint(0,255)))
    ai.forward(30)
    ai.setheading(r.choice(directions))
    ai.pensize(a)
    if a > 10:
        ai.speed(10)
    else:
        ai.speed(a)
    a += 0.1
```

##### Drawing a Spirograph with a random Colour Generator
```
def random_colour():
    r = rand.randint(0,255)
    g = rand.randint(0,255)
    b = rand.randint(0,255)
    return r,g,b

ai = Turtle()
ai.speed(0)
the_angle_between_circles = 17
for _ in range(0,361,the_angle_between_circles):
    ai.color((random_colour()))
    ai.circle(100)
    ai.setheading(_)
```