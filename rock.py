from gesture import Gesture
class Rock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Rock"
        self.wins_against = {"Lizard": "Rock crushes Lizard", "Rock": "Rock crushes Scissors"}

    def do_i_win(self, other_gesture):
        if other_gesture.name in self.wins_against.keys():
            print(self.wins_against[other_gesture.name])
            return True
        else:
            return False