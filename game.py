import random
from human import Human
from ai import AI

class Game():
    def __init__(self):
        self.leaderboard = [] #append a tuple of name of player and append score i.e ("John", 3)
        self.player_one = Human()
        self.player_two = AI() #Default to AI unless otherwise specified 

    def run_game(self):
            self.display_welcome()
            self.show_options()
            self.single_player_multi_player_selection()


    def single_player_multi_player_selection(self):
        user_input = None
        while True:
            print("---------------------------------------------------")
            user_input = int(input("Do you you want to play single player or multiplayer: <Select (1) for single player | Select (2) for multiplayer>  "))
            if user_input == 1 or user_input == 2:
                if user_input == 1:
                    self.player_two = AI()
                    self.compare_gestures_AI()
                    return
                else:
                    self.player_two = Human()
                    self.compare_gestures_multiplayer()
                    return

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock")
        self.show_rules()
        print("Best of 3 wins: ")
        print("---------------------------------------------------")


    def compare_gestures_AI(self):
        #ask user for current gesture
        user_input_one = int(input("Select the number of your gesture:  ")) #player one
        user_input_two = random.choice(range(0, len(self.player_two.gestures))) #player two
        while user_input_one in range(0 , 6) and user_input_two in range(0 , 6):
            # while player_one.scores < 2 and player_two.scores < 2:
            if user_input_one == 0 and user_input_two == 1:
                print(f"{user_input_one} and {user_input_two} : Paper covers Rock") #add one to player two counter
                self.player_two.scores += 1
            elif user_input_one == 0 and user_input_two == 2:
                print(f"{user_input_one} and {user_input_two} : Rock crushes Scissors")
                self.player_one.scores += 1
            elif user_input_one == 0 and user_input_two == 3:
                print(f"{user_input_one} and {user_input_two} : Rock crushes Lizard")
                self.player_one.scores += 1
            elif user_input_one == 0 and user_input_two == 4:
                print(f"{user_input_one} and {user_input_two} : Spock vaporizes Rock")
                self.player_two.scores += 1
            elif user_input_one == 1 and user_input_two == 0:
                print(f"{user_input_one} and {user_input_two} : Paper covers Rock")
                self.player_one.scores += 1
            elif user_input_one == 1 and user_input_two == 2:
                print(f"{user_input_one} and {user_input_two} : Scissors cuts Paper")
                self.player_two.scores += 1
            elif user_input_one == 1 and user_input_two == 3:
                print(f"{user_input_one} and {user_input_two} : Lizard eats Paper")
                self.player_two.scores += 1
            elif user_input_one == 1 and user_input_two == 4:
                print(f"{user_input_one} and {user_input_two} : Paper disproves Spock")
                self.player_one.scores += 1
            elif user_input_one == 2 and user_input_two == 0:
                print(f"{user_input_one} and {user_input_two} : Rock crushes Scissors")
                self.player_two.scores += 1
            elif user_input_one == 2 and user_input_two == 1:
                print(f"{user_input_one} and {user_input_two} : Scissors cuts Paper")
                self.player_one.scores += 1
            elif user_input_one == 2 and user_input_two == 3:
                print(f"{user_input_one} and {user_input_two} : Scissors decapitates Lizard")
                self.player_one.scores += 1
            elif user_input_one == 2 and user_input_two == 4:
                print(f"{user_input_one} and {user_input_two} : Spock smashes Scissors")
                self.player_two.scores += 1
            elif user_input_one == 3 and user_input_two == 0:
                print(f"{user_input_one} and {user_input_two} : Rock crushes Lizard")
                self.player_two.scores += 1
            elif user_input_one == 3 and user_input_two == 1:
                print(f"{user_input_one} and {user_input_two} : Lizard eats Paper")
                self.player_one.scores += 1
            elif user_input_one == 3 and user_input_two == 2:
                print(f"{user_input_one} and {user_input_two} : Scissors decapitates Lizard")
                self.player_two.scores += 1
            elif user_input_one == 3 and user_input_two == 4:
                print(f"{user_input_one} and {user_input_two} : Lizard poisons Spock")
                self.player_one.scores += 1
            elif user_input_one == 4 and user_input_two == 0:
                print(f"{user_input_one} and {user_input_two} : Spock vaporizes Rock")
                self.player_one.scores += 1
            elif user_input_one == 4 and user_input_two == 1:
                print(f"{user_input_one} and {user_input_two} : Paper disproves Spock")
                self.player_two.scores += 1
            elif user_input_one == 4 and user_input_two == 2:
                print(f"{user_input_one} and {user_input_two} : Spock smashes Scissors")
                self.player_one.scores += 1
            elif user_input_one == 4 and user_input_two == 3:
                print(f"{user_input_one} and {user_input_two} : Lizard poisons Spock")
                self.player_two.scores += 1
            else:
                print(f"{user_input_one} ties {user_input_two}") #if input is equal
            print("---------------------------------------------------")
            if(self.player_one.scores == 2 or self.player_two.scores == 2):
                self.display_winners()
                return
            user_input_one = int(input("Select the number of your gesture:  "))
            user_input_two = random.choice(range(0, len(self.player_two.gestures)))
            
    def compare_gestures_multiplayer(self):
        #ask user for current gesture
        user_input_one = int(input("Select the number of your gesture:  ")) #player one
        user_input_two = int(input("Select the number of your gesture:  ")) #player two
        while user_input_one in range(0 , 6) and user_input_two in range(0 , 6):
        # while player_one.scores < 2 and player_two.scores < 2:
            if user_input_one == 0 and user_input_two == 1:
                print(f"{user_input_one} and {user_input_two} : Paper covers Rock") #add one to player two counter
                self.player_two.scores += 1
            elif user_input_one == 0 and user_input_two == 2:
                print(f"{user_input_one} and {user_input_two} : Rock crushes Scissors")
                self.player_one.scores += 1
            elif user_input_one == 0 and user_input_two == 3:
                print(f"{user_input_one} and {user_input_two} : Rock crushes Lizard")
                self.player_one.scores += 1
            elif user_input_one == 0 and user_input_two == 4:
                print(f"{user_input_one} and {user_input_two} : Spock vaporizes Rock")
                self.player_two.scores += 1
            elif user_input_one == 1 and user_input_two == 0:
                print(f"{user_input_one} and {user_input_two} : Paper covers Rock")
                self.player_one.scores += 1
            elif user_input_one == 1 and user_input_two == 2:
                print(f"{user_input_one} and {user_input_two} : Scissors cuts Paper")
                self.player_two.scores += 1
            elif user_input_one == 1 and user_input_two == 3:
                print(f"{user_input_one} and {user_input_two} : Lizard eats Paper")
                self.player_two.scores += 1
            elif user_input_one == 1 and user_input_two == 4:
                print(f"{user_input_one} and {user_input_two} : Paper disproves Spock")
                self.player_one.scores += 1
            elif user_input_one == 2 and user_input_two == 0:
                print(f"{user_input_one} and {user_input_two} : Rock crushes Scissors")
                self.player_two.scores += 1
            elif user_input_one == 2 and user_input_two == 1:
                print(f"{user_input_one} and {user_input_two} : Scissors cuts Paper")
                self.player_one.scores += 1
            elif user_input_one == 2 and user_input_two == 3:
                print(f"{user_input_one} and {user_input_two} : Scissors decapitates Lizard")
                self.player_one.scores += 1
            elif user_input_one == 2 and user_input_two == 4:
                print(f"{user_input_one} and {user_input_two} : Spock smashes Scissors")
                self.player_two.scores += 1
            elif user_input_one == 3 and user_input_two == 0:
                print(f"{user_input_one} and {user_input_two} : Rock crushes Lizard")
                self.player_two.scores += 1
            elif user_input_one == 3 and user_input_two == 1:
                print(f"{user_input_one} and {user_input_two} : Lizard eats Paper")
                self.player_one.scores += 1
            elif user_input_one == 3 and user_input_two == 2:
                print(f"{user_input_one} and {user_input_two} : Scissors decapitates Lizard")
                self.player_two.scores += 1
            elif user_input_one == 3 and user_input_two == 4:
                print(f"{user_input_one} and {user_input_two} : Lizard poisons Spock")
                self.player_one.scores += 1
            elif user_input_one == 4 and user_input_two == 0:
                print(f"{user_input_one} and {user_input_two} : Spock vaporizes Rock")
                self.player_one.scores += 1
            elif user_input_one == 4 and user_input_two == 1:
                print(f"{user_input_one} and {user_input_two} : Paper disproves Spock")
                self.player_two.scores += 1
            elif user_input_one == 4 and user_input_two == 2:
                print(f"{user_input_one} and {user_input_two} : Spock smashes Scissors")
                self.player_one.scores += 1
            elif user_input_one == 4 and user_input_two == 3:
                print(f"{user_input_one} and {user_input_two} : Lizard poisons Spock")
                self.player_two.scores += 1
            else:
                print(f"{user_input_one} ties {user_input_two}") #if input is equal
            print("---------------------------------------------------")
            if(self.player_one.scores == 2 or self.player_two.scores == 2):
                self.display_winners()
                return
            user_input_one = int(input("Select the number of your gesture:  "))
            user_input_two = int(input("Select the number of your gesture:  "))
            



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

    
