# imports all the modules needed 
import tkinter as tk
from tkinter import messagebox
import webbrowser
import os

# Creates the Tk Window
windows = tk.Tk()
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
        
def web_clicked():
    webbrowser.open('https://explodingkittens.com/how-to-play') # Opens the how to play web site

def show_about():
    # Shows the about messagebox
    messagebox.showinfo("About", "Exploding Kittens Game, recreated in python by Noah Beaudin\nVersion: Alpha Build 3\nGithub Page: github.com/nerbler09\nCheck the licence for sharing and use of the source code")

def show_licence_file():
    # Opens the licence.html File In The Webbrowser
    webbrowser.open("file://" + os.path.realpath("Licence/licence.html"), new = 1)

# Opens My Github page
def open_github():
    webbrowser.open("https://github.com/nerbler09")

# Opens the Github repo
def open_github_repo():
    webbrowser.open("https://github.com/nerbler09/exploding-kittens-in-python.git")

def exit():
    # Quits the game
    windows.destroy()

    quit()

# Creates the title
title = tk.Label(windows, text = "Exploding Kittens!", font = "Times 50", bg= "#FE2E2E")
title.place(x = 500, y = 205)

# Creates the play button
play_button = tk.Button(windows, text="PLAY", bg = "#DF0101", font = "40", command=play_button_clicked)
play_button.place(x = 650, y = 300)

# Creates the menubar
title_menu = tk.Menu(windows, bg = "#DF0101")
windows.config(menu = title_menu) # Sets the title_menu to be the main menu

option_menu = tk.Menu(title_menu)
title_menu.add_cascade(label = "Options", menu = option_menu)
option_menu.add_command(label = "Open Help To Play", command = web_clicked)
option_menu.add_command(label = "Quit", command = exit)

help_menu = tk.Menu(title_menu)
title_menu.add_cascade(label = "Help", menu = help_menu)
help_menu.add_cascade(label = "Github Page", command = open_github)
help_menu.add_cascade(label = "Github Repo", command = open_github_repo)
help_menu.add_command(label = "Open About", command = show_about)
help_menu.add_command(label = "Open Licence File", command = show_licence_file)

windows.mainloop()
