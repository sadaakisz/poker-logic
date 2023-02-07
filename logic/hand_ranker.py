import model.card as crd
def rank(dict_hand: dict) -> str:
    print(dict_hand)
    
    return

    # Royal Flush
    possible_rf = sum(dict_hand.keys()[:5])==60 # Figure out the formula
    if possible_rf:
        flush_symbol = ''
        for i in range(14, 9, -1):
            for symbol in dict_hand[i]:
                flush_symbol = symbol
        for symbol in dict_hand(14):
            # Check if symbol is present in next 5

