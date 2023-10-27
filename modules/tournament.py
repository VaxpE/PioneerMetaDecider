from Deck import Deck

import sys
print(sys.path)

def tournament(tournament, meta):
    tournament_result = []
    total_poins_of_deck = []

    for deck in tournament:
        tournament_result.append(Deck(deck[0:deck.rfind(' ')],deck[deck.rfind(' ')+1:]))
    #Считываем из файла результаты каждого пилота

    tournament_result = sorted(tournament_result, reverse=True)
    counter = False
    for deck in tournament_result:
        for deck1 in total_poins_of_deck:
            if deck.name == deck1.name:
                counter = True
                deck1.score_on_metagame += int(deck.score_on_tournament)
                deck1.quantity_on_tournament += 1
        if counter == False:
            total_poins_of_deck.append(deck)
            deck.score_on_metagame = int(deck.score_on_tournament)
        counter = False

    total_poins_of_deck = sorted(total_poins_of_deck, reverse=True)
    

    for deck in total_poins_of_deck:
        print(f'{deck}', file=meta)
    
