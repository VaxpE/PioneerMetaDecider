from modules.tournament import tournament
from modules.Deck import Deck
from modules.meta import meta



with open('data.txt', 'r') as tournament_resul:
    with open('results.txt', 'r') as current_meta:
        temp = meta(current_meta, tournament_resul)
f = open('results.txt', 'w+')
f.seek(0)
f.close()
with open('results.txt', 'w') as current_meta:
    for deck in temp:
        print(deck, file = current_meta)
