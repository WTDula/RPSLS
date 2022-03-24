from gesture import Gesture
class Lizard(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Lizard"

    def do_i_win(self, other_gesture):
        if other_gesture.name == "Spock":
            print("Lizard poisons Spock")
            return True
        elif other_gesture.name == "Paper":
            print("Lizard eats Paper")
            return True
        else:
            return False
