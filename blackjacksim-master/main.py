import random 


blackjack = 21
suites = ["Spades", "Clubs", "Diamonds", "Hearts"]
class cards():
    def __init__(self) -> None:
        deck = cards.initDeck()

    def initDeck():
        deck = [dict() for x in range(52)] 
        i = 0
        for suite in suites: 
            for j in range(1,14):
                deck[i] = cards.createCard(
                    suite,
                    j,
                    j > 10,
                    i
                )
                i += 1

        return deck            

    def createCard(suite, value, royalty, index):
        return {
            "Suite": suite, 
            "Value": value, 
            "Royalty": royalty, 
            "Deck position": index
            }



    
class deal():
    def __init__(self) -> None:
        pass
    
if __name__ == "__main__": 
    cards.initDeck()
   