from helpers.utils import Utils

class Player:
    def __init__(self, name):
        self.id = Utils().sanitize(name)
        self.name = name
        self.kills = 0
    
    def increase_score(self):
        self.kills = self.kills + 1
    
    def decrease_score(self):
        self.kills = self.kills + 1