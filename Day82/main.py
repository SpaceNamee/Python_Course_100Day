from classes import MorseConverter
import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Text to Morse Converter")

# Variables
original_text = tk.StringVar()
morse_text = tk.StringVar()

# Main frame
frame = tk.Frame(root, 
                bg="lightblue")
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Text input field
text_input = tk.Entry(frame,
                      width=30,
                      font=("Arial", 14),
                      justify=tk.CENTER,
                      textvariable=original_text
                      )
text_input.insert(0, "Text")
text_input.pack(pady=(50, 10), )

def press_buton():
    return morse_text.set(MorseConverter().text_to_morse(original_text.get()))

# Convert button
button_converter = tk.Button(frame,
                            text="Convert to Morse",
                            command=press_buton,
)
button_converter.pack(pady=10)

label_text = tk.Label(frame,
                        font=("Arial", 10),
                        fg="black",
                        text="Original Text: ",
                        bg="lightblue",
                        anchor=tk.W
                        )
label_text.pack(pady=5, padx=10, fill=tk.X)    

label_original_text = tk.Label(label_text,
                        textvariable=original_text,
                        font=("Arial", 10),
                        fg="black",
                        bg="lightblue",
                        )
label_original_text.pack(pady=5, padx=(100, 10), side=tk.LEFT)

label_morse = tk.Label(frame,
                        font=("Arial", 10),
                        fg="black",
                        text="Morse Code: ",
                        bg="lightblue",
                        anchor=tk.W
                        )
label_morse.pack(pady=5, padx=10, fill=tk.X)    

label_morse_code = tk.Label(label_morse,
                        textvariable=morse_text,
                        font=("Arial", 10),
                        fg="black",
                        bg="lightblue",
                        )
label_morse_code.pack(pady=5, padx=(100, 10), side=tk.LEFT)


root.mainloop()


