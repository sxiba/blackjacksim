#! usr/bin/python3
from blackjack import * 

MIN_BET = 2
MAX_BET = 500
blackjack = 21 


if __name__ == "__main__": 
    print("Welcome.\n" + '-'*80)
    player_balance = int(input("How much would you like to deposit (number)? \n"))
    player = Player(player_balance)
    dealer = Player(float('inf')) #or None)
    game = True
    while game:
        game_deck = Deck()
                
        player_bet = int(input("How much would you like to bet (number)? \n"))
        player.set_bet = player_bet
        print("You bet: " + str(player_bet) + "\n")
        
        player.set_hand(game_deck.deal_hand())
        dealer.set_hand(game_deck.deal_hand())
        
        print("Your hand: " + str(player.print_hand()) )        
        
        game = False
