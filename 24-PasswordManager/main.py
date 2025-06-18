import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def create_password():
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_txtbox.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_txtbox.get()
    email = email_txtbox.get()
    password = password_txtbox.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)  # reading old data
        except FileNotFoundError:
            data = new_data
        else:
            data.update(new_data)  # updating data
        finally:
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)  # writing new data

    website_txtbox.delete(0, tkinter.END)
    password_txtbox.delete(0, tkinter.END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_website():
    website = website_txtbox.get()

    if website == "":
        messagebox.showinfo(title="Oops", message="Please enter the website name!")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("There are no passwords saved, currently.")
        else:
            if website in data.keys():
                messagebox.showinfo(title=f"{website}",
                                    message=f"Email: {data[website]["email"]}\n Password: {data[website]["password"]}")
            else:
                messagebox.showinfo(title="Error", message=f"The password for {website} is not saved here.")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
locket_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(140, 100, image=locket_image)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website: ")
website_label.grid(column=0, row=1)
website_txtbox = tkinter.Entry(width=21)
website_txtbox.focus()
website_txtbox.grid(column=1, row=1, sticky="we")
search_button = tkinter.Button(text="Search", command=search_website)
search_button.grid(column=2, row=1, columnspan=2, sticky="we")

email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
email_txtbox = tkinter.Entry(width=35)
email_txtbox.insert(0, "example@gmail.com")
email_txtbox.grid(column=1, row=2, columnspan=2, sticky="we")

password_label = tkinter.Label(text="Password: ")
password_label.grid(column=0, row=3)
password_txtbox = tkinter.Entry(width=21)
password_txtbox.grid(column=1, row=3, sticky="we")
password_button = tkinter.Button(text="Generate Password", command=create_password)
password_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="we")

window.mainloop()
