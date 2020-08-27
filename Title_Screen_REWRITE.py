# imports all the modules needed 
from tkinter import *
from tkinter import messagebox
import webbrowser

# Creates the Tk Window
windows = Tk()
windows.title("Exploding Kittens Main Menu") # Renames the windows to: Exploding Kittens Main Menu from: tk
windows.configure(bg='#DF0101') # Sets the bg color
windows.geometry("1366x600") # Sets the size
windows.resizable(0, 0) # Makes so the window is not resizable

# Functions needed 
def play_button_clicked():
    play = messagebox.askquestion("Exploding Kittens Main Menu", "The game is very incomplete, are you sure you want to continue?")

    if play == "yes":
        windows.destroy()

        import WelcomeTEST
        WelcomeTEST
    else:
        messagebox.showinfo("Exploding Kittens Main Menu", "The window will now close")

        windows.destroy()

        quit()        

def web_clicked():
    webbrowser.open('https://explodingkittens.com/how-to-play') # Opens the how to play web site

def show_about():
    # Shows the about messagebox
    messagebox.showinfo("About", "Exploding Kittens Game, recreated in python by Noah Beaudin\nVersos: Alpha Build 1\nGithub Page: github.com/nerbler09\nCheck the licence for sharing and use of the source code")

def show_licence_file():
    # Opens the Licence.rft File In Wordpad
    webbrowser.open("Licence.rtf")

def exit():
    # Quits the game
    windows.destroy()

    quit()

# Creates the title
title = Label(windows, text = "Exploding Kittens!", font = "Times 50", bg= "#FE2E2E")
title.place(x = 500, y = 205)

# Creates the play button
play_button = Button(windows, text="PLAY", bg = "#DF0101", font = "40", command=play_button_clicked)
play_button.place(x = 650, y = 300)

# Creates the menubar
title_menu = Menu(windows, bg = "#DF0101")
windows.config(menu = title_menu) # Sets the title_menu to be the main menu

option_menu = Menu(title_menu)
title_menu.add_cascade(label = "Options", menu = option_menu)
option_menu.add_command(label = "Open Help To Play", command = web_clicked)
option_menu.add_command(label = "Quit", command = exit)

help_menu = Menu(title_menu)
title_menu.add_cascade(label = "Help", menu = help_menu)
help_menu.add_command(label = "Open About", command = show_about)
help_menu.add_command(label = "Open Licence File", command = show_licence_file)

windows.mainloop()
