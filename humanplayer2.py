from player import Player


class HumanPlayer2(Player):

    def human_selection(self):
        user_input = input("Rock=0, Paper=1, Scissors=2, Lizard=3, Spock=4")
        selection = int(user_input)
        action = self.player_choice[selection]
        return action
