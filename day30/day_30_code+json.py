from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
from json import JSONDecodeError


def check_user_name():
    """check user login in data. If more than 1st launch auto entry user login in program"""
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            name = json.load(f)
            return name['login']
    except FileNotFoundError or JSONDecodeError:
        return 'user'
    except JSONDecodeError:
        return 'user'


FONT = ('Courier', 12, 'bold')
user_name = check_user_name()


# Password gen
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password_gen = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, password_gen)
    pyperclip.copy(password_gen)


# Password save
def to_file():
    """Save entry from user. Check for file and create it if it not exists"""
    web = website_entry.get()
    us = user_entry.get()
    pw = password_entry.get()
    data_save = {web: {
        'user': us,
        'password': pw,
    }}
    login_save = {f'login': user_entry.get()}

    if len(web) < 1 or len(us) < 1 or len(pw) < 1:
        messagebox.showinfo('Oops', "Please don't leave any fields empty")
    else:
        its_ok = messagebox.askokcancel(title=web, message=f"There are the details entered: \nEmail: {us} \n"
                                                           f"Password {pw}\nIs it ok to save?")
        if its_ok:
            global user_name
            user_name = check_user_name()
            try:
                with open('data.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if user_name != us:
                        new_data = {'login': us}
                        f.seek(0)
                        data.update(new_data)

            except FileNotFoundError:
                # create data.txt in the folder with program data
                with open('data.json', 'w', encoding='utf-8') as file:
                    json.dump(login_save, file, indent=4, ensure_ascii=False)

            except JSONDecodeError:
                with open('data.json', 'w', encoding='utf-8') as file:
                    json.dump(login_save, file, indent=4, ensure_ascii=False)

            else:
                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)

            with open('data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                data.update(data_save)

            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# Check site in data
def check_button():
    """Taking input and look for it in data.json. If True: return login and password. Else error"""
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

    except FileNotFoundError:
        messagebox.showerror(title='Password manager error', message='There is no file data.json')
    else:
        check = website_entry.get()
        if check in data:
            web = data[check]
            user_output = web['user']
            password_output = web['password']
            messagebox.showinfo(title=f'{check}', message=f'login: {user_output}\nPassword: {password_output}'
                                                          f'\nPassword have been copied.')
            pyperclip.copy(password_output)
        else:
            messagebox.showerror(title='Website error', message="Can't find this website.\nPlease check the entry.")


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
website_entry = Entry(width=32)
user_entry = Entry(width=50)
password_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
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
check_site_in_data = Button(text='Check', command=check_button, width=13)
check_site_in_data.grid(row=1, column=2)

window.mainloop()
