import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_value = -90  # --> dipakai untuk koordinat setiap turtle buat ditaro di sisi kiri layar
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.shapesize(1)
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_value)
    y_value = y_value + 40
    all_turtles.append(new_turtle)

user_guess = screen.textinput(title='Make your guess!', prompt='Which turtle will win the race? enter a color: ')\
    .lower()

if user_guess:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_guess == winning_color:
                print(f"You've won!, {user_guess.title()} turtle is the winner")
            else:
                print(f"You've Lost!, {user_guess.title()} turtle is losing like a loser")

        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


screen.exitonclick()
