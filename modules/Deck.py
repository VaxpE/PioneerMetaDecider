class Deck:
    score_on_metagame = 0
    quantity_on_tournament = 1
    
    def __init__(self,name, score_on_tournament) -> None:
        self.name = name
        self.score_on_tournament = score_on_tournament

    def __str__(self) -> str:
        return f'{self.name} {self.score_on_metagame},{self.quantity_on_tournament}'
    
    def __repr__(self) -> str:
        return f'{self.name} {self.score_on_metagame},{self.quantity_on_tournament}'
    
    def __lt__(self,other) -> bool:
        if self.score_on_metagame >= other.score_on_metagame:
            return False
        elif self.score_on_metagame < other.score_on_metagame:
            return True 
