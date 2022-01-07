from tkinter import *

KM = 0
# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=300, height=200)

# Labels
equal = Label(text="is equal to")
equal.place(x=20, y=70)
score = Label(text=KM)
score.place(x=100, y=70)
kilometrs = Label(text='Km')
kilometrs.place(x=190, y=50)
miles = Label(text='Miles')
miles.place(x=190, y=70)
# Buttons
def convert():
    km_inp = inp.get()
    km_score = float(km_inp) * 1.60934
    score.config(text=round(km_score, 6))

convert_b = Button(text='calculate', command=convert)
convert_b.place(x=100, y=100)


# entry
inp = Entry(width=10)
inp.place(x=100, y=50)

window.mainloop()
