import unittest
from unittest.mock import Mock
from src.usecase.report import Report
from src.domain.history import History
from src.domain.game_interaction import GameInteraction

class TestReport(unittest.TestCase):
    def test_game_report(self):
        history = self._populate_history()
        report = Report(history)
        report._print_dict = Mock()
        expected = {
            "game_1": {
                "total_kills": 3,
                "kill_by_means": {
                    "MOD_RAILGUN": 1,
                    "MOD_TRIGGER_HURT": 2,
                },
                "players": ['foo', 'bar'],
                "kills": {
                    "foo": 0,
                    "bar": -1
                }
            },
            "game_2": {
                "total_kills": 2,
                "kill_by_means": {
                    "MOD_RAILGUN": 2
                },
                "players": ['foo', 'bar'],
                "kills": {
                    "foo": 2,
                    "bar": 0
                }
            }
        }

        report.game_report()

        report._print_dict.assert_called_once_with(expected)

    def test_player_ranking(self):
        history = self._populate_history()
        report = Report(history)
        report._print_dict = Mock()
        expected = {
            "players": [
                {
                    "player": "foo",
                    "kills": 2,
                },
                {
                    "player": "bar",
                    "kills": -1,
                },
            ]
        }

        report.player_ranking()

        report._print_dict.assert_called_once_with(expected)

    def test_all_kills_by_means(self):
        history = self._populate_history()
        report = Report(history)
        report._print_dict = Mock()
        expected = {
            "means": [
                {
                    "mean": "MOD_RAILGUN",
                    "kills": 3,
                },
                {
                    "mean": "MOD_TRIGGER_HURT",
                    "kills": 2,
                },
            ]
        }

        report.all_kills_by_means()

        report._print_dict.assert_called_once_with(expected)
    
    def _populate_history():
        interactions = [
            GameInteraction('', '', '', 'InitGame'),
            GameInteraction('foo', 'bar', 'MOD_RAILGUN', ''),
            GameInteraction('<world>', 'foo', 'MOD_TRIGGER_HURT', ''),
            GameInteraction('<world>', 'bar', 'MOD_TRIGGER_HURT', ''),
            GameInteraction('', '', '', 'InitGame'),
            GameInteraction('foo', 'bar', 'MOD_RAILGUN', ''),
            GameInteraction('foo', 'bar', 'MOD_RAILGUN', ''),
        ]

        history = History()
        for i in interactions:
            history.handle_interaction(i)

        return history

if __name__ == '__main__':
    unittest.main()