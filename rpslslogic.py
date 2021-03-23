from computerplayer import ComputerPlayer
from humanplayer import HumanPlayer
import random



class RpslsLogic:
    def __init__(self):
        self.ComputerPlayer = ComputerPlayer()
        self.HumanPlayer = HumanPlayer()


print("Welcome to RPSLS, a game of choice")
print("""Rules are the following:# * Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock,
        Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard,
        Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock""")

 print("Do you wish to play another Human or the Computer? press 9 for human or 8 for computer")


play_again = input("Play again? 6 = yes, 7 = No")
if play_again.lower() != "y":
    break

