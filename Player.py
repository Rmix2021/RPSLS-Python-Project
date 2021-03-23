from ActionChoices import ActionChoice


class Player:
    def __init__(self, name):
        self.name = name
        self.player_choice = [ActionChoice("rock"), ActionChoice("paper"), ActionChoice("scissors"),
                            ActionChoice("lizard"), ActionChoice("spock")]
