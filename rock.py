from gesture import Gesture
class Rock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Rock"

    def do_i_win(self, other_gesture):
        if other_gesture.name == "Scissors":
            print("Rock crushes Scissors")
            return True
        elif other_gesture.name == "Lizard":
            print("Rock crushes Lizard")
            return True
        else:
            return False