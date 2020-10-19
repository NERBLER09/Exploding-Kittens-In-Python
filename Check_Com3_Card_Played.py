import Com3_Behavior as C3B
import time
from tkinter import messagebox
import Game_REWRITE
import random
import Check_Card_Played as CCP

def check_card_played():
    # Checks if com 3 has played an skip card
    if C3B.card_to_play == "skip":
        time.sleep(1)

        print("Com 3 has played a skip card")
        messagebox.showinfo("Exploding Kittens Game", "Com 3 has skiped there turn, it's now currently your turn")
        Game_REWRITE.discard_pile_text.set(C3B.card_to_play + "\n\n\n")
        Game_REWRITE.com3_turn = False
        Game_REWRITE.com2_turn = False
        Game_REWRITE.com1_turn = False
        Game_REWRITE.player_turn = True

    # Checks if com 3 has played an attack card
    elif C3B.card_to_play == "attack":
        time.sleep(1)

        print("Com 3 has played a attack card")
        messagebox.showinfo("Exploding Kittens Game", "Com 3 has played an attack. Com 3Com 2 has played an attack. Com 2 has skiped there turn and made you have 2 turns has skiped there turn and made you have 2 turns")
        Game_REWRITE.discard_pile_text.set(C3B.card_to_play + "\n\n\n")
        Game_REWRITE.com3_turn = False
        Game_REWRITE.com2_turn = False
        Game_REWRITE.com1_turn = False
        Game_REWRITE.player_turn = True

    # Checks if com 3 has played an favor card
    elif C3B.card_to_play == "favor":
        time.sleep(1)

        print("Com 3 has played a favor card")
        messagebox.showinfo("Exploding Kittens Game", "Com 3 has played a favor card, it's now currently your turn.")
        Game_REWRITE.discard_pile_text.set(C3B.card_to_play + "\n\n\n")
        Game_REWRITE.com3_turn = False
        Game_REWRITE.com2_turn = False
        Game_REWRITE.com1_turn = False
        Game_REWRITE.player_turn = True

    # Checks if com 3 has played an shuffle card
    elif C3B.card_to_play == "shuffle":
        time.sleep(1)

        print("Com 3 has played a shuffle card")

        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)

        messagebox.showinfo("Exploding Kittens Game", "Com 3 has shuffled the deck, it's now your turn")

    # Checks if com 3 has played an see the future card
    elif C3B.card_to_play == "see the future":
        time.sleep(1)

        print("Com 3 has played a see the future card")

        # Assigns the top 3 cards to a random choice, this will be used to be find the top 3 cards
        CCP.first_card = random.choice(Game_REWRITE.cards)
        CCP.second_card = random.choice(Game_REWRITE.cards)
        CCP.third_card = random.choice(Game_REWRITE.cards)

        # Prints the top 3 card assigned above
        print("--------------")
        print(CCP.first_card)
        print(CCP.second_card)
        print(CCP.third_card)
        print("--------------")

        messagebox.showinfo("Exploding Kittens Game", "Com 3 has played a see the future")
        Game_REWRITE.discard_pile_text.set(C3B.card_to_play + "\n \n \n")

        messagebox.showinfo("Exploding Kittens Game", "Com 3 has played a see the future card, it's now currently you turn")

    elif C3B.card_to_play == 'potato cat' or 'taco cat' or 'rainbow ralphing cat' or 'beard cat' or 'cattermellon':
        time.sleep(1)

        print("Com 3 has played a " + C3B.card_to_play + " card")

        # TODO steal card

    Game_REWRITE.com1_turn = False
    Game_REWRITE.com2_turn = False
    Game_REWRITE.com3_turn = False
    Game_REWRITE.player_turn = True
