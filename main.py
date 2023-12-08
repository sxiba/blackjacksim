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
    print(__cards)
    print("value: " + str(check_hand_value(hand)))
    print()

def deal_hands(game_deck):
# need to have check for consistent 21 or if dealer busts or if player busts. 
# deals hand, player gets 2 cards, dealer gets 2 but second draw is hidden. 

    # initialize cards 
    # 52 cards from game deck 
    # new list of pulled cards, removing from game deck 
    
    player_hand = [draw_card(game_deck), draw_card(game_deck)]
    print("")
    print_cards(player_hand)

    dealer_hand = [draw_card(game_deck), draw_card(game_deck)]
    print_cards(dealer_hand)
    print("what player sees: " + dealer_hand[0].card + " " + dealer_hand[0].suit)

    return player_hand, dealer_hand

# either we are checking value more than we print or vise 
def check_hand_value(hand):
    return (sum(int(card.value) for card in hand))

# Start game loop. 
def start_game():
    # game state starts as false, while user hasn't quit, continue game. 
    quit = False
    print("Welcome to blackjack.")
    print("--------------------\n\n")
    print("\nYour money: $" + str(hand))
    game_deck = Deck.create_deck()
    player_hand, dealer_hand = deal_hands(game_deck)
    while not quit: 

        # hit, stand, double, split, quit program 
        user_input = input("Hit (H) --- Stand (S) --- Quit (Q)\n")
        match user_input.lower():
            case 'h': 
                player_hand.append(draw_card(game_deck))
                print_cards(player_hand)
                
                if check_hand_value(player_hand) > 21:
                    print("You have: " + str(check_hand_value(player_hand)) + ". Sorry!")
                    quit = True
                # random sets dealer card
            case 's':
                print("\n\nDealer's turn:\n")
                while check_hand_value(dealer_hand) < 16:
                    dealer_hand.append(draw_card(game_deck))
                    if check_hand_value(dealer_hand) > 21:
                        print("Dealer has: " + str(check_hand_value(player_hand)) + ". You win!")
                print_cards(dealer_hand)

                if check_hand_value(player_hand) < check_hand_value(dealer_hand):
                    print("Dealer wins.")

                elif check_hand_value(player_hand) > check_hand_value(dealer_hand):
                    print("You win!")
                else: 
                    print("Push. Your bet is returned.")
                quit = True 
                # dealer does their thing, compares, then exits the dealt session
                # in stand, we check for 21 after dealer thinks they have a decent draw 
            case 'q':
                print("Thanks for playing!")
                quit = True
            case '_':
                print("\nInput not recognized. Try again.\n\n")
 
    exit()
   
if __name__ == "__main__": 
    start_game()
    