import model.card as crd

class Pocket:
    def __init__(self) -> None:
        self.cards = []

    def append(self, card: crd.Card) -> None:
        self.cards.append(card)

    def hand(self, board) -> list:
        return sorted(self.cards+board, reverse=True)

    def dict_hand(self, board) -> dict:
        hand_dict = {}
        hand_tuples = [card.as_tuple() for card in self.hand(board)]
        for card_tuple in hand_tuples:
            if hand_dict.get(card_tuple[0]) is None:
                hand_dict[card_tuple[0]] = []
            hand_dict[card_tuple[0]].append(card_tuple[1])
        return hand_dict

    def __repr__(self) -> str:
        return str(self.cards)
