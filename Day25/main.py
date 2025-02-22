import pandas
import turtle

# --------------------- Use CSV ---------------------------
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# --------------------- Use Pandas ---------------------------
# data = pandas.read_csv("weather_data.csv")
# print(data)
# ----------- Get a colon -----------
# print(data["temp"])

# data_list = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# ----------- Get a row with define value -----------
# grey_squirrels_count = len(data_list[data_list["Primary Fur Color"] == "Gray"])
# black_squirrels_count = len(data_list[data_list["Primary Fur Color"] == "Black"])
# cinnamon_squirrels_count = len(data_list[data_list["Primary Fur Color"] == "Cinnamon"])
# print(cinnamon_squirrels_count)

# all_color = data_list["Primary Fur Color"]
#
# color_counter = {}
# for color in all_color:
#     if color not in color_counter:
#         color_counter[color] = 1
#     else:
#         color_counter[color] += 1
#
# print(color_counter)

# --------------------- Use Pandas + Turtle ---------------------------
screen = turtle.Screen()
screen.title("U.S. State Game")

# Set background
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

# Read file
data = pandas.read_csv("50_states.csv")

states = data.state
a = "Alaska"
for l in states:
    if a == l:
        print("True")
max_amount = len(states)
guess_amount = 0
while True:
    if guess_amount == max_amount: break
    answer_state = screen.textinput(title="Guess the State", prompt=f"What's another state {guess_amount}/{max_amount}")
    answer_state.title()
    point = turtle.Turtle()
    point.penup()
    point.hideturtle()

    for state in states:
        if answer_state == state:
            print("i'm here")
            guess_amount += 1
            new_x = data[data.state == answer_state].x.item()
            new_y = data[data.state == answer_state].y.item()
            point.setpos(new_x,new_y)
            print(new_x)
            point.write(f"{answer_state}")

turtle.mainloop()
