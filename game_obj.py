from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock

class GameObj:
    def __init__(self):
        self.rpsls_list = []

    def create_game_obj(self):
        self.rpsls_list.append(Rock())
        self.rpsls_list.append(Paper())
        self.rpsls_list.append(Scissors())
        self.rpsls_list.append(Lizard())
        self.rpsls_list.append(Spock())