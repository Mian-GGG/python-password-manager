import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
from customtkinter import *
from PIL import Image


# ---------------------------- PASSWORD FINDER ------------------------------- #

def find_password():
    try:
        with open("Password File.json", "r") as file:
            password_dic = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="You have no passwords saved, please save some passwords first then"
                                                    " search.")
    else:
        try:
            searched_pass = password_dic[website_entry.get()]
        except KeyError:
            messagebox.showerror(title="Error", message="There no saved password associated to this website, please"
                                                        " check if website name is correct and try again.")
        else:
            pyperclip.copy(searched_pass['Password:'])
            messagebox.showinfo(title=f"{website_entry.get()}", message=f"Email: {searched_pass['Email/Username:']} \n"
                                                                        f"Password: {searched_pass['Password:']} \n\n"
                                                                        f"Password copied to clipboard!")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for n in range(randint(8, 10))]

    password_list += [choice(symbols) for m in range(randint(2, 4))]

    password_list += [choice(numbers) for b in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    password_entered = password_entry.get()
    username = username_entry.get()

    new_data = {
        website: {
            "Email/Username:": username,
            "Password:": password_entered
        }
    }

    if website == '' or password_entered == '' or username == '':
        messagebox.showerror(title="Error", message="Please don't leave any boxes empty.")
    else:

        is_ok = messagebox.askyesno(title=website, message=f"These are the details entered: \n"
                                                           f"Username: {username} \n"
                                                           f"Password: {password_entered} \n"
                                                           f"Are these details ok to save?")

        if is_ok:
            try:
                with open("Password File.json", "r") as f:
                    data = json.load(f)
                    data.update(new_data)
            except FileNotFoundError or FileExistsError:
                with open("Password File.json", "w") as new_file:
                    json.dump(new_data, new_file, indent=4)
            else:
                with open("Password File.json", "w") as file:
                    json.dump(data, file, indent=5)
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = CTk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
set_appearance_mode("light")
canvas = CTkCanvas(height=200, width=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1, padx=5, pady=5)

website_label = CTkLabel(text="Website:", font=("Courier", 15, "bold"), master=window)
website_label.grid(row=1, column=0, padx=5, pady=5)

username_label = CTkLabel(text="Emai/Username:", font=("Courier", 15, "bold"), master=window)
username_label.grid(row=2, column=0, padx=5, pady=5)

password_label = CTkLabel(text="Password:", font=("Courier", 15, "bold"), master=window)
password_label.grid(row=3, column=0, padx=5, pady=5)

website_entry = CTkEntry(width=170, master=window)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w", padx=5, pady=5)
website_entry.focus()

username_entry = CTkEntry(width=200, master=window)
username_entry.grid(row=2, column=1, columnspan=2, sticky="w", padx=5, pady=5)
username_entry.insert(0, "youremailhere@outlook.com")

password_entry = CTkEntry(width=170, master=window)
password_entry.grid(row=3, column=1, columnspan=2, sticky="w", padx=5, pady=5)

generate_pass_button = CTkButton(text="Generate Password", command=generate_password, master=window)
generate_pass_button.grid(row=3, column=2, padx=5, pady=5)

add_button = CTkButton(text="Add", width=200, command=save, master=window)
add_button.grid(row=4, column=1, columnspan=2, sticky="w", padx=5, pady=5)

search_button = CTkButton(text="Search", command=find_password, master=window)
search_button.grid(row=1, column=2, padx=5, pady=5)

window.mainloop()
