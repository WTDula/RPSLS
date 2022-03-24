import random
from player import Player
class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        return random.choice(range(0, 5))