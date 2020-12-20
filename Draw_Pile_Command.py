# Imports all the modules needed
import Game_REWRITE
import Check_Card_Played as CCP
import Check_Card_Drawn as CCD
import Com1_Behavior as C1B
import Com2_Behavior as C2B
import Com3_Behavior as C3B
import WelcomeTEST as wt
import tkinter as tk
import random
from tkinter import messagebox
import Check_Com2_Card_Played as CC2CP
import Check_Com1_Card_Played as CC1CP
import Check_Com3_Card_Played as CC3CP

# Function draws the player a card
def draw_card():
    drawn_card = "" # Creates A String To Store The Drawn Card

    # Checks if it's the players turn and that they played one or more of there cards
    if Game_REWRITE.player_turn == True and Game_REWRITE.card1_played == True or Game_REWRITE.card2_played == True or Game_REWRITE.card1_played == True or Game_REWRITE.card3_played == True or \
    Game_REWRITE.card1_played == True or Game_REWRITE.card4_played == True or Game_REWRITE.card5_played == True or Game_REWRITE.card6_played == True or Game_REWRITE.card7_played == True:

        # Checks if there is a card is the position in the list
        if Game_REWRITE.reserve_cards[0] != " ":
            drawn_card = Game_REWRITE.reserve_cards[0] # Sets the draw_card variable to the card in the list position
            Game_REWRITE.reserve_cards[0] = " " # Sets the section in the list to be an empty string

        # Checks if there is a card is the slot in the list
        elif Game_REWRITE.reserve_cards[1] != " ":
            drawn_card = Game_REWRITE.reserve_cards[1] # Sets the draw_card variable to the card in the list position
            Game_REWRITE.reserve_cards[1] = " " # Sets the section in the list to be an empty string

        # Checks if there is a card is the slot in the list
        elif Game_REWRITE.reserve_cards[2] != " ":
            drawn_card = Game_REWRITE.reserve_cards[2] # Sets the draw_card variable to the card in the list position
            Game_REWRITE.reserve_cards[2] = " " # Sets the section in the list to be an empty string

        # Checks if there is a card is the slot in the list
        elif Game_REWRITE.reserve_cards[3] != " ":
            drawn_card = Game_REWRITE.reserve_cards[3] # Sets the draw_card variable to the card in the list position
            Game_REWRITE.reserve_cards[3] = " " # Sets the section in the list to be an empty string

        # Checks if there is a card is the slot in the list
        elif Game_REWRITE.reserve_cards[4] != " ":
            drawn_card = Game_REWRITE.reserve_cards[4] # Sets the draw_card variable to the card in the list position
            Game_REWRITE.reserve_cards[4] = " " # Sets the section in the list to be an empty string

        # Checks if there is a card is the slot in the list
        elif Game_REWRITE.reserve_cards[5] != " ":
            drawn_card = Game_REWRITE.reserve_cards[5] # Sets the draw_card variable to the card in the list position
            Game_REWRITE.reserve_cards[5] = " " # Sets the section in the list to be an empty string

        # Checks if there is a card is the slot in the list
        elif Game_REWRITE.reserve_cards[6] != " ":
            drawn_card = Game_REWRITE.reserve_cards[6] # Sets the draw_card variable to the card in the list position
            Game_REWRITE.reserve_cards[6] = " " # Sets the section in the list to be an empty string

        # Checks if there is a card is the slot in the list
        elif Game_REWRITE.reserve_cards[7] != " ":
            drawn_card = Game_REWRITE.reserve_cards[7] # Sets the draw_card variable to the card in the list position
            Game_REWRITE.reserve_cards[7] = " " # Sets the section in the list to be an empty string

        # Checks if the variable was assigned because the player or com 1 played a see the future
        elif CCP.first_card != " ":
            drawn_card = CCP.first_card # Sets the draw_card variable to the top card seen in the see the future
            CCP.first_card = " " # Re-assigns the variable to be an empty string

        # Checks if the variable was assigned because the player or com 1 played a see the future
        elif CCP.second_card != " ":
            drawn_card = CCP.second_card # Sets the draw_card variable to the top card seen in the see the future
            CCP.second_card = " " # Re-assigns the variable to be an empty string

        # Checks if the variable was assigned because the player or com 1 played a see the future
        elif CCP.third_card != " ":
            drawn_card = CCP.third_card # Sets the draw_card variable to the top card seen in the see the future
            CCP.third_card = " " # Re-assigns the variable to be an empty string

        else:
            drawn_card = random.choice(Game_REWRITE.cards) # Randomly draws a card from the cards list

        display_card(drawn_card) # Displays the drawn cards

        messagebox._show("Exploding Kittens Game", "You've drawn a: " + drawn_card) # Tells the player which card they've drawn

        # Checks if the player selected 1 com player (This isolates com 1 behavior, since the behavior is best with 1 com player)
        if wt.com_number == 1:
                Game_REWRITE.com1_turn = True # Makes it be com 1's turn
                # Checks if com 1 has played an attack
                if C1B.card_to_play == "attack":
                    messagebox.showerror("Exploding Kittens Game", "It is your turn again since com1 has played an attack card") # Tells the player thats it there turn again because com 1 played a attack card
                    Game_REWRITE.player_turn = True # Makes it the players turn
                    C1B.card_to_play = "" # # Sets com 1's card to play to an empty string so the the next time the player goes to draw this if statement doesn't repeat
                else:
                    C1B.decied_card_to_play() # Makes it be con 1's turn
        elif wt.com_number == 2:
            Game_REWRITE.com1_turn = True
            Game_REWRITE.com2_turn = True

            # Checks if com 2 played an attack card
            if CC2CP.com2_played_attack == True:
                messagebox.showerror("Exploding Kittens Game", "It is your turn again since com2  has played an attack card")
                Game_REWRITE.player_turn = True
                CC2CP.com2_played_attack = False
            else:
                C1B.decied_card_to_play()

        elif wt.com_number == 3:
            Game_REWRITE.com1_turn = True
            Game_REWRITE.com2_turn = True
            Game_REWRITE.com3_turn = True

            C1B.decied_card_to_play()

    # Checks if it's the players turn, but they have not played any cards
    elif Game_REWRITE.player_turn == True:
        Game_REWRITE.add_to_reserve_cards() # Adds a card to the players reserve hand

        print(wt.com_number)

        Game_REWRITE.player_turn = False # Makes it not be the players turn

        # Checks if the player selected 1 com player (This isolates com 1 behavior, since the behavior is best with 1 com player)
        if wt.com_number == 1:
            Game_REWRITE.com1_turn = True # Makes it be com 1's turn

            # Checks if com 1 has played an attack
            if C1B.card_to_play == "attack":
                messagebox.showerror("Exploding Kittens Game", "It is your turn again since com1 has played an attack card") # Tells the player thats it there turn again because com 1 played a attack card
                Game_REWRITE.player_turn = True # Makes it the players turn
                C1B.card_to_play = "" # # Sets com 1's card to play to an empty string so the the next time the player goes to draw this if statement doesn't repeat
            else:
                C1B.decied_card_to_play() # Makes it be con 1's turn

        # Checks if the player selected com 1 and 2 (This makes this so when com 1 draws it's com 2's turn instead the players)
        elif wt.com_number == 2:
            Game_REWRITE.com1_turn = True
            Game_REWRITE.com2_turn = True

            # Checks if com 2 played an attack card
            if CC2CP.com2_played_attack == True:
                messagebox.showerror("Exploding Kittens Game", "It is your turn again since com2  has played an attack card")
                Game_REWRITE.player_turn = True
                CC2CP.com2_played_attack = False
            else:
                C1B.decied_card_to_play()
                
        elif wt.com_number == 3:
            Game_REWRITE.com1_turn = True
            Game_REWRITE.com2_turn = True
            Game_REWRITE.com3_turn = True

            C1B.decied_card_to_play()

    # Checks if it's not the player's turn
    elif Game_REWRITE.player_turn == False:
        messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's the there turn

# Function displays the drawn card
def display_card(card_to_display):
    # Checks if the player played the card
    if Game_REWRITE.card1_played == True:
        print("Card Drawn: " + card_to_display) # Prints the card that was drawn

        # Creates a function to be used when the card is displayed
        def card1_command():
            # Checks if its the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(card_to_display + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card1.destroy() # Destroys the card

                Game_REWRITE.card1_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[0] = "" # Re-assigns the slot in the list to match that the played card

                CCP.check_card_to_play(card_to_display) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + card_to_display, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + card_to_display) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card1_played = True  # Makes the bollen False

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card1.destroy() # Destroys the card

                    Game_REWRITE.player_cards[0] = "" # Re-assigns the slot in the list to match that the played card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND1, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND1)
                    Game_REWRITE.card1_played = True
                    C2B.card_to_play = ""

                    show_card1.destroy()
                    Game_REWRITE.player_cards[0] = ""

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            # Checks if com 3 played a favor
            elif C3B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com 3 your " + Game_REWRITE.CARDS_IN_HAND1, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com 3 your " + Game_REWRITE.CARDS_IN_HAND1)
                    Game_REWRITE.card1_played = True
                    C3B.card_to_play = ""

                    show_card1.destroy()
                    Game_REWRITE.player_cards[0] = ""

                    CC3CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND1)

                    CC3CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 3")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card1 = tk.Button(Game_REWRITE.gameScreen, text = card_to_display, font = "20", command = card1_command) # Creates the card
        show_card1.place(x = 650, y = 600) # Places the card at x = 650,y = 600

        Game_REWRITE.card1_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_turn = False # Makes it so it's not the player's turn

        CCD.check_card(card_to_display) # Checks the card that was drawn

        Game_REWRITE.player_cards[0] = card_to_display # Re-assigns the slot in the list to match that the drawn card

    # Checks if the player played the card
    elif Game_REWRITE.card2_played == True:
        print("Card Drawn: " + card_to_display) # Prints the card that was drawn

        # Creates a function to be used when the card is displayed
        def card2_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(card_to_display + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card2.destroy() # Destroys the card

                Game_REWRITE.card2_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[1] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(card_to_display) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + card_to_display, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + card_to_display) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card2_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card2.destroy() # Destroys the card

                    Game_REWRITE.player_cards[1] = "" # Assigns the empty slot to the given card

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com2 your " + Game_REWRITE.CARDS_IN_HAND2, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com2 your " + Game_REWRITE.CARDS_IN_HAND2)
                    Game_REWRITE.card2_played = True
                    C2B.card_to_play = ""

                    show_card2.destroy()
                    Game_REWRITE.player_cards[1] = ""

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            # Checks if com 3 played a favor
            elif C3B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com 3 your " + Game_REWRITE.CARDS_IN_HAND2, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com 3 your " + Game_REWRITE.CARDS_IN_HAND2)
                    Game_REWRITE.card2_played = True
                    C3B.card_to_play = ""

                    show_card1.destroy()
                    Game_REWRITE.player_cards[1] = ""

                    CC3CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND2)

                    CC3CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 3")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        CCD.check_card(card_to_display) # Checks the card that was drawn
        show_card2 = tk.Button(Game_REWRITE.gameScreen, text = card_to_display, font = "20", command = card2_command) # Creates the card
        show_card2.place(x = 810, y = 600) # Places the card at x = 810,y = 600

        Game_REWRITE.card2_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_turn = False # Makes it so it's not the player's turn

        Game_REWRITE.player_cards[1] = card_to_display # Re-assigns the slot in the list to match that the played card

    # Checks if the player played the card
    elif Game_REWRITE.card3_played == True:
        print("Drawn Card: " + card_to_display) # Prints the card that was drawn

        # Creates a function to be used when the card is displayed
        def card3_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(card_to_display + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card3.destroy() # Destroys the card

                Game_REWRITE.card3_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[2] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(card_to_display) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + card_to_display, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Asks the player for if they a sure they want to give that card to com 1
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + card_to_display) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card3_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card3.destroy() # Destroys the card

                    Game_REWRITE.player_cards[2] = "" # Assigns the empty slot to the given card

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND3, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND3)
                    Game_REWRITE.card3_played = True
                    C2B.card_to_play = ""

                    show_card3.destroy()
                    Game_REWRITE.player_cards[2] = ""

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            # Checks if com 3 played a favor
            elif C3B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com 3 your " + Game_REWRITE.CARDS_IN_HAND1, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com 3 your " + Game_REWRITE.CARDS_IN_HAND3)
                    Game_REWRITE.card1_played = True
                    C3B.card_to_play = ""

                    show_card3.destroy()
                    Game_REWRITE.player_cards[2] = ""

                    CC3CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND3)

                    CC3CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 3")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn


        CCD.check_card(card_to_display) # Checks the card that was drawn
        show_card3 = tk.Button(Game_REWRITE.gameScreen, text = card_to_display, font = "20", command = card3_command) # Creates the card
        show_card3.place(x = 980, y = 600) # Places the card at x = 980,y = 600

        Game_REWRITE.card3_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_turn = False # Makes it so it's not the player's turn

        Game_REWRITE.player_cards[2] = card_to_display # Re-assigns the slot in the list to match that the played card

    # Checks if the player played the card
    elif Game_REWRITE.card4_played == True:
        print("Drawn Card: " + card_to_display) # Prints the card that was drawn

        # Creates a function to be used when the card is displayed
        def card4_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(card_to_display + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card4.destroy() # Destroys the card

                Game_REWRITE.card4_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[3] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(card_to_display) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + card_to_display, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + card_to_display) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card4_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card4.destroy() # Destroys the card

                    Game_REWRITE.player_cards[3] = "" # Assigns the empty slot to the given card

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND4, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND4)
                    Game_REWRITE.card4_played = True
                    C2B.card_to_play = ""

                    show_card4.destroy()
                    Game_REWRITE.player_cards[3] = ""

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            # Checks if com 3 played a favor
            elif C3B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com 3 your " + Game_REWRITE.CARDS_IN_HAND4, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com 3 your " + Game_REWRITE.CARDS_IN_HAND4)
                    Game_REWRITE.card3_played = True
                    C3B.card_to_play = ""

                    show_card3.destroy()
                    Game_REWRITE.player_cards[2] = ""

                    CC3CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND4)

                    CC3CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 3")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        CCD.check_card(card_to_display) # Checks the card that was drawn
        show_card4 = tk.Button(Game_REWRITE.gameScreen, text = card_to_display, font = "20", command = card4_command) # Creates the card
        show_card4.place(x = 1090, y = 600) # Places the card at x = 1090,y = 600

        Game_REWRITE.card4_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_turn = False # Makes it so it's not the player's turn

        Game_REWRITE.player_cards[3] = card_to_display # Re-assigns the slot in the list to match that the played card

    # Checks if the player played the card
    elif Game_REWRITE.card5_played == True:
        print("Drawn Card: " + card_to_display) # Prints the card that was drawn

        # Creates a function to be used when the card is displayed
        def card5_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(card_to_display + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card5.destroy() # Destroys the card

                Game_REWRITE.card5_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[4] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(card_to_display) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + card_to_display, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + card_to_display) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card5_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat
                    Game_REWRITE.player_cards[3] = "" # Assigns the empty slot to the given card

                    show_card5.destroy() # Destroys the card

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com2") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com2 your " + Game_REWRITE.CARDS_IN_HAND5, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com2 your " + Game_REWRITE.CARDS_IN_HAND5)
                    Game_REWRITE.card5_played = True
                    C2B.card_to_play = ""

                    show_card5.destroy()
                    Game_REWRITE.player_cards[4] = ""

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            # Checks if com 3 played a favor
            elif C3B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com 3 your " + Game_REWRITE.CARDS_IN_HAND5, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com 3 your " + Game_REWRITE.CARDS_IN_HAND5)
                    Game_REWRITE.card5_played = True
                    C3B.card_to_play = ""

                    show_card5.destroy()
                    Game_REWRITE.player_cards[4] = ""

                    CC3CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND5)

                    CC3CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 3")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        CCD.check_card(card_to_display) # Checks the card that was drawn
        show_card5 = tk.Button(Game_REWRITE.gameScreen, text = card_to_display, font = "20", command = card5_command) # Creates the card
        show_card5.place(x = 170, y = 600) # Places the card at x = ,y = 600

        Game_REWRITE.card5_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_turn = False # Makes it so it's not the player's turn

        Game_REWRITE.player_cards[4] = card_to_display # Re-assigns the slot in the list to match that the played card

    # Checks if the player played the card
    elif Game_REWRITE.card6_played == True:
        print("Drawn Card: " + card_to_display) # Prints the card that was drawn

        # Creates a function to be used when the card is displayed
        def card6_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(card_to_display + "\n \n \n") # Sets the discard pile display text to the card that you've played

                show_card6.destroy() # Destroys the card

                Game_REWRITE.card6_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[5] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(card_to_display) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game", "Are you sure you want to give com1 your " + card_to_display, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + card_to_display) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card6_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card6.destroy() # Destroys the card

                    Game_REWRITE.player_cards[5] = "" # Assigns the empty slot to the given card

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND6, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND6)
                    Game_REWRITE.card6_played = True
                    C2B.card_to_play = ""

                    show_card6.destroy()
                    Game_REWRITE.player_cards[5] = ""

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            # Checks if com 3 played a favor
            elif C3B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com 3 your " + Game_REWRITE.CARDS_IN_HAND6, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com 3 your " + Game_REWRITE.CARDS_IN_HAND6)
                    Game_REWRITE.card6_played = True
                    C3B.card_to_play = ""

                    show_card6.destroy()
                    Game_REWRITE.player_cards[5] = ""

                    CC3CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND6)

                    CC3CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 3")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn


        CCD.check_card(card_to_display) # Checks the card that was drawn
        show_card6 = tk.Button(Game_REWRITE.gameScreen, text = card_to_display, font = "20", command = card6_command) # Creates the card
        show_card6.place(x = 330, y = 600) # Places the card at x = 330,y = 600

        Game_REWRITE.card6_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_turn = False # Makes it so it's not the player's turn

        Game_REWRITE.player_cards[5] = card_to_display # Re-assigns the slot in the list to match that the played card

    # Checks if the player played the card
    elif Game_REWRITE.card7_played == True:
        print("Drawn Card: " + card_to_display) # Prints the card that was drawn

        # Creates a function to be used when the card is displayed
        def card7_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(card_to_display + "\n \n \n") # Sets the discard pile display text to the card that you've played

                show_card7.destroy() # Destroys the card

                Game_REWRITE.card7_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[6] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(card_to_display) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + card_to_display, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + card_to_display) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card7_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card7.destroy() # Destroys the card

                    Game_REWRITE.player_cards[6] = "" # Assigns the empty slot to the given card

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com2 your " + Game_REWRITE.CARDS_IN_HAND7, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com2 your " + Game_REWRITE.CARDS_IN_HAND7)
                    Game_REWRITE.card7_played = True
                    C2B.card_to_play = ""

                    show_card7.destroy()
                    Game_REWRITE.player_cards[6] = ""

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            # Checks if com 3 played a favor
            elif C3B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com 3 your " + Game_REWRITE.CARDS_IN_HAND7, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com 3 your " + Game_REWRITE.CARDS_IN_HAND7)
                    Game_REWRITE.card7_played = True
                    C3B.card_to_play = ""

                    show_card7.destroy()
                    Game_REWRITE.player_cards[6] = ""

                    CC3CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND7)

                    CC3CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 3")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        CCD.check_card(card_to_display) # Checks the card that was drawn
        show_card7 = tk.Button(Game_REWRITE.gameScreen, text = card_to_display, font = "20", command = card7_command) # Creates the card
        show_card7.place(x = 490, y = 600) # Places the card at x = 490,y = 600

        Game_REWRITE.card7_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_turn = False # Makes it so it's not the player's turn

        Game_REWRITE.player_cards[6] = card_to_display # Re-assigns the slot in the list to match that the played card
