from copy import deepcopy

def check_special_flush(dict_hand: dict, max_value: int) -> bool:
    if max_value not in dict_hand.keys():
        return False
    if 14 in dict_hand.keys():
        dict_hand[1] = dict_hand[14]
    value_index = list(dict_hand.keys()).index(max_value)
    possible_sf = sum(list(dict_hand.keys())[value_index:value_index+5])==(max_value-2)*5 
    if possible_sf:
        max_symbol = ''
        for symbol in dict_hand[max_value]:
            max_symbol = symbol
            other_symbols = []
            for i in range(max_value-1, max_value-5, -1):
                other_symbols.append(dict_hand[i])
            if other_symbols == [[max_symbol] for _ in range(4)]:
                return True
    return False

def check_pair(dict_hand: dict) -> str:
    for key in dict_hand:
        if len(dict_hand[key])==2:
            return str(key)+' Pair'
    return ''

def check_repeated(dict_hand: dict) -> str:
    for key in dict_hand:
        if len(dict_hand[key])==4:
            return str(key)+' Four of a Kind'
        if len(dict_hand[key])==3:
            pair = check_pair(dict_hand)
            if pair: return str(key)+' '+pair.split()[0]+' Full House'
            return str(key)+' Three of a Kind'
    return ''

def rank(dict_hand: dict) -> str:
    print(dict_hand)

    if check_special_flush(dict_hand, 14):
        return str(14)+' Royal Flush'
    
    for i in range(13, 4, -1):
        if check_special_flush(dict_hand, i):
            return str(i)+' Straight Flush'
    
    repeated = check_repeated(dict_hand)
    if repeated: return repeated

    return 'High Card'

