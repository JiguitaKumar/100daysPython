import tkinter
import pandas
import random
import os.path
BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_COLOR_2 = "#91c2af"

# -------------------------------- GET WORD -------------------------------- #

df = pandas.read_csv("./data/norwegian_words.csv")
list_dict = df.to_dict("records")
random_word = {}

def update_list():
    global random_word

    list_dict.remove(random_word)
    with open("./data/words_to_learn.csv", "w") as f:
        new_df = pandas.DataFrame(list_dict)
        new_df.to_csv(f, index=False)

    get_random_word()

def get_translation():
    global random_word

    canvas.itemconfig(canvas_image, image=back_card_image)
    label_language.config(text="English", background=BACKGROUND_COLOR_2, foreground="white")
    label.config(text=random_word["English"], background=BACKGROUND_COLOR_2, foreground="white")


def get_random_word():
    global flip_timer, random_word
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=front_card_image)

    if os.path.isfile("./data/words_to_learn.csv"):
        remaining_words_df = pandas.read_csv("./data/norwegian_words.csv")
        use_dict = remaining_words_df.to_dict("records")
    else:
        use_dict = list_dict

    random_word = random.choice(use_dict)
    label_language.config(text="Norwegian", background="white", foreground="black")
    label.config(text=random_word["Norwegian"], background="white", foreground="black")

    flip_timer = window.after(3000, get_translation)

# ----------------------------- CONFIGURE WINDOW ---------------------------- #


window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, get_translation)

canvas = tkinter.Canvas(width=800, height=526, border=0, background=BACKGROUND_COLOR, highlightthickness=0)
front_card_image = tkinter.PhotoImage(file="./images/card_front.png")
back_card_image = tkinter.PhotoImage(file="./images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=front_card_image)
canvas.grid(column=0, row=0, columnspan=2)

right_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_image, borderwidth=0, highlightthickness=0, command=update_list)
right_button.grid(column=0, row=1)

label_language = tkinter.Label(text="", anchor="center", background="white", foreground="black", font=("Arial", 40, "italic"), width=33)
label_language.place(x=6, y=150)

label = tkinter.Label(text="", compound="center", background="white", foreground="black", font=("Arial", 60, "bold"), width=22)
label.place(x=10, y=263)

wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, borderwidth=0, highlightthickness=0, command=get_random_word)
wrong_button.grid(column=1, row=1)

get_random_word()

window.mainloop()
