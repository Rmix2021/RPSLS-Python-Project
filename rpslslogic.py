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

    def ask_user_for_input(self):
        global player2, player1
        user_input = input()
        input("Do you wish to play another Human or the Computer? press '8' for human or '9' for computer")
        if user_input == 8:
            player1 = HumanPlayer
            player2 = HumanPlayer

        if user_input == 9:
            player1 = HumanPlayer
            player2 = ComputerPlayer



        while x < 3 and y < 3:

            HumanPlayer.human_selection()
            ComputerPlayer.computer_selection()

            player1_wins = x
            player2_wins = y
            x = 0
            y = 0
            if player1 == 0:
                player2 == 2
                x += 1
                print("Rock crushes Scissors, you win!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
            if player1 == 0:
                player2 == 3
                x +=1
                print("Rock squashes Lizard, you win!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
            if player1 == 0:
                and player2 == 1
                y += 1
                print("Paper covers Rock, you lose!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
            if player1 == 0:
                and player2 == 3
                y += 1
                print("Rock squashes Lizard, you lose!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
            if player1 == 1:
                and player2 == 0
                x += 1
                print("Paper covers Rock, you win!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
            if player1 == 1:
                and player2 == 4
                x += 1
                print("Paper disproves Spock, you win!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
            if player1 == 1:
                and player2 == 2
                y += 1
                print("Scissors cut Paper, you lose!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
            if player1 == 1:
                and player2 == 3
                y += 1
                print("Lizard eats Paper, you lose!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
            if player1 == 2:
                and player2 == 1
                x += 1
                print("Scissors cuts Paper, you win!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
            if player1 == 2:
                and player2 ==3
                x += 1
                print("Scissors decapitates Liazrd, you win!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
            if player1 == 2:
                and player2 == 0
                y += 1
                print("Rock crushes Scissors, you lose!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
             if player1 == 2:
                and player2 == 4
                y += 1
                print("Spock smashes Scissors, you lose!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
            if player1 == 3:
                and player2 == 1
                x += 1
                print("Lizard eats Paper, you win!")
                print("Player1 = " + str(player1_wins) + "Player2 = " +str(player2_wins))
            if player1 == 3:
                and player2 == 4
                x += 1
                print("Lizard poison Spock, you win!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
            if player1 == 3:
                and player2 == 2
                y += 1
                print("Scissors decapitates Lizard, you lose!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))
            if player1 == 3:
                and player2 == 0
                y += 1
                print("Rock squashes Lizard, you lose!")
                print("Player1 = " + str(player1_wins) + "Player2 = " + str(player2_wins))

                if player1_wins == 3:
                    print("Player 1 Wins")
                if player2_wins == 3:
                    print("Player 2 Wins")


    user_input = input("Play again? 6 = yes, 7 = No")


