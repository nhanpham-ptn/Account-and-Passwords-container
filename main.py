# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import json

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]

    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password_entry.insert(0, "".join(password_list))

#-----------------------------FIND PASSWORD----------------------------------#
def find_password():
    website = website_entry.get()
    try:
        file = open("password_file.json", mode= "r")
        data_dict = json.load(file)
    except:
        tkinter.messagebox.showwarning(title= "ERROR", message= "No Data File Found")
    else:
        if website_entry.get() in data_dict.keys():
                email_username = data_dict[website]["Email/User"]
                password = data_dict[website]["Password"]
                tkinter.messagebox.showinfo(title=website, message=f"Email/Username: {email_username}\nPassword: {password}")
        else:
                tkinter.messagebox.showinfo(title = website, message = "No details for the website exist")


# ---------------------------- SAVE PASSWORD ------------------------------- #
import tkinter.messagebox


def save_password():
    if website_entry.get() == "" or password_entry.get() == "" or email_entry == "":
        tkinter.messagebox.askokcancel(title= "Attention", message= "Please enter the information")
    else:
        is_ok =tkinter.messagebox.askokcancel(title= website_entry.get(), message= f"These are the details entered: \nEmail: {email_entry.get()} \nPassword: {password_entry.get()} \nIs it okay to save?")

        if is_ok:
            new_data = {website_entry.get():{
                "Email/User": email_entry.get(),
                "Password"  : password_entry.get()
            }}
            try:
                with open("password_file.json", mode= "r") as file:
                    data = json.load(file)

            except FileNotFoundError:
                with open("password_file.json", mode= "w") as file:
                    json.dump(new_data, file, indent= 4)
            else:
                data.update(new_data)


                with open("password_file.json", mode= "w") as file:
                    json.dump(data, file, indent= 4)
            finally:
                website_entry.delete(0, 100)
                password_entry.delete(0, 100)
                email_entry.delete(0, 100)
  # ---------------------------- UI SETUP ------------------------------- #

import tkinter

window = tkinter.Tk()
window.config(padx= 50, pady= 50)
window.title("Password Manager")

#Website
Website = tkinter.Label(text= "Website:",font= ("Arial", 13))
Website.grid(row= 1, column= 0)

website_entry = tkinter.Entry(width=35, highlightthickness= 0 )
website_entry.grid(row= 1, column= 1)
website_entry.focus()

#Search
search = tkinter.Button(width=16, highlightthickness=0, text= "Search", font=("Arial", 13), command= find_password )
search.grid(row= 1,column=2 )

#Email

email = tkinter.Label(text= "Email/Username:",font= ("Arial", 13) )
email.grid(row= 2, column= 0 )

email_entry = tkinter.Entry(width= 62, highlightthickness=0 )
email_entry.insert(0, "nhanpham.ptn2110@gmail.com")
email_entry.grid(row= 2, column= 1, columnspan= 2)


#Password 
password = tkinter.Label(text = "Password:" ,font= ("Arial", 13))
password.grid(row= 3, column= 0)

password_entry = tkinter.Entry(width= 35, highlightthickness= 0 )
password_entry.grid(row= 3, column= 1)

password_button = tkinter.Button( highlightthickness=0, text= "Generate Password", font=("Arial", 13), command= generate)
password_button.grid(row= 3, column=2)

#add
add = tkinter.Button(highlightthickness=0, text= "Add", font=("Arial", 13), width= 40, command= save_password)
add.grid(row= 4, column= 1, columnspan= 2)


canvas = tkinter.Canvas(width= 200, height= 200, highlightthickness= 0)
lock_image = tkinter.PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image = lock_image)
canvas.grid(row= 0, column= 1)


window.mainloop()

