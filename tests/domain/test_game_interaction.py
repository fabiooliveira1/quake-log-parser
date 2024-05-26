import unittest
from src.domain.game_interaction import GameInteraction

class TestGameInteraction(unittest.TestCase):
    def test_is_new_game_true(self):
        game_interaction = GameInteraction('', '', '', 'InitGame')

        result = game_interaction.is_new_game()

        self.assertTrue(result)

    def test_is_new_game_false(self):
        game_interaction = GameInteraction('foo', 'bar', 'bar', '')

        result = game_interaction.is_new_game()

        self.assertFalse(result)

    def test_is_world_kill_true(self):
        game_interaction = GameInteraction('<world>', 'bar', 'bar', '')

        result = game_interaction.is_world_kill()

        self.assertTrue(result)

    def test_is_world_kill_false(self):
        game_interaction = GameInteraction('foo', 'bar', 'bar', '')

        result = game_interaction.is_world_kill()

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
