# imports all the modules needed
from tkinter import messagebox
from time import sleep
import Check_Card_Played as CCP
import Com1_Behavior as C1B
import Deal_To_Com_Players as DTCP
import Game_REWRITE
import Deal_To_Com_Players as DTCP
import Check_Card_Drawn as CCD
import Game_REWRITE
import random
import Com2_Behavior as C2B
import WelcomeTEST as wt
 
com1_played_attack = False

# Function makes com 1 draw a card and adds that card to com 1 hands
def draw_card():
    sleep(1)

    # Checks if card 1 is equal to ""
    if DTCP.com1_card1 == "":
        # Checks if com 1 or the player has played a see the future
        if CCP.first_card != " ":
            print(CCP.first_card) # Prints the top card seen from the see the future

            DTCP.com1_card1 = CCP.first_card # Assigns the com 1's card 1 to the drawn card
            DTCP.com1_cards[0] = DTCP.com1_card1 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card1) # Removes the card from the deck

            print(DTCP.com1_cards) # Prints com 1's hand

            CCP.first_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.second_card != " ":
            DTCP.com1_card1 = CCP.second_card # Assigns the com 1's card 1 to the drawn card
            DTCP.com1_cards[0] = DTCP.com1_card1 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card1) # Removes the card from the deck

            CCP.second_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.third_card != " ":
            DTCP.com1_card1 = CCP.third_card # Assigns the com 1's card 1 to the drawn card
            DTCP.com1_cards[0] = DTCP.com1_card1 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card1) # Removes the card from the deck

            CCP.third_card = " " # Assigns the card seen from the see the future to be " "

        else:
            DTCP.com1_card1 = random.choice(Game_REWRITE.cards) # Assigns the com 1's card 1 to a random choice of the draw pile
            print(DTCP.com1_card1) # Prints the drawn card
            DTCP.com1_cards[0] = DTCP.com1_card1 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card1) # Removes the card from the deck

        print(DTCP.com1_cards) # Prints com 1's hand 

    # Checks if card 2 is equal to ""
    elif DTCP.com1_card2 == "":
        # Checks if com 1 or the player has played a see the future
        if CCP.first_card != " ":
            print(CCP.first_card) # Prints the top card seen from the see the future

            DTCP.com1_card2 = CCP.first_card # Assigns the com 1's card 2 to the drawn card
            DTCP.com1_cards[1] = DTCP.com1_card2 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card2) # Removes the card from the deck

            print(DTCP.com1_cards) # Prints com 1's hand

            CCP.first_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.second_card != " ":
            DTCP.com1_card2 = CCP.second_card # Assigns the com 1's card 2 to the drawn card
            DTCP.com1_cards[1] = DTCP.com1_card2 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card2) # Removes the card from the deck

            CCP.second_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.third_card != " ":
            DTCP.com1_card2 = CCP.third_card # Assigns the com 1's card 2 to the drawn card
            DTCP.com1_cards[1] = DTCP.com1_card2 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card2) # Removes the card from the deck

            CCP.third_card = " " # Assigns the card seen from the see the future to be " "

        else:
            DTCP.com1_card2 = random.choice(Game_REWRITE.cards) # Assigns the com 1's card 1 to a random choice of the draw pile
            print(DTCP.com1_card2) # Prints the drawn card
            DTCP.com1_cards[1] = DTCP.com1_card2 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card2) # Removes the card from the deck

        print(DTCP.com1_cards) # Prints com 1's hand

    # Checks if card 3 is equal to ""
    elif DTCP.com1_card3 == "":
        # Checks if com 1 or the player has played a see the future
        if CCP.first_card != " ":
            print(CCP.first_card) # Prints the top card seen from the see the future

            DTCP.com1_card3 = CCP.first_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[2] = DTCP.com1_card3 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card3) # Removes the card from the deck

            print(DTCP.com1_cards) # Prints com 1's hand

            CCP.first_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.second_card != " ":
            DTCP.com1_card3 = CCP.second_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[2] = DTCP.com1_card3 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card3) # Removes the card from the deck

            CCP.second_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.third_card != " ":
            DTCP.com1_card3 = CCP.third_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[2] = DTCP.com1_card3 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card3) # Removes the card from the deck

            CCP.third_card = " " # Assigns the card seen from the see the future to be " "

        else:
            DTCP.com1_card3 = random.choice(Game_REWRITE.cards) # Assigns the com 1's card 1 to a random choice of the draw pile
            print(DTCP.com1_card3) # Prints the drawn card
            DTCP.com1_cards[2] = DTCP.com1_card3 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card3) # Removes the card from the deck

        print(DTCP.com1_cards) # Prints com 1's hand

    # Checks if card 4 is equal to ""
    elif DTCP.com1_card4 == "":
        # Checks if com 1 or the player has played a see the future
        if CCP.first_card != " ":
            print(CCP.first_card) # Prints the top card seen from the see the future

            DTCP.com1_card4 = CCP.first_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[3] = DTCP.com1_card4 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card4) # Removes the card from the deck

            print(DTCP.com1_cards) # Prints com 1's hand

            CCP.first_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.second_card != " ":
            DTCP.com1_card4 = CCP.second_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[3] = DTCP.com1_card4 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card4) # Removes the card from the deck

            CCP.second_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.third_card != " ":
            DTCP.com1_card4 = CCP.third_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[3] = DTCP.com1_card4 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card4) # Removes the card from the deck

            CCP.third_card = " " # Assigns the card seen from the see the future to be " "

        else:
            DTCP.com1_card4 = random.choice(Game_REWRITE.cards) # Assigns the com 1's card 1 to a random choice of the draw pile
            print(DTCP.com1_card4) # Prints the drawn card
            DTCP.com1_cards[3] = DTCP.com1_card4 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card4) # Removes the card from the deck

        print(DTCP.com1_cards) # Prints com 1's hand

    # Checks if card 5 is equal to ""
    elif DTCP.com1_card5 == "":
        # Checks if com 1 or the player has played a see the future
        if CCP.first_card != " ":
            print(CCP.first_card) # Prints the top card seen from the see the future

            DTCP.com1_card5 = CCP.first_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[4] = DTCP.com1_card5 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card5) # Removes the card from the deck

            print(DTCP.com1_cards) # Prints com 1's hand

            CCP.first_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.second_card != " ":
            DTCP.com1_card5 = CCP.second_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[4] = DTCP.com1_card5 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card5) # Removes the card from the deck

            CCP.second_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.third_card != " ":
            DTCP.com1_card5 = CCP.third_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[4] = DTCP.com1_card5 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card5) # Removes the card from the deck

            CCP.third_card = " " # Assigns the card seen from the see the future to be " "

        else:
            DTCP.com1_card5 = random.choice(Game_REWRITE.cards) # Assigns the com 1's card 1 to a random choice of the draw pile
            print(DTCP.com1_card5) # Prints the drawn card
            DTCP.com1_cards[4] = DTCP.com1_card5 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card5) # Removes the card from the deck

        print(DTCP.com1_cards) # Prints com 1's hand

    # Checks if card 6 is equal to ""
    elif DTCP.com1_card6 == "":
        # Checks if com 1 or the player has played a see the future
        if CCP.first_card != " ":
            print(CCP.first_card) # Prints the top card seen from the see the future

            DTCP.com1_card6 = CCP.first_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[5] = DTCP.com1_card6 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card6) # Removes the card from the deck

            print(DTCP.com1_cards) # Prints com 1's hand

            CCP.first_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.second_card != " ":
            DTCP.com1_card6 = CCP.second_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[5] = DTCP.com1_card6 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card6) # Removes the card from the deck

            CCP.second_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.third_card != " ":
            DTCP.com1_card6 = CCP.third_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[5] = DTCP.com1_card6 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card6) # Removes the card from the deck

            CCP.third_card = " " # Assigns the card seen from the see the future to be " "

        else:
            DTCP.com1_card6 = random.choice(Game_REWRITE.cards) # Assigns the com 1's card 1 to a random choice of the draw pile
            print(DTCP.com1_card6) # Prints the drawn card
            DTCP.com1_cards[5] = DTCP.com1_card6 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card6) # Removes the card from the deck

        print(DTCP.com1_cards) # Prints com 1's hand

    # Checks if card 7 is equal to ""
    elif DTCP.com1_card7 == "":
        # Checks if com 1 or the player has played a see the future
        if CCP.first_card != " ":
            print(CCP.first_card) # Prints the top card seen from the see the future

            DTCP.com1_card7 = CCP.first_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[6] = DTCP.com1_card7 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card7) # Removes the card from the deck

            print(DTCP.com1_cards) # Prints com 1's hand

            CCP.first_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.second_card != " ":
            DTCP.com1_card7 = CCP.second_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[6] = DTCP.com1_card7 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card7) # Removes the card from the deck

            CCP.second_card = " " # Assigns the card seen from the see the future to be " "

        # Checks if com 1 or the player has played a see the future
        elif CCP.third_card != " ":
            DTCP.com1_card7 = CCP.third_card # Assigns the com 1's card 3 to the drawn card
            DTCP.com1_cards[6] = DTCP.com1_card7 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card7) # Removes the card from the deck

            CCP.third_card = " " # Assigns the card seen from the see the future to be " "

        else:
            DTCP.com1_card7 = random.choice(Game_REWRITE.cards) # Assigns the com 1's card 1 to a random choice of the draw pile
            print(DTCP.com1_card7) # Prints the drawn card
            DTCP.com1_cards[6] = DTCP.com1_card7 # Assigns the part in the list to the drawn card

            CCD.check_card(DTCP.com1_card7) # Removes the card from the deck

        print(DTCP.com1_cards) # Prints com 1's hand
    
    else:
        print("An error has been encountered") # Prints "An error has been encountered"
        messagebox.showinfo("Exploding Kittens Game", "Com1 has drawn, it's now currently your turn") # Tells the player that com 1 has drawn and that its there turn
        Game_REWRITE.player_turn = True # Makes its the players turn
        Game_REWRITE.com1_turn = False # Makes it not be com 1's turn

    # Checks if the player played an attack card
    if CCP.attack_card_played == True:
        messagebox.showinfo("Exploding Kittens Game", "It is now Com1 turn again because you played a attack card") # Tells the player that it's com 1's turn again because they played an attack card
        CCP.attack_card_played = False # Re-assigns the bollen to be false
        C1B.decied_card_to_play() # Calls the function

    # Checks if the player selected 2 com players
    elif Game_REWRITE.com2_turn == True:
        C2B.decied_card_to_play()

    else:
        messagebox.showinfo("Exploding Kittens Game", "Com1 has drawn, it's now currently your turn") # Tells the player that com 1 has drawn and that it's there turn
        Game_REWRITE.player_turn = True # Makes it the players turns
        Game_REWRITE.com1_turn = False # Makes it not be com 1's turns

    C1B.card_to_play = "" # Assigns card_to_play to ""

# Function adds cards gotten from a favor card or stolen from a cat card combo to com 1's hand
def get_favor_or_stolen_card(card_to_add):
    # Checks if com 1 played there card 1
    if DTCP.com1_card1 == "":
        DTCP.com1_card1 = card_to_add # Assign the played card to the card gotten from a favor or stolen by playing to matching cat cards
        DTCP.com1_cards[0] = DTCP.com1_card1 # Assign the part in the list to card 1

        print(DTCP.com1_cards) # Prints com 1's hand

    # Checks if com 1 played there card 2
    elif DTCP.com1_card2 == "":
        DTCP.com1_card2 = card_to_add # Assign the played card to the card gotten from a favor or stolen by playing to matching cat cards
        DTCP.com1_cards[1] = DTCP.com1_card2 # Assign the part in the list to card 2

        print(DTCP.com1_cards) # Prints com 1's hand

    # Checks if com 1 played there card 3
    elif DTCP.com1_card3 == "":
        DTCP.com1_card3 = card_to_add # Assign the played card to the card gotten from a favor or stolen by playing to matching cat cards
        DTCP.com1_cards[2] = DTCP.com1_card1 # Assign the part in the list to card 3

        print(DTCP.com1_cards) # Prints com 1's hand

    # Checks if com 1 played there card 4
    elif DTCP.com1_card4 == "":
        DTCP.com1_card4 = card_to_add # Assign the played card to the card gotten from a favor or stolen by playing to matching cat cards
        DTCP.com1_cards[3] = DTCP.com1_card1 # Assign the part in the list to card 4

        print(DTCP.com1_cards) # Prints com 1's hand

    # Checks if com 1 played there card 5
    elif DTCP.com1_card5 == "":
        DTCP.com1_card5 = card_to_add # Assign the played card to the card gotten from a favor or stolen by playing to matching cat cards
        DTCP.com1_cards[4] = DTCP.com1_card1 # Assign the part in the list to card 5

        print(DTCP.com1_cards) # Prints com 1's hand

    # Checks if com 1 played there card 6
    elif DTCP.com1_card6 == "":
        DTCP.com1_card6 = card_to_add # Assign the played card to the card gotten from a favor or stolen by playing to matching cat cards
        DTCP.com1_cards[5] = DTCP.com1_card1 # Assign the part in the list to card 6

        print(DTCP.com1_cards) # Prints com 1's hand


    # Checks if com 1 played there card 7
    elif DTCP.com1_card7 == "":
        DTCP.com1_card7 = card_to_add # Assign the played card to the card gotten from a favor or stolen by playing to matching cat cards
        DTCP.com1_cards[6] = DTCP.com1_card1 # Assign the part in the list to card 7

        print(DTCP.com1_cards) # Prints com 1's hand

    else:
        print("An error has been encountered")

# Function lets com 1 play 2 matching cat cards and than steal a card from the player than adds it to there hand
def get_cat_card(com1_cat_card):
    looped_on_card = ""

    # Enters a for loop checking if the card pass through in the argument equals to a card in com 1's hand
    for cards_in_com1_hand in DTCP.com1_cards:
        looped_on_card = cards_in_com1_hand

        # Checks if cards_in_com1_hand is equal to the argument passed
        if cards_in_com1_hand == com1_cat_card:
            print("Theres a match") # Prints Theres a match
            messagebox.showinfo("Exploding Kittens Game", "Com1 has successfully play 2 " + cards_in_com1_hand + " cards") # Tells the player that com 1 has played 2 mathing cat cards

            steal_card = random.choice(Game_REWRITE.player_cards) # Assing a variable to a random choice from the player hand, that will be card com 1 steals from the players hand

            # Enters a while loop if steal_card equals to ""
            while steal_card == "":
                steal_card = random.choice(Game_REWRITE.player_cards) # Re-assigns the variable to a random choice

            get_favor_or_stolen_card(steal_card) # Adds the stolen card to the com 1's hand
            messagebox.showerror("Exploding Kittens Game", "Com1 has stolen your " + steal_card) # Tells the user that com 1 has stolen x card from them
            break # Breaks the for loop
        else:
            print("Theres not currently a match") # Prints Theres not currently a match
    
    print("Looped card is " + looped_on_card)

    # After the loop is compleated and the first cat card that com 1 has played do not have any matching cards in there in there hand
    if looped_on_card != com1_cat_card:
        messagebox.showerror("Exploding Kittens Game", 'Com1 has not successfully played 2 cat cards') # Tells the player that com 1 has failed to play to matching cat cards

# Checks what card com 1 has played so it can do it's respected function
def check_com1_card():
    global com1_played_attack

    print(C1B.card_to_play) # Prints what com 1 has chosen to play

    # Checks if com 1 has played an attack card
    if C1B.card_to_play == "skip":
        sleep(1) # Sleeps the program for 1 second (Makes it like com 1 is choosing a card to play)
        
        # Checks if the player selected 1 com player
        if wt.com_number == 1:
            messagebox.showinfo("Exploding Kittens Game", "Com1 has skip there turn, it is currently your turn") # Tells the player that con 1 has skiped there turn
            Game_REWRITE.discard_pile_text.set(C1B.card_to_play + "\n \n \n") # Changes the display text of the draw pile
            Game_REWRITE.player_turn = True # Sets the players turn to be true
            Game_REWRITE.com1_turn = False # Sets com 1's turn to be false

        # Checks if the player selected 2 or 3 com players
        elif wt.com_number == 2 or 3:
            messagebox.showinfo("Exploding Kittens Game", "Com1 has skip there turn, it is now com 2's turn") # Tells the player that con 1 has skiped there turn
            Game_REWRITE.discard_pile_text.set(C1B.card_to_play + "\n \n \n") # Changes the display text of the draw pile
            Game_REWRITE.com2_turn = True 
            Game_REWRITE.com1_turn = False # Sets com 1's turn to be false

            Game_REWRITE.com2_turn = True
            C2B.decied_card_to_play()

    # Checks if com 1 has played an attack card
    elif C1B.card_to_play == "attack":
        sleep(1) # Sleeps the program for 1 second (Makes it like com 1 is choosing a card to play)
       
        Game_REWRITE.discard_pile_text.set(C1B.card_to_play + "\n \n \n") # Sets the discard text to "attack"
        Game_REWRITE.com1_turn = False # Makes it not be com 1's turn

        # Checks if the player selected 1 com player    
        if wt.com_number == 1:
            Game_REWRITE.com1_turn = False
            Game_REWRITE.player_turn = True
            messagebox.showinfo("Exploding Kittens Game", "Com1 has played an attack. Com1 has skiped there turn\nand made you have 2 turns") # Tells the player that com 1 has played an attack card and made you have 2 turns
            com1_played_attack = True

        # Checks if the player selected 2 or 3 com players
        elif wt.com_number == 2 or 3:
            Game_REWRITE.com2_turn = True
            Game_REWRITE.com1_turn = False 
            com1_played_attack = True
            messagebox.showinfo("Exploding Kittens Game", "Com1 has played an attack. Com1 has skiped there turn\nand made con 2 have 2 turns")
            C2B.decied_card_to_play()
        
    # Checks if com 1 has play a favor card
    elif C1B.card_to_play == "favor":
        sleep(1) # Sleeps the program for 1 second (Makes it like com 1 is choosing a card to play)
        messagebox.showinfo("Exploding Kittens Game", "Com1 has played a favor, click a card to give to them.") # Tells the player that com 1 has played a favor
        Game_REWRITE.discard_pile_text.set(C1B.card_to_play + "\n \n \n") # Sets the discard pile text to the current card that com 1 has played

    # Checks if com 1 has player a shuffle card
    elif C1B.card_to_play == "shuffle":
        sleep(1) # Sleeps the program for 1 second (Makes it like com 1 is choosing a card to play)

        # Shuffles the deck
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)

        messagebox.showinfo("Exploding Kittens Game", "Com1 has shuffled the deck") # Tells the player that com 1 has shuffled the deck

        draw_card() # Makes com 1 draw a card

    # Checks if com 1 has played a see the future card
    elif C1B.card_to_play == "see the future":
        sleep(1) # Sleeps the program for 1 second (Makes it like com 1 is choosing a card to play)

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

        messagebox.showinfo("Exploding Kittens Game", "Com1 has played a see the future") # Tells the player that com 1 has played a see the future card

        Game_REWRITE.discard_pile_text.set(C1B.card_to_play + "\n \n \n") # Sets the text of the discard pile to the card the com 1 has played

        draw_card() # Makes com 1 draw a card

    # Checks if com 1 has played a cat card
    elif C1B.card_to_play == 'potato cat' or 'taco cat' or 'rainbow ralphing cat' or 'beard cat' or 'cattermellon':
        get_cat_card(C1B.card_to_play) # Calls the function and passes the card that com 1 has played as an argument

        draw_card() # Makes com 1 draw a card

    else:
        print("An error has been encountered") # Prints "An error has been encountered"
