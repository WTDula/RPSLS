from human import Human
from ai import AI

class Game():
    def __init__(self):
        self.leaderboard = [] #append a tuple of name of player and append score i.e ("John", 3)
        self.player_one = Human()
        self.player_two = None 


    def run_game(self):
        #initialize
        #while
        pass

    def single_player_multi_player_selection(self):
        pass

    def display_welcome(self):
        self.single_player_multi_player_selection()

    def turn(self, current_player):
        current_player.select_gesture()

    def compare_gestures(self, string_one, string_two):
        if string_one == string_two:
            self.show_options()
            pass

    def show_rules(self):
        print("Rock crushes Scissors\t\ttScissors cuts Paper\nPaper covers Rock\t\tRock crushes Lizard\n Lizard poisons Spock\t\t Spock smashes Scissors\n Scissors decapitates Lizard\t\t Lizard eats Paper\n Paper disproves Spock\t\t Spock vaporizes Rock")

    def show_options(self):
        print("Here are the gestures: ")
        for gesture in self.player_one.gestures:
            print(gesture)
        self.show_rules()

    def display_winners(self):
        pass

g1 = Game()
g1.show_options()