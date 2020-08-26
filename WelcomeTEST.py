# imports all the modules needed 
from tkinter import *
from tkinter import messagebox

# Creates the Tk Window
welcome = Tk()
welcome.title("Welcome to Exploding Kittens!") # Renames the windows to: Welcome to Exploding Kittens!
welcome.resizable(0, 0) # Makes so the window is not resizable

com_value = IntVar()

com_number = 0

username = ""

# Functions needed 
def com_click(value):
    # Gets the value of the selected radiobutton

    global com_number
    com_number = value

    if value == 1:
        com_number = 1
    elif value == 2:
        com_number = 2
    elif value == 3:
        com_number = 3  

def open_game():
    global username

    username = name_box.get()

    # Checks if the player inputted the amount of com players and/or there username
    if com_number == 0:
        messagebox.showerror('Welcome to Exploding Kittens!', 'You have not selected the amount of com players')
    elif username == "":
        messagebox.showerror('Welcome to Exploding Kittens!', 'You have not entered your username')
    else:
        welcome.destroy()

        import Game_REWRITE

        Game_REWRITE

# Creates labels
welcome_label = Label(welcome, text="We will need to set up a few things before you can play", font = "40")
welcome_label.grid(row=0, column = 0)

com_label = Label(welcome, text="\nHow many computer players do you want.", font="20")
com_label.grid(row=1, column = 0)

# Computer Player Radio Buttons 
Radiobutton(welcome, text="1 Computer Player", variable=com_value, value=1, command=lambda: com_click(1)).grid(row=2, column=0)
Radiobutton(welcome, text="2 Computer Players", variable=com_value, value=2, command=lambda: com_click(2)).grid(row=3, column=0)
Radiobutton(welcome, text="3 Computer Players", variable=com_value, value=3, command=lambda: com_click(3)).grid(row=4, column=0)

# Username Input Entry

name_label = Label(welcome, text="Please enter a Username", font = "20")
name_label.grid(row = 5 , column = 0)

name_box = Entry(welcome, width=50)
name_box.grid(row=6, column=0)
name_box.insert(0, "EXAMPLE")
## username = name_box.get()

# Submit Button

submit_buton = Button(welcome, text="Submit", font="15", command=open_game)
submit_buton.grid(row=7, column = 0)

welcome.mainloop()