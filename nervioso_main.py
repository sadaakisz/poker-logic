import nervioso_classes as nc
import time as t
from pytimedinput import timedKey
import os


def main():

    # create players
    player_1 = nc.Player('a', 'Empe')
    player_2 = nc.Player('l', 'Roro')

    # create deck
    deck = nc.Deck([])

    # let's play!
    turn_number = 0
    table_cards = []

    while deck.number_cards != 0:
        # initialize turn as 1
        turn_number += 1

        if turn_number == 14:
            turn_number = 1

        # Get a card from deck and put it in the table
        card = deck.get_card()
        table_cards.append(card)

        # Show card and actual turn
        print(str(turn_number) + ': ' + str(card.symbol) + ' ' + str(card.number))

        # difficulty: unadded feature (not implemented) timeout
        first_player, timedOut = timedKey(
            prompt="Waiting Input...", timeout=1.5, resetOnInput=True, allowCharacters="al")

        # coincidence turn
        if turn_number == card.number:
            if timedOut:
                print('Lost a chance')
            elif first_player:
                if first_player == 'a':
                    winner = player_1
                else:
                    winner = player_2
                # case when loser gets cards, and turn and table_cards reset
                print(winner.name + ' wins the turn')
                loser = player_2 if winner == player_1 else player_1
                loser.add_cards(table_cards)
                turn_number = 0
                table_cards = []
                print(loser.name + ' gets the cards')
                print('Player: ' + player_1.name + ' has ' +
                      str(player_1.number_cards) + ' cards')
                print('Player: ' + player_2.name + ' has ' +
                      str(player_2.number_cards) + ' cards')
                print('Get Ready...')
                t.sleep(3)
                os.system('cls')
        else:
            if timedOut:
                continue
            elif first_player:
                if first_player == 'a':
                    loser = player_1
                else:
                    loser = player_2
                # case when the player gets nervioso and mete mano when it's not the time
                print('Player:' + loser.name + ' loses because is nervioso')
                winner = player_1 if loser == player_2 else player_2
                loser.add_cards(table_cards)
                turn_number = 0
                table_cards = []
                print('Player: ' + player_1.name + ' has ' +
                      str(player_1.number_cards) + ' cards')
                print('Player: ' + player_2.name + ' has ' +
                      str(player_2.number_cards) + ' cards')
                print('Get Ready...')
                t.sleep(3)
                os.system('cls')

    print('Results')
    print('Player: ' + player_1.name + ' has ' +
          str(player_1.number_cards) + ' cards')
    print('Player: ' + player_2.name + ' has ' +
          str(player_2.number_cards) + ' cards')

    if player_1.number_cards < player_2.number_cards:
        print('Winner is player: ' + player_1.name)
    elif player_1.number_cards > player_2.number_cards:
        print('Winner is player: ' + player_2.name)
    else:
        print('Draw')


main()
