# Imports all the modules needed
import random
import Game_REWRITE
import Check_Card_Played as CCP
import Check_Card_Drawn as CCD
import tkinter as tk
from tkinter import messagebox

# Sets up a variables needed 
com1_card1 = ""
com1_card2 = ""
com1_card3 = ""
com1_card4 = ""
com1_card5 = ""
com1_card6 = ""
com1_card7 = ""

com2_card1 = ""
com2_card2 = ""
com2_card3 = ""
com2_card4 = ""
com2_card5 = ""
com2_card6 = ""
com2_card7 = ""

com3_card1 = ""
com3_card2 = ""
com3_card3 = ""
com3_card4 = ""
com3_card5 = ""
com3_card6 = ""
com3_card7 = ""

com1_cards = [" ", " ", " ", " ", " ", " ", " "]
com2_cards = [" ", " ", " ", " ", " ", " ", " "]
com3_cards = [" ", " ", " ", " ", " ", " ", " "]

# Creates a function to be used when the player clicked on one of the com player cards
def com_card_command(com_card, com_player):
    # Checks if the player played two mathing cards and that the player targeted com 1 and that they clicked on one of com 1 cards
    if CCP.cat_combo == True and CCP.message_box2 == "1" and com_player == "com1":
        messagebox.showinfo("Cat Cards", "You stole com 1's: " + com_card + " card") # Tells the player which card they stole
        CCP.cat_combo = False # Makes so the the player hasn't played 2 matching cat cards
        CCP.displayed_stolen_card(com_card) # Displays the card that the played stole in there hands

    # Checks if the player played two mathing cards and that the player targeted com 2 and that they clicked on one of com 2 cards
    if CCP.cat_combo == True and CCP.message_box2 == "2" and com_player == "com2":
        messagebox.showinfo("Cat Cards", "You got a " + com_card) # Tells the player which card they stole
        CCP.cat_combo = False # Makes so the the player hasn't played 2 matching cat cards
        CCP.displayed_stolen_card(com_card) # Displays the card that the played stole in there hands
 
    # Checks if the player played two mathing cards and that the player targeted com 3 and that they clicked on one of com 3 cards
    if CCP.cat_combo == True and CCP.message_box2 == "3" and com_player == "com3":
        messagebox.showinfo("Cat Cards", "You got a " + com_card) # Tells the player which card they stole
        CCP.cat_combo = False # Makes so the the player hasn't played 2 matching cat cards
        CCP.displayed_stolen_card(com_card) # Displays the card that the played stole in there hands
 
    # Checks if the player played two mathing cards and that they clicked on one of com 1 cards
    if CCP.cat_combo == True and com_player == "com1":
        messagebox.showinfo("Cat Cards", "You got a " + com_card) # Tells the player which card they stole
        CCP.cat_combo = False # Makes so the the player hasn't played 2 matching cat cards
        CCP.displayed_stolen_card(com_card) # Displays the card that the played stole in there hands

    # Checks if the player played 2 matching card, but clicked under com 2 or 3 insted of com 1
    if CCP.cat_combo == True and CCP.message_box2 == "1" and com_player == "com2" and com_player == "com3":
        messagebox.showerror("Cat Cards","You have clicked under the wrong com player, try again") # Tells the player that they clicked under the wrong com player and to try again

    # Checks if the player played 2 matching card, but clicked under com 1 or 3 insted of com 2
    if CCP.cat_combo == True and CCP.message_box2 == "2" and com_player == "com1" and com_player == "com3":
        messagebox.showerror("Cat Cards", "You have clicked under the wrong com player") # Tells the player that they clicked under the wrong com player and to try again

    # Checks if the player played 2 matching card, but clicked under com 1 or 2 insted of com 3
    if CCP.cat_combo == True and CCP.message_box2 == "3" and com_player == "com2" and com_player == "com1":
        messagebox.showerror("Cat Cards","You have clicked under the wrong com player") # Tells the player that they clicked under the wrong com player and to try again

    # Checks if the player hasn't played 2 matching cards
    if CCP.cat_combo == False:
        messagebox.showerror("Cat Cards", "You have not played a cat card combo") # Tells the player that they have not played 2 matching cat cards

# Creates a function to be called if the player only selected 1 com player
def com1_amount1():
    global com1_cards, com1_card1, com1_card2, com1_card3, com1_card4, com1_card5, com1_card6, com1_card7

    # Draws com 1's card and checks the card that was drawn 
    com1_card1 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card1)

    com1_card2 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card2)
    
    com1_card3 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card3)
    
    com1_card4 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card4)
    
    com1_card5 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card5)
        
    com1_card6 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card6)

    com1_card7 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card7)

    # Assigns the parts in the com1_cards list to the matching card drawn
    com1_cards[0] = com1_card1
    com1_cards[1] = com1_card2
    com1_cards[2] = com1_card3
    com1_cards[3] = com1_card4
    com1_cards[4] = com1_card5
    com1_cards[5] = com1_card6
    com1_cards[6] = com1_card7

    # Creates and displays com 1's cards
    show_com1_card1 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card1, "com1"))
    show_com1_card1.place(y =30, x = 650) # Creates and places the card at x = 650, y = 30 
    show_com1_card2 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card2, "com1"))
    show_com1_card2.place(y =30, x = 810) # Creates and places the card at x = 810, y = 30 
    show_com1_card3 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card3, "com1"))
    show_com1_card3.place(y =30, x = 980) # Creates and places the card at x = 980, y = 30 
    show_com1_card4 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card4, "com1"))
    show_com1_card4.place(y =30, x = 1090) # Creates and places the card at x = 1090, y = 30 
    show_com1_card5 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card5, "com1"))
    show_com1_card5.place(y =30, x = 170) # Creates and places the card at x = 170, y = 30 
    show_com1_card6 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card6, "com1"))
    show_com1_card6.place(y =30, x = 330) # Creates and places the card at x = 330, y = 30 
    show_com1_card7 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card7, "com1"))
    show_com1_card7.place(y =30, x = 490) # Creates and places the card at x = 490, y = 30 

# Creates a function to be called if the player selected 2 com players
def com1_amount2():
    # Draws com 1's card and checks the card that was drawn 
    com1_card1 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card1)

    com1_card2 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card2)
    
    com1_card3 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card3)
    
    com1_card4 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card4)
    
    com1_card5 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card5)
    
    com1_card6 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card6)
    
    com1_card7 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card7)

    # Assigns the parts in the com1_cards list to the matching card drawn
    com1_cards[0] = com1_card1
    com1_cards[1] = com1_card2
    com1_cards[2] = com1_card3
    com1_cards[3] = com1_card4
    com1_cards[4] = com1_card5
    com1_cards[5] = com1_card6
    com1_cards[6] = com1_card7

    # Creates and displays com 1's cards
    show_com1_card1 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card1, "com1"))
    show_com1_card1.place(y =420, x = 80) # Creates and places the card at x = 80, y = 420
    show_com1_card2 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card2, "com1"))
    show_com1_card2.place(y =470, x = 80) # Creates and places the card at x = 80, y = 470 
    show_com1_card3 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card3, "com1"))
    show_com1_card3.place(y =520, x = 80) # Creates and places the card at x = 80, y = 520
    show_com1_card4 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card4, "com1"))
    show_com1_card4.place(y =570, x = 80) # Creates and places the card at x = 80, y = 570
    show_com1_card5 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card5, "com1"))
    show_com1_card5.place(y =270, x = 80) # Creates and places the card at x = 80, y = 270
    show_com1_card6 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card6, "com1"))
    show_com1_card6.place(y =320, x = 80) # Creates and places the card at x = 80, y = 320
    show_com1_card7 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card7, "com1"))
    show_com1_card7.place(y =370, x = 80) # Creates and places the card at x = 80, y = 370

# Creates a function to be called if the player selected all com players
def com1_amount3():
    # Draws com 1's card and checks the card that was drawn 
    com1_card1 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card1)

    com1_card2 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card2)
    
    com1_card3 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card3)
    
    com1_card4 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card4)
    
    com1_card5 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card5)
    
    com1_card6 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card6)
    
    com1_card7 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com1_card7)

    # Assigns the parts in the com1_cards list to the matching card drawn
    com1_cards[0] = com1_card1
    com1_cards[1] = com1_card2
    com1_cards[2] = com1_card3
    com1_cards[3] = com1_card4
    com1_cards[4] = com1_card5
    com1_cards[5] = com1_card6
    com1_cards[6] = com1_card7

    # Creates and displays com 1's cards
    show_com1_card1 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card1, "com1"))
    show_com1_card1.place(y =420, x = 80) # Creates and places the card at x = 80, y = 420
    show_com1_card2 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card2, "com1"))
    show_com1_card2.place(y =470, x = 80) # Creates and places the card at x = 80, y = 470 
    show_com1_card3 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card3, "com1"))
    show_com1_card3.place(y =520, x = 80) # Creates and places the card at x = 80, y = 520
    show_com1_card4 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card4, "com1"))
    show_com1_card4.place(y =570, x = 80) # Creates and places the card at x = 80, y = 570
    show_com1_card5 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card5, "com1"))
    show_com1_card5.place(y =270, x = 80) # Creates and places the card at x = 80, y = 270
    show_com1_card6 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card6, "com1"))
    show_com1_card6.place(y =320, x = 80) # Creates and places the card at x = 80, y = 320
    show_com1_card7 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card7, "com1"))
    show_com1_card7.place(y =370, x = 80) # Creates and places the card at x = 80, y = 370

# Creates a function to be called if the player selected 2 com players
def com2_amount2():
    global com2_card1, com2_card2, com2_card3, com2_card4, com2_card5, com2_card6, com2_card7, com2_cards

    # Draws com 2's card and checks the card that was drawn
    com2_card1 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card1)

    com2_card2 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card2)
    
    com2_card3 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card3)
    
    com2_card4 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card4)
    
    com2_card5 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card5)
    
    com2_card6 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card6)
    
    com2_card7 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card7)

    # Assigns the parts in the com1_cards list to the matching card drawn
    com2_cards[0] = com2_card1
    com2_cards[1] = com2_card2
    com2_cards[2] = com2_card3
    com2_cards[3] = com2_card4
    com2_cards[4] = com2_card5
    com2_cards[5] = com2_card6
    com2_cards[6] = com2_card7

    # Creates and displays com 2's cards
    show_com2_card1 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card1, "com2"))
    show_com2_card1.place(y =420, x = 1210) # Creates and places the card at x = 1210, y = 420
    show_com2_card2 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card2, "com2"))
    show_com2_card2.place(y =470, x = 1210) # Creates and places the card at x = 1210, y = 470
    show_com2_card3 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card3, "com2"))
    show_com2_card3.place(y =520, x = 1210) # Creates and places the card at x = 1210, y = 520
    show_com2_card4 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card4, "com2"))
    show_com2_card4.place(y =570, x = 1210) # Creates and places the card at x = 1210, y = 570
    show_com2_card5 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card5, "com2"))
    show_com2_card5.place(y =270, x = 1210) # Creates and places the card at x = 1210, y = 270
    show_com2_card6 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card6, "com2"))
    show_com2_card6.place(y =320, x = 1210) # Creates and places the card at x = 1210, y = 320
    show_com2_card7 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card7, "com2"))
    show_com2_card7.place(y =370, x = 1210) # Creates and places the card at x = 1210, y = 370

# Creates a function to be called if the player selected all com players
def com2_amount3():
    # Draws com 2's card and checks the card that was drawn
    com2_card1 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card1)

    com2_card2 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card2)
    
    com2_card3 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card3)
    
    com2_card4 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card4)
    
    com2_card5 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card5)
    
    com2_card6 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card6)
    
    com2_card7 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com2_card7)

    # Assigns the parts in the com1_cards list to the matching card drawn
    com2_cards[0] = com2_card1
    com2_cards[1] = com2_card2
    com2_cards[2] = com2_card3
    com2_cards[3] = com2_card4
    com2_cards[4] = com2_card5
    com2_cards[5] = com2_card6
    com2_cards[6] = com2_card7

    # Creates and displays com 2's cards
    show_com2_card1 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card1, "com1"))
    show_com2_card1.place(y =30, x = 650) # Creates and places the card at x = 650, y = 30 
    show_com2_card2 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card2, "com1"))
    show_com2_card2.place(y =30, x = 810) # Creates and places the card at x = 810, y = 30 
    show_com2_card3 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card3, "com1"))
    show_com2_card3.place(y =30, x = 980) # Creates and places the card at x = 980, y = 30 
    show_com2_card4 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card4, "com1"))
    show_com2_card4.place(y =30, x = 1090) # Creates and places the card at x = 1090, y = 30 
    show_com2_card5 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card5, "com1"))
    show_com2_card5.place(y =30, x = 170) # Creates and places the card at x = 170, y = 30 
    show_com2_card6 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card6, "com1"))
    show_com2_card6.place(y =30, x = 330) # Creates and places the card at x = 330, y = 30 
    show_com2_card7 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com1_card7, "com1"))
    show_com2_card7.place(y =30, x = 490) # Creates and places the card at x = 490, y = 30 

# Creates a function to be called if the player selected all com players
def com3_amount3():
    # Draws com 3's card and checks the card that was drawn 
    com3_card1 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com3_card1)

    com3_card2 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com3_card2)
    
    com3_card3 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com3_card3)
    
    com3_card4 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com3_card4)
    
    com3_card5 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com3_card5)
    
    com3_card6 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com3_card6)

    com3_card7 = random.choice(Game_REWRITE.cards)
    CCD.check_card(com3_card7)

    # Assigns the parts in the com1_cards list to the matching card drawn
    com3_cards[0] = com3_card1
    com3_cards[1] = com3_card2
    com3_cards[2] = com3_card3
    com3_cards[3] = com3_card4
    com3_cards[4] = com3_card5
    com3_cards[5] = com3_card6
    com3_cards[6] = com3_card7

    # Creates and displays com 's cards
    show_com3_card1 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card1, "com3"))
    show_com3_card1.place(y =420, x = 1210) # Creates and places the card at x = 1210, y = 420
    show_com3_card2 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card2, "com3"))
    show_com3_card2.place(y =470, x = 1210) # Creates and places the card at x = 1210, y = 470
    show_com3_card3 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card3, "com3"))
    show_com3_card3.place(y =520, x = 1210) # Creates and places the card at x = 1210, y = 520
    show_com3_card4 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card4, "com3"))
    show_com3_card4.place(y =570, x = 1210) # Creates and places the card at x = 1210, y = 570
    show_com3_card5 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card5, "com3"))
    show_com3_card5.place(y =270, x = 1210) # Creates and places the card at x = 1210, y = 270
    show_com3_card6 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card6, "com3"))
    show_com3_card6.place(y =320, x = 1210) # Creates and places the card at x = 1210, y = 320
    show_com3_card7 = tk.Button(Game_REWRITE.gameScreen, text = "     ", font = "15", command = lambda: com_card_command(com2_card7, "com3"))
    show_com3_card7.place(y =370, x = 1210) # Creates and places the card at x = 1210, y = 370
