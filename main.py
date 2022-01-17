import turtle
import pandas
from write_on_map import WriteOnMap

screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
data = pandas.read_csv("50_states.csv")
state_name = data.state.to_list()
correct_guess = []
write_on_map = WriteOnMap()


while len(correct_guess) < 50:
    user_answer = screen.textinput(title=f"{len(correct_guess)}/50 States correct", prompt="What's another state's name?").title()
    if user_answer == "Exit":
        missing_states = [state for state in state_name if state not in correct_guess]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missing states.csv")
        break
    if user_answer in state_name:
        correct_guess.append(user_answer)
        extract_state = data[data.state == user_answer]
        write_on_map.write_new_state(int(extract_state.x), int(extract_state.y), user_answer)



