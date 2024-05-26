import re
from domain import game_interaction

class Parser:
    def __init__(self, callback):
        self.pattern = re.compile('\d: (.*) killed (.*) by (.*)|:\d+ (InitGame)')
        self.callback = callback

    def parse(self, line):
        result = self.pattern.findall(line)
        if result and result[0]:
            self.callback(game_interaction.GameInteraction(*result[0]))
    
