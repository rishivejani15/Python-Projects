from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

score = 0
correct_guesses = []
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    else:
        pass

    tim = Turtle()
    tim.hideturtle()
    tim.penup()

    for each_state in range(50):
        if answer_state == all_states[each_state]:
            state_data = data[data.state == answer_state]
            tim.goto(int(state_data.x), int(state_data.y))
            tim.write(answer_state)
            correct_guesses.append(answer_state)
            score += 1
