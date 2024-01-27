#!/usr/bin/python3
import random

# Create card object 
class Cards(): 
    def __init__(self, suit, card, value) -> None:
        self.suit = suit
        self.card = card 
        self.value = value
        pass
    
    # prints a singular card
    def print_card(self):
        return self.card + " " + self.suit
    
    
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
        self.deck = Deck.create_deck()
        pass
    def create_deck():
        """Creates n number of decks where n is a random integer (1-8)."""
        _deck = []
        for suit in Deck.suits: 
            for card in Deck.cards:
                _deck.append(Cards(suit, card, Deck.card_values[card]))
        return _deck*random.randint(1,8)
    
    def draw_card(self):
        """Draw a card from a deck"""
        drawn = random.choice(self.deck)
        self.deck.remove(drawn)
        return drawn
    def deal_hand(self):
        # returns a list of cards (two)
        hand = [self.draw_card() for i in range(0,2)]
        return hand
    
class Player():
    def __init__(self, bal) -> None:
        self.hand = None
        self.balance = bal
        self.bet_amount = None
        self.hand_value = None
        pass
    
    def update_balance(self,bal):
        self.balance += bal
        
    def set_bet(self,bet):
        self.bet_amount = bet
 
    def set_hand(self, hand):
        self.hand = hand 
        self.update_value()
    
    def append_card_to_hand(self, card):
        self.hand.append(card)
        self.update_value()
        
    def update_value(self):
        ace_count, total_value = 0, 0
        for card in self.hand:
            value = card.value
            ace_count += (value == 11)
            total_value += value

        # Aces are valued 1 if they would cause a bust if valued at 11
        if total_value > 21 and ace_count > 0:
            reductions_needed = int((total_value - 21)/10) + 1 # refer to pep 8?
            total_value -= reductions_needed*10 if reductions_needed <= ace_count else ace_count*10
        self.hand_value = total_value
        
    def print_hand(self):
        hand = []
        for card in self.hand:
            hand.append(card.print_card())
        return hand
