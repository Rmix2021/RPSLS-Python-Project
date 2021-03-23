from player import Player
import random


class ComputerPlayer(Player):

    def computer_selection(self):
        selection = random.randint(0, 4)
        action = self.player_choice[selection]
        return action
