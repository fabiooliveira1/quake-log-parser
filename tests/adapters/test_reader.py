import unittest
from unittest.mock import call, Mock
from src.adapters.reader import Reader

class TestReader(unittest.TestCase):
    def test_not_found(self):
        parse = Mock()
        reader = Reader("not-found.log", parse)

        self.assertRaises(FileNotFoundError, reader.read_all)
        parse.assert_not_called()

    def test_callback(self):
        parse = Mock()
        reader = Reader("tests/static/reader.log", parse)

        reader.read_all()

        parse.assert_has_calls([
            call('this\n'), call('is\n'), call('a\n'), call('test\n')
        ])

if __name__ == '__main__':
    unittest.main()