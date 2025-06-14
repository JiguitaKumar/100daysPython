from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✓"
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
    top_label.config(text="Timer", fg=GREEN)
    reps = 0
    checkmark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    print(reps)
    if reps == 7:
        top_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        top_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    else:
        top_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        number = count_sec
        count_sec = f"0{number}"
    if count_min < 10:
        number = count_min
        count_min = f"0{number}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            num_checks = math.floor(reps/2)
            checkmark_label.config(text=CHECKMARK*num_checks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)
window.config(background=YELLOW)

top_label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), background=YELLOW, foreground=GREEN)
top_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", pady=0, padx=0, bd=0, highlightthickness=0)
start_button.config(width=1, height=1, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", pady=0, padx=0, bd=0, highlightthickness=0)
reset_button.config(width=1, height=1, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(background=YELLOW, foreground=GREEN, font=(FONT_NAME, 30, "normal"))
checkmark_label.grid(column=1, row=3)

window.mainloop()
