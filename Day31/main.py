from tkinter import *
from tkinter import messagebox
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"

# ------------------------ Read Data ---------------------------- #
vocabulary = read_csv("data/french_words.csv")
column_names = vocabulary.columns.to_list()
from_lang = column_names[0]
to_lang = column_names[1]
pair_of_word = []
# ------------------------ Generate words ---------------------------- #
def generate_words():

    vocabulary_list = vocabulary.to_dict(orient='records')
    word = random.choice(vocabulary_list)

    try:
        file = open('known_words_by_user', mode="r")
        data = file.read()
    except FileNotFoundError:
        # background_canvas.itemconfig(foreign_word, text=word[from_lang])
        word = word
    else:
        while True:
            if data.find(word[to_lang]) == -1:
                break
            else:
                word = random.choice(vocabulary_list)
    flip_to_back(word)
    # global pair_of_word
    # pair_of_word = word

# ------------------------ Saving knowing words ---------------------------- #
def save_word():
    txt = background_canvas.itemcget(foreign_word, 'text')
    with open("known_words_by_user", mode="a", encoding="utf-8") as file:

        file.write(f"{str(txt)} ")

    generate_words()
# ------------------------ Flip cards ---------------------------- #
def flip_to_front(word):
    btn_wrong.config(state=ACTIVE)
    btn_right.config(state=ACTIVE)
    background_canvas.itemconfig(hand_of_cards, image=img_front)
    background_canvas.itemconfig(language, text=to_lang)
    background_canvas.itemconfig(foreign_word, text=word[to_lang])


def flip_to_back(word):
    background_canvas.itemconfig(hand_of_cards, image=img_background)
    background_canvas.itemconfig(language, text=from_lang)
    background_canvas.itemconfig(foreign_word, text=word[from_lang])

    btn_wrong.config(state=DISABLED)
    btn_right.config(state=DISABLED)
    window.after(1500, flip_to_front, word)
# ------------------------ UI ---------------------------- #
window = Tk()
window.title("Flash Cards")

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

img_background = PhotoImage(file="images/card_back.png")
img_front = PhotoImage(file="images/card_front.png")
background_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
hand_of_cards = background_canvas.create_image(400, 260)
language = background_canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
foreign_word = background_canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
background_canvas.grid(column=0, row=0, columnspan=2)

# Buttons
img_right = PhotoImage(file="images/right.png")
btn_right = Button(image=img_right, highlightthickness=0, command=save_word)
btn_right.grid(column=0, row=1)

img_wrong = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=img_wrong, highlightthickness=0, command=generate_words)
btn_wrong.grid(column=1, row=1)



generate_words()

window.mainloop()