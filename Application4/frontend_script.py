from tkinter import *

import backend_script


""" connect to database server """
db = backend_script.Book_Database("root", 'password', 'db_server_addr', 'dbtest')


""" 
    mouse click event

    if the box is empty, nothing will happen when clicked

    clicked specified item, the information will formatting into entries

    @bid -- global variable, it is a key to delete and update, because these operations will use bid in database
"""
def get_selected_row(event):

    if list_box.size() == 0:
        return
    
    index = list_box.curselection()[0]
    selected_item = list_box.get(index)
    infos = substring_item(selected_item)

    global bid

    bid = infos[0]
    title = infos[1]
    author = infos[2]
    year = infos[3]
    isbn = infos[4]

    en_title.delete(0, END)
    en_title.insert(END, title)
    en_author.delete(0, END)
    en_author.insert(END, author)
    en_year.delete(0, END)
    en_year.insert(END, year)
    en_isbn.delete(0, END)
    en_isbn.insert(END, isbn)
    

""" format the string which got from the listbox """
def substring_item(item):
    
    index_bid = item.index(" ")
    bbid = item[:index_bid]

    book_start = item.index("<<")
    book_end = item.index(">>")
    book = item[book_start+2:book_end]
    
    staff = item.split(" ")
    isbn = staff[-1]
    year = staff[-2]

    author_end = item.index(year)
    author = item[book_end+3:author_end-1]

    items = [bbid, book, author, year, isbn]

    return items


""" display all items from database into the listbox """
def view_command():
    list_box.delete(0, END)

    for row in db.view_items():
        list_box.insert(END, row)


""" search by contents of entries """
def search_command():
    list_box.delete(0, END)
    for row in db.search_by(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list_box.insert(END, row)


""" insert a item into database and display into the listbox """
def add_command():
    db.insert_item(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_box.delete(0, END)
    view_command()


""" 
    update in database

    click the specified item, and modify values with the content of entries 

    bid will certained which item will be modified in database
"""
def update_command():
    db.update(bid, title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()


""" delete item by bid """
def delete_command():
    db.delete_by_id(bid)
    view_command()


"""
    create a window
    `wm_title(#title)` -- setup a window name
"""
window = Tk()
window.wm_title("Book Store")


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

butt_update = Button(window, text="Update", width=12, command=update_command)
butt_update.grid(row=5, column=3)

butt_delete = Button(window, text="Delete", width=12, command=delete_command)
butt_delete.grid(row=6, column=3)

butt_close = Button(window, text="Close", width=12, command=window.destroy)
butt_close.grid(row=7, column=3)


"""
    Selector

"""
list_box.bind('<<ListboxSelect>>', get_selected_row)


window.mainloop()