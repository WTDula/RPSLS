import random
from human import Human
from ai import AI

class Game():
    def __init__(self):
        self.leaderboard = [] #append a tuple of name of player and append score i.e ("John", 3)
        self.human_one = Human()
        self.player_two = None 




    def single_player_multi_player_selection(self):
        user_input = None
        while True:
            user_input = int(input("Do you you want to play single player or multiplayer: <Select (1) for single player | Select (2) for multiplayer>"))
            if user_input == 1 or user_input == 2:
                if user_input == 1:
                    self.human_one = Human()
                    self.player_two = AI()
                    self.compare_gestures_AI(self.human_one, self.player_two)
                    return
                else:
                    self.human_one = Human()
                    self.player_two = Human()
                    self.compare_gestures_multiplayer(self.human_one, self.player_two)
                    return

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock")
        self.show_rules()
        print("Best of 3 wins: ")



    def compare_gestures_AI(self, player_one, player_two):
        #ask user for current gesture
        user_input_one = int(input("Select the number of your gesture:  ")) #player one
        user_input_two = random.choice(range(0, len(player_two.gestures))) #player two
        while user_input_one in range(0 , 6) and user_input_two in range(0 , 6):
            while player_one.scores < 2 and player_two.scores < 2:
                if user_input_one == 0 and user_input_two == 1:
                    print(f"{user_input_one} and {user_input_two} : Paper covers Rock") #add one to player two counter
                    player_two.scores += 1
                elif user_input_one == 0 and user_input_two == 2:
                    print(f"{user_input_one} and {user_input_two} : Rock crushes Scissors")
                    player_one.scores += 1
                elif user_input_one == 0 and user_input_two == 3:
                    print(f"{user_input_one} and {user_input_two} : Rock crushes Lizard")
                    player_one.scores += 1
                elif user_input_one == 0 and user_input_two == 4:
                    print(f"{user_input_one} and {user_input_two} : Spock vaporizes Rock")
                    player_two.scores += 1
                elif user_input_one == 1 and user_input_two == 0:
                    print(f"{user_input_one} and {user_input_two} : Paper covers Rock")
                    player_one.scores += 1
                elif user_input_one == 1 and user_input_two == 2:
                    print(f"{user_input_one} and {user_input_two} : Scissors cuts Paper")
                    player_two.scores += 1
                elif user_input_one == 1 and user_input_two == 3:
                    print(f"{user_input_one} and {user_input_two} : Lizard eats Paper")
                    player_two.scores += 1
                elif user_input_one == 1 and user_input_two == 4:
                    print(f"{user_input_one} and {user_input_two} : Paper disproves Spock")
                    player_one.scores += 1
                elif user_input_one == 2 and user_input_two == 0:
                    print(f"{user_input_one} and {user_input_two} : Rock crushes Scissors")
                    player_two.scores += 1
                elif user_input_one == 2 and user_input_two == 1:
                    print(f"{user_input_one} and {user_input_two} : Scissors cuts Paper")
                    player_one.scores += 1
                elif user_input_one == 2 and user_input_two == 3:
                    print(f"{user_input_one} and {user_input_two} : Scissors decapitates Lizard")
                    player_one.scores += 1
                elif user_input_one == 2 and user_input_two == 4:
                    print(f"{user_input_one} and {user_input_two} : Spock smashes Scissors")
                    player_two.scores += 1
                elif user_input_one == 3 and user_input_two == 0:
                    print(f"{user_input_one} and {user_input_two} : Rock crushes Lizard")
                    player_two.scores += 1
                elif user_input_one == 3 and user_input_two == 1:
                    print(f"{user_input_one} and {user_input_two} : Lizard eats Paper")
                    player_one.scores += 1
                elif user_input_one == 3 and user_input_two == 2:
                    print(f"{user_input_one} and {user_input_two} : Scissors decapitates Lizard")
                    player_two.scores += 1
                elif user_input_one == 3 and user_input_two == 4:
                    print(f"{user_input_one} and {user_input_two} : Lizard poisons Spock")
                    player_one.scores += 1
                elif user_input_one == 4 and user_input_two == 0:
                    print(f"{user_input_one} and {user_input_two} : Spock vaporizes Rock")
                    player_one.scores += 1
                elif user_input_one == 4 and user_input_two == 1:
                    print(f"{user_input_one} and {user_input_two} : Paper disproves Spock")
                    player_two.scores += 1
                elif user_input_one == 4 and user_input_two == 2:
                    print(f"{user_input_one} and {user_input_two} : Spock smashes Scissors")
                    player_one.scores += 1
                elif user_input_one == 4 and user_input_two == 3:
                    print(f"{user_input_one} and {user_input_two} : Lizard poisons Spock")
                    player_two.scores += 1
                else:
                    print(f"{user_input_one} ties {user_input_two}") #if input is equal
                user_input_one = int(input("Select the number of your gesture:  "))
                user_input_two = random.choice(range(0, len(player_two.gestures)))

    def compare_gestures_multiplayer(self, player_one, player_two):
        #ask user for current gesture
        user_input_one = int(input("Select the number of your gesture:  ")) #player one
        user_input_two = int(input("Select the number of your gesture:  ")) #player two
        while user_input_one in range(0 , 6) and user_input_two in range(0 , 6):
            while player_one.scores < 2 and player_two.scores < 2:
                if user_input_one == 0 and user_input_two == 1:
                    print(f"{user_input_one} and {user_input_two} : Paper covers Rock") #add one to player two counter
                    player_two.scores += 1
                elif user_input_one == 0 and user_input_two == 2:
                    print(f"{user_input_one} and {user_input_two} : Rock crushes Scissors")
                    player_one.scores += 1
                elif user_input_one == 0 and user_input_two == 3:
                    print(f"{user_input_one} and {user_input_two} : Rock crushes Lizard")
                    player_one.scores += 1
                elif user_input_one == 0 and user_input_two == 4:
                    print(f"{user_input_one} and {user_input_two} : Spock vaporizes Rock")
                    player_two.scores += 1
                elif user_input_one == 1 and user_input_two == 0:
                    print(f"{user_input_one} and {user_input_two} : Paper covers Rock")
                    player_one.scores += 1
                elif user_input_one == 1 and user_input_two == 2:
                    print(f"{user_input_one} and {user_input_two} : Scissors cuts Paper")
                    player_two.scores += 1
                elif user_input_one == 1 and user_input_two == 3:
                    print(f"{user_input_one} and {user_input_two} : Lizard eats Paper")
                    player_two.scores += 1
                elif user_input_one == 1 and user_input_two == 4:
                    print(f"{user_input_one} and {user_input_two} : Paper disproves Spock")
                    player_one.scores += 1
                elif user_input_one == 2 and user_input_two == 0:
                    print(f"{user_input_one} and {user_input_two} : Rock crushes Scissors")
                    player_two.scores += 1
                elif user_input_one == 2 and user_input_two == 1:
                    print(f"{user_input_one} and {user_input_two} : Scissors cuts Paper")
                    player_one.scores += 1
                elif user_input_one == 2 and user_input_two == 3:
                    print(f"{user_input_one} and {user_input_two} : Scissors decapitates Lizard")
                    player_one.scores += 1
                elif user_input_one == 2 and user_input_two == 4:
                    print(f"{user_input_one} and {user_input_two} : Spock smashes Scissors")
                    player_two.scores += 1
                elif user_input_one == 3 and user_input_two == 0:
                    print(f"{user_input_one} and {user_input_two} : Rock crushes Lizard")
                    player_two.scores += 1
                elif user_input_one == 3 and user_input_two == 1:
                    print(f"{user_input_one} and {user_input_two} : Lizard eats Paper")
                    player_one.scores += 1
                elif user_input_one == 3 and user_input_two == 2:
                    print(f"{user_input_one} and {user_input_two} : Scissors decapitates Lizard")
                    player_two.scores += 1
                elif user_input_one == 3 and user_input_two == 4:
                    print(f"{user_input_one} and {user_input_two} : Lizard poisons Spock")
                    player_one.scores += 1
                elif user_input_one == 4 and user_input_two == 0:
                    print(f"{user_input_one} and {user_input_two} : Spock vaporizes Rock")
                    player_one.scores += 1
                elif user_input_one == 4 and user_input_two == 1:
                    print(f"{user_input_one} and {user_input_two} : Paper disproves Spock")
                    player_two.scores += 1
                elif user_input_one == 4 and user_input_two == 2:
                    print(f"{user_input_one} and {user_input_two} : Spock smashes Scissors")
                    player_one.scores += 1
                elif user_input_one == 4 and user_input_two == 3:
                    print(f"{user_input_one} and {user_input_two} : Lizard poisons Spock")
                    player_two.scores += 1
                else:
                    print(f"{user_input_one} ties {user_input_two}") #if input is equal
                user_input_one = int(input("Select the number of your gesture:  "))
                user_input_two = int(input("Select the number of your gesture:  "))



    def show_rules(self):
        print("Rock crushes Scissors\t\ttScissors cuts Paper\nPaper covers Rock\t\tRock crushes Lizard\n Lizard poisons Spock\t\t Spock smashes Scissors\n Scissors decapitates Lizard\t\t Lizard eats Paper\n Paper disproves Spock\t\t Spock vaporizes Rock")

    def show_options(self):
        print("Use the following numbers to select the gesture: ")
        for gesture in self.human_one.gestures:
            gesture_index = self.human_one.gestures.index(gesture)
            print(f"{gesture} : {gesture_index}")
        self.show_rules()

    def display_winners(self, player_one, player_two):
        if player_one.scores > player_two.scores:
            print("Player one wins")
        else:
            print("Player two wins")

    def run_game(self):
        self.display_welcome()
        self.show_options()
        self.single_player_multi_player_selection()
        self.display_winners(self.human_one, self.player_two)


