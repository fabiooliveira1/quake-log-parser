import unittest
from unittest.mock import Mock
from src.controller.controller import Controller

class TestController(unittest.TestCase):
    def test_populate_history(self):
        controller = Controller()
        controller.reader.read_all = Mock()

        controller.populate_history()

        controller.reader.read_all.assert_called_once()

    def test_get_game_report(self):
        controller = Controller()
        controller.report.game_report = Mock()

        controller.get_game_report()

        controller.report.game_report.assert_called_once()

    def test_player_ranking(self):
        controller = Controller()
        controller.report.player_ranking = Mock()

        controller.get_player_ranking()

        controller.report.player_ranking.assert_called_once()

    def test_get_all_kills_by_means(self):
        controller = Controller()
        controller.report.all_kills_by_means = Mock()

        controller.get_all_kills_by_means()

        controller.report.all_kills_by_means.assert_called_once()


if __name__ == '__main__':
    unittest.main()