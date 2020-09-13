import time
import Game_REWRITE
import Com2_Behavior as C2B
from tkinter import messagebox

def check_card_played():
    # Checks is com 2 has played an skip card
    if C2B.card_to_play == "skip":
        time.sleep(1)
        messagebox.showinfo("Exploding Kitens Game", "Com 2 has skiped there turn, it's now currently your turn")
        Game_REWRITE.discard_pile_text.set(C2B.card_to_play + "\n\n\n")
        Game_REWRITE.player_turn = True
        Game_REWRITE.com1_turn = False
        Game_REWRITE.com2_turn = False

    # TODO Add rest of cards
