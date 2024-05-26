from usecase import report
from domain import history
from adapters import parse_to_data, reader

class Controller:
    def __init__(self):
        self.history = history.History()
        self.parser = parse_to_data.Parser(self.history.handle_interaction)
        self.reader = reader.Reader('src/static/qgames.log', self.parser.parse)
        self.report = report.Report(self.history)
    
    def populate_history(self):
        self.reader.read_all()
    
    def get_game_report(self):
        self.report.game_report()
    
    def get_player_ranking(self):
        self.report.player_ranking()
    
    def get_all_kills_by_means(self):
        self.report.all_kills_by_means()