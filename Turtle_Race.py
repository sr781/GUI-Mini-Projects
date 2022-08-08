# Turtle Race by Sulav Rai

from turtle import Turtle, Screen
import random
race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Race by Sulav Rai", prompt="Which turtle will win the race? Enter a colour: ") # Asks the user to enter which colored turtle they think will in
colours = ("red", "orange", "yellow", "green", "blue", "purple") # Colours are stored in a tuple
all_turt = []
y_pos = -140
screen.bgcolor("grey")


def turtle_race(colour, y_pos): # This function creates an instance from the Turtle() class
    turt = Turtle(shape="turtle")
    turt.color(colour)
    turt.penup()
    turt.goto(x=-200, y=y_pos)
    all_turt.append(turt)


for a in colours:  # This for loop creates a turtle instance for each colour using the turtle_race function
    y_pos = y_pos + 40
    turtle_race(a, y_pos)

if user_bet:
    race = True

while race:  # While race is active, code within will run
    for turtle in all_turt:
        if turtle.xcor() > 230:  # If turtle reaches the end of the screen, the race will end and the winner announced
            race = False
            winner = turtle.pencolor()
            if winner == user_bet:

                print(f"You have won! The {winner} turtle won")
            else:
                print(f"You have lost! The {winner} turtle won")
        random_distance = random.randint(0, 10)  # Turtle moves at a random pace between 0 - 10
        turtle.forward(random_distance)

screen.exitonclick()
