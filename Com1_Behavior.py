# imports all the modules needed
import Game_REWRITE
import Deal_To_Com_Players as DTCP
import random
import Check_Com1_Card_Played as CC1CP
from tkinter import messagebox

# Creates a string to house the card com 1 is going to play
card_to_play = ""
  
# Function to removes the card com 1 played from there hands
def get_rid_of_card():
    print("Card to remove from com 1's hand " + card_to_play)

    # Checks if the card that com 1 is going to play is equal to com 1 card 1
    if card_to_play == DTCP.com1_cards[0]:
        DTCP.com1_card1 = "" # Makes the card equal to an empty string
        DTCP.com1_cards[0] = DTCP.com1_card1 # Makes the slot equal to the com 1 card 2

    # Checks if the card that com 1 is going to play is equal to com 1 card 2
    elif card_to_play == DTCP.com1_cards[1]:
        DTCP.com1_card2 = "" # Makes the card equal to an empty string
        DTCP.com1_cards[1] = DTCP.com1_card2 # Makes the slot equal to the com 1 card 1

    # Checks if the card that com 1 is going to play is equal to com 1 card 3
    elif card_to_play == DTCP.com1_cards[2]:
        DTCP.com1_card3 = "" # Makes the card equal to an empty string
        DTCP.com1_cards[2] = DTCP.com1_card3 # Makes the slot equal to the com 1 card 3

    # Checks if the card that com 1 is going to play is equal to com 1 card 4
    elif card_to_play == DTCP.com1_cards[3]:
        DTCP.com1_card4 = "" # Makes the card equal to an empty string
        DTCP.com1_cards[3] = DTCP.com1_card4 # Makes the slot equal to the com 1 card 4

    # Checks if the card that com 1 is going to play is equal to com 1 card 5
    elif card_to_play == DTCP.com1_cards[4]:
        DTCP.com1_card5 = "" # Makes the card equal to an empty string
        DTCP.com1_cards[4] = DTCP.com1_card5 # Makes the slot equal to the com 1 card 5

    # Checks if the card that com 1 is going to play is equal to com 1 card 6
    elif card_to_play == DTCP.com1_cards[5]:
        DTCP.com1_card6 = "" # Makes the card equal to an empty string
        DTCP.com1_cards[5] = DTCP.com1_card6 # Makes the slot equal to the com 1 card

    # Checks if the card that com 1 is going to play is equal to com 1 card 7
    elif card_to_play == DTCP.com1_cards[6]:
        DTCP.com1_card7 = "" # Makes the card equal to an empty string
        DTCP.com1_cards[6] = DTCP.com1_card7 # Makes the slot equal to the com 1 card

    else:
        print("An error has been encountered") # Prints An error has been encountered

    print(DTCP.com1_cards)

# Function to check the card com 1 is going to play to check that there not playing an already played card
def check_card_to_play(card_to_check):
    global card_to_play

    # Checks if the passed augment is equal to ""
    if card_to_check == "":
        card_to_play = random.choice(DTCP.com1_cards) # Assigns the card that com 1 is going to play from a random choice from com 1 cards

        print(card_to_play) # Prints com 1's cards

        check_card_to_play(card_to_play) # Checks the card that com 1 is going to play so it doesn't play an already played card

    # Checks if com 1 is going to play a nope card
    elif card_to_check == "nope":
        card_to_play = random.choice(DTCP.com1_cards) # Assigns the card that com 1 is going to play from a random choice from com 1 cards

        print(card_to_play) # Prints com 1's cards

        check_card_to_play(card_to_play) # Checks the card that com 1 is going to play so it doesn't play an already played card

# Main function that decides the card com 1 should play
def decied_card_to_play():
    global card_to_play

    # Checks if it's com 1's turn
    if Game_REWRITE.com1_turn == True:
        messagebox.showinfo("Exploding Kittens Game", "It is currently com1's turn.") # Tells the player that it's com 1's turn

        print(DTCP.com1_cards) # Prints com 1's cards

        card_to_play = random.choice(DTCP.com1_cards) # Assigns the card that com 1 is going to play from a random choice from com 1 cards

        print(card_to_play) # Prints the card com 1 is going to play

        check_card_to_play(card_to_play) # Checks the card that com 1 is going to play so it doesn't play an already played card

        get_rid_of_card() # Gets rid the card from com 1's hand

        CC1CP.check_com1_card() # Checks the card to for the respected function
