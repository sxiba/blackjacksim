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
            # grey out the check for double prior to player decision if they do not have enough
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
                    player.bet_amount*=2 
                    if player.bet_amount > player_balance:
                        print("You do not have enough to double. Try again.\n")
                        continue
                    return
                case 's':
                    print("You choose to stand.\n")
                    return    
                case 'q':
                    print("Thanks for playing!\n")
                    exit()
                case _:
                    print("Input not recognized. Try again.\n")
                    
    def game_resolution(): 
        print("Your hand: " + str(player.print_hand()))        
        print("Dealer's hand:" + str(dealer.print_hand()) + "\n")
        if player.hand_value > 21: 
            print("Your hand was over 21, you lose.\n")
            # print(player.bet_amount)
            player.update_balance(-1)
            return
        elif player.hand_value <= 21: 
            if dealer.hand_value > 21: 
                print("The dealer busts. You win!\n")
                player.update_balance(1)
                return 
                
            elif dealer.hand_value <= 21: 
                if player.hand_value == dealer.hand_value: 
                    print("You tied with the dealer. Your funds will be returned to your balance shortly.\n")
                    player.update_balance(0)
                    return

                # natural blackjack
                elif dealer.hand_value == 21 and len(dealer.hand) == 2:
                    print("The dealer drew a blackjack. You lose.\n")
                    player.update_balance(-1)
                    return
                
                # natural blackjack
                elif player.hand_value == 21 and len(player.hand) == 2:
                    print("You drew a blackjack. You win!\n")
                    player.update_balance(-1)
                    return
                
                elif dealer.hand_value > player.hand_value:
                    print("You lose.")
                    player.update_balance(-1)
                    return
                # player has greater hand value than dealer, wins 
                else: 
                    print("You win! You will be paid out shortly.\n")
                    player.update_balance(1) 
                    return
        else:
            return
        
    while game:
        game_deck = Deck()
                
        player_bet = int(input("How much would you like to bet (number)? \n"))
        if player_bet > player.balance or player_bet < MIN_BET: 
            print("Your bet is invalid. Try again.\n")
            continue
        player.set_bet(player_bet)

        print("\nYou bet: " + str(player_bet) + "\n")
        
        player.set_hand(game_deck.deal_hand())
        dealer.set_hand(game_deck.deal_hand())
        
        print("Your hand: " + str(player.print_hand()))        
        print("Dealer's hand:" + str([dealer.hand[0].print_card()]) + "\n")
        
        # blackjack.
        if player.hand_value == 21:
            print("You win! You have blackjack!\n")
            game_resolution()
            continue 
     
        hands = [player.hand]
        # check for pairs/split
        if player.hand[0].value == player.hand[1].value:
            player_split = str(input("Would you like to split (Enter Y/N)? \n\n")).lower()
            if player_split == "y":
                num_hands = 2 
                print("You split.")
                hands = [player.hand[0]], [player.hand[1]]
                print(hands)

        for i in range(0, num_hands):
            
            print(f"Your {i+1} thstrd hand: ")
            player.hand = hands[i]
            
            player_decision()
            
        # dealer hand
        while dealer.hand_value < 17: 
            dealer.append_card_to_hand(game_deck.draw_card())
            
        for i in range(0, num_hands):
            player.hand = hands[i]
            game_resolution()
            
        print("Your current balance is: " + str(player.balance))
        play_again = input("Play again? (Yes/No)\n").lower()
        match play_again:
            case 'yes' | 'y':
                if player.balance <= 0: 
                    print("Insufficient funds. Deposit more funds.\n")
                    game = False
                continue
            case 'no' | 'n':
                print("Thanks for playing!")
                game = False
                break
            case '_':
                print("Input not recognized. Try again.\n")