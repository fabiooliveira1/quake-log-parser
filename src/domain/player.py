from helpers import utils

class Player:
    def __init__(self, name):
        self.id = utils.Utils().sanitize(name)
        self.name = name
        self.kills = 0
    
    def increase_score(self):
        self.kills = self.kills + 1
    
    def decrease_score(self):
        self.kills = self.kills + 1