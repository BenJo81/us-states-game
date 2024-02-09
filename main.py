import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_count = 0
states_guessed = []

states = pandas.read_csv("50_states.csv")
states_dict = states.to_dict()

turtle = turtle.Turtle()

while state_count < 50:
    answer_state = screen.textinput(title=f"Guess the State {state_count}/50",
                                    prompt="What's another state's name?").lower()
    if answer_state == "exit":
        break
    for state in states.state:
        if state.lower() == answer_state:
            state_count += 1
            states_guessed.append(state)
            new_turtle = turtle
            new_turtle.hideturtle()
            new_turtle.penup()
            x_cor = states[states.state == state]
            y_cor = states[states.state == state]
            new_turtle.goto(int(x_cor.x), int(y_cor.y))
            new_turtle.write(state, align="left")

# states_to_learn.csv
learn_list = []

for state in states.state:
    if state.title() not in states_guessed:
        learn_list.append(state.title())

data_dict = {
    "States to Learn": learn_list
}
data = pandas.DataFrame(data_dict)
data.to_csv("states_to_learn.csv")