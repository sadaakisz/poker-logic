import model.card as crd
import model.deck as dck
import model.pocket as pck
import logic.hand_ranker as hr

for a in range(20):

    deck = dck.Deck()
    board = []
    pocket = pck.Pocket()

    for i in range(2):
        pocket.append(deck.get_card())

    for i in range(5):
        board.append(deck.get_card())

    print(hr.rank(pocket.dict_hand(board)))