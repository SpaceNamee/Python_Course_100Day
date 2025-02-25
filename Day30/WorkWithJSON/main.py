import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# write  | json.dump()
# read   | json.load()
# Update | json.update()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web = entry_website.get()
    name = entry_name.get()
    passw = entry_password.get()

    new_data = {
        web: {
            "name":name,
            "password":passw,
        }
    }
    is_ok = messagebox.askokcancel(title="Info",
                                   message=f"Save website: {web}\n Name/email: {name}\n Password: {passw}?")

    if (web != '' and passw != ''  and  name != "") and is_ok:
        try:
            with open("key.json", "r") as memory:
                data = json.load(memory)
        except:
            with open("key.json", "w") as memory:
                json.dump(new_data, memory, indent=4)
        else:
            data.update(new_data)

            with open("key.json", "w") as memory:
                json.dump(data, memory, indent=4)

        messagebox.showinfo(title="Info", message="Saving succeed")
    else:
        messagebox.showinfo(title="ERROR", message="Your input is not valid.")

        entry_website.delete(0, END)
        entry_password.delete(0, END)
# ---------------------------- Find Password ------------------------------- #

def find_password():
    website = entry_website.get()

    try:
        with open("key.json", "r") as file:
            data = json.load(file)
        name = data[website]["name"]
        password = data[website]["password"]
    except KeyError:
        messagebox.showerror(message="No such data.")
    except FileNotFoundError:
        messagebox.showerror(message="Your history is empty.")
    else:
        messagebox.showinfo(title=website, message=f"Name: {name} \nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #
# with open("key.json", "r") as file:
#     data = json.load(file)
# print(data["Instagram"]["password"])

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=2, row=1)

label_website = Label(text="Website: ", font=("Arial", 14, "normal"))
label_website.grid(column=1, row=2, sticky="e")

label_name = Label(text="Email/Username: ", font=("Arial", 14, "normal"))
label_name.grid(column=1, row=3, sticky="e")

label_password = Label(text="Password: ", font=("Arial", 14, "normal"))
label_password.grid(column=1, row=4, sticky="e ")

entry_website = Entry(width=30)
entry_website.grid(column=2, row=2, sticky="w")
entry_website.focus()

entry_name = Entry(width=50)
entry_name.grid(column=2, row=3, columnspan=2, sticky="w")
entry_name.insert(0, "mariannabenkalovych@gmail.com")

entry_password = Entry(width=30)
entry_password.grid(column=2, row=4, sticky="w")

btn_generator_pass = Button(text="Generate Password",highlightthickness=0, font=("Arial", 8, "normal"), command=generate_pass)
btn_generator_pass.grid(column=3, row=4, sticky="w")

btn_add = Button(text="Add", width=40,highlightthickness=0, command=save_data)
btn_add.grid(column=2, row=5,columnspan=2)

btn_search = Button(text="Search", font=("Arial", 8, "normal"), width=15, command=find_password)
btn_search.grid(column=3, row=2, sticky="w")

window.mainloop()