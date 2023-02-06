import random
import model.card as crd

class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.create_deck()
    
    def create_deck(self) -> None:
        self.cards = []
        for symbol in list(crd.Symbol):
            for value in list(crd.Value):
                self.cards.append(crd.Card(value.value, symbol.value))
        self.shuffle_deck()
    
    def shuffle_deck(self) -> None:
        random.shuffle(self.cards)

    def get_card(self) -> crd.Card:
        return self.cards.pop()