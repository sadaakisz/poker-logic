import model.deck as dck
import model.pocket as pck
import logic.hand_ranker as hr
import logic.hand_maker as hm
import dataset.test_runner as tr

class Player:
    def __init__(self, name, bankroll = 500, pocket = pck.Pocket()) -> None:
        self.name = name
        self.pocket = pocket
        self.bankroll = bankroll
    def bet(self, amount):
        if self.bankroll>=amount:
            self.bankroll -= amount
            return amount
        else:
            amount = self.bankroll
            self.bankroll -= amount
            return amount

deck = dck.Deck()
board = []

pl1 = Player('Empe', 500, pck.Pocket())
pl2 = Player('Roro', 500, pck.Pocket())
pl3 = Player('Juanca', 500, pck.Pocket())
pl4 = Player('Succ', 500, pck.Pocket())

table = [pl1, pl2, pl3, pl4]
winner = ''

roundCounter = 0

while 1:
    roundCounter += 1
    betAmount = 200
    pot = 0

    print('Round', str(roundCounter)+':')
    if roundCounter%5==0:
        betAmount *= roundCounter//5

    for player in table:
        pot += player.bet(betAmount)

    print('Pot:', pot)

    deck = dck.Deck()
    board = []

    for i in range(2):
        for player in table:
            player.pocket.append(deck.get_card())
    
    for i in range(5):
        board.append(deck.get_card())

    for player in table:
            print(player.name, player.bankroll, player.pocket)
    print(board)

    list_ranks = []
    for player in table:
        list_ranks.append(hr.list_rank(player.pocket.dict_hand(board)))

    print(hr.winner(list_ranks, show_hand=True))
    winnerId = hr.winner(list_ranks)
    if len(winnerId) == 1:
        table[winnerId[0]].bankroll += pot
    else:
        winnerQuantity = len(winnerId)
        for w in winnerId:
            table[w].bankroll += pot//winnerQuantity

    for player in table:
        player.pocket.clear()
        if player.bankroll == 0:
            table.remove(player)
    
    if len(table) == 1:
        break

print('The winner is', table[0].name)