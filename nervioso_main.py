import nervioso_classes as nc
import time as t
from pytimedinput import timedKey

def main():

    #create players
    player_1 = nc.Player('a', 'Empe')
    player_2 = nc.Player('l', 'Roro')

    #create deck
    deck = nc.Deck([])

    #let's play!

    turn_number = 1

    """while deck.number_cards != 0:
        card = deck.get_card()
        print(str(card.symbol) + ' '+ str(card.number))

        #difficukty: unadded deature
        t.sleep(1.5)

        if turn_number == card.number and input():"""
    
    
    aux, timedOut = timedKey(prompt="PRESIONA ALGO", timeout = 1.5, resetOnInput=True, allowCharacters="al")

    if(timedOut):
        print("Siguiente carta")
    else:
        if(aux == "a"):
            print("JUGADOR 1")
        else:
            print("JUGADOR2")
            




main()