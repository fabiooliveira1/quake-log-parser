class GameInteraction:
    def __init__(self, killer, victim, mean, initGame):
        self.killer = killer
        self.victim = victim
        self.mean = mean
        self.new_game = bool(initGame)
    
    def is_new_game(self):
        return self.new_game
    
    def is_world_kill(self):
        return self.killer == '<world>'

    def __eq__(self, other):
        if isinstance(other, GameInteraction):
            return (self.killer == other.killer and
                self.victim == other.victim and
                self.mean == other.mean and
                self.new_game == other.new_game)

        return False
