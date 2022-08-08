# Etch a Sketch by Sulav Rai

from turtle import Turtle, Screen

arrow = Turtle()
screen = Screen()


def move_fwd():
    arrow.forward(20)


def move_bck():
    arrow.back(20)


def move_rgt():
    arrow.right(20)


def move_lft():
    arrow.left(20)


def clear():
    arrow.penup()
    arrow.clear()
    arrow.home()
    arrow.pendown()


screen.listen()
screen.onkey(move_fwd, "w")  # control the Sketch using "wasd"
screen.onkey(move_lft, "a")
screen.onkey(move_bck, "s")
screen.onkey(move_rgt, "d")
screen.onkey(clear, "c")  # To reset, press "c"
screen.exitonclick()

