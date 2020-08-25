# imports all the moduals needed
from tkinter import *
from Game_REWIRTE import *
import Game_REWIRTE
from WelcomeTEST import com_number
from tkinter import messagebox, simpledialog
import random
from Deal_To_Com_Players import *
import Deal_To_Com_Players
from Com1_Behevior import *
import Com1_Behevior as C1B

# Creates all the varibles needed
message_box1 = ' '
message_box2 = ""

first_card = " "
second_card = " "
thrid_card = " "

cat_card_played = False
cat_combo = False
cat_card_clicked = ""

favor_card = ""

attack_card_played = False

def display_favored_card(favored_card):
    # Checks if the player played card 1
    if Game_REWIRTE.card1_played == True:
        CARDS_IN_HAND1 = favored_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card1_command():
            # Checks if its the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(CARDS_IN_HAND1 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card1.destroy() # Destroys the card

                Game_REWIRTE.card1_played = True # Sets the bollen from the Game_REWIRTE script to True

                Game_REWIRTE.player_cards[0] = "" # Re-assings the slot in the list to match that the played card

                check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND1, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND1) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card1_played = True  # Makes the bollen False

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate

                    show_card1.destroy() # Destroys the card

                    Game_REWIRTE.player_cards[0] = "" # Re-assings the slot in the list to match that the played card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card1 = Button(Game_REWIRTE.gameScreen, text = favored_card, command = card1_command, font = "20") # Creates the card
        show_card1.place(x = 650, y = 600) # Places the card a x = 650 and y = 600

        Game_REWIRTE.card1_played = False # Makes so that the played haven't played card 1

        Game_REWIRTE.player_cards[0] = CARDS_IN_HAND1 # Assings the empty slot to the gaved card

    # Checks if the player played card 2

    # Checks if the player played card 2

    # Checks if the player played card 2
    elif Game_REWIRTE.card2_played == True:
        CARDS_IN_HAND2 = favored_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card2_command():
            # Checks if it's  the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(CARDS_IN_HAND2 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card2.destroy() # Destroys the card

                Game_REWIRTE.card2_played = True # Sets the bollen from the Game_REWIRTE script to True

                Game_REWIRTE.player_cards[1] = "" # Assings the empty slot to the played card

                check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND2, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND2) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card2_played = True # Sets the bollen from the Game_REWIRTE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate

                    show_card2.destroy() # Destroys the card

                    Game_REWIRTE.player_cards[1] = "" # Assings the empty slot to the gaved card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card2 = Button(Game_REWIRTE.gameScreen, text = favored_card, command = card2_command, font = "20") # Creates the card
        show_card2.place(x = 810, y = 600) # Places the card at x = 810, y = 600

        Game_REWIRTE.card2_played = False # Makes so that the played haven't played card 2

        Game_REWIRTE.player_cards[1] = CARDS_IN_HAND2 # Assings the empty slot to the gaved card

    # Checks if the player played card 3
    elif Game_REWIRTE.card3_played == True:
        CARDS_IN_HAND3 = favored_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card3_command():
            # Checks if it's  the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(CARDS_IN_HAND3 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card3.destroy() # Destroys the card

                Game_REWIRTE.card3_played = True # Sets the bollen from the Game_REWIRTE script to True

                Game_REWIRTE.player_cards[2] = "" # Assings the empty slot to the played card

                CCP.check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND3, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Asks the player for if they a sure they want to give that card to com 1
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND3) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card3_played = True # Sets the bollen from the Game_REWIRTE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate

                    show_card3.destroy() # Destroys the card

                    Game_REWIRTE.player_cards[2] = "" # Assings the empty slot to the gaved card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card3 = Button(Game_REWIRTE.gameScreen, text = favored_card, command = card3_command, font = "20") # Creates the card
        show_card3.place(x = 960, y = 600) # Places the card at x = 960,y = 600

        Game_REWIRTE.card3_played = False # Makes so that the played haven't played card

        Game_REWIRTE.player_cards[2] = CARDS_IN_HAND3 # Re-assings the slot in the list to match that the played card

    # Checks if the player played card 4
    elif Game_REWIRTE.card4_played == True:
        CARDS_IN_HAND4 = favored_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card4_command():
            # Checks if it's  the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(CARDS_IN_HAND4 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card4.destroy() # Destroys the card

                Game_REWIRTE.card4_played = True # Sets the bollen from the Game_REWIRTE script to True

                Game_REWIRTE.player_cards[3] = "" # Assings the empty slot to the played card

                CCP.check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND4, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND4) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card4_played = True # Sets the bollen from the Game_REWIRTE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate

                    show_card4.destroy() # Destroys the card

                    Game_REWIRTE.player_cards[3] = "" # Assings the empty slot to the gaved card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card4 = Button(Game_REWIRTE.gameScreen, text = favored_card, command = card4_command, font = "20") # Creates the card
        show_card4.place(x = 1090, y = 600) # Places the card at x = 1090,y = 600

        Game_REWIRTE.card4_played = False # Makes so that the played haven't played card

        Game_REWIRTE.player_cards[3] = CARDS_IN_HAND4 # Re-assings the slot in the list to match that the played card

    # Checks if the player played card 5
    elif Game_REWIRTE.card5_played == True:
        CARDS_IN_HAND5 = favored_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card5_command():
            # Checks if it's  the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(CARDS_IN_HAND5 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card5.destroy() # Destroys the card

                Game_REWIRTE.card5_played = True # Sets the bollen from the Game_REWIRTE script to True
                Game_REWIRTE.player_cards[4] = "" # Assings the empty slot to the played card

                CCP.check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND5, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND5) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card5_played = True # Sets the bollen from the Game_REWIRTE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate
                    Game_REWIRTE.player_cards[3] = "" # Assings the empty slot to the gaved card

                    show_card5.destroy() # Destroys the card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card5 = Button(Game_REWIRTE.gameScreen, text = favored_card, command = card5_command, font = "20") # Creates the card
        show_card5.place(x = 170, y = 600) # Places the card at x = 170,y = 600

        Game_REWIRTE.card5_played = False # Makes so that the played haven't played card

        player_cards[4] = CARDS_IN_HAND5 # Re-assings the slot in the list to match that the played card

    # Checks if the player played card 6
    elif Game_REWIRTE.card6_played == True:
        CARDS_IN_HAND6 = favored_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card6_command():
            # Checks if it's  the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(CARDS_IN_HAND6 + "\n \n \n") # Sets the discard pile display text to the card that you've played

                show_card6.destroy() # Destroys the card

                Game_REWIRTE.card6_played = True # Sets the bollen from the Game_REWIRTE script to True

                Game_REWIRTE.player_cards[5] = "" # Assings the empty slot to the played card

                CCP.check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game", "Are you sure you want to give com1 your " + CARDS_IN_HAND6, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND6) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card6_played = True # Sets the bollen from the Game_REWIRTE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate

                    show_card6.destroy() # Destroys the card

                    Game_REWIRTE.player_cards[5] = "" # Assings the empty slot to the gaved card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card6 = Button(Game_REWIRTE.gameScreen, text = favored_card, command = card6_command, font = "20") # Creates the card
        show_card6.place(x = 330, y = 600) # Places the card at x = ,y = 600

        Game_REWIRTE.card6_played = False # Makes so that the played haven't played card

        Game_REWIRTE.player_cards[5] = CARDS_IN_HAND6 # Re-assings the slot in the list to match that the played card

    # Checks if the player played card 7
    elif Game_REWIRTE.card7_played == True:
        CARDS_IN_HAND7 = favored_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card7_command():
            # Checks if it's  the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(favored_card + "\n \n \n") # Sets the discard pile display text to the card that you've played

                show_card7.destroy() # Destroys the card

                Game_REWIRTE.card7_played = True # Sets the bollen from the Game_REWIRTE script to True

                Game_REWIRTE.player_cards[6] = "" # Assings the empty slot to the played card

                CCP.check_card_to_play(favored_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND7, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND7) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card7_played = True # Sets the bollen from the Game_REWIRTE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate

                    show_card7.destroy() # Destroys the card

                    Game_REWIRTE.player_cards[6] = "" # Assings the empty slot to the gaved card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card7 = Button(Game_REWIRTE.gameScreen, text = favored_card, command = card7_command, font = "20") # Creates the card
        show_card7.place(x = 490, y = 600) # Places the card at x = 490,y = 600

        Game_REWIRTE.card7_played = False # Makes so that the played haven't played card

        Game_REWIRTE.player_cards[6] = CARDS_IN_HAND7 # Re-assings the slot in the list to match that the played card

# Displays the cards that the player gotten from stealing a card from the com player by playing a 2 cat cards
def displayed_stolen_card(stolen_card):
    # Checks if the player played card 1
    if Game_REWIRTE.card1_played == True:
        CARDS_IN_HAND1 = stolen_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card1_command():
            # Checks if its the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(CARDS_IN_HAND1 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card1.destroy() # Destroys the card

                Game_REWIRTE.card1_played = True # Sets the bollen from the Game_REWIRTE script to True

                Game_REWIRTE.player_cards[0] = "" # Re-assings the slot in the list to match that the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND1, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND1) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card1_played = True  # Makes the bollen False

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate

                    show_card1.destroy() # Destroys the card

                    Game_REWIRTE.player_cards[0] = "" # Re-assings the slot in the list to match that the played card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card1 = Button(Game_REWIRTE.gameScreen, text = stolen_card, command = card1_command, font = "20") # Creates the card
        show_card1.place(x = 650, y = 600) # Places the card a x = 650 and y = 600

        Game_REWIRTE.card1_played = False # Makes so that the played haven't played card 1

        Game_REWIRTE.player_cards[0] = CARDS_IN_HAND1 # Assings the empty slot to the gaved card

    # Checks if the player played card 2

    elif Game_REWIRTE.card2_played == True:
        CARDS_IN_HAND2 = stolen_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card2_command():
            # Checks if it's  the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(CARDS_IN_HAND2 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card2.destroy() # Destroys the card

                Game_REWIRTE.card2_played = True # Sets the bollen from the Game_REWIRTE script to True

                Game_REWIRTE.player_cards[1] = "" # Assings the empty slot to the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND2, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND2) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card2_played = True # Sets the bollen from the Game_REWIRTE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate

                    show_card2.destroy() # Destroys the card

                    Game_REWIRTE.player_cards[1] = "" # Assings the empty slot to the gaved card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card2 = Button(Game_REWIRTE.gameScreen, text = stolen_card, command = card2_command, font = "20") # Creates the card
        show_card2.place(x = 810, y = 600) # Places the card at x = 810, y = 600

        Game_REWIRTE.card2_played = False # Makes so that the played haven't played card 2

        Game_REWIRTE.player_cards[1] = CARDS_IN_HAND2 # Re-assings the slot in the list to match that the played card

    # Checks if the player played card 3
    elif Game_REWIRTE.card3_played == True:
        CARDS_IN_HAND3 = stolen_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card3_command():
            # Checks if it's  the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(CARDS_IN_HAND3 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card3.destroy() # Destroys the card

                Game_REWIRTE.card3_played = True # Sets the bollen from the Game_REWIRTE script to True

                Game_REWIRTE.player_cards[2] = "" # Assings the empty slot to the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND3, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Asks the player for if they a sure they want to give that card to com 1
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND3) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card3_played = True # Sets the bollen from the Game_REWIRTE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate

                    show_card3.destroy() # Destroys the card

                    Game_REWIRTE.player_cards[2] = "" # Assings the empty slot to the gaved card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card3 = Button(Game_REWIRTE.gameScreen, text = stolen_card, command = card3_command, font = "20") # Creates the card
        show_card3.place(x = 960, y = 600) # Places the card at x = 960,y = 600

        Game_REWIRTE.card3_played = False # Makes so that the played haven't played card

        Game_REWIRTE.player_cards[2] = CARDS_IN_HAND3 # Re-assings the slot in the list to match that the played card

    # Checks if the player played card 4
    elif Game_REWIRTE.card4_played == True:
        CARDS_IN_HAND4 = stolen_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card4_command():
            # Checks if it's  the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(CARDS_IN_HAND4 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card4.destroy() # Destroys the card

                Game_REWIRTE.card4_played = True # Sets the bollen from the Game_REWIRTE script to True

                Game_REWIRTE.player_cards[3] = "" # Assings the empty slot to the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND4, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND4) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card4_played = True # Sets the bollen from the Game_REWIRTE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate

                    show_card4.destroy() # Destroys the card

                    Game_REWIRTE.player_cards[3] = "" # Assings the empty slot to the gaved card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card4 = Button(Game_REWIRTE.gameScreen, text = stolen_card, command = card4_command, font = "20") # Creates the card
        show_card4.place(x = 1090, y = 600) # Places the card at x = 1090,y = 600

        Game_REWIRTE.card4_played = False # Makes so that the played haven't played card

        Game_REWIRTE.player_cards[3] = CARDS_IN_HAND4 # Re-assings the slot in the list to match that the played card

    # Checks if the player played card 5
    elif Game_REWIRTE.card5_played == True:
        CARDS_IN_HAND5 = stolen_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card5_command():
            # Checks if it's  the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(CARDS_IN_HAND5 + "\n \n \n") # Sets the discard pile display text to the card that you've played
                show_card5.destroy() # Destroys the card

                Game_REWIRTE.card5_played = True # Sets the bollen from the Game_REWIRTE script to True
                Game_REWIRTE.player_cards[4] = "" # Assings the empty slot to the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND5, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND5) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card5_played = True # Sets the bollen from the Game_REWIRTE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate
                    Game_REWIRTE.player_cards[3] = "" # Assings the empty slot to the gaved card

                    show_card5.destroy() # Destroys the card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card5 = Button(Game_REWIRTE.gameScreen, text = stolen_card, command = card5_command, font = "20") # Creates the card
        show_card5.place(x = 170, y = 600) # Places the card at x = 170,y = 600

        Game_REWIRTE.card5_played = False # Makes so that the played haven't played card

        player_cards[4] = CARDS_IN_HAND5 # Re-assings the slot in the list to match that the played card

    # Checks if the player played card 6
    elif Game_REWIRTE.card6_played == True:
        CARDS_IN_HAND6 = stolen_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card6_command():
            # Checks if it's  the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(Game_REWIRTE.CARDS_IN_HAND6 + "\n \n \n") # Sets the discard pile display text to the card that you've played

                show_card6.destroy() # Destroys the card

                Game_REWIRTE.card6_played = True # Sets the bollen from the Game_REWIRTE script to True

                Game_REWIRTE.player_cards[5] = "" # Assings the empty slot to the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game", "Are you sure you want to give com1 your " + CARDS_IN_HAND6, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND6) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card6_played = True # Sets the bollen from the Game_REWIRTE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate

                    show_card6.destroy() # Destroys the card

                    Game_REWIRTE.player_cards[5] = "" # Assings the empty slot to the gaved card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card6 = Button(Game_REWIRTE.gameScreen, text = stolen_card, command = card6_command, font = "20") # Creates the card
        show_card6.place(x = 330, y = 600) # Places the card at x = ,y = 600

        Game_REWIRTE.card6_played = False # Makes so that the played haven't played card

        Game_REWIRTE.player_cards[5] = CARDS_IN_HAND6 # Re-assings the slot in the list to match that the played card

    # Checks if the player played card 7
    elif Game_REWIRTE.card7_played == True:
        CARDS_IN_HAND7 = stolen_card # Creates a varible from the argument pass through when the function was called

        # Creates a function to be used when the card is shown
        def card7_command():
            # Checks if it's  the players turn
            if Game_REWIRTE.player_turn == True:
                Game_REWIRTE.discard_pile_text.set(Game_REWIRTE.CARDS_IN_HAND7 + "\n \n \n") # Sets the discard pile display text to the card that you've played

                show_card7.destroy() # Destroys the card

                Game_REWIRTE.card7_played = True # Sets the bollen from the Game_REWIRTE script to True

                Game_REWIRTE.player_cards[6] = "" # Assings the empty slot to the played card

                CCP.check_card_to_play(stolen_card) # Checks the card, so it can do its respected function

            # Checks if com 1 played a favor
            elif C1B.card_to_play == "favor":
                favoraction = messagebox.askyesno("Exploding Kittens Game","Are you sure you want to give com1 your " + CARDS_IN_HAND7, icon = "warning") # Asks the player for if they a sure they want to give that card to com 1

                # Checks if the player clicked on "yes"
                if favoraction == True:
                    messagebox.showinfo("Exploding Kittens Game", "You have given com1 your " + CARDS_IN_HAND7) # Tells the player that there card was add to com 1's hand

                    Game_REWIRTE.card7_played = True # Sets the bollen from the Game_REWIRTE script to True

                    C1B.card_to_play = "" # Sets com 1's card to play to an empty string so the the next time the player gose to click on another card this if statment dosn't repeate

                    show_card7.destroy() # Destroys the card

                    Game_REWIRTE.player_cards[6] = "" # Assings the empty slot to the gaved card

                    draw_card() # Makes com 1 draw a card
                else:
                    messagebox.showerror("Exploding Kittens Game", "You have not given your card to com1") # Tells the player that the card that they clicked on wasn't given to com 1

            else:
                messagebox.showerror('Exploding Kittens Game', "Sorry, it's not your turn") # Tells the player that it's not there turn

        show_card7 = Button(Game_REWIRTE.gameScreen, text = stolen_card, command = card7_command, font = "20") # Creates the card
        show_card7.place(x = 490, y = 600) # Places the card at x = 490,y = 600

        Game_REWIRTE.card7_played = False # Makes so that the played haven't played card

        Game_REWIRTE.player_cards[6] = CARDS_IN_HAND7 # Re-assings the slot in the list to match that the played card

def steal_card():
    global message_box2 # Creates a global varible to be used in the Deal_To_Com_Players.py file

    # Checks if the player selected 1 com player
    if com_number == 1:
        messagebox.showwarning('Cat Cards', 'Click a card under Com 1 (Closing is required, but you can still get a card.)') # Tells the player to click a card under com 1 and that they can steal a card

    # Checks if the player selected 2 com player
    elif com_number == 2:
        message_box2 = simpledialog.askstring('Cat Cards', 'Enter the com player you want to steal from (1 or 2)') # Asks if the player who they want to steal from

        # If the player entered a number larger or smaller then 1-3 or a string
        if message_box2 > '2' or message_box2 < '1':
            messagebox.showerror('Cat Cards', 'You entered a larger number than what was expected or was a not a number.\nPlease try agin') # Tells the user that they inputed somthing that was not expected

            steal_card() # Repeates the function

        # Checks if the player inputed "1" as there input
        elif message_box2 == '1':
            messagebox.showwarning('Cat Cards', 'Click a card under Com 1 (Closing is required, but you can still get a card.)') # Tells the player to click a card under com 1 and that they can steal a card

        # Checks if the player inputed "2" as there input
        elif message_box2 == '2':
            messagebox.showwarning('Cat Cards', 'Click a card under Com 2 (Closing is required, but you can still get a card.)') # Tells the player to click a card under com 2 and that they can steal a card

    # Checks if the player selected 3 com players
    elif com_number == 3:
        message_box2 = simpledialog.askstring('Cat Cards', 'Enter the com player you want to steal from (1, 2, or 3)') # Asks the player who they want to steal a card from

        # Checks if the player inputed a number less than 1 or larger then 3 or a string
        if message_box2 > '3' or message_box2 < '1':
            messagebox.showerror('Cat Cards', 'You entered a larger number than what was expected or was a not a number.\nPlease try agin') # Tells the player that they inputed a number that was not expected

            steal_card() # Repeates the function

        # Checks if the player inputed "1" as there target
        elif message_box2 == '1':
            messagebox.showwarning('Cat Cards', 'Click a card under Com 1 (Closing is required, but you can still get a card.)') # Tells the player to click a card under com 1

        # Checks if the player inputed "2" as there target
        elif message_box2 == '2':
            messagebox.showwarning('Cat Cards', 'Click a card under Com 2 (Closing is required, but you can still get a card.)') # Tells the player to click a card under com 2

        # Checks if the player inputed "3" as there target
        elif message_box2 == '3':
            messagebox.showwarning('Cat Cards', 'Click a card under Com 3 (Closing is required, but you can still get a card.)') # Tells the player to click a card under com 3

def get_favor():
    # Checks if the player selected 3 com players
    if com_number == 3:
        message_box1 = simpledialog.askstring('Favor', 'Please enter the com player you want to ask (1, 2, 3)') # Asks the com player who they want to get a favor from

        # If the player entered a number larger or smaller then 1-3 or a string
        if message_box1 > '3' or message_box1 < '1':
            messagebox.showerror('Favor', 'You entered a larger number than what was expected or was a not a number.\nPlease try agin') # Tells the player that they've enter a larger or smaller number than what wan expected

            get_favor() # Repeates the function

        # Checks if the player want to get a favor from com 3
        elif message_box1 == '3':
            favor_card = random.choice(Game_REWIRTE.cards) # Creates a string from a random choice from the cards list
            messagebox._show('Favor', 'Com 3 has given you a ' + favor_card) # Tells the player has given them the card selected in the favor_card
            display_favored_card(favor_card) # Displays the favor
        # Checks if the player want to get a favor from com 2
        elif message_box1 == '2':
            favor_card = random.choice(Game_REWIRTE.cards)  # Creates a string from a random choice from the cards list
            messagebox._show('Favor', 'Com 2 has given you a ' + favor_card) # Tells the player has given them the card selected in the favor_card
            display_favored_card(favor_card) # Displays the favor
        # Checks if the player want to get a favor from com 1
        elif message_box1 == '1':
            favor_card = random.choice(Game_REWIRTE.cards) # Creates a string from a random choice from the cards list
            messagebox._show('Favor', 'Com 1 has given you a ' + favor_card) # Tells the player has given them the card selected in the favor_card
            display_favored_card(favor_card) # Displays the favor

    # Checks if the player selected 1 com player
    elif com_number == 1:
        favor_card = random.choice(Game_REWIRTE.cards) # Creates a string from a random choice from the cards list
        messagebox.showinfo('Favor', 'Com 1 has given you a ' + favor_card) # Tells the player has given them the card selected in the favor_card
        display_favored_card(favor_card) # Displays the favor

    # Checks if the player selected 2 com player
    elif com_number == 2:
        message_box1 = simpledialog.askstring('Favor', 'Please enter the com player you want to ask (1 or 2)') # Asks the com player who they want to get a favor from

        # If the player entered a number larger or smaller then 1-3 or a string
        if message_box1 > '2' or message_box1 < '1':
            messagebox.showerror('Favor', 'You entered a larger number than what was expected or was a not a number.\nPlease try agin') # Tells the player that they've enter a larger or smaller number than what wan expected

            get_favor() # Repeates the function
        # Checks if the player want to get a favor from com 2
        elif message_box1 == '2':
            favor_card = random.choice(Game_REWIRTE.cards) # Creates a string from a random choice from the cards list
            messagebox._show('Favor', 'Com 2 has given you a ' + favor_card) # Tells the player has given them the card selected in the favor_card
            display_favored_card(favor_card) # Displays the favor
        # Checks if the player want to get a favor from com 1
        elif message_box1 == '1':
            favor_card = random.choice(Game_REWIRTE.cards) # Creates a string from a random choice from the cards list
            messagebox._show('Favor', 'Com 1 has given you a ' + favor_card) # Tells the player has given them the card selected in the favor_card
            display_favored_card(favor_card) # Displays the favor

def cat_card_fuction(cat_card):
    global cat_card_played, cat_combo, cat_card_clicked

    # If the player has played a cat card, but has a cat card as there last card run the command below
    if cat_card_played == False:
        messagebox.showwarning('Cat Cards', 'Please play another ' + cat_card) # Tells the user to play another card of what ever cat card they played

        cat_card_played = True # Makes cat_card_played = True
        cat_card_clicked = cat_card # Used for checking if the user is played the the same kind of cat_card

    # If the cat_card_played == Ture and both cards match run the statment
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

    global first_card, second_card, thrid_card, attack_card_played

    print("Card Played: " + card_to_check)

    # If the player play a skip skip there turn and make it com1's turn
    if card_to_check == "skip":
        messagebox._show("Skip", "You have skipped your turn.")
        Game_REWIRTE.player_turn = False

        Game_REWIRTE.com1_turn = True
        C1B.decied_card_to_play()

    # If the player play a skip skip there turn and make it com1's turn and make them has 2 turns
    elif card_to_check == "attack":
        messagebox.showinfo("Attack" , "You have skiped your turn and made the com 1 player have 2 turns.")
        Game_REWIRTE.player_turn = False

        attack_card_played = True

        Game_REWIRTE.com1_turn = True
        C1B.decied_card_to_play()

    # If the player played a favor run the function below
    elif card_to_check == "favor":
        get_favor()

    # If the player played a shuffle randomly reorder the cards list
    elif card_to_check == "shuffle":
        random.shuffle(Game_REWIRTE.cards)
        random.shuffle(Game_REWIRTE.cards)
        random.shuffle(Game_REWIRTE.cards)
        random.shuffle(Game_REWIRTE.cards)
        random.shuffle(Game_REWIRTE.cards)
        random.shuffle(Game_REWIRTE.cards)
        random.shuffle(Game_REWIRTE.cards)

    # If the player played a see the future randomly pick 3 cards from the cards list and display them to the user
    elif card_to_check == "see the future":
        first_card = random.choice(Game_REWIRTE.cards)
        second_card = random.choice(Game_REWIRTE.cards)
        thrid_card = random.choice(Game_REWIRTE.cards)

        messagebox.showinfo('See The Future', 'Top card: ' + first_card + " Middle card: " + second_card + " Bottom card: " + thrid_card)

    # If the player played a cat card run the function below
    elif card_to_check == 'potato cat' or 'taco cat' or 'rainbow ralphing \n cat' or 'beard cat' or 'cattermellon':
        cat_card_fuction(card_to_check)
