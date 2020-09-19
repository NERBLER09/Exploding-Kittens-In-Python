import time
import Game_REWRITE
import Com2_Behavior as C2B
import Check_Card_Played as CCP
import Deal_To_Com_Players as DTCP
import Check_Card_Drawn as CCD
import random
from tkinter import messagebox

def draw_card():
    # Checks if DTCP.com2_card1 is equal to ""
    if DTCP.com2_card1 == "":
        DTCP.com2_card1 = random.choice(Game_REWRITE.cards)
        DTCP.com2_cards[0] = DTCP.com2_card1

        messagebox.showinfo("Exploding Kittens Game", "Com 2 has drawn, it's now currently your turn") 
        Game_REWRITE.player_turn = True 
        Game_REWRITE.com1_turn = False
        Game_REWRITE.com2_turn = False

        CCD.check_card(DTCP.com2_card1)

    # Checks if DTCP.com2_card2 is equal to ""
    elif DTCP.com2_card2 == "":
        DTCP.com2_card2 = random.choice(Game_REWRITE.cards)
        DTCP.com2_cards[1] = DTCP.com2_card2

        messagebox.showinfo("Exploding Kittens Game", "Com 2 has drawn, it's now currently your turn") 
        Game_REWRITE.player_turn = True 
        Game_REWRITE.com1_turn = False
        Game_REWRITE.com2_turn = False

        CCD.check_card(DTCP.com2_cards)

    # Checks if DTCP.com2_card3 is equal to ""
    elif DTCP.com2_card3 == "":
        DTCP.com2_card3 = random.choice(Game_REWRITE.cards)
        DTCP.com2_cards[2] = DTCP.com2_card2

        messagebox.showinfo("Exploding Kittens Game", "Com 2 has drawn, it's now currently your turn") 
        Game_REWRITE.player_turn = True 
        Game_REWRITE.com1_turn = False
        Game_REWRITE.com2_turn = False

        CCD.check_card(DTCP.com2_cards)

    # Checks if DTCP.com2_card4 is equal to ""
    elif DTCP.com2_card4 == "":
        DTCP.com2_card4 = random.choice(Game_REWRITE.cards)
        DTCP.com2_cards[3] = DTCP.com2_card2

        messagebox.showinfo("Exploding Kittens Game", "Com 2 has drawn, it's now currently your turn") 
        Game_REWRITE.player_turn = True 
        Game_REWRITE.com1_turn = False
        Game_REWRITE.com2_turn = False

        CCD.check_card(DTCP.com2_cards)

    print("After Drawn: " + str(DTCP.com2_cards))

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

        draw_card()
 
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

        draw_card()

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

        draw_card()

    # Checks if com 2 has played a cat card 
    elif C2B.card_to_play == 'potato cat' or 'taco cat' or 'rainbow ralphing cat' or 'beard cat' or 'cattermellon':
        messagebox.showinfo("Exploding Kittens Game", "Com 2 has played a cat card")

        draw_card()

    # TODO Update com 2 to draw card

    Game_REWRITE.player_turn = True

    messagebox.showinfo("Exploding Kittens Game", "It's now currently your turn.")
