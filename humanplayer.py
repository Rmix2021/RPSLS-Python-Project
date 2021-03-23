from player import Player


class HumanPlayer(Player):

    def human_selection(self):
        user_input = input("promp the user to make a selection")
        selection = int(user_input)
        action = self.player_choice[selection]
        return action
