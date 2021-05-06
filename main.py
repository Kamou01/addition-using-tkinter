from tkinter import *
window = Tk()
lb1 = Label(window, text="Enter first number")
lb1.place(x=50, y=50)
entry1 = Entry(window)
entry1.place(x=200, y=50)
lb2 = Label(window, text="Enter second number")
lb2.place(x=50, y=100)
entry2 = Entry(window)
entry2.place(x=200, y=100)
lb3 = Label(window, text="Your answer")
lb3.place(x=50, y=150)
entry3 = Entry(window, state="readonly")
entry3.place(x=200, y=150)


def add_2_numbers():
     total = sum(int(i.get()) for i in (entry1, entry2))
     entry3.config(state="normal")
     entry3.insert(0, total)
     entry3.config(state="readonly")


def delete():
    entry1.delete(0, 'End')
    entry2.delete(0, 'End')
    entry3.config(state="normal")
    entry3.delete(0, END)
    entry3.config(state="readonly")


add = Button(window, text="Add", width=15, command=add_2_numbers).place(x=100, y=200)
clear = Button(window, text="Clear", width=15, command=delete).place(x=200, y=200)
quit = Button(window, text="Exit", width=15, command="exit").place(x=300, y=200)
window.geometry("400x300")
window.mainloop()
