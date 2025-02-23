import tkinter
from  tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    name.config(text="Timer")
    check_mark.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(start=True):

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        name.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        name.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        name.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 9:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(100, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #4
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00",fill="white", font=(FONT_NAME, 35, "bold") )

canvas.grid(column=2, row=2)

name = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
name.grid(column=2, row=1)

start_btn = Button(text="Start", bg="white", font=(FONT_NAME, 10, "normal"), command=start_timer)
start_btn.grid(column=1, row=3)


reset_btn = Button(text="Reset", bg="white", font=(FONT_NAME, 10, "normal"), command=reset_timer)
reset_btn.grid(column=3, row=3)

check_mark = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, "normal"))
check_mark.grid(column=2, row=4 )

window.mainloop()