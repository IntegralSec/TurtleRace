from turtle import Turtle, Screen
import random

# user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win?")

# =========================
# Global Variables
# =========================
turtle_colors = ("orange", "red", "grey", "purple", "blue", "green")
max_turtles = len(turtle_colors)
turtle_list = {}
Racing = True


def create_turtle(turtle_number, turtle_color, start_pos_y):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color)
    new_turtle.penup()
    go_to_y = start_pos_y + (turtle_number * 25)
    go_to_x = ((screen.window_width()/2)-40)*-1
    new_turtle.goto(x=go_to_x, y=go_to_y)
    new_turtle.pendown()
    return new_turtle


def move_turtle_rand(the_turtle):
    move_distance = random.randint(1, 15)
    if move_distance <= 3:
        move_heading = random.randint(-2, 2)
    elif move_distance > 3 <= 10:
        move_heading = random.randint(-10, 10)
    else:
        move_heading = random.randint(-40, 40)

    the_turtle.forward(move_distance)
    the_turtle.setheading(move_heading)


def is_winner(the_turtle):
    if the_turtle.xcor() >= ((screen.window_width()/2)-20):
        return True
    else:
        return False


def start_race():
    screen.clear()
    start_pos_y = ((screen.window_height()/2)-100) * -1
    racing = True
    # Create the turtles
    for i in range(0, max_turtles):
        turtle_list[turtle_colors[i]] = create_turtle(i, turtle_colors[i], start_pos_y)
    while racing:
        for j in range(0, max_turtles):
            current_turtle = turtle_list[turtle_colors[j]]
            if is_winner(current_turtle):
                racing = False
                print("The Winner is: " + str(current_turtle.pencolor()))
                print("Position: " + str(current_turtle.xcor()))
                break
            move_turtle_rand(current_turtle)
    return


if __name__ == "__main__":
    screen = Screen()
    keep_playing = True
    screen.setup(width=900, height=400)
    screen.title("Welcome to the turtle zoo!")
    while keep_playing:
        start_race()
        keep_playing = screen.textinput(title="Make a bet", prompt="Race again?")
