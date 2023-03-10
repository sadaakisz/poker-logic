from copy import deepcopy

hand_name_to_value = {
    'Royal_Flush': 9,
    'Straight_Flush': 8,
    'Four_of_a_Kind': 7,
    'Full_House': 6,
    'Flush': 5,
    'Straight': 4,
    'Three_of_a_Kind': 3,
    'Two_Pairs': 2,
    'Pair': 1,
    'High_Card': 0
}

hand_value_to_name = {v: k for k, v in hand_name_to_value.items()}

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
                if symbol in fl_dict_hand[i]:
                    other_symbols.append([symbol])
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
    if key<5:
        return ''
    fl_dict_hand = deepcopy(dict_hand)
    if 14 in fl_dict_hand.keys():
        fl_dict_hand[1] = fl_dict_hand[14]
    keys_list = list(fl_dict_hand.keys())
    value_index = keys_list.index(key)
    possible_s = sum(keys_list[value_index:value_index+5])==(key-2)*5
    if possible_s:
        return str(key)+' Straight'
    return ''

def check_repeated(dict_hand: dict) -> str:
    flush_checked = False
    pair_present = False
    pair_key = None
    for key in dict_hand:
        if len(dict_hand[key])==4:
            return str(key)+' Four_of_a_Kind'
        if len(dict_hand[key])==3 and check_pair(dict_hand):
            pair = check_pair(dict_hand)
            return str(key)+' '+pair.split()[0]+' Full_House'
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
            return str(key)+' Three_of_a_Kind'
        if len(dict_hand[key])==2:
            pair = check_pair(dict_hand, key)
            if pair:
                return str(key)+' '+pair.split()[0]+' Two_Pairs'
            pair_present = True
            pair_key = key
    if pair_present:
        return str(pair_key)+' Pair'
    return ''

def rank(dict_hand: dict) -> str:
    #print(dict_hand)

    if check_special_flush(dict_hand, 14):
        return str(14)+' Royal_Flush'
    for key in dict_hand:
        if key<5:
            break
        if check_special_flush(dict_hand, key):
            return str(key)+' Straight_Flush'

    repeated = check_repeated(dict_hand)
    if repeated:
        return repeated

    return str(list(dict_hand.keys())[0])+' High_Card'

def list_rank(dict_hand: dict) -> str:
    str_rank = rank(dict_hand)
    spl_rank = str_rank.split()
    if len(spl_rank)==2: 
        return [hand_name_to_value[spl_rank[-1]], int(spl_rank[0])]
    elif len(spl_rank)==3:
        return [hand_name_to_value[spl_rank[-1]], int(spl_rank[0]), int(spl_rank[1])]
    else:
        return NotImplementedError
    
def winner(list_ranks: list, show_hand=False) -> int:
    winner_list = []
    max_hand = max(list_ranks)
    for i in range(list_ranks.count(max_hand)):
        winner_idx = [m for m, n in enumerate(list_ranks) if n == max_hand][i]
        winner_list.append(winner_idx)
    if not show_hand:
        return winner_list
    else:
        return winner_list, hand_value_to_name[max_hand[0]]