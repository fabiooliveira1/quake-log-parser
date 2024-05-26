from . import player, game
from copy import copy

class History:
    def __init__(self):
        self.games = []
        self.players = {}
        self.kills_by_means = {}
        self.total_kills = 0
    
    def add_game(self):
        number = len(self.games) + 1
        self.games.append(game.Game(number))
    
    def add_player(self, player_instance):
        if player_instance.id not in self.players:
            self.players[player_instance.id] = player_instance

    def increase_player_score(self, player_instance):
        self.add_player(player_instance)
        self.players[player_instance.id].increase_score()
    
    def decrease_player_score(self, player_instance):
        self.add_player(player_instance)
        self.players[player_instance.id].decrease_score()
    
    def increase_kill_by_mean(self, mean):
        if mean not in self.kills_by_means:
            self.kills_by_means[mean] = 0

        self.kills_by_means[mean] = self.kills_by_means[mean] + 1
        self.increase_total_kills()

    def increase_total_kills(self):
        self.total_kills = self.total_kills + 1
    
    def handle_interaction(self, interaction):
        if interaction.is_new_game():
            self.add_game()
            return
        
        current_game = len(self.games) - 1
        if interaction.is_world_kill():
            self.decrease_player_score(player.Player(interaction.victim))
            self.games[current_game].decrease_player_score(player.Player(interaction.victim))
        else:
            self.increase_player_score(player.Player(interaction.killer))
            self.add_player(player.Player(interaction.victim))

            self.games[current_game].increase_player_score(player.Player(interaction.killer))
            self.games[current_game].add_player(player.Player(interaction.victim))

        self.increase_kill_by_mean(interaction.mean)
        self.games[current_game].increase_kill_by_mean(interaction.mean)
