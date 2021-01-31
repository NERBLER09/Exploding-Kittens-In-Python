# Imports all the modules needed 
# from Game_REWRITE import *
import Game_REWRITE

# Creates a dictionary containing all the amounts of cards
card_amounts = {
    'nope': 5,
    'attack': 4,
    'skip': 4,
    'favor': 4,
    'shuffle': 4,
    'see the future': 5,
    'potato cat': 5,
    'taco cat': 5,
    'rainbow ralphing cat': 5,
    'beard cat': 5,
    'cattermellon': 5,
    "diffuse": 6
}

# Creates a function to check the the card that com player(s) or the player has drawn to get removed from the deck
def check_card(card_to_check):
    # Checks if card drawn is equal to "nope"
    if card_to_check == 'nope':
        card_amounts['nope'] -= 1 # Removes the card from the deck

        # Checks if there is no more nope cards 
        if card_amounts['nope'] == 0:
            Game_REWRITE.cards.remove('nope') # Removes the card from the cards list 
            print("There is no nope cards") # Prints "There is no nope cards" (For Debuging)

    # Checks if card drawn is equal to "attack"
    elif card_to_check == 'attack': 
        card_amounts['attack'] -= 1 # Removes the card from the deck

        # Checks if there is no more attack cards 
        if card_amounts['attack'] == 0:
            Game_REWRITE.cards.remove('attack') # Removes the card from the cards list 
            print("There is no attack cards") # Prints "There is no attack cards" (For Debuging)

    # Checks if card drawn is equal to "skip"
    elif card_to_check == 'skip':
        card_amounts['skip'] -= 1 # Removes the card from the deck

        # Checks if there is no more skip cards 
        if card_amounts['skip'] == 0:
            Game_REWRITE.cards.remove('skip') # Removes the card from the cards list 
            print("There is no skip cards") # Prints "There is no skip cards" (For Debuging)

    # Checks if card drawn is equal to "favor"
    elif card_to_check ==  'favor':
        card_amounts['favor'] -= 1 # Removes the card from the deck

        # Checks if there is no more favor cards 
        if card_amounts[ 'favor'] == 0:
            Game_REWRITE.cards.remove( 'favor') # Removes the card from the cards list
            print("There is no favor cards") # Prints "There is no favor cards" (For Debuging)

    # Checks if card drawn is equal to "see the future"
    elif card_to_check == 'see the future':
        card_amounts['see the future'] -= 1 # Removes the card from the deck

        # Checks if there is no more see the future cards 
        if card_amounts['see the future'] == 0:
            Game_REWRITE.cards.remove('see the future') # Removes the card from the cards list 
            print("There is no see the future cards") # Prints "There is no see the future cards" (For Debuging)

    # Checks if card drawn is equal to "shuffle"
    elif card_to_check == 'shuffle':
        card_amounts['shuffle'] -= 1 # Removes the card from the deck

        # Checks if there is no more shuffle cards 
        if card_amounts['shuffle'] == 0:
            Game_REWRITE.cards.remove('shuffle') # Removes the card from the cards list 
            print("There is no shuffle cards") # Prints "There is no shuffle cards" (For Debuging)

    # Checks if card drawn is equal to "potato cat"
    elif card_to_check == 'potato cat':
        card_amounts['potato cat'] -= 1 # Removes the card from the deck

        # Checks if there is no more potato cat cards 
        if card_amounts['potato cat'] == 0:
            Game_REWRITE.cards.remove('potato cat') # Removes the card from the cards list 
            print("There is no potato cat cards") # Prints "There is no potato cat cards" (For Debuging)

    # Checks if card drawn is equal to "taco cat"
    elif card_to_check == 'taco cat':
        card_amounts['taco cat'] -= 1 # Removes the card from the deck

        # Checks if there is no more taco cat cards 
        if card_amounts['taco cat'] == 0:
            Game_REWRITE.cards.remove('taco cat') # Removes the card from the cards list 
            print("There is no taco cat cards") # Prints "There is no taco cat cards" (For Debuging)

    # Checks if card drawn is equal to " rainbow ralphing cat"
    elif card_to_check == 'rainbow ralphing \n cat':
        card_amounts['rainbow ralphing cat'] -= 1 # Removes the card from the deck

        # Checks if there is no more rainbow ralphing cat cards 
        if card_amounts['rainbow ralphing cat'] == 0:
            Game_REWRITE.cards.remove('rainbow ralphing \n cat') # Removes the card from the cards list  
            print("There is no rainbow ralphing cat cards") # Prints "There is no rainbow ralphing cat cards" (For Debuging)

    # Checks if card drawn is equal to "beard cat"
    elif card_to_check ==  'beard cat':
        card_amounts['beard cat'] -= 1 # Removes the card from the deck

        # Checks if there is no more beard cat cards 
        if card_amounts['beard cat'] == 0:
            Game_REWRITE.cards.remove('beard cat') # Removes the card from the cards list
            print("There is no beard cat cards") # Prints "There is no beard cat cards" (For Debuging)

    # Checks if card drawn is equal to "cattermellon"
    elif card_to_check == 'cattermellon':
        card_amounts['cattermellon'] -= 1 # Removes the card from the deck

        # Checks if there is no more cattermellon cards 
        if card_amounts['cattermellon'] == 0:
            Game_REWRITE.cards.remove('cattermellon') # Removes the card from the cards list 
            print("There is no cattermellon cards") # Prints "There is no cattermellon cards" (For Debuging)

    # Removes a given or drawn a diffuse card
    elif card_to_check == "diffuse":
        card_amounts["diffuse"] -= 1
        
        if card_amounts["diffuse"] == 0:
            Game_REWRITE.cards.remove("diffuse")
