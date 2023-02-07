from copy import deepcopy

def check_special_flush(dict_hand: dict, max_value: int) -> bool:
    fl_dict_hand = deepcopy(dict_hand)
    if max_value not in fl_dict_hand.keys():
        return False
    if 14 in fl_dict_hand.keys():
        fl_dict_hand[1] = fl_dict_hand[14]
    keys_list = list(fl_dict_hand.keys())
    value_index = keys_list.index(max_value)
    possible_sf = sum(keys_list[value_index:value_index+5])==(max_value-2)*5 
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

def check_flush(dict_hand: dict) -> str:
    symbols = ['D','C','H','S']
    max_value = {'D': 0, 'C': 0, 'H': 0, 'S': 0}
    symbol_counter = []
    for symbol in symbols:
        symbol_counter.append(0)
        for key in dict_hand:
            if symbol in dict_hand[key]:
                max_value[symbol] = max(max_value[symbol], key)
                symbol_counter[-1]+=1
    if 5 in symbol_counter:
        mv = max_value[symbols[symbol_counter.index(5)]]
        return str(mv)+' Flush'
    return ''

def check_straight(dict_hand: dict, key: int) -> str:
    if key<5: return ''
    fl_dict_hand = deepcopy(dict_hand)
    if 14 in fl_dict_hand.keys():
        fl_dict_hand[1] = fl_dict_hand[14]
    keys_list = list(fl_dict_hand.keys())
    value_index = keys_list.index(key)
    possible_s = sum(keys_list[value_index:value_index+5])==(key-2)*5 
    if possible_s: return str(key)+' Straight'
    return ''

def check_repeated(dict_hand: dict) -> str:
    flush_checked = False
    for key in dict_hand:
        if len(dict_hand[key])==4:
            return str(key)+' Four of a Kind'
        if len(dict_hand[key])==3 and check_pair(dict_hand):
            pair = check_pair(dict_hand)
            return str(key)+' '+pair.split()[0]+' Full House'
        
        # Flush (wrong len statement) bool checked flush
        if not flush_checked:
            flush = check_flush(dict_hand)
            flush_checked = True
            if flush: 
                return flush
        # Straight
        straight = check_straight(dict_hand, key)
        if straight:
            return straight

        if len(dict_hand[key])==3:
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
    
    for key in dict_hand:
        if key<5: break
        if check_special_flush(dict_hand, key):
            return str(key)+' Straight Flush'

    repeated = check_repeated(dict_hand)
    if repeated: return repeated

    return str(list(dict_hand.keys())[0])+' High Card'

