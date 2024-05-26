from helpers.utils import Utils

class Report:
    def __init__(self, history):
        self.history = history
    
    def game_report(self):
        games = {}
        for game in self.history.games:
            game_dict = {
                "total_kills": game.total_kills,
                "kill_by_means": game.kills_by_means,
                "players": [],
                "kills": {}
            }
            for player in game.players.values():
                game_dict["players"].append(player.name)
                game_dict["kills"][player.name] = player.kills
            games[game.id] = game_dict

        self._print_dict(games)

    def player_ranking(self):
        ranking = {"players": []}
        players = sorted(self.history.players.values(), key=lambda player: player.kills, reverse=True)
        for player in players:
            ranking["players"].append({
                "player": player.name,
                "kills": player.kills,
            })

        self._print_dict(ranking)

    def all_kills_by_means(self):
        ranking = {"means": []}

        for mean in self.history.kills_by_means.keys():
            ranking["means"].append({
                "mean": mean,
                "kills": self.history.kills_by_means[mean],
            })
        
        self._print_dict(ranking)

    def _print_dict(self, dict):
        print(Utils().dict_to_json(dict))