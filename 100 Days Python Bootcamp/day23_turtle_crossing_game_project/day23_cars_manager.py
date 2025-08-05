from turtle import Turtle
import random
LANES = [-240,-220, -200, -180, -160,- 140, -120, -100, -80, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240]
STARTING_POINTS = [300,340,380,420]

class CarManager:

    def __init__(self):
        self.cars = []
        self.base_speed = 2
        self.colours = [
            "medium blue","light green","hot pink","blue violet","dark green","deep sky blue",
            "cornflower blue","sea green","teal","medium purple","plum","purple","medium violet red",
            "indigo","dark slate blue","gold"
        ]

    # generate starting cars
    def generate_cars(self,level):
        in_screen_cars = (level * 5) + 10
        for _ in range(in_screen_cars):
            self.create_car()

        return in_screen_cars

    def create_car(self):
        max_attempts = 20  # Prevent infinite loop
        spacing_threshold = 20  # Minimum vertical distance between cars

        for _ in range(max_attempts):
            x = random.choice(STARTING_POINTS)
            y = random.choice(LANES)

            # Check overlap with existing cars
            if all(abs(y - car.ycor()) > spacing_threshold and abs(x - car.xcor()) > (spacing_threshold * 2) for car in self.cars):
                car = Turtle("square")
                car.shapesize(stretch_wid=1, stretch_len=2)
                car.penup()
                car.color(random.choice(self.colours))
                car.goto(x, y)
                car.setheading(180)
                self.cars.append(car)
                return  # Successfully added a car

        # If no valid position after max_attempts, skip this car

    def move_cars(self,level,player):
        speed = self.base_speed + level * 1.2
        for car in self.cars:
            car.forward(speed)
            if car.xcor() < -310:
                car.color(random.choice(self.colours))
                car.teleport(random.choice(STARTING_POINTS)+40,random.choice(LANES))
            if car.distance(player) < 25:
                is_collision = True
                return is_collision

        is_collision = False
        return is_collision
