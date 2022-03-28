from tkinter import *
from time import strftime

screen = Tk()
screen.title("Digital Clock")
screen.geometry("550x100")
screen.configure(bg="black")

def time():
    lbl.config(text = strftime("%H:%M:%S"))
    lbl.after(1000,time)

lbl = Label(screen,bg="black",fg="green",font="arial 50 italic")
lbl.pack(anchor="center", fill="both",expand = 1)

time()
mainloop()