from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")
        self.count = 0
        self.score_label = Label(text=f"Score: {self.count}", pady=20, bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        self.canvas_question = Canvas(width=300, height=250)

        self.question = self.canvas_question.create_text(150, 130, text="rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr", font=("Arial", 20, "italic"), width=270)
        self.canvas_question.grid(column=0, row=1, columnspan=2, pady=20)

        img_right = PhotoImage(file="images/true.png")
        img_wrong = PhotoImage(file="images/false.png")

        self.btn_right = Button(image=img_right, highlightthickness=0, command=lambda: self.get_answer_checking("True"))
        self.btn_right.grid(column=0, row=2)

        self.btn_wrong = Button(image=img_wrong, highlightthickness=0, command=lambda: self.get_answer_checking("False"))
        self.btn_wrong.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas_question.config(bg="white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas_question.itemconfig(self.question, text=q_text)
        else:
            self.canvas_question.itemconfig(self.question, text="You reached the end.")
            self.btn_wrong.config(state="disabled")
            self.btn_right.config(state="disabled")

    def get_answer_checking(self, answer):
        if self.quiz.check_answer(answer):
            self.give_feedback(True)
            self.count += 1
            self.score_label.config(text=f"Score: {self.count}")
        else:
            self.give_feedback(False)

        print(f"Your current score is: {self.count}/{self.quiz.question_number}\n")

    def give_feedback(self, state):
        if state: self.canvas_question.config(bg="green")
        else: self.canvas_question.config(bg="red")

        self.window.after(600, self.get_next_question)


