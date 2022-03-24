from gesture import Gesture
class Spock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Spock"
        self.wins_against = {"Scissors" : "Spock smashes Scissors" , "Rock": "Spock vaporizes Rock"}

    def do_i_win(self, other_gesture):
        if other_gesture.name in self.wins_against.keys():
            print(self.wins_against[other_gesture.name])
            return True
        else:
            return False