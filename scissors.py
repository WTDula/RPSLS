from gesture import Gesture
class Scissors(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Scissors"

        self.wins_against = {"Paper": "Scissors cuts Paper",  "Lizard" : "Scissors decapitates Lizard", }

    def do_i_win(self, other_gesture):
        if other_gesture.name in self.wins_against.keys():
            print(self.wins_against[other_gesture.name])
            return True
        else:
            return False