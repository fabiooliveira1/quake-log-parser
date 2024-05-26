import unittest
from src.domain.player import Player

class TestPlayer(unittest.TestCase):
    def test_sanitize(self):
        player = Player('Foo Bar')

        self.assertEqual('foo_bar', player.id)

    def test_increase_score(self):
        player = Player('Foo Bar')

        player.increase_score()
        player.increase_score()
        player.increase_score()

        self.assertEqual(3, player.kills)

    def test_decrease_score(self):
        player = Player('Foo Bar')

        player.decrease_score()
        player.decrease_score()

        self.assertEqual(-2, player.kills)

if __name__ == '__main__':
    unittest.main()
