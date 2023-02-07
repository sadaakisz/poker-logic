import model.card as crd
import model.deck as dck
import model.pocket as pck
import logic.hand_ranker as hr

deck = dck.Deck()
board = []
pocket = pck.Pocket()

for i in range(2):
    pocket.append(deck.get_card())

print(pocket)

for i in range(5):
    board.append(deck.get_card())

print(board)

print(pocket.hand(board))

print(hr.rank(pocket.dict_hand(board)))

board2 = []
board2.append(crd.Card(14, 'H'))
board2.append(crd.Card(13, 'H'))
board2.append(crd.Card(12, 'H'))
board2.append(crd.Card(11, 'H'))
board2.append(crd.Card(10, 'H'))

pocket2 = pck.Pocket()
pocket2.append(crd.Card(9, 'H'))
pocket2.append(crd.Card(8, 'H'))

print(hr.rank(pocket2.dict_hand(board2)))

board3 = []
board3.append(crd.Card(13, 'H'))
board3.append(crd.Card(12, 'C'))
board3.append(crd.Card(11, 'H'))
board3.append(crd.Card(10, 'H'))
board3.append(crd.Card(9, 'H'))

pocket3 = pck.Pocket()
pocket3.append(crd.Card(8, 'C'))
pocket3.append(crd.Card(7, 'H'))

print(hr.rank(pocket3.dict_hand(board3)))