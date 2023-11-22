import random 
import sys
import time 

hand = 250 

blackjack = 21 
class Cards():
    def __init__(self) -> None:
        suits = {"Hearts", "Spades", "Clubs", "Diamonds"}
        deck = {
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
def start_game():
    quit = False
    if quit == True: 
        print("here")
        exit()
    else: 
        while not quit: 
            print("Welcome to blackjack.")
            print("--------------------")
            print("Will you play?\n\n")
            print("Hit (H) --- Quit (Q)")
            user_input = input("Hit (H) --- Quit (Q)")
            if user_input.lower() == "h": 
                print("Your pool: $" + str(hand))
                Deal.hit()
                print("")
            elif user_input.lower() == "q":
                print("Thanks for playing!")
                quit = True
            else:
                print("Input not recognized. Try again.")
        
    pass 
   
if __name__ == "__main__": 
    start_game()
    