# imports all the modals needed 
import random
import tkinter as tk
import WelcomeTEST as WT
import Check_Card_Played as CCP
import Check_Card_Drawn as CCD
import Draw_Pile_Command as DPC
import Deal_To_Com_Players as dtcp
import Com1_Behavior as C1B
from Check_Com1_Card_Played import draw_card, get_favor_or_stolen_card

# Creates the Tk Window
gameScreen = tk.Tk()
gameScreen.title("Exploding Kittens Game") # Renames the windows to: Exploding Kittens Game
gameScreen.geometry("1366x800") # Sets the bg color
gameScreen.configure(bg = '#00FFFF') # Sets the size
gameScreen.resizable(0, 0) # Makes so the window is not resizable

# Creates a list containing all the cards in the game
cards = ['nope', 'attack', \
        'skip', 'favor', 'shuffle', 'see the future', 'potato cat', \
        'taco cat', 'rainbow ralphing \n cat', 'beard cat', 'cattermellon']

# Bollens to check if a card was played
card1_played = False
card2_played = False
card3_played = False
card4_played = False
card5_played = False
card6_played = False
card7_played = False

com1_turn  = False
player_turn = True

reserve_cards = [" ", " ", " ", " ", " ", " ", " ", " "]

# Functions Needed
def exit_app():
    # Exits the app

    MsgBox = tk.messagebox.askquestion ('Exploding Kittens Game','Are you sure you want to exit?', icon = 'warning') # Asks the player if they want to quit
    
    # Checks if the player clicked on "yes"
    if MsgBox == 'yes':
       gameScreen.destroy()
       exit()

def add_to_reserve_cards():
    global player_turn

    # When the player draws, but they played no cards this will fill an empty section in the reserve hand

    # Checks if there is an empty slot in the list 
    if reserve_cards[0] == " ":
        reserve_cards[0] = random.choice(cards) # Assigns the slot a random choice from the cards list

        tk.messagebox.showinfo("Exploding Kittens Game", "Heres your new card: " + reserve_cards[0] + ", it was added to your reserve hand (to access it first play a card then draw)") # Tells the player which card they got
    
    # Checks if there is an empty slot in the list 
    elif reserve_cards[1] == " ":
        reserve_cards[1] = random.choice(cards) # Assigns the slot a random choice from the cards list

        tk.messagebox.showinfo("Exploding Kittens Game", "Heres your new card: " + reserve_cards[1] + ", it was added to your reserve hand (to access it first play a card then draw)") # Tells the player which card they got
    
    # Checks if there is an empty slot in the list 
    elif reserve_cards[2] == " ":
        reserve_cards[2] = random.choice(cards) # Assigns the slot a random choice from the cards list

        tk.messagebox.showinfo("Exploding Kittens Game", "Heres your new card: " + reserve_cards[2] + ", it was added to your reserve hand (to access it first play a card then draw)") # Tells the player which card they got
    
    # Checks if there is an empty slot in the list 
    elif reserve_cards[3] == " ":
        reserve_cards[3] = random.choice(cards) # Assigns the slot a random choice from the cards list

        tk.messagebox.showinfo("Exploding Kittens Game", "Heres your new card: " + reserve_cards[3] + ", it was added to your reserve hand (to access it first play a card then draw)") # Tells the player which card they got
    
    # Checks if there is an empty slot in the list 
    elif reserve_cards[4] == " ":
        reserve_cards[4] = random.choice(cards) # Assigns the slot a random choice from the cards list

        tk.messagebox.showinfo("Exploding Kittens Game", "Heres your new card: " + reserve_cards[4] + ", it was added to your reserve hand (to access it first play a card then draw)") # Tells the player which card they got
    
    # Checks if there is an empty slot in the list  
    elif reserve_cards[5] == " ":
        reserve_cards[5] = random.choice(cards) # Assigns the slot a random choice from the cards list

        tk.messagebox.showinfo("Exploding Kittens Game", "Heres your new card: " + reserve_cards[5] + ", it was added to your reserve hand (to access it first play a card then draw)") # Tells the player which card they got
    
    # Checks if there is an empty slot in the list 
    elif reserve_cards[6] == " ":
        reserve_cards[6] = random.choice(cards) # Assigns the slot a random choice from the cards list

        tk.messagebox.showinfo("Exploding Kittens Game", "Heres your new card: " + reserve_cards[6] + ", it was added to your reserve hand (to access it first play a card then draw)") # Tells the player which card they got
    
    # Checks if there is an empty slot in the list 
    elif reserve_cards[7] == " ":
        reserve_cards[7] = random.choice(cards) # Assigns the slot a random choice from the cards list

        tk.messagebox.showinfo("Exploding Kittens Game", "Heres your new card: " + reserve_cards[7] + ", it was added to your reserve hand (to access it first play a card then draw)") # Tells the player which card they got
    
    else:
        tk.messagebox.showerror("Exploading Kittens Game", "You have to many cards in your reserve hand. You can hold up to 8 cards") # Tells the player that they reached the limit of cards that they can have in there reserve hand

    player_turn = False # Sets the players turn to false

# Card functions
def card1_command():
    global card1_played

    # Checks if its the players turn
    if player_turn == True:
        discard_pile_text.set(CARDS_IN_HAND1 + "\n \n \n") # Sets the discard pile display text to the card that you've played 
        show_card1.destroy() # Destroys the card

        card1_played = True # Sets the bollen from the Game_REWRITE script to True 

        player_cards[0] = "" # Re-Assigns the slot in the list to match that the played card

        CCP.check_card_to_play(CARDS_IN_HAND1) # Checks the card, so it can do its respected function
    
    # Checks if com 1 played a favor
    elif C1B.card_to_play == "favor":
        favoraction = tk.messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND1, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

        # Checks if the player clicked on "yes"
        if favoraction == True:
            tk.messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND1) # Tells the player that there card was add to com 1's hand
            
            card1_played = True  # Makes the bollen False

            C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

            show_card1.destroy() # Destroys the card

            player_cards[0] = "" # Re-Assigns the slot in the list to match that the played card

            draw_card() # Makes com 1 draw a card
        else:
            tk.messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1
    
    else:        
        tk.messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

def card2_command():
    global card2_played

    # Checks if it's  the players turn
    if player_turn == True:
        discard_pile_text.set(CARDS_IN_HAND2 + "\n \n \n") # Sets the discard pile display text to the card that you've played
        show_card2.destroy() # Destroys the card

        card2_played = True # Sets the bollen from the Game_REWRITE script to True 

        player_cards[1] = "" # Assigns the empty slot to the played card

        CCP.check_card_to_play(CARDS_IN_HAND2) # Checks the card, so it can do its respected function

    # Checks if com 1 played a favor
    elif C1B.card_to_play == "favor":
        favoraction = tk.messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND2, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

        # Checks if the player clicked on "yes" 
        if favoraction == True:
            tk.messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND2) # Tells the player that there card was add to com 1's hand
            
            card2_played = True # Sets the bollen from the Game_REWRITE script to True 

            C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

            show_card2.destroy() # Destroys the card

            player_cards[1] = "" # Assigns the empty slot to the gave card

            draw_card() # Makes com 1 draw a card
        else:
            tk.messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

    else:        
        tk.messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

def card3_command():
    global card3_played

    # Checks if it's  the players turn
    if player_turn == True:
        discard_pile_text.set(CARDS_IN_HAND3 + "\n \n \n") # Sets the discard pile display text to the card that you've played
        show_card3.destroy() # Destroys the card

        card3_played = True # Sets the bollen from the Game_REWRITE script to True 

        player_cards[2] = "" # Assigns the empty slot to the played card

        CCP.check_card_to_play(CARDS_IN_HAND3) # Checks the card, so it can do its respected function
    
    # Checks if com 1 played a favor
    elif C1B.card_to_play == "favor":
        favoraction = tk.messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND3, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

        # Asks the player for if they a sure they want to give that card to com 1
        if favoraction == True:
            tk.messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND3) # Tells the player that there card was add to com 1's hand 
            
            card3_played = True # Sets the bollen from the Game_REWRITE script to True 

            C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

            show_card3.destroy() # Destroys the card

            player_cards[2] = "" # Assigns the empty slot to the gave card

            draw_card() # Makes com 1 draw a card
        else:
            tk.messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

    else:        
        tk.messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

def card4_command():
    global card4_played

    # Checks if it's  the players turn
    if player_turn == True:
        discard_pile_text.set(CARDS_IN_HAND4 + "\n \n \n") # Sets the discard pile display text to the card that you've played
        show_card4.destroy() # Destroys the card

        card4_played = True # Sets the bollen from the Game_REWRITE script to True 
        
        player_cards[3] = "" # Assigns the empty slot to the played card

        CCP.check_card_to_play(CARDS_IN_HAND4) # Checks the card, so it can do its respected function
    
    # Checks if com 1 played a favor
    elif C1B.card_to_play == "favor":
        favoraction = tk.messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND4, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

        # Checks if the player clicked on "yes"
        if favoraction == True:
            tk.messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND4) # Tells the player that there card was add to com 1's hand 
            
            card4_played = True # Sets the bollen from the Game_REWRITE script to True 

            C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

            show_card4.destroy() # Destroys the card

            player_cards[3] = "" # Assigns the empty slot to the gave card

            draw_card() # Makes com 1 draw a card
        else:
            tk.messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

    else:        
        tk.messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

def card5_command():
    global card5_played

    # Checks if it's  the players turn
    if player_turn == True:
        discard_pile_text.set(CARDS_IN_HAND5 + "\n \n \n") # Sets the discard pile display text to the card that you've played
        show_card5.destroy() # Destroys the card

        card5_played = True # Sets the bollen from the Game_REWRITE script to True 
        player_cards[4] = "" # Assigns the empty slot to the played card

        CCP.check_card_to_play(CARDS_IN_HAND5) # Checks the card, so it can do its respected function

    # Checks if com 1 played a favor
    elif C1B.card_to_play == "favor":
        favoraction = tk.messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND5, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

        # Checks if the player clicked on "yes" 
        if favoraction == True:
            tk.messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND5) # Tells the player that there card was add to com 1's hand 
            
            card5_played = True # Sets the bollen from the Game_REWRITE script to True 

            C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat
            player_cards[4] = "" # Assigns the empty slot to the gaged card

            show_card5.destroy() # Destroys the card

            draw_card() # Makes com 1 draw a card
        else: 
            tk.messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

    else:        
        tk.messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

def card6_command():
    global card6_played

    # Checks if it's  the players turn
    if player_turn == True: 
        discard_pile_text.set(CARDS_IN_HAND6 + "\n \n \n") # Sets the discard pile display text to the card that you've played

        show_card6.destroy() # Destroys the card

        card6_played = True # Sets the bollen from the Game_REWRITE script to True 

        player_cards[5] = "" # Assigns the empty slot to the played card

        CCP.check_card_to_play(CARDS_IN_HAND6) # Checks the card, so it can do its respected function
        
    # Checks if com 1 played a favor
    elif C1B.card_to_play == "favor":
        favoraction = tk.messagebox.askyesno("Exploding Kittens Game", "Are you sure you want to give com1 your " + CARDS_IN_HAND6, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

        # Checks if the player clicked on "yes"
        if favoraction == True:
            tk.messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND6) # Tells the player that there card was add to com 1's hand 
            
            card6_played = True # Sets the bollen from the Game_REWRITE script to True 

            C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

            show_card6.destroy() # Destroys the card

            player_cards[5] = "" # Assigns the empty slot to the gave card

            draw_card() # Makes com 1 draw a card
        else:
            tk.messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

    else:        
        tk.messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

def card7_command():
    global card7_played

    # Checks if it's  the players turn
    if player_turn == True:
        discard_pile_text.set(CARDS_IN_HAND7 + "\n \n \n") # Sets the discard pile display text to the card that you've played

        show_card7.destroy() # Destroys the card

        card7_played = True # Sets the bollen from the Game_REWRITE script to True 

        player_cards[6] = "" # Assigns the empty slot to the played card

        CCP.check_card_to_play(CARDS_IN_HAND7) # Checks the card, so it can do its respected function

    # Checks if com 1 played a favor
    elif C1B.card_to_play == "favor":
        favoraction = tk.messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND7, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

        # Checks if the player clicked on "yes"
        if favoraction == True:
            tk.messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND7) # Tells the player that there card was add to com 1's hand 
            
            card7_played = True # Sets the bollen from the Game_REWRITE script to True 

            C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

            show_card7.destroy() # Destroys the card

            player_cards[6] = "" # Assigns the empty slot to the given card

            draw_card() # Makes com 1 draw a card
        else:
            tk.messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1
    
    else:
        tk.messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

def show_com_players():
    if WT.com_number == 1:
        display_com_1 = tk.Label(gameScreen, text = "COM 1", font = "15")
        display_com_1.place(y =0, x = 650) 

        dtcp.com1_amount1()
    elif WT.com_number == 2:
        display_com_1 = tk.Label(gameScreen, text = "COM 1", font = "15")
        display_com_1.place(y =400, x = 0)
        display_com_2 = tk.Label(gameScreen, text = "COM 2", font = "15")
        display_com_2.place(y = 400, x = 1300) 

        dtcp.com1_amount2()
        dtcp.com2_amount2()
    elif WT.com_number == 3:
        display_com_1 = tk.Label(gameScreen, text = "COM 1", font = "15")
        display_com_1.place(y =400, x = 0) 
        display_com_2 = tk.Label(gameScreen, text = "COM 2", font = "15")
        display_com_2.place(y = 0, x = 650)
        display_com_3 = tk.Label(gameScreen, text = "COM 3", font = "15")
        display_com_3.place(y = 400, x = 1300) 
         
        dtcp.com1_amount3()
        dtcp.com2_amount3()
        dtcp.com3_amount3()

## Shows username
usernameLabel = tk.Label(gameScreen, text = WT.username, font = "15")
usernameLabel.place(x = 650, y = 660)

show_com_players()

## Chose + Show cards       
CARDS_IN_HAND1 = random.choice(cards)
# CARDS_IN_HAND1 = "attack"
CCD.check_card(CARDS_IN_HAND1) # Checks the card drawn

CARDS_IN_HAND2 = random.choice(cards)
CCD.check_card(CARDS_IN_HAND2) # Checks the card drawn

CARDS_IN_HAND3 = random.choice(cards)
CCD.check_card(CARDS_IN_HAND3) # Checks the card drawn

CARDS_IN_HAND4 = random.choice(cards)
CCD.check_card(CARDS_IN_HAND4) # Checks the card drawn

CARDS_IN_HAND5 = random.choice(cards)
CCD.check_card(CARDS_IN_HAND5) # Checks the card drawn

CARDS_IN_HAND6 = random.choice(cards)
CCD.check_card(CARDS_IN_HAND6) # Checks the card drawn 

CARDS_IN_HAND7 = random.choice(cards)
CCD.check_card(CARDS_IN_HAND7) # Checks the card drawn

# Creates a list containing all player cards
player_cards = [CARDS_IN_HAND1, CARDS_IN_HAND2, CARDS_IN_HAND3, CARDS_IN_HAND4, CARDS_IN_HAND5, CARDS_IN_HAND6, CARDS_IN_HAND7]

## Shows cards in tk window  
show_card1 = tk.Button(gameScreen, text = CARDS_IN_HAND1, font = "20", command = card1_command)
show_card1.place(x = 650, y = 600)

show_card2 = tk.Button(gameScreen, text = CARDS_IN_HAND2, font = "20", command = card2_command)
show_card2.place(x = 810, y = 600)

show_card3 = tk.Button(gameScreen, text = CARDS_IN_HAND3, font = "20", command = card3_command)
show_card3.place(x = 960, y = 600)

show_card4 = tk.Button(gameScreen, text = CARDS_IN_HAND4, font = "20", command  = card4_command)
show_card4.place(x = 1090, y = 600)

show_card5 = tk.Button(gameScreen, text = CARDS_IN_HAND5, font = "20", command = card5_command)
show_card5.place(x = 170, y = 600)

show_card6 = tk.Button(gameScreen, text = CARDS_IN_HAND6, font = "20", command = card6_command)
show_card6.place(x = 330, y = 600)

show_card7 = tk.Button(gameScreen, text = CARDS_IN_HAND7, font = "20", command = card7_command)
show_card7.place(x = 490, y = 600)

## Shows draw and discard piles
draw_pile = tk.Button(gameScreen, text = "Draw \n \n Pile", font = "Arial 50" , bg  = "red", command = DPC.draw_card)
draw_pile.place(x = 400, y = 200)

discard_pile_text = tk.StringVar()
discard_pile = tk.Label(gameScreen, textvariable = discard_pile_text, font = "Arial 30", bg  = "red")
discard_pile.place(x = 800, y = 200)
discard_pile_text.set("Discard \n \n Text")

# Quit button
quit_button = tk.Button(gameScreen, text = "QUIT", command = exit_app)
quit_button.place(x = 0, y = 0)

tk.messagebox.showinfo("Exploding Kittens Game", "It is currently your turn.")

gameScreen.mainloop()
