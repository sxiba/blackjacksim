import random 
import sys
import time 

hand = 250 

blackjack = 21 

# create card object
class Cards():
    def __init__(self) -> None:
        self.suit = None
        self.card = None 
        self.value = None
        __suits__ = ["Hearts", "Spades", "Clubs", "Diamonds"]
        __cards__ = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']
        __card_values__ = {
            "A" : 1, 
            "2" : 2,  
            "3" : 3,  
            "4" : 4,  
            "5" : 5,  
            "6" : 6,  
            "7" : 7,  
            "8" : 8,  
            "9" : 9,  
            "10" : 10,  
            "J" : 10,  
            "Q" : 10,  
            "K" : 10  
            }
        pass
    
class Deal():
    # need to have check for consistent 21 or if dealer busts or if player busts. 
    
    # deals hand, player gets 2 cards, dealer gets 2 but second draw is hidden. 
    def __init__(self, player, dealer) -> None:
        self.player = player
        self.dealer = dealer 
 
        pass
    # player gets another card if they choose 
    def hit():

        pass
    
# Start game loop. 
def start_game():
    # game state starts as false, while user hasn't quit, continue game. 
    quit = False
    while not quit: 
        print("Welcome to blackjack.")
        print("--------------------")
        print("Will you play?\n\n")
        print("Hit (H) --- Quit (Q)")
        user_input = input("Hit (H) --- Quit (Q)\n")
        if user_input.lower() == "h": 
            print("\nYour money: $" + str(hand))
            Deal.hit()
            print("")
        elif user_input.lower() == "q":
            print("Thanks for playing!")
            quit = True
        else:
            print("\nInput not recognized. Try again.\n\n")
    exit()
   
if __name__ == "__main__": 
    start_game()
    