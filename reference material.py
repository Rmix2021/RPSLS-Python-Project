
# import random
# from enum import IntEnum
#
# class Action(IntEnum):
#     Rock = 0
#     Paper = 1
#     Scissors = 2
#
#
# def get_user_selection():
#     user_input = input("Enter a choice (rock[0], paper[1], scissors[2]): ")
#     selection = int(user_input)
#     action = Action(selection)
#     return action
#
# def get_user_selection():
#     choices = [f"{action.name}[{action.value}]" for action in Action]
#     choices_str = ", ".join(choices)
#     selection = int(input(f"Enter a choice ({choices_str}): "))
#     action = Action(selection)
#     return action
#
# >>> get_user_selection()
# Enter a choice (rock[0], paper[1], scissors[2]): 0
# <Action.Rock: 0>
#
# def get_computer_selection():
#     selection = random.randint(0, len(Action) - 1)
#     action = Action(selection)
#     return action
#
# >>> get_computer_selection()
# <Action.Scissors: 2>
#
# def determine_winner(user_action, computer_action):
#     if user_action == computer_action:
#         print(f"Both players selected {user_action.name}. It's a tie!")
#     elif user_action == Action.Rock:
#         if computer_action == Action.Scissors:
#             print("Rock smashes scissors! You win!")
#         else:
#             print("Paper covers rock! You lose.")
#     elif user_action == Action.Paper:
#         if computer_action == Action.Rock:
#             print("Paper covers rock! You win!")
#         else:
#             print("Scissors cuts paper! You lose.")
#     elif user_action == Action.Scissors:
#         if computer_action == Action.Paper:
#             print("Scissors cuts paper! You win!")
#         else:
#             print("Rock smashes scissors! You lose.")
#
# >>> determine_winner(Action.Rock, Action.Scissors)
# Rock smashes scissors! You win!
#
# >>> Action(3)
# ValueError: 3 is not a valid Action
#
# try:
#     user_action = get_user_selection()
# except ValueError as e:
#     range_str = f"[0, {len(Action) - 1}]"
#     print(f"Invalid selection. Enter a value in range {range_str}")
#     continue
#
# computer_action = get_computer_selection()
# determine_winner(user_action, computer_action)
#
# play_again = input("Play again? (y/n): ")
# if play_again.lower() != "y":
#     break
#
# def determine_winner(user_action, computer_action):
#     if user_action == computer_action:
#         print(f"Both players selected {user_action.name}. It's a tie!")
#     elif user_action == Action.Rock:
#         if computer_action == Action.Scissors:
#             print("Rock smashes scissors! You win!")
#         else:
#             print("Paper covers rock! You lose.")
#     elif user_action == Action.Paper:
#         if computer_action == Action.Rock:
#             print("Paper covers rock! You win!")
#         else:
#             print("Scissors cuts paper! You lose.")
#     elif user_action == Action.Scissors:
#         if computer_action == Action.Paper:
#             print("Scissors cuts paper! You win!")
#         else:
#             print("Rock smashes scissors! You lose.")
#
# def determine_winner(user_action, computer_action):
#     victories = {
#         Action.Rock: [Action.Scissors],  # Rock beats scissors
#         Action.Paper: [Action.Rock],  # Paper beats rock
#         Action.Scissors: [Action.Paper]  # Scissors beats paper
#     }
#
#     defeats = victories[user_action]
#     if user_action == computer_action:
#         print(f"Both players selected {user_action.name}. It's a tie!")
#     elif computer_action in defeats:
#         print(f"{user_action.name} beats {computer_action.name}! You win!")
#     else:
#         print(f"{computer_action.name} beats {user_action.name}! You lose.")
#
# class Action(IntEnum):
#     Rock = 0
#     Paper = 1
#     Scissors = 2
#     Lizard = 3
#     Spock = 4
#
#     Action.Scissors: [Action.Lizard, Action.Paper],
#     Action.Paper: [Action.Spock, Action.Rock],
#     Action.Rock: [Action.Lizard, Action.Scissors],
#     Action.Lizard: [Action.Spock, Action.Paper],
#     Action.Spock: [Action.Scissors, Action.Rock]
# }




import random

module
import random

# Print multiline instruction
# performstring concatenation of string
print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")

while True:
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")

    # take the input from user
    choice = int(input("User turn: "))

    # OR is the short-circuit operator
    # if any one of the condition is true
    # then it return True value

    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

        # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'

    # print user choice
    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")

    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

        # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

    # condition for winning
    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("paper wins => ", end="")
        result = "paper"

    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end="")
        result = "Rock"
    else:
        print("scissor wins =>", end="")
        result = "scissor"

    # Printing either user or computer wins
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input()

    # if user input n or N then condition is True
    if ans == 'n' or ans == 'N':
        break

# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing")

# classes
# gestures = gestures list
# game is highest class has player1 and player2
# player list of gestures
# human
# computer

