import random
import model.card as C
import model.deck as D

deck = []

for i in range(5):
    deck.append(C.Card(random.choice(list(C.Value)).value, random.choice(list(C.Symbol)).value))

print(deck)
deck.sort()
print(deck)
flatdeck = [str(x) for x in deck]
if '14H' in flatdeck or \
   '2H' in flatdeck or \
   '3H' in flatdeck or \
   '4H' in flatdeck or \
   '5H' in flatdeck or \
   '6H' in flatdeck or \
   '7H' in flatdeck or \
   '8H' in flatdeck or \
   '9H' in flatdeck or \
   '10H' in flatdeck or \
   '11H' in flatdeck or \
   '12H' in flatdeck or \
   '13H' in flatdeck:
    print('Heart found!')

deck = D.Deck()
print(deck.cards, len(deck.cards))