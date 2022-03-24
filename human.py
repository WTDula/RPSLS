from player import Player
class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        return int(input("Select the number of your gesture for player two:  "))