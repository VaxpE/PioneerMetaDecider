from modules.tournament import tournament
from modules.Deck import Deck


meta = open('results.txt', 'w')
f = open('data.txt', 'r')
tournament(f, meta)
f.close()
meta.close()
