from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_get = website_entry.get()
    email_get = email_entry.get()
    password = password_entry.get()

    if len(website_get) == 0 or len(password) == 0:
        messagebox.showinfo(title="MISSING FIELD", message="Please Fill the form before submitting.")
    else:
        is_ok = messagebox.askokcancel(title=website_get, message=f"These are the details: \n Email : {email_get}\n Password"
                                                                  f" : {password}\n Click OK to save.")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_get} | {email_get} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50, bg= "white")

canvas = Canvas(height= 200, width= 200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(row = 0, column=1)

website_label = Label(text="Website:", bg= "white",fg="black")
website_label.grid(row = 1, column = 0)

website_entry = Entry(bg="white", fg = "black", highlightthickness= 0, width= 39)
website_entry.grid(row = 1, column=1, columnspan= 2)
website_entry.focus()

email_label = Label(text = "Email/Username:", bg = "white", fg = "black")
email_label.grid(row = 2, column = 0)

email_entry = Entry(bg="white", fg = "black", highlightthickness=0, width= 39)
email_entry.grid(row = 2, column=1, columnspan= 2)
email_entry.insert(0, "example@gmail.com")

password_label = Label(text = "Password:", bg = "white", fg = "black")
password_label.grid(row = 3, column= 0)

password_entry = Entry(width= 21, bg= "white", fg = "black", highlightthickness=0)
password_entry.grid(row=3, column=1)

pass_generate_button = Button(text="Generate Password", fg="black", bg="white", highlightthickness= 0, command=generate_password)
pass_generate_button.grid(row = 3, column= 2)

add_button = Button(text="Add", bg="white", fg= "black", width= 36, highlightthickness= 0, command=save_password)
add_button.grid(row = 4, column=1, columnspan= 2)


window.mainloop()
