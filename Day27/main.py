from tkinter import *

window = Tk()
window.title("My window")
window.minsize(width=500, height=500)
window.config(padx=200, pady=200)

# _____________ Label ____________
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))

my_label["text"] = "Other text"
my_label.config(text="Other text 2")
my_label.grid(column=0, row=0)

#____________ Entry component ____________
input = Entry(width=15)
input.grid(column=1, row=1)


# _____________ Button  ____________
def button_clicked():
    my_label["text"] = input.get()

button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)



# #____________ Text ____________
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END,"Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# # ____________ Spinbox ____________
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# # ____________ Scale ____________
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
#

window.mainloop()


# from tkinter import ttk
# Setting up the Main Application Window
# root = Tk()
# root.title("Feet to Meters")
#
# # Creating a Content Frame
# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky="n, w, e, s")
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
#
# # Creating the Entry Widget
# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=20, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky="w, e")
#
# # Creating the Remaining Widgets
# def calculate():
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass
#
# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky="w, e")
#
# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky="w")
#
# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky="w")
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky="e")
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky="w")
#
# # Adding Some Polish
# for child in mainframe.winfo_children():
#     child.grid_configure(padx=5, pady=5)
# feet_entry.focus()
# root.bind(<Return>, calculate)
#
#
# root.mainloop()
