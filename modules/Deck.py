class Deck:
    quantity_on_tournament = 1
    score_on_metagame = 0
    avg_pnts_on_trn = score_on_metagame/quantity_on_tournament
    
    def __init__(self,name, score_on_tournament = 0, score_on_metagame = 0) -> None:
        self.name = name
        self.score_on_tournament = score_on_tournament
        self.score_on_metagame = score_on_metagame

    def __str__(self) -> str:
        return f'{self.name} {self.score_on_metagame},{self.quantity_on_tournament}'
    
    def __repr__(self) -> str:
        return f'{self.name} {self.score_on_metagame},{self.quantity_on_tournament}'
    
    def __lt__(self,other) -> bool:
        if self.score_on_metagame >= other.score_on_metagame:
            return False
        elif self.score_on_metagame < other.score_on_metagame:
            return True 

class Player(Deck):
    
    def __init__(self, name, score_on_tournament=0, score_on_metagame=0) -> None:
        super().__init__(name, score_on_tournament, score_on_metagame)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    def __lt__(self, other) -> bool:
        return super().__lt__(other)