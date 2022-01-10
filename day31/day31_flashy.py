from tkinter import *
import random
import pandas
from tkinter import messagebox


dont_know = []
# ---------------Data to Dict----------
try:
    data = pandas.read_csv('data/to_learn.csv.csv', encoding='utf-8')
except FileNotFoundError:
    data = pandas.read_csv('data/words_en_ru.csv', encoding="utf-8")
# words_dict = {row['English']: row['Russian'] for (index, row) in data.iterrows()}
to_learn = data.to_dict(orient='records')


# ---------------Change card-----------
def flip_card():
    canvas.itemconfig(card_word, text=current_card['Russian'], fill='white')
    canvas.itemconfig(card, image=card_back_img)


# ---------------Buttons Config--------
def unknown_btn_click():
    global dont_know
    dont_know.append(current_card)
    next_card()


def oke_btn_click():
    next_card()
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/to_learn.csv', index=False)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_word, text=current_card['English'], fill='black')
    canvas.itemconfig(card, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        try:
            data = pandas.read_csv('data/words_to_learn.csv', encoding='utf-8')
        except FileNotFoundError:
            data = pandas.DataFrame(dont_know)
            data.to_csv('data/words_to_learn.csv', index=False)
        else:
            data = data.append(pandas.DataFrame(dont_know))
            data.to_csv('data/words_to_learn.csv', index=False, encoding='utf-8')
        window.destroy()
# ---------------UI Setup--------------
window = Tk()
window.config(padx=50, pady=50, background='#aae0c0')
window.minsize(width=600, height=470)
window.title('flashy')

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=500, height=370, background='#aae0c0', highlightthickness=0)
card_front_img = PhotoImage(file='img/word1.PNG')
card_back_img = PhotoImage(file='img/translate1.PNG')

card = canvas.create_image(250, 185, image=card_front_img)
card_word = canvas.create_text(250, 185, text='word', font=('Ariel', 50, 'bold'))
canvas.place(x=0, y=0)

# Button
cross_img = PhotoImage(file='img/wrong.png')
unknown_btn = Button(image=cross_img, background="#aae0c0", highlightthickness=0, command=unknown_btn_click)
unknown_btn.place(x=55, y=230)
oke_img = PhotoImage(file='img/ok.png')
oke_btn = Button(image=oke_img, background="#aae0c0", highlightthickness=0, command=oke_btn_click)
oke_btn.place(x=340, y=230)

next_card()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
