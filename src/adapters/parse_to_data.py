import re
from domain.game_interaction import GameInteraction

class Parser:
    def __init__(self, callback):
        self.pattern = re.compile('\d: (.*) killed (.*) by (.*)|:\d+ (InitGame)')
        self.callback = callback

    def parse(self, line):
        result = self.pattern.findall(line)
        if result and result[0]:
            self.callback(GameInteraction(*result[0]))
    
