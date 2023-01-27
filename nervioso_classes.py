import random


class Card:
    def __init__(self, number, symbol):
        self.number = number
        self.symbol = symbol


class Player:
    def __init__(self, key, name):
        self.key = key
        self.stack = []
        self.name = name
        self.number_cards = 0

    def add_cards(self, new_stack):
        self.stack = self.stack + new_stack
        self.number_cards = len(self.stack)


class Deck:
    def __init__(self, cards: list[Card]):
        self.cards = []
        self.number_cards = len(self.cards)
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        # create the 52 cards
        for i in range(1, 14):
            symbols = ['spades', 'hearts', 'diamonds', 'clubs']
            for j in range(4):
                card = Card(i, symbols[j])
                self.cards.append(card)
        # initialize the number of cards (52)
        self.number_cards = len(self.cards)
    
    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.cards)
    
    def get_card(self):
        # get a card from the deck
        card = self.cards.pop()
        self.number_cards = len(self.cards)
        return card
    
    def reset_deck(self):
        # reset the deck
        self.cards = []
        self.number_cards = len(self.cards)
        self.create_deck()
        self.shuffle()

