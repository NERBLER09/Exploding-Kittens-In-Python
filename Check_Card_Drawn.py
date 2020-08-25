# Imports all the moduals needed 
# from Game_REWIRTE import *
import Game_REWIRTE

# Creates a dictonay caontaing all the ammounts of cards
card_ammounts = {
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
}

# Creates a function to check the the com player(s) or the player drawed 
def check_card(card_to_check):
    # Checks if card drawn is equal to "nope"
    if card_to_check == 'nope':
        card_ammounts['nope'] -= 1 # Removes the card from the deck

        # Checks if there is no more nope cards 
        if card_ammounts['nope'] == 0:
            Game_REWIRTE.cards.remove('nope') # Revoves the card from the cards list 
            print("There is no nope cards") # Prints "There is no nope cards" (For Debuging)

    # Checks if card drawn is equal to "attack"
    elif card_to_check == 'attack': 
        card_ammounts['attack'] -= 1 # Removes the card from the deck

        # Checks if there is no more attack cards 
        if card_ammounts['attack'] == 0:
            Game_REWIRTE.cards.remove('attack') # Revoves the card from the cards list 
            print("There is no attack cards") # Prints "There is no attack cards" (For Debuging)

    # Checks if card drawn is equal to "skip"
    elif card_to_check == 'skip':
        card_ammounts['skip'] -= 1 # Removes the card from the deck

        # Checks if there is no more skip cards 
        if card_ammounts['skip'] == 0:
            Game_REWIRTE.cards.remove('skip') # Revoves the card from the cards list 
            print("There is no skip cards") # Prints "There is no skip cards" (For Debuging)

    # Checks if card drawn is equal to "favor"
    elif card_to_check ==  'favor':
        card_ammounts['favor'] -= 1 # Removes the card from the deck

        # Checks if there is no more favor cards 
        if card_ammounts[ 'favor'] == 0:
            Game_REWIRTE.cards.remove( 'favor') # Revoves the card from the cards list
            print("There is no favor cards") # Prints "There is no favor cards" (For Debuging)

    # Checks if card drawn is equal to "see the future"
    elif card_to_check == 'see the future':
        card_ammounts['see the future'] -= 1 # Removes the card from the deck

        # Checks if there is no more see the future cards 
        if card_ammounts['see the future'] == 0:
            Game_REWIRTE.cards.remove('see the future') # Revoves the card from the cards list 
            print("There is no see the future cards") # Prints "There is no see the future cards" (For Debuging)

    # Checks if card drawn is equal to "shuffle"
    elif card_to_check == 'shuffle':
        card_ammounts['shuffle'] -= 1 # Removes the card from the deck

        # Checks if there is no more shuffle cards 
        if card_ammounts['shuffle'] == 0:
            Game_REWIRTE.cards.remove('shuffle') # Revoves the card from the cards list 
            print("There is no shuffle cards") # Prints "There is no shuffle cards" (For Debuging)

    # Checks if card drawn is equal to "potato cat"
    elif card_to_check == 'potato cat':
        card_ammounts['potato cat'] -= 1 # Removes the card from the deck

        # Checks if there is no more potato cat cards 
        if card_ammounts['potato cat'] == 0:
            Game_REWIRTE.cards.remove('potato cat') # Revoves the card from the cards list 
            print("There is no potato cat cards") # Prints "There is no potato cat cards" (For Debuging)

    # Checks if card drawn is equal to "taco cat"
    elif card_to_check == 'taco cat':
        card_ammounts['taco cat'] -= 1 # Removes the card from the deck

        # Checks if there is no more taco cat cards 
        if card_ammounts['taco cat'] == 0:
            Game_REWIRTE.cards.remove('taco cat') # Revoves the card from the cards list 
            print("There is no taco cat cards") # Prints "There is no taco cat cards" (For Debuging)

    # Checks if card drawn is equal to " rainbow ralphing cat"
    elif card_to_check == 'rainbow ralphing \n cat':
        card_ammounts['rainbow ralphing cat'] -= 1 # Removes the card from the deck

        # Checks if there is no more rainbow ralphing cat cards 
        if card_ammounts['rainbow ralphing cat'] == 0:
            Game_REWIRTE.cards.remove('rainbow ralphing \n cat') # Revoves the card from the cards list  
            print("There is no rainbow ralphing cat cards") # Prints "There is no rainbow ralphing cat cards" (For Debuging)

    # Checks if card drawn is equal to "beard cat"
    elif card_to_check ==  'beard cat':
        card_ammounts['beard cat'] -= 1 # Removes the card from the deck

        # Checks if there is no more beard cat cards 
        if card_ammounts['beard cat'] == 0:
            Game_REWIRTE.cards.remove('beard cat') # Revoves the card from the cards list
            print("There is no beard cat cards") # Prints "There is no beard cat cards" (For Debuging)

    # Checks if card drawn is equal to "cattermellon"
    elif card_to_check == 'cattermellon':
        card_ammounts['cattermellon'] -= 1 # Removes the card from the deck

        # Checks if there is no more cattermellon cards 
        if card_ammounts['cattermellon'] == 0:
            Game_REWIRTE.cards.remove('cattermellon') # Revoves the card from the cards list 
            print("There is no cattermellon cards") # Prints "There is no cattermellon cards" (For Debuging)
