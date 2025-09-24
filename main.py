# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import json
import tkinter
import tkinter.messagebox

# ---------------------------- GENERATE PASSWORD ------------------------------- #
def generate():
    # Define possible characters for the password
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly decide how many of each type of character will be included
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Build a list of random characters from each category
    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    # Shuffle the list so characters are not in predictable order
    random.shuffle(password_list)

    # Insert the generated password into the password entry field
    password_entry.insert(0, "".join(password_list))


# ---------------------------- FIND PASSWORD ---------------------------------- #
def find_password():
    website = website_entry.get()  # Get the website name user typed
    try:
        # Try to open the JSON file that stores saved passwords
        file = open("password_file.json", mode="r")
        data_dict = json.load(file)
    except:
        # If file not found, show error message
        tkinter.messagebox.showwarning(title="ERROR", message="No Data File Found")
    else:
        # If website exists in saved data, show the email and password
        if website_entry.get() in data_dict.keys():
            email_username = data_dict[website]["Email/User"]
            password = data_dict[website]["Password"]
            tkinter.messagebox.showinfo(title=website, message=f"Email/Username: {email_username}\nPassword: {password}")
        else:
            # If no details for this website, notify the user
            tkinter.messagebox.showinfo(title=website, message="No details for the website exist")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # Check if any field is empty
    if website_entry.get() == "" or password_entry.get() == "" or email_entry.get() == "":
        tkinter.messagebox.askokcancel(title="Attention", message="Please enter the information")
    else:
        # Confirm before saving the password
        is_ok = tkinter.messagebox.askokcancel(
            title=website_entry.get(),
            message=f"These are the details entered: \nEmail: {email_entry.get()} \nPassword: {password_entry.get()} \nIs it okay to save?"
        )

        if is_ok:
            # New data to save
            new_data = {
                website_entry.get(): {
                    "Email/User": email_entry.get(),
                    "Password": password_entry.get()
                }
            }
            try:
                # Try to read existing data
                with open("password_file.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                # If file doesn't exist, create a new one with new data
                with open("password_file.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Update old data with new data
                data.update(new_data)
                with open("password_file.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                # Clear the entry fields after saving
                website_entry.delete(0, 100)
                password_entry.delete(0, 100)
                email_entry.delete(0, 100)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

# Website label + input
Website = tkinter.Label(text="Website:", font=("Arial", 13))
Website.grid(row=1, column=0)

website_entry = tkinter.Entry(width=35, highlightthickness=0)
website_entry.grid(row=1, column=1)
website_entry.focus()

# Search button
search = tkinter.Button(width=16, highlightthickness=0, text="Search", font=("Arial", 13), command=find_password)
search.grid(row=1, column=2)

# Email/Username label + input
email = tkinter.Label(text="Email/Username:", font=("Arial", 13))
email.grid(row=2, column=0)

email_entry = tkinter.Entry(width=62, highlightthickness=0)
email_entry.insert(0, "nhanpham.ptn2110@gmail.com")  # Default email
email_entry.grid(row=2, column=1, columnspan=2)

# Password label + input + generate button
password = tkinter.Label(text="Password:", font=("Arial", 13))
password.grid(row=3, column=0)

password_entry = tkinter.Entry(width=35, highlightthickness=0)
password_entry.grid(row=3, column=1)

password_button = tkinter.Button(highlightthickness=0, text="Generate Password", font=("Arial", 13), command=generate)
password_button.grid(row=3, column=2)

# Add button to save the password
add = tkinter.Button(highlightthickness=0, text="Add", font=("Arial", 13), width=40, command=save_password)
add.grid(row=4, column=1, columnspan=2)

# Lock image at the top of the UI
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
lock_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Run the UI loop
window.mainloop()
