import os
import random
import sys
from time import sleep


def clrscr():
    # Check if Operating System is Mac and Linux or Windows
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')


# function code for game
def game():
    possible_action = ['Rock', 'Paper', 'Scissors']
    user_action = input("\nEnter Rock, Paper or Scissors: ")

    computer_action = random.choice(possible_action)

    if computer_action.lower() == user_action.lower():
        print(f"\nComputer Choose {computer_action}")
        print(f"{name} Choose {user_action}")
        print("\nThe game is Tie")
    elif computer_action.lower() == 'rock' and user_action.lower() == 'scissors':
        print(f"\nComputer Choose {computer_action}")
        print(f"{name} Choose {user_action}")
        print(f"\n{name},You won The Game")
    elif computer_action.lower() == 'scissors' and user_action.lower() == 'rock':
        print(f"\nComputer Choose {computer_action}")
        print(f"{name} Choose {user_action}")
        print("\nComputer won The Game")
    elif computer_action.lower() == 'paper' and user_action.lower() == 'rock':
        print(f"\nComputer Choose {computer_action}")
        print(f"{name} Choose {user_action}")
        print("\nComputer won The Game")
    elif computer_action.lower() == 'rock' and user_action.lower() == 'paper':
        print(f"\nComputer Choose {computer_action}")
        print(f"{name} Choose {user_action}")
        print(f"\n{name}, You won The Game")
    elif computer_action.lower() == 'scissors' and user_action.lower() == 'paper':
        print(f"\nComputer Choose {computer_action}")
        print(f"{name} Choose {user_action}")
        print("\nComputer won The Game")
    elif computer_action.lower() == 'paper' and user_action.lower() == 'scissors':
        print(f"\nComputer Choose {computer_action}")
        print(f"{name} Choose {user_action}")
        print(f"\n{name}, You won The Game")


name = input("\nEnter Your name: ")
# print('\nHi ' + name + "! Welcome to Rock, Paper or Scissors game")
# time.sleep(1.0)

words = '\nHi ' + name + "! Welcome to Rock, Paper or Scissors game" \
                         "\n\nThe rules remain the same as the original game: Rock beats scissors, " \
                         "Scissors beats paper and paper beats rock. The rules are easy, the game is simple, " \
                         "the fun continues in this online version of the absolute classic game. " \
                         "Win three times in a row to win the duel outright and win any disagreement that you could " \
                         "ever have!\n "

for char in words:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()

# Wrap this text.


ans = input("\nAre you ready to play - Yes/no: ")
ans = ans.lower()
if ans == "yes":
    game()
elif ans == "no":
    print(f"\n{name} See You again")
    quit()
else:
    print("Enter Yes or No Only")

res = str(input("\nDo you want to try again y/n?:  "))

while res:
    if res.lower() == "y":
        clrscr()
        game()
        print()
        res = str(input("\nDo you want to try again? "))
    else:
        quit()
