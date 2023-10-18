# Password Manager using tkinter
from tkinter import *
from tkinter import messagebox
import pandas
import random


# -----------------------------------------Random Password Generation------------------------------------------#
def generatePass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_nums = [random.choice(numbers) for i in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_list = password_letters + password_nums + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    passwordEntry.delete(0, END)
    passwordEntry.insert(0, password)
    print(f"Your password is: {password}")


# ------------------------------------Save Data------------------------------------------------#
def save_data():
    website = webEntry.get()
    username = emailEntry.get()
    password = passwordEntry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Fields", message="Fields are still empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details:\nEmail: {username} "
                                                      f"\nPassword: {password} \nIs it ok to save??")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
            webEntry.delete(0, END)
            emailEntry.delete(0, END)
            passwordEntry.delete(0, END)

# --------------------------------------UI SETUP----------------------------------------------#
window = Tk()
window.title("Password Manager")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)

# canvas
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="D:\PyCharm Community Edition 2020.3\pythonCourse\Day-29\logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=2 , rowspan=2)

# label
webLabel = Label(text="Website:")
webLabel.grid(row=2, column=0)

emailLabel = Label(text="Email/Username:")
emailLabel.grid(row=3, column=0)

passwordLabel = Label(text="Password:")
passwordLabel.grid(row=4, column=0)

# Entry
webEntry = Entry()
webEntry.config(width=44)
webEntry.focus()
webEntry.grid(row=2, column=1, columnspan=3)

emailEntry = Entry()
emailEntry.config(width=44)
emailEntry.grid(row=3, column=1, columnspan=3)

passwordEntry = Entry()
passwordEntry.config(width=35)
passwordEntry.grid(row=4, column=1, columnspan=2)

# buttons
generateButton = Button(text="Generate", command=generatePass)
generateButton.grid(row=4, column=3)

addButton = Button(text="ADD Entry", command=save_data)
addButton.config(width=40)
addButton.grid(row=5, column=1, columnspan=4)

window.mainloop()
