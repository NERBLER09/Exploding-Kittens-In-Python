import Game_REWRITE
from tkinter import messagebox
import Deal_To_Com_Players as DTCP
import random

# Function to removes the card com 2 played from there hands
def get_rid_of_card(card_to_remove):
    if card_to_remove == DTCP.com3_card1:
        DTCP.com3_card1 = "" 
        DTCP.com3_cards[0] = DTCP.com3_card1 

    elif card_to_remove == DTCP.com3_card2:
        DTCP.com3_card2 = "" 
        DTCP.com3_cards[1] = DTCP.com3_card2 

    elif card_to_remove == DTCP.com3_card3:
        DTCP.com3_card3 = ""
        DTCP.com3_cards[2] = DTCP.com3_card3

    elif card_to_remove == DTCP.com3_card4:
        DTCP.com3_card4 = "" 
        DTCP.com3_cards[3] = DTCP.com3_card4 

    elif card_to_remove == DTCP.com3_card5:
        DTCP.com3_card5 = "" 
        DTCP.com3_cards[4] = DTCP.com3_card5 

    elif card_to_remove == DTCP.com3_card6:
        DTCP.com3_card6 = ""
        DTCP.com3_cards[5] = DTCP.com3_card6

    elif card_to_remove == DTCP.com3_card7:
        DTCP.com3_card7 = "" 
        DTCP.com3_cards[6] = DTCP.com3_card7 

    else:
        print("An error has been encountered")

    print("Com 2's hand after remove: " + str(DTCP.com3_cards))

# Main function that decides the card com 3 should play
def decied_card_to_play():
    if Game_REWRITE.com3_turn == True:
        messagebox.showinfo("Exploding Kittens Game", "It is currently com 3's turn.")

        print("Com 3's hand: " + str(DTCP.com3_cards))

        card_to_play = random.choice(DTCP.com3_cards)

        print("Card Com 3's going to play " + str(card_to_play))
