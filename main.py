from tkinter import *
from tkinter import  messagebox
from random import randint, choice,  shuffle
import pyperclip
import json

# ---------------------------- SEARCH ------------------------------- #
def search():
    query = website_entry.get()

    try:
        with open("db.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Oopsies", message="There are no saved passwords")
    else:
        if len(query) == 0:
            messagebox.showerror(title="Oopsie Poopsie", message="Please enter a website to search for")
        elif query in data:
            query_data = data[query]
            messagebox.showinfo(title="Here you go", message=f"Email: {query_data['email']}\nPassword: {query_data['password']}")
        else:
            messagebox.showerror(title="omg", message="Couldn't find the entered website")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate_password():
    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any empty fields")
    else:
        try:
            with open("db.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data

        with open("db.json", "w") as f:
            json.dump(data, f, indent=4)

        website_entry.delete(0, "end")
        password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(row=1, column=1)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
user_entry = Entry(width=51)
user_entry.insert(0, "elon@tesla.com")
user_entry.grid(row=2, column=1, columnspan= 2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()