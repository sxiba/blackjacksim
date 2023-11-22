import random 
import sys
import time 

hand = 250 

blackjack = 21 
class cards():
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
    
class deal():
    def __init__(self) -> None:
        pass
    def hit():
        pass
    
if __name__ == "__main__": 
    quit = False
    while not quit: 
        
        print("Welcome to blackjack.")
        print("--------------------")
        print("Will you play?\n\n")
        print("Hit (H) --- Quit (Q)")
        user_input = input("Hit (H) --- Quit (Q)")
        if user_input.lower() == "H": 
            print("Your pool: $" + str(hand))
            deal.hit()
            print("")
        elif user_input.lower() == "Q":
            print("Thanks for playing!")
            quit = True
            exit()
        else:
            print("Input not recognized. Try again.")
        
    pass 
   