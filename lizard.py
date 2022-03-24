from gesture import Gesture
class Lizard(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Lizard"
        self.wins_against = {"Spock" : "Lizard poisons Spock", "Paper": "Lizard eats Paper"}
        
    def do_i_win(self, other_gesture):
        if other_gesture.name in self.wins_against.keys():
            print(self.wins_against[other_gesture.name])
            return True
        else:
            return False