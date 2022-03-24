from gesture import Gesture
class Lizard(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Lizard"

    def do_i_win(self, other_gesture):
        pass