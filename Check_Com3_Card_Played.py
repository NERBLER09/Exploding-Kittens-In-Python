import Com3_Behavior as C3B
import time
from tkinter import messagebox
import Game_REWRITE
import random
import Check_Card_Played as CCP
import Deal_To_Com_Players as DTCP
import Check_Card_Drawn as CCD
import Check_Com2_Card_Played as CC2CP

# Function draws a card for com 3
def draw_card():
    # Checks if DTCP.com3_card1 is equal to ""
    if DTCP.com3_card1 == "":
        # Checks if com 1, com 2 or the player has played a see the future
        if CCP.first_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card1 = CCP.first_card
            DTCP.com3_cards[0] = DTCP.com3_card1

            CCD.check_card(DTCP.com3_card1)

            CCP.first_card = " "

        elif CCP.second_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card1 = CCP.first_card
            DTCP.com3_cards[0] = DTCP.com3_card1

            CCD.check_card(DTCP.com3_card1)

            CCP.second_card = " "

        elif CCP.third_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card1 = CCP.first_card
            DTCP.com3_cards[0] = DTCP.com3_card1

            CCD.check_card(DTCP.com3_card1)

            CCP.third_card = " "

        else:  
            # Draws card from draw pile then adds to com 2's hand
            DTCP.com3_card1 = random.choice(Game_REWRITE.cards)
            DTCP.com3_cards[0] = DTCP.com3_card1
            CCD.check_card(DTCP.com3_card1)

    # Checks if DTCP.com3_card2 is equal to ""
    elif DTCP.com3_card2 == "":
        # Checks if com 1, com 2 or the player has played a see the future
        if CCP.first_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card2 = CCP.first_card
            DTCP.com3_cards[1] = DTCP.com3_card2

            CCD.check_card(DTCP.com3_card2)

            CCP.first_card = " "

        elif CCP.second_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card2 = CCP.first_card
            DTCP.com3_cards[1] = DTCP.com3_card2

            CCD.check_card(DTCP.com1_card2)

            CCP.second_card = " "

        elif CCP.third_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card2 = CCP.first_card
            DTCP.com3_cards[1] = DTCP.com3_card2

            CCD.check_card(DTCP.com1_card2)

            CCP.third_card = " "

        else:  
            # Draws card from draw pile then adds to com 2's hand
            DTCP.com3_card2 = random.choice(Game_REWRITE.cards)
            DTCP.com3_cards[1] = DTCP.com3_card2
            CCD.check_card(DTCP.com3_card2)

    # Checks if DTCP.com3_card3 is equal to ""
    elif DTCP.com3_card3 == "":
        # Checks if com 1, com 2 or the player has played a see the future
        if CCP.first_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card1 = CCP.first_card
            DTCP.com3_cards[0] = DTCP.com3_card1

            CCD.check_card(DTCP.com1_card1)

            CCP.first_card = " "

        elif CCP.second_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card1 = CCP.first_card
            DTCP.com3_cards[0] = DTCP.com3_card1

            CCD.check_card(DTCP.com1_card1)

            CCP.second_card = " "

        elif CCP.third_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card1 = CCP.first_card
            DTCP.com3_cards[0] = DTCP.com3_card1

            CCD.check_card(DTCP.com1_card1)

            CCP.third_card = " "

        else:  
            # Draws card from draw pile then adds to com 2's hand
            DTCP.com3_card1 = random.choice(Game_REWRITE.cards)
            DTCP.com3_cards[0] = DTCP.com3_card1
            CCD.check_card(DTCP.com3_card1)

    # Checks if DTCP.com3_card4 is equal to ""
    elif DTCP.com3_card4 == "":
        # Checks if com 1, com 2 or the player has played a see the future
        if CCP.first_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card4 = CCP.first_card
            DTCP.com3_cards[3] = DTCP.com3_card4

            CCD.check_card(DTCP.com1_card4)

            CCP.first_card = " "

        elif CCP.second_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card4 = CCP.first_card
            DTCP.com3_cards[3] = DTCP.com3_card4

            CCD.check_card(DTCP.com1_card4)

            CCP.second_card = " "

        elif CCP.third_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card4 = CCP.first_card
            DTCP.com3_cards[3] = DTCP.com3_card4

            CCD.check_card(DTCP.com1_card4)

            CCP.third_card = " "

        else:  
            # Draws card from draw pile then adds to com 2's hand
            DTCP.com3_card4 = random.choice(Game_REWRITE.cards)
            DTCP.com3_cards[3] = DTCP.com3_card4
            CCD.check_card(DTCP.com3_card4)

    # Checks if DTCP.com3_card5 is equal to ""
    elif DTCP.com3_card5 == "":
        # Checks if com 1, com 2 or the player has played a see the future
        if CCP.first_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card5 = CCP.first_card
            DTCP.com3_cards[4] = DTCP.com3_card5

            CCD.check_card(DTCP.com1_card5)

            CCP.first_card = " "

        elif CCP.second_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card6 = CCP.first_card
            DTCP.com3_cards[4] = DTCP.com3_card5

            CCD.check_card(DTCP.com1_card4)

            CCP.second_card = " "

        elif CCP.third_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card5 = CCP.first_card
            DTCP.com3_cards[4] = DTCP.com3_card5

            CCD.check_card(DTCP.com1_card5)

            CCP.third_card = " "

        else:  
            # Draws card from draw pile then adds to com 2's hand
            DTCP.com3_card5 = random.choice(Game_REWRITE.cards)
            DTCP.com3_cards[4] = DTCP.com3_card5
            CCD.check_card(DTCP.com3_card5)

    # Checks if DTCP.com3_card6 is equal to ""
    elif DTCP.com3_card6 == "":
        # Checks if com 1, com 2 or the player has played a see the future
        if CCP.first_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card6 = CCP.first_card
            DTCP.com3_cards[5] = DTCP.com3_card6

            CCD.check_card(DTCP.com1_card4)

            CCP.first_card = " "

        elif CCP.second_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card6 = CCP.first_card
            DTCP.com3_cards[5] = DTCP.com3_card6

            CCD.check_card(DTCP.com1_card4)

            CCP.second_card = " "

        elif CCP.third_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card6 = CCP.first_card
            DTCP.com3_cards[5] = DTCP.com3_card6

            CCD.check_card(DTCP.com1_card4)

            CCP.third_card = " "

        else:  
            # Draws card from draw pile then adds to com 2's hand
            DTCP.com3_card6 = random.choice(Game_REWRITE.cards)
            DTCP.com3_cards[5] = DTCP.com3_card6
            CCD.check_card(DTCP.com3_card6)

    # Checks if DTCP.com3_card7 is equal to ""
    elif DTCP.com3_card7 == "":
        # Checks if com 1, com 2 or the player has played a see the future
        if CCP.first_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card7 = CCP.first_card
            DTCP.com3_cards[6] = DTCP.com3_card7

            CCD.check_card(DTCP.com1_card4)

            CCP.first_card = " "

        elif CCP.second_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card7 = CCP.first_card
            DTCP.com3_cards[6] = DTCP.com3_card7

            CCD.check_card(DTCP.com1_card4)

            CCP.second_card = " "

        elif CCP.third_card != " ":
            # Adds the cards to com 2's hand
            DTCP.com3_card7 = CCP.first_card
            DTCP.com3_cards[6] = DTCP.com3_card7

            CCD.check_card(DTCP.com1_card4)

            CCP.third_card = " "

        else:  
            # Draws card from draw pile then adds to com 2's hand
            DTCP.com3_card7 = random.choice(Game_REWRITE.cards)
            DTCP.com3_cards[6] = DTCP.com3_card7
            CCD.check_card(DTCP.com3_card7)


    if CC2CP.com2_played_attack == True:
        messagebox.showinfo("Exploding Kittens Game", "It's com 3's turn again because com 2 has played an attack card")

        CC2CP.com2_played_attack = False
        
        C3B.decied_card_to_play()
    else:
        messagebox.showinfo("Exploding Kittens Game", "Com 3 has drawn, it's now your turn")

        Game_REWRITE.com1_turn = False
        Game_REWRITE.com2_turn = False
        Game_REWRITE.com3_turn = False
        Game_REWRITE.player_turn = True    

# Add cards gotten from favor or cat cards to com 3's hand
def add_card_to_hand(card_to_add_to_hand):
    # Adds the card to there 1st card slot
    if DTCP.com3_card1 == "":
        DTCP.com3_card1 = card_to_add_to_hand 
        DTCP.com3_cards[0] = DTCP.com3_card1

    # Adds the card to there 2st card slot
    elif DTCP.com3_card2 == "":
        DTCP.com3_card2 = card_to_add_to_hand 
        DTCP.com3_cards[0] = DTCP.com3_card2

    # Adds the card to there 3st card slot
    elif DTCP.com3_card3 == "":
        DTCP.com3_card3 = card_to_add_to_hand 
        DTCP.com3_cards[0] = DTCP.com3_card3

    # Adds the card to there 4st card slot
    elif DTCP.com3_card4 == "":
        DTCP.com3_card4 = card_to_add_to_hand 
        DTCP.com3_cards[0] = DTCP.com3_card4

    # Adds the card to there 5st card slot
    elif DTCP.com3_card5 == "":
        DTCP.com3_card5 = card_to_add_to_hand 
        DTCP.com3_cards[0] = DTCP.com3_card5

    # Adds the card to there 6st card slot
    elif DTCP.com3_card6 == "":
        DTCP.com3_card6 = card_to_add_to_hand 
        DTCP.com3_cards[0] = DTCP.com3_card6

    # Adds the card to there 7st card slot
    elif DTCP.com3_card7 == "":
        DTCP.com3_card7 = card_to_add_to_hand 
        DTCP.com3_cards[0] = DTCP.com3_card7

    else:
        print("An error has been encountered.")

# Steals card from player when com 3 plays a cat
def steal_cat_card(cat_card):
    looped_on_card = ""

    # Loops through com 3's hand for matching card
    for cards_in_com3_hand in DTCP.com3_cards:
        looped_on_card = cards_in_com3_hand

        # Checks if the looped on card match the played card
        if cards_in_com3_hand == cat_card:
            print("Com 3 has played 2 " + cat_card + " cards")

            messagebox.showinfo("Exploding Kittens Game", "Com 3 has played 2 matching "  + cat_card +  " cards")

            steal_card = random.choice(Game_REWRITE.player_cards) # Gets a card from the player that com 3 is going to steal

            while steal_card == "":
                steal_card = random.choice(Game_REWRITE.player_cards) # Gets a card from the player that com 3 is going to steal

            print(steal_card)

            messagebox.showinfo("Exploding Kittens Game", "Com 3 has stolen your " + steal_card + " card")

            add_card_to_hand(steal_card)

            break

        else:
            print("Com 3 hasn't played 2 " + cat_card + "cards")

    print("Looped card is " + looped_on_card)

    if looped_on_card != cat_card:
        messagebox.showerror("Exploding Kittens Game", 'Com 3 has not successfully played 2 cat cards')

def check_card_played():
    # Checks if com 3 has played an skip card
    if C3B.card_to_play == "skip":
        time.sleep(1)

        print("Com 3 has played a skip card")
        messagebox.showinfo("Exploding Kittens Game", "Com 3 has skiped there turn, it's now currently your turn")
        Game_REWRITE.discard_pile_text.set(C3B.card_to_play + "\n\n\n")
        Game_REWRITE.com3_turn = False
        Game_REWRITE.com3_turn = False
        Game_REWRITE.com1_turn = False
        Game_REWRITE.player_turn = True

    # Checks if com 3 has played an attack card
    elif C3B.card_to_play == "attack":
        time.sleep(1)

        print("Com 3 has played a attack card")
        messagebox.showinfo("Exploding Kittens Game", "Com 3 has played an attack and make you have 2 turns")
        Game_REWRITE.discard_pile_text.set(C3B.card_to_play + "\n\n\n")
        Game_REWRITE.com3_turn = False
        Game_REWRITE.com3_turn = False
        Game_REWRITE.com1_turn = False
        Game_REWRITE.player_turn = True

    # Checks if com 3 has played an favor card
    elif C3B.card_to_play == "favor":
        time.sleep(1)

        print("Com 3 has played a favor card")
        messagebox.showinfo("Exploding Kittens Game", "Com 3 has played a favor card, it's now currently your turn.")
        Game_REWRITE.discard_pile_text.set(C3B.card_to_play + "\n\n\n")
        Game_REWRITE.com3_turn = False
        Game_REWRITE.com3_turn = False
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

        draw_card()

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

        draw_card()

    elif C3B.card_to_play == 'potato cat' or 'taco cat' or 'rainbow ralphing cat' or 'beard cat' or 'cattermellon':
        time.sleep(1)

        print("Com 3 has played a " + C3B.card_to_play + " card")

        steal_cat_card(C3B.card_to_play)

        draw_card()

    Game_REWRITE.com1_turn = False
    Game_REWRITE.com3_turn = False
    Game_REWRITE.com3_turn = False
    Game_REWRITE.player_turn = True
