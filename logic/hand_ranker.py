from copy import deepcopy

def check_special_flush(dict_hand: dict, max_value: int) -> bool:
    fl_dict_hand = deepcopy(dict_hand)
    if max_value not in fl_dict_hand.keys():
        return False
    if 14 in fl_dict_hand.keys():
        fl_dict_hand[1] = fl_dict_hand[14]
    value_index = list(fl_dict_hand.keys()).index(max_value)
    possible_sf = sum(list(fl_dict_hand.keys())[value_index:value_index+5])==(max_value-2)*5 
    if possible_sf:
        max_symbol = ''
        for symbol in fl_dict_hand[max_value]:
            max_symbol = symbol
            other_symbols = []
            for i in range(max_value-1, max_value-5, -1):
                other_symbols.append(fl_dict_hand[i])
            if other_symbols == [[max_symbol] for _ in range(4)]:
                return True
    return False

def check_pair(dict_hand: dict, existing_pair=0) -> str:
    for key in dict_hand:
        if key==existing_pair:
            continue
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
        if len(dict_hand[key])==2:
            pair = check_pair(dict_hand, key)
            if pair: return str(key)+' '+pair.split()[0]+' Two Pairs'
            return str(key)+' Pair'
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

    return str(list(dict_hand.keys())[0])+' High Card'

