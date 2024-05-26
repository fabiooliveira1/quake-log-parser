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


