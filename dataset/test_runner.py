import os
import logic.hand_maker as hm
import logic.hand_ranker as hr

hand_eq = {
    '9': 'Royal_Flush',
    '8': 'Straight_Flush',
    '7': 'Four_of_a_Kind',
    '6': 'Full_House',
    '5': 'Flush',
    '4': 'Straight',
    '3': 'Three_of_a_Kind',
    '2': 'Two_Pairs',
    '1': 'Pair',
    '0': 'High_Card'
}

suit = {
    '1': 'H',
    '2': 'S',
    '3': 'D',
    '4': 'C'
}

def run_test():
    # Transform ace from 1 to 14
    #fname = 'poker-hand-training-true.data'
    fname = 'poker-hand-testing.data' # Full dataset
    script_dir = os.path.dirname(__file__)
    fh = open(os.path.join(script_dir, fname))
    line_number = 0
    for line in fh:
        line_number += 1
        line = line.rstrip('\n')
        values = line.split(',')
        
        str_cards = []
        correct_hand = hand_eq[values[-1]]
        for i in range(0, 10, 2):
            suit_card = suit[values[i]]
            value_card = 14 if values[i+1]=='1' else values[i+1]
            str_cards.append(str(value_card)+str(suit_card))
        hand = hm.make_hand(str_cards)
        if not correct_hand==hr.rank(hand).split()[-1]:
            print('Line number:', line_number, '-------------------------------')
            print(str_cards)
            print(correct_hand)
            print(hr.rank(hand).split()[-1])
