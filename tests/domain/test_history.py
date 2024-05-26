import unittest
from unittest.mock import Mock
from src.domain.history import History
from src.domain.game_interaction import GameInteraction
from src.domain.player import Player

class TestHistory(unittest.TestCase):
    def test_add_game(self):
        history = History()

        history.add_game()

        self.assertEqual('game_1', history.games[0].id)

    def test_add_game_twice(self):
        history = History()

        history.add_game()
        history.add_game()

        self.assertEqual('game_1', history.games[0].id)
        self.assertEqual('game_2', history.games[0].id)

    def test_add_player(self):
        history = History()
        player = Player('foo')

        history.add_player(player)

        self.assertEqual(1, len(history.players.keys()))
        self.assertEqual(player, history.players[player.id])

    def test_add_player_duplicate(self):
        history = History()
        player = Player('foo')

        history.add_player(player)
        history.add_player(player)

        self.assertEqual(1, len(history.players.keys()))

    def test_increase_score_new_player(self):
        history = History()
        player = Player('foo')

        history.increase_player_score(player)

        self.assertEqual(1, len(history.players.keys()))
        self.assertEqual(1, history.players[player.id].kills)

    def test_increase_score_existing_player(self):
        history = History()
        player = Player('foo')

        history.add_player(player)
        history.increase_player_score(player)

        self.assertEqual(1, len(history.players.keys()))
        self.assertEqual(1, history.players[player.id].kills)

    def test_decrease_score_new_player(self):
        history = History()
        player = Player('foo')

        history.decrease_player_score(player)

        self.assertEqual(1, len(history.players.keys()))
        self.assertEqual(-1, history.players[player.id].kills)

    def test_decrease_score_existing_player(self):
        history = History()
        player = Player('foo')

        history.add_player(player)
        history.decrease_player_score(player)

        self.assertEqual(1, len(history.players.keys()))
        self.assertEqual(-1, history.players[player.id].kills)

    def test_increase_kill_by_mean_new_mean(self):
        history = History()
        mean = 'foo'

        history.increase_kill_by_mean(mean)

        self.assertEqual(1, len(history.kills_by_means.keys()))
        self.assertEqual(1, history.kills_by_means[mean])
        self.assertEqual(1, history.total_kills)

    def test_increase_kill_by_mean_existing_mean(self):
        history = History()
        mean = 'foo'

        history.increase_kill_by_mean(mean)
        history.increase_kill_by_mean(mean)

        self.assertEqual(1, len(history.kills_by_means.keys()))
        self.assertEqual(2, history.kills_by_means[mean])
        self.assertEqual(2, history.total_kills)

    def test_increase_total_kills(self):
        history = History()

        history.increase_total_kills()

        self.assertEqual(1, history.total_kills)

    def test_handle_interaction_new_game(self):
        history = History()
        interaction = GameInteraction('', '', '', 'InitGame')
        history.add_game = Mock()
        history.decrease_player_score = Mock()
        history.increase_player_score = Mock()
        history.add_player = Mock()
        history.increase_kill_by_mean = Mock()

        history.handle_interaction(interaction)

        history.add_game.assert_called()
        history.decrease_player_score.assert_not_called()
        history.increase_player_score.assert_not_called()
        history.add_player.assert_not_called()
        history.increase_kill_by_mean.assert_not_called()

    def test_handle_interaction_world_kill(self):
        history = History()
        history.add_game()
        interaction = GameInteraction('<world>', 'foo', 'bar', '')

        history.add_game = Mock()
        history.decrease_player_score = Mock()
        history.increase_player_score = Mock()
        history.add_player = Mock()
        history.increase_kill_by_mean = Mock()

        history.games[0].decrease_player_score = Mock()
        history.games[0].increase_player_score = Mock()
        history.games[0].add_player = Mock()
        history.games[0].increase_kill_by_mean = Mock()

        history.handle_interaction(interaction)

        history.add_game.assert_not_called()
        history.decrease_player_score.assert_called()
        history.increase_player_score.assert_not_called()
        history.add_player.assert_called()
        history.increase_kill_by_mean.assert_called()

        history.games[0].decrease_player_score.assert_called()
        history.games[0].increase_player_score.assert_not_called()
        history.games[0].add_player.assert_called()
        history.games[0].increase_kill_by_mean.assert_called()

        self.assertNotEqual(
            history.decrease_player_score.call_args[0],
            history.games[0].decrease_player_score.call_args[0])
        self.assertNotEqual(
            history.add_player.call_args[0],
            history.games[0].add_player.call_args[0])
        self.assertEqual(
            history.increase_kill_by_mean.call_args[0],
            history.games[0].increase_kill_by_mean.call_args[0])

    def test_handle_interaction_player_kill(self):
        history = History()
        history.add_game()
        interaction = GameInteraction('player', 'foo', 'bar', '')

        history.add_game = Mock()
        history.decrease_player_score = Mock()
        history.increase_player_score = Mock()
        history.add_player = Mock()
        history.increase_kill_by_mean = Mock()

        history.games[0].decrease_player_score = Mock()
        history.games[0].increase_player_score = Mock()
        history.games[0].add_player = Mock()
        history.games[0].increase_kill_by_mean = Mock()

        history.handle_interaction(interaction)

        history.add_game.assert_not_called()
        history.decrease_player_score.assert_not_called()
        history.increase_player_score.assert_called()
        history.add_player.assert_called()
        history.increase_kill_by_mean.assert_called()

        history.games[0].decrease_player_score.assert_not_called()
        history.games[0].increase_player_score.assert_called()
        history.games[0].add_player.assert_called()
        history.games[0].increase_kill_by_mean.assert_called()

        self.assertNotEqual(
            history.increase_player_score.call_args[0],
            history.games[0].decrease_player_score.call_args[0])
        self.assertNotEqual(
            history.add_player.call_args[0],
            history.games[0].add_player.call_args[0])
        self.assertEqual(
            history.increase_kill_by_mean.call_args[0],
            history.games[0].increase_kill_by_mean.call_args[0])

if __name__ == '__main__':
    unittest.main()
