from modules.Deck import Deck
from modules.tournament import tournament


def meta(meta, tournament_result):
   
    last_tournament_result = tournament(tournament_result)
    current_meta = []
    counter = False
    
    for line in meta:
        if line[line.rfind(' ')+1:line.find(',')] == '':
            break
        deck = Deck(line[0:line.rfind(' ')], score_on_metagame = int(line[line.rfind(' ')+1:line.find(',')]))
        current_meta.append(deck)
        deck.quantity_on_tournament = int(line[line.find(',')+1:-1])
        
    for deck in last_tournament_result:
        for deck1 in current_meta:
            if deck.name == deck1.name:
                counter = True
                deck1.score_on_metagame += int(deck.score_on_metagame)
                deck1.quantity_on_tournament += deck.quantity_on_tournament
        if counter == False:
            current_meta.append(deck)
        counter = False
    current_meta = sorted(current_meta, reverse=True)
    return current_meta