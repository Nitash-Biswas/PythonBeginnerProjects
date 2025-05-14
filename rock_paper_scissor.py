import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = { ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃' }
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, Scissors? (r/p/s):").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Choice! Try again")

def get_computer_choice():
    return random.choice(choices)

def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"The computer chose {emojis[computer_choice]}")

def find_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif(
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        return "You Win!"
    else:
        return "You Lose!"

def play():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        display_choices(user_choice, computer_choice)
        print(find_winner(user_choice, computer_choice))

        should_continue = input("Play again? (y/n): ").lower()
        if should_continue == "n":
            break

play()
