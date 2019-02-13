from tkinter import *
import backend

def clear_all():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def insert_command():
    list1.delete(0,END)
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        clear_all()
        list1.insert(END,row)

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()
    clear_all()

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    search_command()

window = Tk()
window.title("SIMPLE CRUD")

l1 =Label(window,text="BOOKNAME")
l1.grid(row=0,column=0)

l2 = Label(window,text="AUTHOR")
l2.grid(row=0,column=2)

l3 = Label(window,text="YEAR")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text = StringVar()
e1 = Entry(window,textvariable = title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window,textvariable = author_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window,textvariable = year_text)
e3.grid(row=1,column=1)

isbn_text = StringVar()
e4 = Entry(window,textvariable = isbn_text)
e4.grid(row=1,column=3)

b1 = Button(window,text="Search",height=2,width =20,command=search_command)
b1.grid(row=2,column=3)

b2 = Button(window,text="Viewall",height=2,width =20,command=view_command)
b2.grid(row=3,column=3)

b3 = Button(window,text="Insert",height=2,width =20,command=insert_command)
b3.grid(row=4,column=3)

b4 = Button(window,text="Delete",height=2,width =20,command=delete_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Update",height=2,width =20,command=update_command)
b5.grid(row=6,column=3)

b6 = Button(window,text="Clear",height=2,width =20,command=clear_all)
b6.grid(row=7,column=3)

b7 = Button(window,text="Close",height=2,width =20,command=window.destroy)
b7.grid(row=8,column=3)

list1 = Listbox(window,height=14,width=50)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

sb2 = Scrollbar(window,orient=HORIZONTAL)
sb2.grid(row=8,column=0,columnspan=2)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.configure(xscrollcommand = sb2.set)
sb2.configure(command = list1.xview)

list1.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()
