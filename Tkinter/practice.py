from tkinter import *

window = Tk()

### convert weight
### KG convert to grams, pounds and ounces
def convert_func():
    grams = float(entry_input_val.get()) * 1000
    pounds = float(entry_input_val.get()) * 2.20462
    ounces = float(entry_input_val.get()) * 35.274

    # empty the text boxes
    text_gram.delete("0.0", END)
    text_gram.insert(END, grams)

    text_pound.delete("0.0", END)
    text_pound.insert(END, pounds)

    text_ounce.delete("0.0", END)
    text_ounce.insert(END, ounces)


label = Label(window, text="KG: ", height=1, width=20)
label.grid(row=0, column=0)


entry_input_val = StringVar()
entry_input = Entry(window, textvariable=entry_input_val)
entry_input.grid(row=0, column=1)


button_convert = Button(window, text="Convert", command=convert_func)
button_convert.grid(row=0, column=2)


label_gram= Label(window, text="Grams: ", height=1, width=20)
label_gram.grid(row=1, column=0)
text_gram = Text(window, height=1, width=20)
text_gram.grid(row=1, column=1)

label_pound = Label(window, text="Pounds: ", height=1, width=20)
label_pound.grid(row=2, column=0)
text_pound = Text(window, height=1, width=20)
text_pound.grid(row=2, column=1)

label_ounce = Label(window, text="Ounces: ", height=1, width=20)
label_ounce.grid(row=3, column=0)
text_ounce = Text(window, height=1, width=20)
text_ounce.grid(row=3, column=1)


window.mainloop()