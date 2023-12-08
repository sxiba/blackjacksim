import random 
import sys
import time 

hand = 250 

blackjack = 21 

# create card object, n amount of decks played at once 
class Deck():
    # n sets of deck 
    suits = ["of Hearts", "of Spades", "of Clubs", "of Diamonds"]
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                'J', 'K', 'Q']
    card_values = {
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
    
    def __init__(self) -> None:
        pass
    
    def create_deck():
        _deck = []
        i = 0
        for suit in Deck.suits: 
            for card in Deck.cards:
                _deck.append(Cards(suit, card, Deck.card_values[card]))
        return _deck 
    # intializing deck with standard rules or with house advantage 

    #     if random.randint(0,1) == 0: 
    #           deck.append(Cards('of Spades', 'A', '1'))
    
def draw_card(deck):
    drawn = random.choice(deck)
    deck.remove(drawn)
    return drawn

# Create card object 
class Cards(): 
    def __init__(self, suit, card, value) -> None:
        self.suit = suit
        self.card = card 
        self.value = value
        pass

# card.card moment
def print_cards(hand):
    __cards = []
    for card in hand: 
        __cards.append(card.card + " " + card.suit)
    return __cards

def deal():
# need to have check for consistent 21 or if dealer busts or if player busts. 
# deals hand, player gets 2 cards, dealer gets 2 but second draw is hidden. 

    # initialize cards 
    # 52 cards from game deck 
    # new list of pulled cards, removing from game deck 
    game_deck = Deck.create_deck()
    player_hand = [draw_card(game_deck), draw_card(game_deck)]
    print("")
    print(print_cards(player_hand), )
    dealer_hand = [draw_card(game_deck), draw_card(game_deck)]
    print(print_cards(dealer_hand))
    exit()
    dealer_hand = [random.choice(game_deck), random.choice(game_deck)]
    print(print_cards(dealer_hand[0]), print_cards(dealer_hand[1]))
    # if either cards are ace, show 1 or 11
    if player_hand[0] == 1: 
        print(player_hand[0][2], player_hand[1][2])
        print("Hand is either " + player_hand[0][2] + " or 11")
        
        
         
    pass
# Start game loop. 
def start_game():
    # game state starts as false, while user hasn't quit, continue game. 
    quit = False
    while not quit: 
        print("Welcome to blackjack.")
        print("--------------------\n\n")
        # print("Will you play?\n\n")
        
        # hit, stand, double, split, quit program 
        user_input = input("Hit (H) --- Quit (Q)\n")
        if user_input.lower() == "h": 
            print("\nYour money: $" + str(hand))
            deal()

            print("")
        elif user_input.lower() == "q":
            print("Thanks for playing!")
            quit = True
        else:
            print("\nInput not recognized. Try again.\n\n")
    exit()
   
if __name__ == "__main__": 
    start_game()
    