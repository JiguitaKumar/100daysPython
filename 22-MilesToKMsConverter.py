from tkinter import Tk, Button, Label, Entry

# create window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# create input textbox for the miles
input = Entry(width=10)
input.grid(column=1, row=0)

# create Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# create is equal to label
equal_to = Label(text="is equal to ")
equal_to.grid(column=0, row=1)

# create is equal to label
kms_value = Label(text=0)
kms_value.grid(column=1, row=1)

# create KMs label
kms_label = Label(text="KMs")
kms_label.grid(column=2, row=1)

# create conversion button
def converter():
    miles_input = float(input.get())
    value_in_kms = miles_input * 1.609344
    kms_value.config(text=round(value_in_kms,2))
button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)


window.mainloop()
