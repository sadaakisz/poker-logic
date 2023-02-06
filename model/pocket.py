import model.card as crd

class Pocket:
    def __init__(self) -> None:
        self.cards = []

    def append(self, card: crd.Card) -> None:
        self.cards.append(card)

    def hand(self, board) -> list:
        return sorted(self.cards+board, reverse=True)
    
    def __repr__(self) -> str:
        return str(self.cards)