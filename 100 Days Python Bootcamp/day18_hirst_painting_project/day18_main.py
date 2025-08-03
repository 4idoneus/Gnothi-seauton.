# Hirst Painting Project
# This code creates a digital version of a Hirst-style dot painting using the turtle graphics library
# it extracts colors from an image and uses them to draw a grid of colored dots.
from turtle import Turtle, Screen
import random as rand
import colorgram
screen = Screen()
screen.colormode(255)
colours = []
def get_colour(a_list):
    painting_colours = colorgram.extract("hirst_painting_colours.jpg",25)
    for z in range(0,24):
        a_list.append(painting_colours[z].rgb)
    return colours

colours = get_colour(colours)

def row(a):
    for _ in range(a):
        ai.pendown()
        colour = rand.choice(colours)
        ai.dot(20,colour)
        ai.penup()
        ai.forward(50)
def get_and_set_positon():
    position = ai.position()
    ai.sety((position[1] + 50))
    ai.setx(-300)
ai = Turtle()
ai.penup()
ai.speed(0)
ai.setposition((-300,-300))
circle_and_row_number = 10

for i in range(circle_and_row_number):
    row(circle_and_row_number)
    get_and_set_positon()
ai.hideturtle()

#This code snippet should happen on the bottom of the code
screen.exitonclick()