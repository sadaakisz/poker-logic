import model.card as crd
import model.deck as dck
import model.pocket as pck
import logic.hand_ranker as hr
import logic.hand_maker as hm

for a in range(1):

    deck = dck.Deck()
    board = []
    pocket = pck.Pocket()

    # Royal Flush
    rf_hand = hm.make_hand(['14H', '13H', '12H', '11H', '10H', '9H', '8H'])
    # Straight Flush (edge)
    sf_hand1 = hm.make_hand(['14C', '13H', '12H', '11H', '10H', '9H', '8H'])
    # Straight Flush
    sf_hand2 = hm.make_hand(['9C', '8C', '7C', '6C', '5C', '9H', '8H'])
    # Straight Flush (edge)
    sf_hand3 = hm.make_hand(['5S', '4S', '3S', '2S', '14S', '9H', '8H'])
    print(hr.rank(rf_hand))
    print(hr.rank(sf_hand1))
    print(hr.rank(sf_hand2))
    print(hr.rank(sf_hand3))