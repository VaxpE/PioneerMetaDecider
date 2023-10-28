from modules.Deck import Deck


def tournament(tournament):
    tournament_result = []
    total_poins_of_decks = []

    for deck in tournament:
        tournament_result.append(Deck(deck[0:deck.rfind(' ')],deck[deck.rfind(' ')+1:],0))
    #Считываем из файла результаты каждого пилота

    tournament_result = sorted(tournament_result, reverse=True)
    counter = False
    for deck in tournament_result:
        for deck1 in total_poins_of_decks:
            if deck.name == deck1.name:
                counter = True
                deck1.score_on_metagame += int(deck.score_on_tournament)
                deck1.quantity_on_tournament += 1
        if counter == False:
            total_poins_of_decks.append(deck)
            deck.score_on_metagame = int(deck.score_on_tournament)
        counter = False

    total_poins_of_decks = sorted(total_poins_of_decks, reverse=True)
    
    return total_poins_of_decks
