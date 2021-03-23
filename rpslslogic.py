from computerplayer import ComputerPlayer
from humanplayer import HumanPlayer


def game_rules():
    print("Welcome to RPSLS, a game of choice")
    print("""Rules are the following: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock,
            Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard,
            Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock""")

    class Game:
        def __init__(self):
            self.HumanPlayer = HumanPlayer(self)
            self.ComputerPlayer = ComputerPlayer

        def ask_user_for_input(self):
            user_input = input()
            input("Do you wish to play another Human or the Computer? press '8' for human or '9' for computer")
            if user_input == 8:
                self.HumanPlayer = HumanPlayer(1)
                self.HumanPlayer = HumanPlayer(2)

            if user_input == 9:
                self.HumanPlayer = HumanPlayer(1)
                self.ComputerPlayer = ComputerPlayer


game_rules()


    # def ask_to_play_again(self):
    #
    #     play_again = input("Play again? 6 = yes, 7 = No")
    #     if play_again.lower() != "y":
    #         break
    #