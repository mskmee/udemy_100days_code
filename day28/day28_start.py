from tkinter import *
import math

# Constants

PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BRAKE_MIN = 5
LONG_BRAKE_MIN = 20
reps = 0
timer_on = None


# Timer Reset
def reset():
    window.after_cancel(timer_on)
    global reps
    reps = 0
    title_label.config(text='Timer')
    canvas.itemconfig(timer, text='00:00', fill='#ffffff')
    ok_label.config(text='')


# Time mechanism
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BRAKE_MIN * 60
    long_break_sec = LONG_BRAKE_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        canvas.itemconfig(timer, fill=RED)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        canvas.itemconfig(timer, fill=PINK)
        title_label.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        canvas.itemconfig(timer, fill=GREEN)
        title_label.config(text='Work', fg=GREEN)


# Countdown mechanism
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer_on
        timer_on = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(reps/2)):
            mark += '🗸'
        ok_label.config(text=mark)


# UI Setup
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 25, 'bold'), bg=YELLOW)
title_label.grid(row=0, column=1)
ok_label = Label(text='', fg=GREEN, bg=YELLOW)

# Canvas
canvas = Canvas(width=215, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='Hnet.com-image.png')
canvas.create_image(107, 112, image=tomato_img)
timer = canvas.create_text(107, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1)

# Buttons
reset_b = Button(text='reset', font=(FONT_NAME, 10, 'bold'), command=reset, highlightthickness=0)
reset_b.grid(column=2, row=2)

start_b = Button(text='start', font=(FONT_NAME, 10, 'bold'), command=start_timer, highlightthickness=0)
start_b.grid(column=0, row=2)
ok_label.grid(column=1, row=3)

window.mainloop()
