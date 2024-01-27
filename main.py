#!/usr/bin/python3
from blackjack import * 

MIN_BET = 2
MAX_BET = 500
blackjack = 21 


if __name__ == "__main__": 
    
    print("Welcome.\n" + '-'*80)
    
    player_balance = int(input("How much would you like to deposit (number)? \n"))
    player = Player(player_balance)
    dealer = Player(float('inf')) #or None)
    
    split = False
    num_hands = 1
    game = True
    
    def player_decision():
        while 1:
            user_input = input("Hit (H) --- Stand (S) --- Double (D) --- Quit (Q)\n")            
            match user_input.lower():
                case 'h': 
                    player.append_card_to_hand(game_deck.draw_card())
                    print(player.hand_value)
                    print(player.print_hand())
                    if player.hand_value > 21: 
                        return
                case 'd': 
                    player.append_card_to_hand(game_deck.draw_card())
                    return
                case 's':
                    print("You choose to stand.")
                    return    
                case 'q':
                    print("Thanks for playing!\n")
                    exit()
                case _:
                    print("Input not recognized. Try again.\n")

    while game:
        game_deck = Deck()
                
        player_bet = int(input("How much would you like to bet (number)? \n\n"))
        player.set_bet = player_bet
        print("You bet: " + str(player_bet) + "\n")
        
        player.set_hand(game_deck.deal_hand())
        dealer.set_hand(game_deck.deal_hand())
        
        print("Your hand: " + str(player.print_hand()))        
    
        # blackjack
        if player.hand_value >= 21:
            print("You win! You have blackjack!")
            game = False
        # player.hand[0] = Cards("of Hearts", 'A', 11)
        # player.hand[1] = Cards("of Hearts", 'A', 11)
        
        # check for pairs/split
        if player.hand[0].value == player.hand[1].value:
     
            player_split = str(input("Would you like to split (Enter Y/N)? \n\n")).lower()
            if player_split == "y":
                num_hands = 2 
                print("You split.")
                hands = [player.hand[0]], [player.hand[1]]
                print(hands)
        else:
            hands = [player.hand]
        for i in range(0, num_hands):
            print(f"Your {i+1} thstrd hand: ")
            player.hand = hands[i]
            
            player_decision()
        
        # dealer hand
        while dealer.hand_value < 17: 
            dealer.append_card_to_hand(game_deck.draw_card())
    # TODO: game resolution 
    # TODO: payout 