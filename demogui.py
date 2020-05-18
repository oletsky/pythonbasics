from tkinter import *
from tkinter import messagebox

from tkinter import *
from tkinter import messagebox


def alert():
    messagebox.showinfo("GUI with Python", "Hello, "+message.get())


root = Tk()
root.title("GUI with Python")
root.geometry("400x300")

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

message_button = Button(text="Click Me", command=alert)
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()