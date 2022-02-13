from tkinter import Tk, Button, Label, Entry, Canvas, PhotoImage, END, messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    letters_list = [choice(letters) for _ in range(nr_letters)]
    symbols_list = [choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    # copy the newly created password to the clipboard
    pyperclip.copy(password)
    messagebox.showinfo(title="Info", message="The newly created password saved to clipboard")

# ---------------------------- SAVE PASSWORD ------------------------------------ #


def save():
    website_value = entry_website.get()
    email_username_value = entry_email_username.get()
    password_value = entry_password.get()

    if len(website_value) == 0 or len(password_value) == 0:
        info_message = messagebox.showinfo(title="Oops", message="Do not leave website or password fields empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website_value}", message=f"The details you've entered are:\n"
                                                                         f"website: {website_value}\n"
                                                                         f"email:{email_username_value}\n"
                                                                         f"password: {password_value}\n"
                                                                         f"Add details to the file?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website_value} | {email_username_value} | {password_value}\n")
            # clear website and password fields
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(width=1300, height=1300, padx=20, pady=20)

canvas = Canvas(width=200, height=200, bg="white")
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_email_username = Label(text="Email/Username:")
label_email_username.grid(row=2, column=0)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Entries

entry_website = Entry(width=52)
entry_website.grid(row=1, column=1, columnspan=2, sticky="w")
entry_website.focus()

entry_email_username = Entry(width=52)
entry_email_username.grid(row=2, column=1, columnspan=2, sticky="w")
entry_email_username.insert(END, "i.e. alex@gmail.com")

entry_password = Entry(width=31)
entry_password.grid(row=3, column=1, sticky="w")

# Buttons

btn_generate_password = Button(text="Generate Password", command=generate_password)
btn_generate_password.grid(row=3, column=2, sticky="w")

btn_generate_password = Button(text="Add", width=45, command=save)
btn_generate_password.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
