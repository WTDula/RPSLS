from gesture import Gesture
class Paper(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Paper"
        self.wins_against = {"Rock": "Paper covers Rock", "Spock": "Paper disproves Spock"}

    def do_i_win(self, other_gesture):
        if other_gesture.name in self.wins_against.keys():
            print(self.wins_against[other_gesture.name])
            return True
        else:
            return False