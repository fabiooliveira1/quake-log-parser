from src.usecase.report import Report
from src.domain.history import History
from src.adapters.parse_to_data import Parser
from src.adapters.reader import Reader

class Controller:
    def __init__(self):
        self.history = History()
        self.parser = Parser(self.history.handle_interaction)
        self.reader = Reader('src/static/qgames.log', self.parser.parse)
        self.report = Report(self.history)
    
    def populate_history(self):
        self.reader.read_all()
    
    def get_game_report(self):
        self.report.game_report()
    
    def get_player_ranking(self):
        self.report.player_ranking()
    
    def get_all_kills_by_means(self):
        self.report.all_kills_by_means()