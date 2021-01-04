from tkinter import *

window = Tk()


def button1_func():
    print(e1_value.get())
    miles = float(e1_value.get())*1.6
    ### add content at the end of text
    t1.insert(END, miles)


### create a button
### window -- which window button will be put in 
### text -- display content in button
### command -- clicked the button to execute this function
button1 = Button(window, text='Enter', command=button1_func)
### located 
# button1.pack()
button1.grid(row=0, column=0)  ## first row, and first column


### create an Entry(input)
### textvariable -- get content from entry
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
### locate
e1.grid(row=0, column=1)  ## first row, and second column


### create a text
t1 = Text(window, height=1, width=20)
### locate
t1.grid(row=0, column=2)  ## first row, and third column


### draw the window
window.mainloop()

