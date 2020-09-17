import time
import Game_REWRITE
import Com2_Behavior as C2B
import Check_Card_Played as CCP
import random
from tkinter import messagebox

def check_card_played():
    # Checks if com 2 has played an skip card
    if C2B.card_to_play == "skip":
        time.sleep(1)
        messagebox.showinfo("Exploding Kitens Game", "Com 2 has skiped there turn, it's now currently your turn")
        Game_REWRITE.discard_pile_text.set(C2B.card_to_play + "\n\n\n")
        Game_REWRITE.player_turn = True
        Game_REWRITE.com1_turn = False
        Game_REWRITE.com2_turn = False

    # Checks if com 2 has played an attack card
    elif C2B.card_to_play == "attack":
        time.sleep(1)
        messagebox.showinfo("Exploding Kittens Game", "Com1 has played an attack. Com 2 has skiped there turn and made you have 2 turns")
        Game_REWRITE.discard_pile_text.set(C2B.card_to_play + "\n\n\n")
        Game_REWRITE.player_turn = True
        Game_REWRITE.com1_turn = False
        Game_REWRITE.com2_turn = False
    
    # Checks if com 2 has played an favor card
    elif C2B.card_to_play == "favor":
        time.sleep(1)
        messagebox.showinfo("Exploding Kittens Game", "Com 2 has played a favor, click a card to give to them.")
        Game_REWRITE.discard_pile_text.set(C2B.card_to_play + "\n\n\n")

    # Checks if com 2 has player a shuffle card
    elif C2B.card_to_play == "shuffle":
        time.sleep(1)

        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)

        messagebox.showinfo("Exploding Kittens Game", "Com1 has shuffled the deck, it's now your turn.")

    # Checks if com 2 has played a see the future
    elif C2B.card_to_play == "see the future":
        time.sleep(1)

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

        messagebox.showinfo("Exploding Kittens Game", "Com 2 has played a see the future")
        Game_REWRITE.discard_pile_text.set(C2B.card_to_play + "\n \n \n")

    # Checks if com 2 has played a cat card 
    if C2B.card_to_play == 'potato cat' or 'taco cat' or 'rainbow ralphing cat' or 'beard cat' or 'cattermellon':
        messagebox.showinfo("Exploding Kittens Game", "Com 2 has played a cat card")

    # TODO Update com 2 to draw card

    Game_REWRITE.player_turn = True

    messagebox.showinfo("Exploding Kittens Game", "It's now currently your turn.")
