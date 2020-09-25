import time
import Game_REWRITE
import Com2_Behavior as C2B
import Check_Card_Played as CCP
import Deal_To_Com_Players as DTCP
import Check_Card_Drawn as CCD
import random
from tkinter import messagebox

# Function makes com 2 draw a card and adds that card to there hand
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
        DTCP.com2_cards[2] = DTCP.com2_card3

        messagebox.showinfo("Exploding Kittens Game", "Com 2 has drawn, it's now currently your turn") 
        Game_REWRITE.player_turn = True 
        Game_REWRITE.com1_turn = False
        Game_REWRITE.com2_turn = False

        CCD.check_card(DTCP.com2_cards)

    # Checks if DTCP.com2_card4 is equal to ""
    elif DTCP.com2_card4 == "":
        DTCP.com2_card4 = random.choice(Game_REWRITE.cards)
        DTCP.com2_cards[3] = DTCP.com2_card4

        messagebox.showinfo("Exploding Kittens Game", "Com 2 has drawn, it's now currently your turn") 
        Game_REWRITE.player_turn = True 
        Game_REWRITE.com1_turn = False
        Game_REWRITE.com2_turn = False

    # Checks if DTCP.com2_card5 is equal to ""
    elif DTCP.com2_card5 == "":
        DTCP.com2_card5 = random.choice(Game_REWRITE.cards)
        DTCP.com2_cards[4] = DTCP.com2_card5

        messagebox.showinfo("Exploding Kittens Game", "Com 2 has drawn, it's now currently your turn") 
        Game_REWRITE.player_turn = True 
        Game_REWRITE.com1_turn = False
        Game_REWRITE.com2_turn = False

        CCD.check_card(DTCP.com2_cards)
    
    # Checks if DTCP.com2_card6 is equal to ""
    elif DTCP.com2_card6 == "":
        DTCP.com2_card6 = random.choice(Game_REWRITE.cards)
        DTCP.com2_cards[5] = DTCP.com2_card5

        messagebox.showinfo("Exploding Kittens Game", "Com 2 has drawn, it's now currently your turn") 
        Game_REWRITE.player_turn = True 
        Game_REWRITE.com1_turn = False
        Game_REWRITE.com2_turn = False

        CCD.check_card(DTCP.com2_cards)

    # Checks if DTCP.com2_card7 is equal to ""
    elif DTCP.com2_card7 == "":
        DTCP.com2_card7 = random.choice(Game_REWRITE.cards)
        DTCP.com2_cards[6] = DTCP.com2_card5

        messagebox.showinfo("Exploding Kittens Game", "Com 2 has drawn, it's now currently your turn") 
        Game_REWRITE.player_turn = True 
        Game_REWRITE.com1_turn = False
        Game_REWRITE.com2_turn = False

        CCD.check_card(DTCP.com2_cards)

    print("After Drawn: " + str(DTCP.com2_cards))

# Function adds the card gotten from a favor or a card stolen from a cat card to there hand
def add_favor_or_stolen_card(card_to_add):
    # TODO Add rest of code in if/elif/else statements

    # Adds the card to there 1st card slot
    if DTCP.com2_card1 == "":
        pass

    # Adds the card to there 2st card slot
    elif DTCP.com2_card2 == "":
        pass

    # Adds the card to there 3st card slot
    elif DTCP.com2_card3 == "":
        pass

    # Adds the card to there 3st card slot
    elif DTCP.com2_card3 == "":
        pass

    # Adds the card to there 4st card slot
    elif DTCP.com2_card4 == "":
        pass

    # Adds the card to there 5st card slot
    elif DTCP.com2_card5 == "":
        pass

    # Adds the card to there 6st card slot
    elif DTCP.com2_card6 == "":
        pass

    # Adds the card to there 7st card slot
    elif DTCP.com2_card7 == "":
        pass

    else:
        print("An error has been encountered.")

# Function lets com 2 play 2 matching cat cards and than steal a card from the player or com 2, than adds it to there hand
def get_cat_card(com2_cat_card):
    # Enters a for loop checking if the card pass through in the argument equals to a card in com 2's hand
    for cards_in_com2_hand in DTCP.com2_cards:
        # Checks if cards_in_com1_hand is equal to the argument passed
        if cards_in_com2_hand == com2_cat_card:
            print("Theres a match")
            messagebox.showinfo("Exploding Kittens Game", "Com 2 has successfully play 2 " + cards_in_com2_hand + " cards")

            steal_card = random.choice(Game_REWRITE.player_cards) # Assing a variable to a random choice from the player hand, that will be card com 2 steals

            # Enters a while loop if steal_card equals to ""
            while steal_card == "":
                steal_card = random.choice(Game_REWRITE.player_cards)

            # TODO Make com 2 add stolen card to there hand
            messagebox.showerror("Exploding Kittens Game", "Com 2 has stolen your " + steal_card) # Tells the user that com 1 has stolen x card from them
            break
        
        # Prints if there is no current match 
        else:
            print("Theres not currently a match")

    # Tells the played that com 2 hasn't played 2 matching cat cards
    if cards_in_com2_hand != com2_cat_card:
        messagebox.showerror("Exploding Kittens Game", 'Com 1 has not successfully played 2 cat cards')

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

        get_cat_card(C2B.card_to_play)

        draw_card()

    # TODO Update com 2 to draw card

    Game_REWRITE.player_turn = True

    messagebox.showinfo("Exploding Kittens Game", "It's now currently your turn.")
