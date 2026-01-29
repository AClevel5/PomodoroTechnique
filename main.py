from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

def start_time():
    time_reducer(25)

def time_reducer(count):
    if count > 0:
        canvas.itemconfig(timer_text, text=count)
        window.after(1000, time_reducer, count-1)




canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(row=1, column=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


title_label =Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

start_button = Button(text="Start", bg=YELLOW, fg=GREEN, highlightthickness=0, command=start_time)
start_button.grid(row=2, column=0)

restart_button = Button(text="Restart", bg=YELLOW, fg=GREEN, highlightthickness=0)
restart_button.grid(row=2, column=2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(row=3, column=1)



restart_button = Button(text="Restart")


window.mainloop()