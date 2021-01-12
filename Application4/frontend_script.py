from tkinter import *

import backend_script


db = backend_script.Book_Database("database information")


def view_command():
    list_box.delete(0, END)

    for row in db.view_items():
        list_box.insert(END, row)


def search_command():
    list_box.delete(0, END)
    print(title_text.get()=="", author_text.get()=="", year_text.get()=="", isbn_text.get()=="")
    for row in db.search_by(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list_box.insert(END, row)


def add_command():
    db.insert_item(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_box.delete(0, END)
    view_command()


def update_command():
    db.update()


def delete_command():
    db.delete_by_title(title_text.get())
    view_command()


window = Tk()

""" Labels

    Title
    Author
    Year
    ISBN

"""
label_title = Label(window, text="Title")
label_title.grid(row=0, column=0)

label_author = Label(window, text="Author")
label_author.grid(row=0, column=2)

label_year = Label(window, text="Year")
label_year.grid(row=1, column=0)

label_isbn = Label(window, text="ISBN")
label_isbn.grid(row=1, column=2)


''' Entry

    each label has an entry relately

'''
title_text = StringVar()
en_title = Entry(window, textvariable=title_text)
en_title.grid(row=0, column=1)

author_text = StringVar()
en_author = Entry(window, textvariable=author_text)
en_author.grid(row=0, column=3)

year_text = StringVar()
en_year = Entry(window, textvariable=year_text)
en_year.grid(row=1, column=1)

isbn_text = StringVar()
en_isbn = Entry(window, textvariable=isbn_text)
en_isbn.grid(row=1, column=3)




''' List box

    list_box -- display data which had been operated by button funciton
    scrollbar -- scroll to check more data

    configura -- combine box and scrollbar

    rowspan = #size, columnspan = #size ---  customize the size of box

'''
list_box = Listbox(window, height=10, width=35)
list_box.grid(row=2, column=0, rowspan=10,columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=10)

list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)



''' Buttons 

    view
    search
    add
    update
    delete
    close

'''
butt_view = Button(window, text="View all", width=12, command=view_command)
butt_view.grid(row=2, column=3)

butt_search = Button(window, text="Search", width=12, command=search_command)
butt_search.grid(row=3, column=3)

butt_add = Button(window, text="Add", width=12, command=add_command)
butt_add.grid(row=4, column=3)

butt_update = Button(window, text="Update", width=12)
butt_update.grid(row=5, column=3)

butt_delete = Button(window, text="Delete", width=12, command=delete_command)
butt_delete.grid(row=6, column=3)

butt_close = Button(window, text="Close", width=12)
butt_close.grid(row=7, column=3)




window.mainloop()