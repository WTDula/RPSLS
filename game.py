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


    def show_options(self):
        #print("The following are all of your gesture options: ")
 
    def display_winners(self):
        pass