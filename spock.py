from gesture import Gesture
class Spock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Spock"

    def do_i_win(self, other_gesture):
        if other_gesture.name == "Scissors":
            print("Spock smashes Scissors")
            return True
        elif other_gesture.name == "Rock":
            print("Spock vaporizes Rock")
            return True