import random
from model import card as C

deck = []

for i in range(10):
    deck.append(C.Card(random.choice(list(C.Value)).value, random.choice(list(C.Symbol)).value))

print(deck)
deck.sort()
print(deck)