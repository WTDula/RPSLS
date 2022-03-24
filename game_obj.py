from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock

class GameObj:
    def __init__(self):
        self.rpsls_list = []

    def create_game_obj(self):
        self.rpsls_list.append(Rock())
        self.rpsls_list.append(Paper())
        self.rpsls_list.append(Scissors())
        self.rpsls_list.append(Lizard())
        self.rpsls_list.append(Spock())


# g1 = GameObj()
# g1.create_game_obj()
# for item in g1.rpsls_list:
#     print(item.name)
# r1 = Rock()
# s1 = Scissors()
# print(r1.do_i_win(s1))