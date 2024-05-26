import unittest
from src.domain.game import Game
from src.domain.player import Player

class TestGame(unittest.TestCase):
    def test_game_id(self):
        game = Game(1)

        self.assertEqual('game_1', game.id)

    def test_add_player(self):
        game = Game(1)
        player = Player('foo')

        game.add_player(player)

        self.assertEqual(1, len(game.players.keys()))
        self.assertEqual(player, game.players[player.id])

    def test_add_player_duplicate(self):
        game = Game(1)
        player = Player('foo')

        game.add_player(player)
        game.add_player(player)

        self.assertEqual(1, len(game.players.keys()))

    def test_increase_score_new_player(self):
        game = Game(1)
        player = Player('foo')

        game.increase_player_score(player)

        self.assertEqual(1, len(game.players.keys()))
        self.assertEqual(1, game.players[player.id].kills)

    def test_increase_score_existing_player(self):
        game = Game(1)
        player = Player('foo')

        game.add_player(player)
        game.increase_player_score(player)

        self.assertEqual(1, len(game.players.keys()))
        self.assertEqual(1, game.players[player.id].kills)

    def test_decrease_score_new_player(self):
        game = Game(1)
        player = Player('foo')

        game.decrease_player_score(player)

        self.assertEqual(1, len(game.players.keys()))
        self.assertEqual(-1, game.players[player.id].kills)

    def test_decrease_score_existing_player(self):
        game = Game(1)
        player = Player('foo')

        game.add_player(player)
        game.decrease_player_score(player)

        self.assertEqual(1, len(game.players.keys()))
        self.assertEqual(-1, game.players[player.id].kills)

    def test_increase_kill_by_mean_new_mean(self):
        game = Game(1)
        mean = 'foo'

        game.increase_kill_by_mean(mean)

        self.assertEqual(1, len(game.kills_by_means.keys()))
        self.assertEqual(1, game.kills_by_means[mean])
        self.assertEqual(1, game.total_kills)

    def test_increase_kill_by_mean_existing_mean(self):
        game = Game(1)
        mean = 'foo'

        game.increase_kill_by_mean(mean)
        game.increase_kill_by_mean(mean)

        self.assertEqual(1, len(game.kills_by_means.keys()))
        self.assertEqual(2, game.kills_by_means[mean])
        self.assertEqual(2, game.total_kills)

    def test_increase_total_kills(self):
        game = Game(1)

        game.increase_total_kills()

        self.assertEqual(1, game.total_kills)

if __name__ == '__main__':
    unittest.main()
