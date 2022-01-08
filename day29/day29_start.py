from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def check_user_name():
    """check user login in data. If more than 1st launch auto entry user login in program"""
    with open('data.txt', 'r') as f:
        try:
            name = f.readlines()[0]
            return name.split(' ')[1].strip('\n')
        except IndexError:
            return ''


check_user_name()
FONT = ('Courier', 12, 'bold')
user_name = check_user_name()


# Password gen
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for el in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for el in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for el in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# Password save
def to_file():
    """Save entry from user. Check for file and create it if it not exists"""
    global user_name

    web = website_entry.get()
    us = user_entry.get()
    pw = password_entry.get()

    if len(web) < 1 or len(us) < 1 or len(pw) < 1:
        messagebox.showinfo('Oops', "Please don't leave any fields empty")
    else:
        its_ok = messagebox.askokcancel(title=web, message=f"There are the details entered: \nEmail: {us} \nPassword {pw}\n"
                                                  f"Is it ok to save?")
        if its_ok:
            user_name = check_user_name()
            if user_name == '':
                # create data.txt in the folder with program data
                with open('data.txt', 'w') as f:
                    f.writelines(f'login: {user_entry.get()}')
            with open('data.txt', 'a') as f:
                f.writelines(f'\n {web} | {us} | {pw}')

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# UI Setup
window = Tk()
window.config(padx=30, pady=30)
window.title('Password manager')

# Titles
website = Label(text='Website: ', font=FONT)
user = Label(text='Email/Username: ', font=FONT)
password = Label(text='Password: ', font=FONT)
website.grid(column=0, row=1)
user.grid(column=0, row=2)
password.grid(column=0, row=3)

# Canvas
canvas = Canvas(width=200, height=200)
canvas_img = PhotoImage(file='logo.png')
canvas.create_image(100, 105, image=canvas_img)
canvas.grid(column=1, row=0)

# Entry
website_entry = Entry(width=50)
user_entry = Entry(width=50)
password_entry = Entry(width=32)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
user_entry.grid(column=1, row=2, columnspan=2)
if user_name != '':
    user_entry.insert(END, user_name)
password_entry.grid(column=1, row=3)

# Button
generate_password_b = Button(text='Generate password', command=generate_password)
to_file_b = Button(text='Add', width=43, command=to_file)
generate_password_b.grid(row=3, column=2)
to_file_b.grid(column=1, row=4, columnspan=2)

window.mainloop()
