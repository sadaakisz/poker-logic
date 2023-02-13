import model.deck as dck
import model.pocket as pck
import logic.hand_ranker as hr
import logic.hand_maker as hm
import dataset.test_runner as tr

for a in range(1):
    deck = dck.Deck()
    board = []
    p1 = pck.Pocket()
    p2 = pck.Pocket()
    p3 = pck.Pocket()
    p4 = pck.Pocket()

    for i in range(2):
        p1.append(deck.get_card())
        p2.append(deck.get_card())
        p3.append(deck.get_card())
        p4.append(deck.get_card())
    
    for i in range(5):
        board.append(deck.get_card())

    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(board)

    list_ranks = []
    list_ranks.append(hr.list_rank(p1.dict_hand(board)))
    list_ranks.append(hr.list_rank(p2.dict_hand(board)))
    list_ranks.append(hr.list_rank(p3.dict_hand(board)))
    list_ranks.append(hr.list_rank(p4.dict_hand(board)))

    print(hr.winner(list_ranks, show_hand=True))