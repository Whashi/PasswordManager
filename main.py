from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("db.txt", "a") as f:
        f.write(f"Website: {website_entry.get()}\n")
        f.write(f"Email/Username: {user_entry.get()}\n")
        f.write(f"Password: {password_entry.get()}\n")
        f.write("\n***\n\n")

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
website_entry = Entry(width=51)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan= 2)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
user_entry = Entry(width=51)
user_entry.insert(0, "elon@tesla.com")
user_entry.grid(row=2, column=1, columnspan= 2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)
password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

#row, column, columnspan

window.mainloop()