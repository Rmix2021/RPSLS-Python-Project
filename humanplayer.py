from player import Player


class HumanPlayer(Player):

    def __init__(self, name):
        super().__init__(name)
        self.selection = None #pycharm inserted this#

    def human_selection(self):
        user_input = input("Rock=0, Paper=1, Scissors=2, Lizard=3, Spock=4")
        selection = int(user_input)
        action = self.player_choice[selection]
        return action
