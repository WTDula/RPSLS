from gesture import Gesture
class Scissors(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Scissors"

    def do_i_win(self, other_gesture):
        if other_gesture.name == "Paper":
            print("Scissors cuts Paper")
            return True
        elif other_gesture.name == "Lizard":
            print("Scissors decapitates Lizard")
            return True
        else:
            return False