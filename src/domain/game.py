class Game:
    def __init__(self, number):
        self.id = f"game_{number}"
        self.players = {}
        self.kills_by_means = {}
        self.total_kills = 0
    
    def add_player(self, player):
        if player.id not in self.players:
            self.players[player.id] = player
    
    def increase_player_score(self, player):
        self.add_player(player)
        self.players[player.id].increase_score()
    
    def decrease_player_score(self, player):
        self.add_player(player)
        self.players[player.id].decrease_score()
    
    def increase_kill_by_mean(self, mean):
        if mean not in self.kills_by_means:
            self.kills_by_means[mean] = 0

        self.kills_by_means[mean] = self.kills_by_means[mean] + 1
        self.increase_total_kills()
    
    def increase_total_kills(self):
        self.total_kills = self.total_kills + 1
