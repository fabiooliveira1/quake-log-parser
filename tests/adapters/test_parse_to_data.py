import unittest
from unittest.mock import Mock
from src.adapters.parse_to_data import Parser
from src.domain.game_interaction import GameInteraction

class TestParser(unittest.TestCase):

    def test_callback_no_match(self):
        callback = Mock()
        parser = Parser(callback)
        line = 'dummy dummy line\n'

        parser.parse(line)

        callback.assert_not_called()

    def test_callback_killed_by(self):
        callback = Mock()
        parser = Parser(callback)
        result = GameInteraction('Oootsimo', 'Dono da Bola', 'MOD_ROCKET', '')
        line = ' 13:55 Kill: 3 4 6: Oootsimo killed Dono da Bola by MOD_ROCKET\n'

        parser.parse(line)

        callback.assert_called_once_with(result)

    def test_callback_init_game(self):
        callback = Mock()
        parser = Parser(callback)
        result = GameInteraction('', '', '', 'InitGame')
        line = ' 20:37 InitGame: \sv_floodProtect\1\sv_maxPing\0\sv_minPing\0\sv_maxRate\10000\sv_minRate\0\sv_hostname\Code Miner Server\g_gametype\0\sv_privateClients\2\sv_maxclients\16\sv_allowDownload\0\bot_minplayers\0\dmflags\0\fraglimit\20\timelimit\15\g_maxGameClients\0\capturelimit\8\version\ioq3 1.36 linux-x86_64 Apr 12 2009\protocol\68\mapname\q3dm17\gamename\baseq3\g_needpass\0\n'

        parser.parse(line)

        callback.assert_called_once_with(result)

if __name__ == '__main__':
    unittest.main()