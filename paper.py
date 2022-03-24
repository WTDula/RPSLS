from gesture import Gesture
class Paper(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Paper"

    def do_i_win(self, other_gesture):
        if other_gesture.name == "Rock":
            print("Paper covers Rock")
            return True
        elif other_gesture.name == "Spock":
            print("Paper disproves Spock")
            return True
        else:
            return False