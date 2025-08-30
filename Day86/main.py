import tkinter as tk
import kagglehub
from tkinter import ttk
import csv
import math
import sys

# LINK
# _______________________ How to get selected string __________________________
# https://stackoverflow.com/questions/4073468/how-do-i-get-a-selected-string-in-from-a-tkinter-text-box
path = kagglehub.dataset_download("mattimansha/inspirational-quotes")

data_list = []
with open(f"{path}/insparation.csv", encoding='utf-8', newline="") as file:
    data = csv.reader(file, delimiter=",")
    for row in data:
        row.pop(3)
        row.pop(3)
        row.append(0)
        row.append("Undefind")
        data_list.append(row)
    data_list.pop(0)
    
with open(f"{path}/insparation.csv", encoding='utf-8', newline="", mode="w") as file:
    data = csv.writer(file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    data.writerows(data_list)

# _________________________ Variables ___________________________
# Keys list
keys = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
    ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
    ['CapsLock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter'],
    ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'],
    ["Ctrl",'Space', "Alt"]
]

key_widths = {
    "Backspace": 8,
    "Tab": 6,
    "CapsLock": 7,
    "Enter": 7,
    "Shift": 9,
    "Space": 30
}

# _________________________________ TK GUI ________________________________
# Create main TK window 
root = tk.Tk()
root.title("Typing Speed Test")
root.resizable(False, False)
root.geometry("800x470")

timer = None
# ________________________ Navigation Bar ________________________________
def exit():
    sys.exit()

def new_task(current_task_id=0):
    refresh_task()
    new_id = current_task_id+1
    new_text = data_list[new_id][2]
    if len(new_text) > 100:
        for i in range(100, len(new_text), 100):
            first_part = new_text[:i]
            print(first_part)
            second_part = new_text[i+1:] 
            print(second_part)
            new_text = first_part + "\n" + second_part
            print(new_text)
    task_text.config(text=new_text)
    return new_id

def refresh_task():
    if timer is not None:
        timer_label.after_cancel(timer)
    timer_label.config(text="00:00")
    entered_text.delete("1.0", tk.END)

# Frame for Task and Timer
navigation_button_bar = tk.Frame(root)
navigation_button_bar.pack(fill='x')

# Exit button
exit_button = tk.Button(navigation_button_bar, text="Exit", width=10, borderwidth=2, bg="lightblue", command=exit)
exit_button.pack(side="left", padx="5", pady='1')

# New task button
exit_button = tk.Button(navigation_button_bar, text="New Task", width=10, borderwidth=2, bg="lightblue", command=lambda id:new_task(id))
exit_button.pack(side="left", padx="5", pady='1')

# Retry button
exit_button = tk.Button(navigation_button_bar, text=u"\u293B Refresh", width=10, borderwidth=2, bg="lightblue", command=refresh_task)
exit_button.pack(side="left", padx="5", pady='1')

# Info label
info_label = tk.Label(navigation_button_bar, text="Info result: You are typing text...", borderwidth=2, fg='blue', bg='lightblue')
info_label.pack(side="left", padx="5", pady='1', fill='x', expand=True)


# ____________________________________ Task and Timer Bar _____________________________ 


# Frame for Task and Timer
task_clock_frame = tk.Frame(root)
task_clock_frame.pack(fill='x')

# Text Example
task_text = tk.Label(task_clock_frame,  borderwidth=2, font=("Arial", 10), bg="lightpink", text="Future text")
task_text.pack(side='left',pady=5, fill='both', expand=True)

# Timer
timer_label = tk.Label(task_clock_frame, font=("Arial", 14), bg='lightblue', text="00:00")
timer_label.pack(side="right", pady=5, fill='both')


# __________________________ Entered Text Field ___________________________________
# Entered text frame
entered_text_frame = tk.Frame(root)
entered_text_frame.pack()

# Text Field 
entered_text = tk.Text(entered_text_frame, height=5, width=50, relief=tk.RIDGE, borderwidth=2, font=("Arial", 14), state=tk.DISABLED)
entered_text.pack(side="left", pady=5, fill='x', padx=10)

# Scrollbar
scrollbar = ttk.Scrollbar(entered_text_frame, orient="vertical", command=entered_text.yview)
scrollbar.pack(side="right", fill='y')

entered_text.config(yscrollcommand=scrollbar.set)

# ____________________________ Keyboard ____________________________
# Keyboard frame
keyboard_frame = tk.Frame(root)
keyboard_frame.pack(padx=10, pady=10, fill=tk.Y)

# Keyboard buttons checker
capslock_on = False
shift_on = False

def delete_multiple_characters(string, start_row, start_char, end_row, end_char):
    rows = string.split("\n")

    if start_row - end_row == 0: 
        row_len = len(rows[start_row-1])
        first_row_first_part = ''.join([rows[start_row-1][j] for j in range(0, start_char)])
        first_row_second_part = ''.join([rows[start_row-1][j] for j in range(end_char, row_len)])
        rows[start_row-1] = first_row_first_part + first_row_second_part
    else:
        if end_char == 0:
            row_len = len(rows[end_row-2])
            first_row = ''.join([rows[start_row-1][j] for j in range(0, start_char)])
            rows.pop(end_row-2)
            rows[start_row-1] = first_row 

            for i in range(start_row, end_row-2):
                rows.pop(start_row)
                
            if rows[start_row-1] == "":
                rows.pop(start_row-1)
        else:  
            row_len = len(rows[end_row-1])
            first_row = ''.join([rows[start_row-1][j] for j in range(0, start_char)])
            last_row = ''.join([rows[end_row-1][j] for j in range(end_char, row_len)])
            together = first_row + last_row

            rows.pop(end_row-1)

            rows[start_row-1] = together

            for i in range(start_row, end_row-1):
                rows.pop(start_row)

            if together == '':
                rows.pop(start_row-1)
            
        
    string = '\n'.join(rows)
    return string
    
def on_btn_press(t, mode="Pressed"):
    ''' Print an entered letter from tk keyboard  to text frame'''
    global capslock_on, shift_on
    if mode == "Release":
        shift_on = False
        return

    character_check = False
    for row in keys:
        for text in row:
            if t.lower() == text.lower():
                character_check = True
        for text in special_keys:
            if t.lower() == special_keys[text].lower():
                character_check = True
    
    if not character_check:
        return

    char = t
    
    if char == "Space":
        char = " "
    elif char == "Tab":
        char = "\t"
    elif char == "Enter":
        char = "\n"
    elif char == "Backspace":
        entered_text.config(state=tk.NORMAL)
        text =  entered_text.get("1.0", tk.END)[:-1]
        current_text = entered_text.get("1.0", tk.END)[:-2]
        

        selected_text = entered_text.tag_ranges(tk.SEL)
        if selected_text:
            # print('SELECTED Text is %r' % entered_text.get(tk.SEL_FIRST, tk.SEL_LAST))
            ranges = entered_text.tag_ranges(tk.SEL)
            start_point = str(ranges[0]).split(".")
            end_point = str(ranges[1]).split(".")

            current_text = delete_multiple_characters(text, int(start_point[0]), int(start_point[1]), int(end_point[0]), int(end_point[1]))

            # print("UPDATED Text: ", current_text)
        
        entered_text.delete("1.0", tk.END)
        entered_text.insert(tk.END, current_text)
        entered_text.config(state=tk.DISABLED)
        return
    elif char == 'Ctrl' or char == 'Alt':
        char = ""
    elif char == "Shift":
        shift_on = True
        return 
    elif char == "CapsLock":
        if capslock_on:
            capslock_on = False
        else:
            capslock_on = True
        return
    elif char.isalpha():
        if capslock_on:
            if shift_on:
                char = char.lower()
            else:
                char = char.upper()
        elif capslock_on == False:
            if shift_on:
                char = char.upper() 
            else:
                char = char.lower()  


    entered_text.config(state=tk.NORMAL)
    entered_text.insert(tk.END, char)
    entered_text.config(state=tk.DISABLED)

def count_mistake(text1, text2):
    text1_splited = text1.split('\n') # remove any \n becouse of my adding 
    text1_plain = " ".join(text1_splited)
    
    text2_splited = text2.split('\n')
    text2_plain = " ".join(text2_splited)

    mistake_count = 0
    for letter1, letter2 in zip(text1_plain, text2_plain):
        if letter1 != letter2:
            mistake_count += 1
        
    return mistake_count
    
def text_comprehansion():
    entered_text = entered_text.get("1.0", tk.END)[:-1]
    task_text = task_text.get("1.0", tk.END)[:-1]

    if len(entered_text) == len(task_text):
        info_label.config(text=f"You have mistakes: {count_mistake()}", fg="red")

    if entered_text == task_text:
        info_label.config(text="All right!", fg="green")

    info_label.config(text="Info result: You are typing text...", fg="black")

# Create tk keyboard
buttons = []
buttons_rows_frame = []
for btn_row in keys:
    btn_row_frame = tk.Frame(keyboard_frame)
    for btn_name in btn_row:
        if btn_name in key_widths:
            btn = tk.Button(btn_row_frame, text=btn_name, width=key_widths[btn_name], height=2, relief=tk.RAISED, borderwidth=2, bg="white",
                            command=lambda t=btn_name: on_btn_press(t))
        else:
            btn = tk.Button(btn_row_frame, text=btn_name, width=4, height=2, relief=tk.RAISED, borderwidth=2, bg="white",
                            command=lambda t=btn_name: on_btn_press(t))
        btn.pack(side=tk.LEFT, padx=2, pady=2)  
        
        buttons.append(btn)

    btn_row_frame.pack()
    buttons_rows_frame.append(btn_row_frame)

# A mapping of key names to readable labels
special_keys = {
    "Shift_L": "Shift",
    "Shift_R": "Shift",
    "Control_L": "Ctrl",
    "Control_R": "Ctrl",
    "Alt_L": "Alt",
    "Alt_R": "Alt",
    "Caps_Lock": "CapsLock",
    "Return": "Enter",
    "BackSpace": "Backspace",
    "space": "Space",
    "Tab": "Tab",
    "comma": ",",
    "period": ".",
    "slash": "/",
    "backslash": "\\",
}

def key_press(event):
    key = special_keys.get(event.keysym, event.keysym)
    # print(f"Getted key: {key}")  # fallback to raw name

    for row_key in keys:
        if key.upper() in row_key or key in row_key:
            for btn in buttons:
                if btn.cget('text').lower() == key.lower():
                    btn.config(bg='lightblue')
    on_btn_press(key)

def key_release(event):
    key = special_keys.get(event.keysym, event.keysym)
    for row_key in keys:
        if key.upper() in row_key or key in row_key:
            for btn in buttons:
                if btn.cget('text').lower() == key.lower():
                    btn.config(bg='white')
    if key == "Shift":
        on_btn_press(key, mode="Release")


# Bind all keys you care about
for k in special_keys:
    root.bind(f"<KeyPress-{k}>", key_press)
    root.bind(f"<KeyRelease-{k}>", key_release)

# Also capture any other key
root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

# ____________________ ADD TIMER LOGIC _________________________

def start_timer(sec, format="starting"): 
    """ 
        Implement timer function. Update timer every second by one second less.
        \nThere are two type: 
        \nformat="starting" -  countdown for start (start from 0 to 3)
        \nformat="timer" - countdown for game (start from 10:00)
        
    """
    global timer
    minutes = math.floor(sec / 60)
    second = sec % 60

    if format == "starting" and sec >= 0: # Check type
        top_level_clock_process(sec) # Invoke clock func to procces top level window logic
    elif format == "timer":
        main_clock_process(sec, second, minutes)
        text_comprehansion()


def main_clock_process(sec, second,  minutes):
    """ Formatting view of timer and actual implemnt countdown process for main timer in game"""

    global timer # global timer variable for future "after" method cansellation.
    
    if second < 9: # make formatting for appropriate appearance
        second = f'0{second}'

    if minutes < 9: # make formatting for appropriate appearance
        minutes = f'0{minutes}'

    timer_label.config(text=f"{minutes}:{second}") # update timer text

    if int(second) > 0 or int(minutes) > 0: # actual countdown process
        timer = timer_label.after(100, start_timer, sec-1, "timer")


def top_level_clock_process(sec):
    """ Manage top level timer before starting game and implement countdown process """
    clock_label.config(text=f"{sec}")
    clock_label.after(1000, start_timer, sec-1) # put this statemnt for showing last update "start" during 1s after which the start_timer func won't start a new process with negative number

    if sec == 0:
        clock_label.config(text="Start")

        root.after(500, root.wm_attributes, '-topmost', True) # For hide the top level window smoothly by bringing up the main window
        root.after(500, entered_text.focus_set)

        clock_window.after(500, clock_window.destroy)
        root.after(800, start_timer, 10*60, "timer")

        current_task_id = new_task()
        return current_task_id
    


clock_window = tk.Toplevel(root, bg="lightblue")  #Create top level window
clock_window.title("Timer") 
clock_window.geometry("300x200")

clock_window.grab_set() # top level windwos lestened to all event and "disable" listening to main window
clock_window.wm_attributes('-topmost', True) # bring up the top level window

clock_label = tk.Label(clock_window, width=250, height=100, font=("Aral", 36, "bold"), bg='lightblue')
clock_label.pack(padx=50)

current_task_id = start_timer(3)



root.mainloop()