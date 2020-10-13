import Game_REWRITE
from tkinter import messagebox

def decied_card_to_play():
    if Game_REWRITE.com3_turn == True:
        messagebox.showinfo("Exploding Kittens Game", "It is currently com 3's turn.")
