import tkinter
from tkinter import *
from quiz_brain import QuizBrain
import html

THEME_COLOR = "#375362"


class UInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain_ui = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.ui_canvas = tkinter.Canvas(height=250, width=300, background="white", borderwidth=0, highlightthickness=0)
        self.question_canvas = self.ui_canvas.create_text(150, 125, text="Text Goes Here", font=("Arial", 20, "italic"), fill="black", width=280)
        self.ui_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_button_img = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=self.true_button_img, borderwidth=0, command=lambda: self.update_scope("True"))
        self.true_button.grid(column=0, row=2)

        self.false_button_img = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=self.false_button_img, borderwidth=0, command=lambda: self.update_scope("False"))
        self.false_button.grid(column=1, row=2)

        self.score_label = tkinter.Label(text="Score: 0", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        new_question = html.unescape(self.quiz_brain_ui.next_question()['question'])
        self.ui_canvas.itemconfig(self.question_canvas, text=new_question)

    def update_scope(self, answer: str):
        check_answer = self.quiz_brain_ui.check_answer(answer)
        self.score_label.config(text="Score: " + str(self.quiz_brain_ui.score))

        self.give_feedback(check_answer)

        if self.quiz_brain_ui.still_has_questions():
            self.get_next_question()
        else:
            final_message = f"Your Final score is: {self.quiz_brain_ui.score}"
            self.ui_canvas.itemconfig(self.question_canvas, text=final_message)
            self.ui_canvas.update()
            self.window.after(2000)
            self.window.quit()

    def give_feedback(self, check_answer: bool):
        if check_answer:
            self.ui_canvas.config(background="green")
        else:
            self.ui_canvas.config(background="red")
        self.ui_canvas.update()
        self.window.after(1000)
        self.ui_canvas.config(background="white")
