#! usr/bin/python3

import random 
import sys
import time 

INITIAL_PLAYER_BALANCE = 250 
MIN_BET = 2
MAX_BET = 500
blackjack = 21 

# create card object, n amount of decks played at once 
class Deck():
    # n sets of deck 
    suits = ["of Hearts", "of Spades", "of Clubs", "of Diamonds"]
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']
    card_values = {
        "A" : 11, 
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
        """Creates n number of decks where n is a random integer (1-8)."""
        _deck = []
        for suit in Deck.suits: 
            for card in Deck.cards:
                _deck.append(Cards(suit, card, Deck.card_values[card]))
        return _deck*random.randint(1,8)

# Create card object 
class Cards(): 
    def __init__(self, suit, card, value) -> None:
        self.suit = suit
        self.card = card 
        self.value = value
        pass

def draw_card(deck):
    """Draw random card and remove from deck."""
    drawn = random.choice(deck)
    deck.remove(drawn)
    return drawn

# card.card moment
def print_cards(hand):
    """Helper function to print the cards on hand."""
    __cards = []
    for card in hand: 
        __cards.append(card.card + " " + card.suit)
    print(__cards)
    print("value: " + str(check_hand_value(hand)))
    print()

def deal_hands(game_deck):
    """Draw random cards for player and dealer."""
# need to have check for consistent 21 or if dealer busts or if player busts. 
# deals hand, player gets 2 cards, dealer gets 2 but second draw is hidden. 

    # initialize cards 
    # 52 cards from game deck 
    # new list of pulled cards, removing from game deck 
    
    player_hand = [draw_card(game_deck), draw_card(game_deck)]
    print("")
    print("Player's initial hand:")
    print_cards(player_hand)

    dealer_hand = [draw_card(game_deck), draw_card(game_deck)]
    print("Dealer's initial hand:")
    print_cards(dealer_hand)
    print("what player sees: " + dealer_hand[0].card + " " + dealer_hand[0].suit+"\n")

    return player_hand, dealer_hand

# either we are checking value more than we print or vise 
def check_hand_value(hand):
    #return (sum(int(card.value) for card in hand))
    aceCount = 0
    totalValue = 0
    for card in hand:
        value = card.value
        aceCount += (value == 11)
        totalValue += value

    #Aces are valued 1 if they would cause a bust if valued at 11
    if totalValue > 21 and aceCount > 0:
        reductionsNeeded = int((totalValue - 21)/10) + 1 # refer to pep 8?
        totalValue -= reductionsNeeded*10 if reductionsNeeded <= aceCount else aceCount*10
    return totalValue

def settle_bet(player_balance):
    """
    Asks how much the player wants to bet for the current hand.
    Returns player_bet (int).
    """
    while True:
        bet_input = input("Enter a bet for this hand:\n")
        try:
            player_bet = int(bet_input)
            if player_bet >= MIN_BET and player_bet <= MAX_BET and player_bet <= player_balance:
                return player_bet
            elif player_bet > player_balance:
                print("You bet more than you have. Try again.\n")
            else:
                print("Acceptable bet amounts are between $" + str(MIN_BET) + " and $" 
                    +str(MAX_BET)+"\n")
        except ValueError:
            print("Please enter an integer value.\n")

def player_action():
    """
    Manages player action here (bet, stand, split, double, quit)
    returns string 
    """
    # game state starts as false, while user hasn't quit, continue game. 
    game_deck = Deck.create_deck()
    player_hand, dealer_hand = deal_hands(game_deck)
    split = False
    
    #check for blackjack
    if check_hand_value(player_hand) == 21:
        if(check_hand_value(dealer_hand) == 21):
            print("Both parties have Blackjack! Your bet is returned")
            return "Draw" 
        else:
            print("Blackjack! You win.\n")
            return "Natural"
        quit = True
    elif check_hand_value(dealer_hand) == 21:
        print("Dealer has Blackjack! Dealer wins.\n")
        return "Loss"
    
    # check if the cards are the same before offering split. 
    if player_hand[0].card == player_hand[1].card:
        split = True
        
    while True: 
        # hit, stand, double, split, quit program 
        if split: 
            user_input = input("Hit (H) --- Stand (S) --- Split (X) --- Quit (Q)\n")
                
        else: 
            user_input = input("Hit (H) --- Stand (S) --- Quit (Q)\n")
        match user_input.lower():
            case 'h': 
                player_hand.append(draw_card(game_deck))
                print_cards(player_hand)
                
                if check_hand_value(player_hand) > 21:
                    print("You have: " + str(check_hand_value(player_hand)) 
                        + ". Sorry!")
                    return "Loss"
                # random sets dealer card
            case 's':
                print("\n\nDealer's turn:\n")
                while check_hand_value(dealer_hand) <= 16:
                    dealer_hand.append(draw_card(game_deck))
                    print("Dealer's hand after hitting:")
                    print_cards(dealer_hand)

                #confirm dealer did not bust
                if check_hand_value(dealer_hand) > 21:
                    print("Dealer has: " + str(check_hand_value(dealer_hand)) 
                        + ". You win!\n")
                    return "Win"
                print("End of Dealer's turn\n")

                #print final hands for verification
                print("Player's final hand:")
                print_cards(player_hand)
                print("Dealer's final hand:")
                print_cards(dealer_hand)

                #check the game outcome
                if check_hand_value(player_hand) < check_hand_value(dealer_hand):
                    print("Dealer wins.\n")
                    return "Loss"
                elif check_hand_value(player_hand) > check_hand_value(dealer_hand):
                    print("You win!\n")
                    return "Win"
                else: 
                    print("Push. Your bet is returned.\n")
                    return "Draw"
            # split case, play one hand out entirely before moving to next 
            case 'x': print("peepeepoopoo"); exit()
            case 'q':
                print("Thanks for playing!\n")
                exit()
            case _:
                print("Input not recognized. Try again.\n")

def game_start(player_balance):
    """ Starts and continues game loop."""
    user_input = 'y'
    while True:
        match user_input.lower():
            case "y":
                print("Let's play blackjack.\n"+'-'*80)
                print("Your money: $" + str(player_balance))
                bet_amount = settle_bet(player_balance) 
                result = player_action()
                match result:
                    case "Win": player_balance += bet_amount
                    case "Natural": player_balance += 1.5*bet_amount
                    case "Loss": player_balance -= bet_amount
                    case _: player_balance
            case "q" | "n": exit()
            case _: print("Input not recognized. Try again.\n")   
        user_input = input("Play Again? --- Yes (Y) --- No (N)\n\n")
        
if __name__ == "__main__": 
    print("Welcome.\n" + '-'*80)
    player_balance = int(input("How much would you like to deposit (number)? \n"))
    game_start(player_balance)