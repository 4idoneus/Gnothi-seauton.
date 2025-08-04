from turtle import Turtle, Screen
import random

# Setup screen
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)

# --- Random color with no immediate repeats ---
def random_colour():
    while True:
        new_colour = tuple(random.randint(0, 255) for _ in range(3))
        if new_colour != random_colour.last_colour:
            random_colour.last_colour = new_colour
            return new_colour
random_colour.last_colour = None

# --- Labeling Function ---
def label_turtle(turtle, name, offset=30):
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(offset)
    turtle.write(name, align="center", font=("Arial", 10, "bold"))
    turtle.backward(offset)
    turtle.setheading(0)

def generate_speed():
    speed_value = random.randint(1,10)
    return speed_value
finish = Turtle(shape="classic",undobuffersize=1000,visible=False)
finish.penup()
# --- Turtle Racer Setup ---
turtle_names = ["Ai", "Lethe", "Cathrine", "Philip", "Yui","Sake","Soju"]
start_y = -150
turtles = []

for i, name in enumerate(turtle_names):
    racer = Turtle("turtle")
    racer.color(random_colour())
    racer.penup()
    racer.goto(x=-200, y=start_y + i * 50)
    label_turtle(racer, name, offset=10)
    turtles.append((name, racer))

# --- User Input ---
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a name: ").title()
finish.setposition(210,225)
finish.pendown()
finish.right(90)
finish.forward(550)

in_race = True
winner = ""
while in_race:
    for name,racer in turtles:
        racer.forward(generate_speed())
        if racer.xcor() > 200:  # Finish line at x = 200
            in_race = False
            winner = name
            break
if winner == user_bet:
    print(f"Congrats you win! Your turtle {user_bet} is the fastest turtle. ")
    screen.title(f"Congrats you win! Your turtle {user_bet} is the fastest turtle. ")
else:
    print(f"Sorry You lose. The winner is {winner}")
    screen.title(f"Sorry You lose. The winner is {winner}")

screen.exitonclick()