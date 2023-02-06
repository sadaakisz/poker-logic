import model.card as crd
def rank(hand: list) -> str:
    tuples = [card.as_tuple() for card in hand]

    print(tuples)

    # Royal Flush
    if len(hand)>=5:
        pass