class Card:
    def __init__(self, number, symbol):
        self.number = number
        self.symbol = symbol

class Player:
    def __init__(self, key, stack, name):
        self.key = key
        self.stack = []
        self.name = name
        self.number_cards = 0
    
    def add_cards(self, new_stack):
        self.stack = self.stack + new_stack
        self.number_cards = len(self.stack)

class Deck:
    def __init__(self, cards:list[Card]):
        self.cards = []
    
    #def create_deck(self):

        


