# imports all the modules needed
import tkinter as tk
import Game_REWRITE
from WelcomeTEST import com_number
import random
import Deal_To_Com_Players as DTCP
import Com1_Behavior as C1B
import Com2_Behavior as C2B
import Com3_Behavior as C3B
import Check_Com2_Card_Played as CC2CP
import Check_Com3_Card_Played as CC3CP
import Check_Com1_Card_Played as CC1CP
import Check_Card_Played as CCP
from tkinter import simpledialog, messagebox

# Creates all the variables needed
message_box1 = ' '
message_box2 = ""

first_card = " "
second_card = " "
third_card = " "

cat_card_played = False
cat_combo = False
cat_card_clicked = ""

favor_card = ""

attack_card_played = False

def display_favored_card(favored_card):
    # Checks if the player played card 1
    if Game_REWRITE.card1_played == True:
        Game_REWRITE.CARDS_IN_HAND1 = favored_card # Creates a variables from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card1_command():
            # Checks if its the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(Game_REWRITE.CARDS_IN_HAND1 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card1.destroy() # Destroys the card

                Game_REWRITE.card1_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[0] = "" # Re-assigns the slot in the list to match that the played card

                check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND1, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND1) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card1_played = True  # Makes the bollen False

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card1.destroy() # Destroys the card

                    Game_REWRITE.player_cards[0] = "" # Re-assigns the slot in the list to match that the played card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND1)

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com2 your " + Game_REWRITE.CARDS_IN_HAND1, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com2 your " + Game_REWRITE.CARDS_IN_HAND1)
                    Game_REWRITE.card1_played = True
                    C2B.card_to_play = ""

                    show_card1.destroy()
                    Game_REWRITE.player_cards[0] = ""

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND1)

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

        show_card1 = tk.Button(Game_REWRITE.gameScreen, text = favored_card, command = card1_command, font = "20") # Creates the card
        show_card1.place(x = 650, y = 600) # Places the card a x = 650 and y = 600

        Game_REWRITE.card1_played = False # Makes so that the played haven't played card 1

        Game_REWRITE.player_cards[0] = Game_REWRITE.CARDS_IN_HAND1 # Assigns the empty slot to the gave card

    # Checks if the player played card 2
    elif Game_REWRITE.card2_played == True:
        Game_REWRITE.CARDS_IN_HAND2 = favored_card # Creates a variable from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card2_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(Game_REWRITE.CARDS_IN_HAND2 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card2.destroy() # Destroys the card

                Game_REWRITE.card2_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[1] = "" # Assigns the empty slot to the played card

                check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND2, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND2) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card2_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card2.destroy() # Destroys the card

                    Game_REWRITE.player_cards[1] = "" # Assigns the empty slot to the gave card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND2)

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

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND2)

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

                    show_card2.destroy()
                    Game_REWRITE.player_cards[1] = ""

                    CC3CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND2)

                    CC3CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 3")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card2 = tk.Button(Game_REWRITE.gameScreen, text = favored_card, command = card2_command, font = "20") # Creates the card
        show_card2.place(x = 810, y = 600) # Places the card at x = 810, y = 600

        Game_REWRITE.card2_played = False # Makes so that the played haven't played card 2

        Game_REWRITE.player_cards[1] = Game_REWRITE.CARDS_IN_HAND2 # Assigns the empty slot to the gave card

    # Checks if the player played card 3
    elif Game_REWRITE.card3_played == True:
        Game_REWRITE.CARDS_IN_HAND3 = favored_card # Creates a variable from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card3_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(Game_REWRITE.CARDS_IN_HAND3 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card3.destroy() # Destroys the card

                Game_REWRITE.card3_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[2] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND3, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Asks the player for if they a sure they want to give that card to com 1
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com2 your " + Game_REWRITE.CARDS_IN_HAND3) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card3_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card3.destroy() # Destroys the card

                    Game_REWRITE.player_cards[2] = "" # Assigns the empty slot to the gave card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND1)

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com2 your " + Game_REWRITE.CARDS_IN_HAND3, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com2 your " + Game_REWRITE.CARDS_IN_HAND3)
                    Game_REWRITE.card3_played = True
                    C2B.card_to_play = ""

                    show_card3.destroy()
                    Game_REWRITE.player_cards[2] = ""

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND3)

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            # Checks if com 3 played a favor
            elif C3B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com 3 your " + Game_REWRITE.CARDS_IN_HAND3, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com 3 your " + Game_REWRITE.CARDS_IN_HAND3)
                    Game_REWRITE.card3_played = True
                    C3B.card_to_play = ""

                    show_card1.destroy()
                    Game_REWRITE.player_cards[2] = ""

                    CC3CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND3)

                    CC3CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 3")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card3 = tk.Button(Game_REWRITE.gameScreen, text = favored_card, command = card3_command, font = "20") # Creates the card
        show_card3.place(x = 960, y = 600) # Places the card at x = 960,y = 600

        Game_REWRITE.card3_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_cards[2] = Game_REWRITE.CARDS_IN_HAND3 # Re-assigns the slot in the list to match that the played card

    # Checks if the player played card 4
    elif Game_REWRITE.card4_played == True:
        Game_REWRITE.CARDS_IN_HAND4 = favored_card # Creates a variable from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card4_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(Game_REWRITE.CARDS_IN_HAND4 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card4.destroy() # Destroys the card

                Game_REWRITE.card4_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[3] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND4, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND4) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card4_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card4.destroy() # Destroys the card

                    Game_REWRITE.player_cards[3] = "" # Assigns the empty slot to the gave card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND4)

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com2 your " + Game_REWRITE.CARDS_IN_HAND4, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com2 your " + Game_REWRITE.CARDS_IN_HAND4)
                    Game_REWRITE.card4_played = True
                    C2B.card_to_play = ""

                    show_card4.destroy()
                    Game_REWRITE.player_cards[3] = ""

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND4)

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            # Checks if com 3 played a favor
            elif C3B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com 3 your " + Game_REWRITE.CARDS_IN_HAND4, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com 3 your " + Game_REWRITE.CARDS_IN_HAND4)
                    Game_REWRITE.card1_played = True
                    C3B.card_to_play = ""

                    show_card4.destroy()
                    Game_REWRITE.player_cards[3] = ""

                    CC3CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND4)

                    CC3CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 3")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card4 = tk.Button(Game_REWRITE.gameScreen, text = favored_card, command = card4_command, font = "20") # Creates the card
        show_card4.place(x = 1090, y = 600) # Places the card at x = 1090,y = 600

        Game_REWRITE.card4_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_cards[3] = Game_REWRITE.CARDS_IN_HAND4 # Re-assigns the slot in the list to match that the played card

    # Checks if the player played card 5
    elif Game_REWRITE.card5_played == True:
        Game_REWRITE.CARDS_IN_HAND5 = favored_card # Creates a variable from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card5_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(Game_REWRITE.CARDS_IN_HAND5 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card5.destroy() # Destroys the card

                Game_REWRITE.card5_played = True # Sets the bollen from the Game_REWRITE script to True
                Game_REWRITE.player_cards[4] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND5, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND5) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card5_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat
                    Game_REWRITE.player_cards[4] = "" # Assigns the empty slot to the gave card

                    show_card5.destroy() # Destroys the card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND5)

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

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

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND6)

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            # Checks if com 3 played a favor
            elif C3B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com 3 your " + Game_REWRITE.CARDS_IN_HAND5, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com 3 your " + Game_REWRITE.CARDS_IN_HAND5)
                    Game_REWRITE.card1_played = True
                    C3B.card_to_play = ""

                    show_card5.destroy()
                    Game_REWRITE.player_cards[4] = ""

                    CC3CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND5)

                    CC3CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 3")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card5 = tk.Button(Game_REWRITE.gameScreen, text = favored_card, command = card5_command, font = "20") # Creates the card
        show_card5.place(x = 170, y = 600) # Places the card at x = 170,y = 600

        Game_REWRITE.card5_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_cards[4] = Game_REWRITE.CARDS_IN_HAND5 # Re-assigns the slot in the list to match that the played card

    # Checks if the player played card 6
    elif Game_REWRITE.card6_played == True:
        Game_REWRITE.CARDS_IN_HAND6 = favored_card # Creates a variable from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card6_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(Game_REWRITE.CARDS_IN_HAND6 + "\n \n \n") # Sets the discard pile display text to the card that you've played

                show_card6.destroy() # Destroys the card

                Game_REWRITE.card6_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[5] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game", "Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND6, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND6) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card6_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card6.destroy() # Destroys the card

                    Game_REWRITE.player_cards[5] = "" # Assigns the empty slot to the gave card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND6)

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

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND6)

                    CC2CP.draw_card()

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

        show_card6 = tk.Button(Game_REWRITE.gameScreen, text = favored_card, command = card6_command, font = "20") # Creates the card
        show_card6.place(x = 330, y = 600) # Places the card at x = ,y = 600

        Game_REWRITE.card6_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_cards[5] = Game_REWRITE.CARDS_IN_HAND6 # Re-assigns the slot in the list to match that the played card

    # Checks if the player played card 7
    elif Game_REWRITE.card7_played == True:
        Game_REWRITE.CARDS_IN_HAND7 = favored_card # Creates a variable from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card7_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(favored_card + "\n \n \n") # Sets the discard pile display text to the card that you've played

                show_card7.destroy() # Destroys the card

                Game_REWRITE.card7_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[6] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND7, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND7) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card7_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card7.destroy() # Destroys the card

                    Game_REWRITE.player_cards[6] = "" # Assigns the empty slot to the gave card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND7)

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND7, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND7)
                    card7_played = True
                    C2B.card_to_play = ""

                    show_card7.destroy()
                    Game_REWRITE.player_cards[6] = ""

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND7)

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

        show_card7 = tk.Button(Game_REWRITE.gameScreen, text = favored_card, command = card7_command, font = "20") # Creates the card
        show_card7.place(x = 490, y = 600) # Places the card at x = 490,y = 600

        Game_REWRITE.card7_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_cards[6] = Game_REWRITE.CARDS_IN_HAND7 # Re-assigns the slot in the list to match that the played card

def displayed_stolen_card(stolen_card):
    # Checks if the player played card 1
    if Game_REWRITE.card1_played == True:
        Game_REWRITE.CARDS_IN_HAND1 = stolen_card # Creates a variable from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card1_command():
            # Checks if its the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(Game_REWRITE.CARDS_IN_HAND1 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card1.destroy() # Destroys the card

                Game_REWRITE.card1_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[0] = "" # Re-assigns the slot in the list to match that the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND1, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND1) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card1_played = True  # Makes the bollen False

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card1.destroy() # Destroys the card

                    Game_REWRITE.player_cards[0] = "" # Re-assigns the slot in the list to match that the played card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND1)

                    CC1CP.draw_card() # Makes com 1 draw a card
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

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND1)

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card1 = tk.Button(Game_REWRITE.gameScreen, text = stolen_card, command = card1_command, font = "20") # Creates the card
        show_card1.place(x = 650, y = 600) # Places the card a x = 650 and y = 600

        Game_REWRITE.card1_played = False # Makes so that the played haven't played card 1

        Game_REWRITE.player_cards[0] = Game_REWRITE.CARDS_IN_HAND1 # Assigns the empty slot to the gave card

    # Checks if the player played card 2
    elif Game_REWRITE.card2_played == True:
        Game_REWRITE.CARDS_IN_HAND2 = stolen_card # Creates a variable from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card2_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(Game_REWRITE.CARDS_IN_HAND2 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card2.destroy() # Destroys the card

                Game_REWRITE.card2_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[1] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND2, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND2) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card2_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card2.destroy() # Destroys the card

                    Game_REWRITE.player_cards[1] = "" # Assigns the empty slot to the gave card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND2)

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND2, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND2)
                    Game_REWRITE.card2_played = True
                    C2B.card_to_play = ""

                    show_card2.destroy()
                    Game_REWRITE.player_cards[1] = ""

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND2)

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card2 = tk.Button(Game_REWRITE.gameScreen, text = stolen_card, command = card2_command, font = "20") # Creates the card
        show_card2.place(x = 810, y = 600) # Places the card at x = 810, y = 600

        Game_REWRITE.card2_played = False # Makes so that the played haven't played card 2

        Game_REWRITE.player_cards[1] = Game_REWRITE.CARDS_IN_HAND2 # Re-assigns the slot in the list to match that the played card

    # Checks if the player played card 3
    elif Game_REWRITE.card3_played == True:
        Game_REWRITE.CARDS_IN_HAND3 = stolen_card # Creates a variable from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card3_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(Game_REWRITE.CARDS_IN_HAND3 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card3.destroy() # Destroys the card

                Game_REWRITE.card3_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[2] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND3, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Asks the player for if they a sure they want to give that card to com 1
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND3) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card3_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card3.destroy() # Destroys the card

                    Game_REWRITE.player_cards[2] = "" # Assigns the empty slot to the gave card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND3)

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

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND3)

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card3 = tk.Button(Game_REWRITE.gameScreen, text = stolen_card, command = card3_command, font = "20") # Creates the card
        show_card3.place(x = 960, y = 600) # Places the card at x = 960,y = 600

        Game_REWRITE.card3_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_cards[2] = Game_REWRITE.CARDS_IN_HAND3 # Re-assigns the slot in the list to match that the played card

    # Checks if the player played card 4
    elif Game_REWRITE.card4_played == True:
        Game_REWRITE.CARDS_IN_HAND4 = stolen_card # Creates a variable from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card4_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(Game_REWRITE.CARDS_IN_HAND4 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card4.destroy() # Destroys the card

                Game_REWRITE.card4_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[3] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND4, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND4) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card4_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card4.destroy() # Destroys the card

                    Game_REWRITE.player_cards[3] = "" # Assigns the empty slot to the gave card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND4)

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

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND4)

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card4 = tk.Button(Game_REWRITE.gameScreen, text = stolen_card, command = card4_command, font = "20") # Creates the card
        show_card4.place(x = 1090, y = 600) # Places the card at x = 1090,y = 600

        Game_REWRITE.card4_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_cards[3] = Game_REWRITE.CARDS_IN_HAND4 # Re-assigns the slot in the list to match that the played card

    # Checks if the player played card 5
    elif Game_REWRITE.card5_played == True:
        Game_REWRITE.CARDS_IN_HAND5 = stolen_card # Creates a variable from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card5_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(Game_REWRITE.CARDS_IN_HAND5 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card5.destroy() # Destroys the card

                Game_REWRITE.card5_played = True # Sets the bollen from the Game_REWRITE script to True
                Game_REWRITE.player_cards[4] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND5, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND5) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card5_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat
                    Game_REWRITE.player_cards[3] = "" # Assigns the empty slot to the gave card

                    show_card5.destroy() # Destroys the card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND5)

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND5, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND5)
                    Game_REWRITE.card5_played = True
                    C2B.card_to_play = ""

                    show_card5.destroy()
                    Game_REWRITE.player_cards[4] = ""

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND5)

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card5 = tk.Button(Game_REWRITE.gameScreen, text = stolen_card, command = card5_command, font = "20") # Creates the card
        show_card5.place(x = 170, y = 600) # Places the card at x = 170,y = 600

        Game_REWRITE.card5_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_cards[4] = Game_REWRITE.CARDS_IN_HAND5 # Re-assigns the slot in the list to match that the played card

    # Checks if the player played card 6
    elif Game_REWRITE.card6_played == True:
        Game_REWRITE.CARDS_IN_HAND6 = stolen_card # Creates a variable from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card6_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(Game_REWRITE.CARDS_IN_HAND6 + "\n \n \n") # Sets the discard pile display text to the card that you've played

                show_card6.destroy() # Destroys the card

                Game_REWRITE.card6_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[5] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game", "Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND6, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND6) # Tells the player that there card was add to com 1's hand

                    Game_REWRITE.card6_played = True # Sets the bollen from the Game_REWRITE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card6.destroy() # Destroys the card

                    Game_REWRITE.player_cards[5] = "" # Assigns the empty slot to the gave card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND6)

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

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND6)

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card6 = tk.Button(Game_REWRITE.gameScreen, text = stolen_card, command = card6_command, font = "20") # Creates the card
        show_card6.place(x = 330, y = 600) # Places the card at x = ,y = 600

        Game_REWRITE.card6_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_cards[5] = Game_REWRITE.CARDS_IN_HAND6 # Re-assigns the slot in the list to match that the played card

    # Checks if the player played card 7
    elif Game_REWRITE.card7_played == True:
        Game_REWRITE.CARDS_IN_HAND7 = stolen_card # Creates a variable from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card7_command():
            # Checks if it's  the players turn
            if Game_REWRITE.player_turn == True:
                Game_REWRITE.discard_pile_text.set(Game_REWRITE.CARDS_IN_HAND7 + "\n \n \n") # Sets the discard pile display text to the card that you've played

                show_card7.destroy() # Destroys the card

                Game_REWRITE.card7_played = True # Sets the bollen from the Game_REWRITE script to True

                Game_REWRITE.player_cards[6] = "" # Assigns the empty slot to the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND7, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND7) # Tells the player that there card was add to com 1's hand

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player goes to click on another card this if statement doesn't repeat

                    show_card7.destroy() # Destroys the card

                    Game_REWRITE.player_cards[6] = "" # Assigns the empty slot to the gave card

                    CC1CP.get_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND7)

                    CC1CP.draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            # Checks if com 2 played a favor
            elif C2B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + Game_REWRITE.CARDS_IN_HAND7, icon = "warning")

                # Checks if the player clicked on yes
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + Game_REWRITE.CARDS_IN_HAND7)
                    Game_REWRITE.card7_played = True
                    C2B.card_to_play = ""

                    show_card7.destroy()
                    Game_REWRITE.player_cards[6] = ""

                    CC2CP.add_favor_or_stolen_card(Game_REWRITE.CARDS_IN_HAND7)

                    CC2CP.draw_card()

                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com 2")

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card7 = tk.Button(Game_REWRITE.gameScreen, text = stolen_card, command = card7_command, font = "20") # Creates the card
        show_card7.place(x = 490, y = 600) # Places the card at x = 490,y = 600

        Game_REWRITE.card7_played = False # Makes so that the played haven't played card

        Game_REWRITE.player_cards[6] = Game_REWRITE.CARDS_IN_HAND7 # Re-assigns the slot in the list to match that the played card

def steal_card():
    global message_box2 # Creates a global variable to be used in the Deal_To_Com_Players.py file

    # Checks if the player selected 1 com player
    if com_number == 1:
        messagebox.showwarning('Cat Cards', 'Click a card under Com 1 (Closing is required, but you can still get a card.)') # Tells the player to click a card under com 1 and that they can steal a card

    # Checks if the player selected 2 com player
    elif com_number == 2:
        message_box2 = simpledialog.askstring('Cat Cards', 'Enter the com player you want to steal from (1 or 2)') # Asks if the player who they want to steal from

        # If the player entered a number larger or smaller then 1-3 or a string
        if message_box2 > '2' or message_box2 < '1':
            messagebox.showerror('Cat Cards', 'You entered a larger number than what was expected or was a not a number.\nPlease try agin') # Tells the user that they inputted somthing that was not expected

            steal_card() # repeats the function

        # Checks if the player inputted "1" as there input
        elif message_box2 == '1':
            messagebox.showwarning('Cat Cards', 'Click a card under Com 1 (Closing is required, but you can still get a card.)') # Tells the player to click a card under com 1 and that they can steal a card

        # Checks if the player inputted "2" as there input
        elif message_box2 == '2':
            messagebox.showwarning('Cat Cards', 'Click a card under Com 2 (Closing is required, but you can still get a card.)') # Tells the player to click a card under com 2 and that they can steal a card

    # Checks if the player selected 3 com players
    elif com_number == 3:
        message_box2 = simpledialog.askstring('Cat Cards', 'Enter the com player you want to steal from (1, 2, or 3)') # Asks the player who they want to steal a card from

        # Checks if the player inputted a number less than 1 or larger then 3 or a string
        if message_box2 > '3' or message_box2 < '1':
            messagebox.showerror('Cat Cards', 'You entered a larger number than what was expected or was a not a number.\nPlease try agin') # Tells the player that they inputted a number that was not expected

            steal_card() # repeats the function

        # Checks if the player inputted "1" as there target
        elif message_box2 == '1':
            messagebox.showwarning('Cat Cards', 'Click a card under Com 1 (Closing is required, but you can still get a card.)') # Tells the player to click a card under com 1

        # Checks if the player inputted "2" as there target
        elif message_box2 == '2':
            messagebox.showwarning('Cat Cards', 'Click a card under Com 2 (Closing is required, but you can still get a card.)') # Tells the player to click a card under com 2

        # Checks if the player inputted "3" as there target
        elif message_box2 == '3':
            messagebox.showwarning('Cat Cards', 'Click a card under Com 3 (Closing is required, but you can still get a card.)') # Tells the player to click a card under com 3

def get_favor():
    # Checks if the player selected 3 com players
    if com_number == 3:
        message_box1 = simpledialog.askstring('Favor', 'Please enter the com player you want to ask (1, 2, 3)') # Asks the com player who they want to get a favor from

        # If the player entered a number larger or smaller then 1-3 or a string
        if message_box1 > '3' or message_box1 < '1':
            messagebox.showerror('Favor', 'You entered a larger number than what was expected or was a not a number.\nPlease try agin') # Tells the player that they've enter a larger or smaller number than what wan expected

            get_favor() # repeats the function

        # Checks if the player want to get a favor from com 3
        elif message_box1 == '3':
            favor_card = random.choice(Game_REWRITE.cards) # Creates a string from a random choice from the cards list
            messagebox._show('Favor', 'Com 3 has given you a ' + favor_card) # Tells the player has given them the card selected in the favor_card
            display_favored_card(favor_card) # Displays the favor
        # Checks if the player want to get a favor from com 2
        elif message_box1 == '2':
            favor_card = random.choice(Game_REWRITE.cards)  # Creates a string from a random choice from the cards list
            messagebox._show('Favor', 'Com 2 has given you a ' + favor_card) # Tells the player has given them the card selected in the favor_card
            display_favored_card(favor_card) # Displays the favor
        # Checks if the player want to get a favor from com 1
        elif message_box1 == '1':
            favor_card = random.choice(Game_REWRITE.cards) # Creates a string from a random choice from the cards list
            messagebox._show('Favor', 'Com 1 has given you a ' + favor_card) # Tells the player has given them the card selected in the favor_card
            display_favored_card(favor_card) # Displays the favor

    # Checks if the player selected 1 com player
    elif com_number == 1:
        favor_card = random.choice(Game_REWRITE.cards) # Creates a string from a random choice from the cards list
        messagebox.showinfo('Favor', 'Com 1 has given you a ' + favor_card) # Tells the player has given them the card selected in the favor_card
        display_favored_card(favor_card) # Displays the favor

    # Checks if the player selected 2 com player
    elif com_number == 2:
        message_box1 = simpledialog.askstring('Favor', 'Please enter the com player you want to ask (1 or 2)') # Asks the com player who they want to get a favor from

        # If the player entered a number larger or smaller then 1-3 or a string
        if message_box1 > '2' or message_box1 < '1':
            messagebox.showerror('Favor', 'You entered a larger number than what was expected or was a not a number.\nPlease try agin') # Tells the player that they've enter a larger or smaller number than what wan expected

            get_favor() # Repeats the function
        # Checks if the player want to get a favor from com 2
        elif message_box1 == '2':
            favor_card = random.choice(Game_REWRITE.cards) # Creates a string from a random choice from the cards list
            messagebox._show('Favor', 'Com 2 has given you a ' + favor_card) # Tells the player has given them the card selected in the favor_card
            display_favored_card(favor_card) # Displays the favor
        # Checks if the player want to get a favor from com 1
        elif message_box1 == '1':
            favor_card = random.choice(Game_REWRITE.cards) # Creates a string from a random choice from the cards list
            messagebox._show('Favor', 'Com 1 has given you a ' + favor_card) # Tells the player has given them the card selected in the favor_card
            display_favored_card(favor_card) # Displays the favor

def cat_card_function(cat_card):
    global cat_card_played, cat_combo, cat_card_clicked

    # If the player has played a cat card, but has a cat card as there last card run the command below
    if cat_card_played == False:
        messagebox.showwarning('Cat Cards', 'Please play another ' + cat_card) # Tells the user to play another card of what ever cat card they played

        cat_card_played = True # Makes cat_card_played = True
        cat_card_clicked = cat_card # Used for checking if the user is played the the same kind of cat_card

    # If the cat_card_played == True and both cards match run the statement
    elif cat_card_played == True and cat_card == cat_card_clicked:
        messagebox.showinfo('Cat Cards', 'You played another ' + cat_card)

        steal_card()

        cat_card_played = False
        cat_combo = True

    # If the play played another cat card that don't match it'll tell the play that they don't match
    elif cat_card != cat_card_clicked:
        messagebox.showerror('Cat Cards', 'Sorry, but those cards don\'t match')
        cat_card_played = False

def check_card_to_play(card_to_check):
    # Checks the card played

    global first_card, second_card, third_card, attack_card_played

    print("Card Played: " + card_to_check)

    # If the player play a skip skip there turn and make it com1's turn
    if card_to_check == "skip":
        messagebox._show("Skip", "You have skipped your turn.")
        Game_REWRITE.player_turn = False

        Game_REWRITE.com1_turn = True
        C1B.decied_card_to_play()

    # If the player play a skip skip there turn and make it com1's turn and make them has 2 turns
    elif card_to_check == "attack":
        messagebox.showinfo("Attack" , "You have skiped your turn and made the com 1 player have 2 turns.")
        Game_REWRITE.player_turn = False

        attack_card_played = True

        Game_REWRITE.com1_turn = True
        C1B.decied_card_to_play()

    # If the player played a favor run the function below
    elif card_to_check == "favor":
        get_favor()

    # If the player played a shuffle randomly reorder the cards list
    elif card_to_check == "shuffle":
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)
        random.shuffle(Game_REWRITE.cards)

    # If the player played a see the future randomly pick 3 cards from the cards list and display them to the user
    elif card_to_check == "see the future":
        first_card = random.choice(Game_REWRITE.cards)
        second_card = random.choice(Game_REWRITE.cards)
        third_card = random.choice(Game_REWRITE.cards)

        messagebox.showinfo('See The Future', 'Top card: ' + first_card + " Middle card: " + second_card + " Bottom card: " + third_card)

    # Checks if the player played a nope card
    elif card_to_check == "nope":
        print("Player played a nope card")

        # TODO Add code to cancel what card com 1, 2 or 3 played

    # If the player played a cat card run the function below
    elif card_to_check == 'potato cat' or 'taco cat' or 'rainbow ralphing \n cat' or 'beard cat' or 'cattermellon':
        cat_card_function(card_to_check)
