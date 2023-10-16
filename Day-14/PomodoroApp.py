# pomodoro GUI application using tkinter
from tkinter import *
import time
import math

PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 20
reps = 0
checks = ""
timer = None


def reset_Timer():
    global reps
    global checks
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    label1.config(text="Timer")
    check_marks.config(text="")
    reps = 0
    checks = ""


def start_Timer():
    global reps
    global checks
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK * 60
    long_break_secs = LONG_BREAK * 60
    if reps % 8 == 0:
        # time.sleep(3)
        label1.config(text="Long Break!!!", fg=RED, font=(FONT_NAME, 25, "bold"))
        count_down(long_break_secs)
        reps = 0
        checks = ""
        check_marks.config(text=checks)
    elif reps % 2 == 0:
        # time.sleep(3)
        label1.config(text="Break!!!", fg=PINK, font=(FONT_NAME, 25, "bold"))
        count_down(short_break_secs)
    else:
        label1.config(text="Work!!!", fg=GREEN, font=(FONT_NAME, 25, "bold"))
        count_down(work_secs)


def count_down(count):
    global timer
    mins = math.floor(count/60)
    seconds = math.floor(count % 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    if mins < 10:
        mins = f"0{mins}"
    canvas.itemconfig(timer_text, text=f"{mins}:{seconds}")
    # print(count)
    if count >= 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_Timer()
        global checks
        if reps % 2 == 0:
            checks += "✅"
        check_marks.config(text=checks)


# UI SETUP
window = Tk()
window.title("Pomodoro Application")
window.config(padx=100, pady=50, bg=YELLOW)


# canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="100DayOfCodePython\Day-14\static\pic.jpeg")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Labels
label1 = Label(text="Timer", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
label1.grid(row=0, column=1)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

# buttons
start_button = Button(text="Start", command=start_Timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_Timer)
reset_button.grid(row=2, column=3)

window.mainloop()
