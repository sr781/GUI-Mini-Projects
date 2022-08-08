# Created by Sulav
# This is a simple program that generates a multi-colored Spirograph

from turtle import Turtle, Screen
import turtle
import random
jim = Turtle()
jim.shape("circle")
turtle.colormode(255)
jim.pensize(2)
jim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
def randomwalk(a):
    jim.color(random_color())
    jim.circle(100)
    jim.setheading(a)


for a in range(360):
    a = a*10
    randomwalk(a)


screen = Screen()
screen.exitonclick()
