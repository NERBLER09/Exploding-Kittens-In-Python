# Imports all the modules needed 
import Game_REWRITE
from tkinter import messagebox
import Deal_To_Com_Players as DTCP
import Check_Com2_Card_Played as CC2CP
import random

card_to_play = ""

# Function to removes the card com 2 played from there hands
def get_rid_of_card(card_to_remove):
    if card_to_remove == DTCP.com2_card1:
        DTCP.com2_card1 = "" 
        DTCP.com2_cards[0] = DTCP.com2_card1 

    elif card_to_remove == DTCP.com2_card2:
        DTCP.com2_card2 = "" 
        DTCP.com2_cards[1] = DTCP.com2_card2 

    elif card_to_remove == DTCP.com2_card3:
        DTCP.com2_card3 = ""
        DTCP.com2_cards[2] = DTCP.com2_card3

    elif card_to_remove == DTCP.com2_card4:
        DTCP.com2_card4 = "" 
        DTCP.com2_cards[3] = DTCP.com2_card4 

    elif card_to_remove == DTCP.com2_card5:
        DTCP.com2_card5 = "" 
        DTCP.com2_cards[4] = DTCP.com2_card5 

    elif card_to_remove == DTCP.com2_card6:
        DTCP.com2_card6 = ""
        DTCP.com2_cards[5] = DTCP.com2_card6

    elif card_to_remove == DTCP.com2_card7:
        DTCP.com2_card7 = "" 
        DTCP.com2_cards[6] = DTCP.com2_card7 

    else:
        print("An error has been encountered")

    print("Com 2's hand after remove: " + str(DTCP.com2_cards))

# Function to check the card com 2 is going to play to check that there not playing an already played card
def check_card_to_play(card_to_check):
    global card_to_play

    if card_to_check == "":
        card_to_play = random.choice(DTCP.com2_cards)

        print(card_to_play)

        check_card_to_play(card_to_play)
    
    elif card_to_check == "nope":
        card_to_play = random.choice(DTCP.com2_cards)

        print(card_to_play)

        check_card_to_play(card_to_play)


# Main function that decides the card com 2 should play
def decied_card_to_play():
    global card_to_play

    if Game_REWRITE.com2_turn == True:
        messagebox.showinfo("Exploding Kittens Game", "It is currently com 2's turn.")

        print("Com 2's Hand: " + str(DTCP.com2_cards))

        card_to_play = random.choice(DTCP.com2_cards)

        print(card_to_play)

        get_rid_of_card(card_to_play)

        CC2CP.check_card_played()
