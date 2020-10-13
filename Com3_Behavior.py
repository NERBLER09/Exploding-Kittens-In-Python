import Game_REWRITE
from tkinter import messagebox
import Deal_To_Com_Players as DTCP
import random

# Main function that decides the card com 3 should play
def decied_card_to_play():
    if Game_REWRITE.com3_turn == True:
        messagebox.showinfo("Exploding Kittens Game", "It is currently com 3's turn.")

        print("Com 3's hand: " + str(DTCP.com3_cards))

        card_to_play = random.choice(DTCP.com2_cards)

        print("Card Com 3's going to play " + str(card_to_play))
