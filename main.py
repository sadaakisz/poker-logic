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

hr.rank(pocket.dict_hand(board))