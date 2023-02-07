import model.card as crd
import model.pocket as pck

def make_hand(hand: list) -> dict:
    board = []
    pocket = pck.Pocket()

    for i in range(2):
        str_card = hand[i]
        card = crd.Card(str_card)
        if str(card)!='0NA':
            pocket.append(card)
    for i in range(2, len(hand)):
        str_card = hand[i]
        card = crd.Card(str_card)
        if str(card)!='0NA':
            board.append(card)
    return pocket.dict_hand(board)