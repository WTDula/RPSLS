from human import Human
from ai import AI

class Game():
    def __init__(self):
        self.leaderboard = [] #append a tuple of name of player and append score i.e ("John", 3)
        self.player_one = Human()
        self.player_two = None 


    def run_game(self):
        #single player / multiplayer selection
        #display_welcome()
        #show_options()
        #compare_gestures()
        #display_winner
        pass

    def single_player_multi_player_selection(self):
        pass

    def display_welcome(self):
        self.single_player_multi_player_selection()

    def turn(self, current_player):
        current_player.select_gesture()

    def compare_gestures(self, player_one, player_two):
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
        print("Here are the gestures: ")
        for gesture in self.player_one.gestures:
            gesture_index = self.player_one.gestures.index(gesture)
            print(f"{gesture} : {gesture_index}")
        self.show_rules()

    def display_winners(self):
        pass

g1 = Game()
g1.show_options()
p1 = Human()
p2 = Human()
g1.compare_gestures(p1, p2)