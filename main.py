from tkinter import *
import threading

FONT_TITLE = ("Ariel", 32, "bold")
FONT_BODY = ("Roboto", 14, "normal")
TEXT_COLOR = "#212121"
# DISAPPEAR_COLOR = ["#3a3a3a", "#606060", "#919191", "#c9c7c7", "#f9f9f9"]

first_five = threading
not_first = False


def start_timer(event):
    global first_five, not_first
    if not_first:
        first_five.cancel()
    not_first = True
    first_five = threading.Timer(5, disappear_text)
    first_five.start()


def disappear_text():
    text.delete("1.0", END)


window = Tk()
window.title("Disappearing Text App")
window.config(padx=50, pady=50)

title = Label(text="Welcome to The Disappearing Text App!", font=FONT_TITLE, pady=20)
title.pack()
text = Text(window, height=30, width=60, font=FONT_BODY, foreground=TEXT_COLOR)
text.focus()
text.pack()

type_time = text.bind("<Key>", start_timer)


window.mainloop()
