import random
from game_obj import GameObj
from human import Human
from ai import AI

class GameCopy():
    def __init__(self):
        self.player_one = Human()
        self.player_two = AI() #Default to AI unless otherwise specified 
        self.game_obj = GameObj()
        self.is_single_player = False
        

    def run_game(self):
            self.game_obj.create_game_obj()
            self.display_welcome()
            self.show_options()
            self.single_player_multi_player_selection()


    def single_player_multi_player_selection(self):
        user_input = None
        while True: #Input handling
            print("---------------------------------------------------")
            user_input = int(input("Do you you want to play single player or multiplayer: <Select (1) for single player | Select (2) for multiplayer>  "))
            if user_input == 1 or user_input == 2:
                if user_input == 2: #initiates multiplayer mode
                    print("You have selected multiplayer mode:")
                    self.player_two = Human()
                    self.is_single_player = False
                    self.compare_gestures()
                    return
                else:
                    print("You have selected single player mode:")
                    self.is_single_player = True
                    self.compare_gestures()
                    return 
                    

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock")
        self.show_rules()
        print("Best of 3 wins: ")
        print("---------------------------------------------------")

    def compare_gestures(self):
        user_input_one = int(input("Select the number of your gesture for player one:  ")) #player one
        opponent_input = True
        while user_input_one in range(0 , 5) and opponent_input:
                #ask user for current gesture
            if self.is_single_player:
                opponent_input = self.player_two.choose_gesture()
            else:
                opponent_input = self.player_one.choose_gesture()
        
            p1 = self.game_obj.rpsls_list[user_input_one]
            p2 = self.game_obj.rpsls_list[opponent_input]
            if p1.do_i_win(p2):
                self.player_one.scores += 1
            elif p2.do_i_win(p1):
                self.player_two.scores += 1
            else:
                print(f"It's a tie") #if input is equal
            print("---------------------------------------------------")

            if(self.player_one.scores == 2 or self.player_two.scores == 2):
                self.display_winners()
                return
            user_input_one = int(input("Select the number of your gesture for player one:  "))
            while(user_input_one > 4 or user_input_one < 0) or (opponent_input > 4 or opponent_input < 0):
                user_input_one = int(input("Select the number of your gesture for player one:  "))
                opponent_input = self.player_two.choose_gesture()


    def show_rules(self):
        print("---------------------------------------------------")
        print("Rock crushes Scissors\t\tScissors cuts Paper\nPaper covers Rock\t\tRock crushes Lizard\nLizard poisons Spock\t\tSpock smashes Scissors\nScissors decapitates Lizard\tLizard eats Paper\nPaper disproves Spock\t\tSpock vaporizes Rock")

    def show_options(self):
        print("Use the following numbers to select the gesture: ")
        for gesture in self.player_one.gestures:
            gesture_index = self.player_one.gestures.index(gesture) 
            print(f"{gesture} : {gesture_index}")

    def display_winners(self):
        if self.player_one.scores == 2:
            print("Player one wins!")
        else:
            print("Player two wins!")