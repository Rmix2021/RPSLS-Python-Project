from computerplayer import ComputerPlayer
from humanplayer import HumanPlayer


def game_rules():
    print("Welcome to RPSLS, a game of choice")
    print("""Rules are the following: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock,
            Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard,
            Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock""")


class Game:
    def __init__(self):
        self.player1 = HumanPlayer(self)
        self.player2 = None

    def game_loop(self):
        user_input = input("Do you wish to play another Human or the Computer? press '8' for human or '9' for computer")
        if user_input == 8:
            self.player1 = HumanPlayer
            self.player2 = HumanPlayer

        if user_input == 9:
            self.player1 = HumanPlayer
            self.player2 = ComputerPlayer

    def game_run(self):
        game_rules()
        self.game_loop()
        self.user_action()

    def user_action(self):
        self.player1 = self.player1.selection
        self.player2 = self. player2.selection

        action = HumanPlayer.human_selection(player_choice[selection])
        action2 = ComputerPlayer.computer_selection()

        x = 0
        y = 0

        player1_wins = x
        player2_wins = y
        while x < 3 and y < 3:
            if action == "rock" and action2 == "rock":
                print("Its a tie")
            if action == "rock" and action2 == "scissors":
                y += 1
                print("Rock crushes Scissors, Player1 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "rock" and action2 == "lizard":
                x += 1
                print("Rock squashes Lizard, Player1 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "rock" and action2 == "paper":
                y += 1
                print("Paper covers Rock, Player2 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "rock" and action2 == "lizard":
                y += 1
                print("Rock squashes Lizard, Player2 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "paper" and action2 == "rock":
                x += 1
                print("Paper covers Rock, Player1 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "paper" and action2 == "spock":
                x += 1
                print("Paper disproves Spock, Player1 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "paper" and action2 == "scissors":
                y += 1
                print("Scissors cut Paper, Player2 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "paper" and action2 == "lizard":
                y += 1
                print("Lizard eats Paper, Player2 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "scissors" and action2 == "paper":
                x += 1
                print("Scissors cuts Paper, Player1 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "scissors" and action2 == "lizard":
                x += 1
                print("Scissors decapitates Lizard, Player1 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "scissors" and action2 == "rock":
                y += 1
                print("Rock crushes Scissors, Player2 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "scissors" and action2 == "spock":
                y += 1
                print("Spock smashes Scissors, Player2 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "lizard" and action2 == "paper":
                x += 1
                print("Lizard eats Paper, Player1 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "lizard" and action2 == "spock":
                x += 1
                print("Lizard poison Spock, Player1 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "lizard" and action2 == "scissors":
                y += 1
                print("Scissors decapitates Lizard, Player2 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "spock" and action2 == "rock":
                y += 1
                print("Spock Vaporizes Rock, Player1 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "spock" and action2 == "scissors":
                y += 1
                print("Spock smashes Scissors, Player1 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "spock" and action2 == "paper":
                y += 1
                print("Paper disproves Spock, Player2 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")
            if action == "spock" and action2 == "lizard":
                y += 1
                print("Lizard poisons Spock, Player2 Wins!")
                print(f" Player1 = {player1_wins} Player2 = {player2_wins}")

            if player1_wins == 3:
                print("Player 1 Wins")
            if player2_wins == 3:
                print("Player 2 Wins")

            user_input = input("Play again? 6 = yes, 7 = No")
            if user_input == 6:
                Game().game_loop()
            else:
                break


game_rules()
Game().game_loop()
