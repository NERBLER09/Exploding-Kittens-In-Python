# Imports all the modules needed 
import Game_REWRITE
from tkinter import messagebox
import Deal_To_Com_Players as DTCP

card_to_play = ""

# Main function that decides the card com 2 should play
def decied_card_to_play():
    global card_to_play

    if Game_REWRITE.com2_turn == True:
        messagebox.showinfo("Exploding Kittens Game", "It is currently com 2's turn.")

        print("Com 2's Hand: " + DTCP.com2_cards)