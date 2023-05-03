import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


def write_name(name, x, y):
    name_on_screen = turtle.Turtle()
    name_on_screen.hideturtle()
    name_on_screen.penup()
    name_on_screen.goto(x, y)
    name_on_screen.write(name)


data = pandas.read_csv("50_states.csv")
states = data["state"]
score = 0
x = 0
y = 0
correct_guesses = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt="What's another state's name?").title()
    is_guess_correct = False
    if answer_state == "Exit":
        break
    for state in states:
        if state == answer_state and state not in correct_guesses:
            is_guess_correct = True
            score += 1
            state_row = data[data["state"] == state]
            correct_guesses.append(state)
            write_name(answer_state, int(state_row.x), int(state_row.y))

    print(correct_guesses)

    if len(correct_guesses) == 50:
        game_is_on = False

leftover_states = []
for state in states:
    if state not in correct_guesses:
        leftover_states.append(state)

states_df = pandas.DataFrame(leftover_states)
states_df.to_csv("Leftover States")

turtle.mainloop()
