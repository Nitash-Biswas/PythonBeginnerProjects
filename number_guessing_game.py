import random

number_to_guess = random.randint(1, 100) # includes both 1 and 100

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == number_to_guess:
            print("YAYYY!You guessed the number!")
            continue_guessing = input("Do you want to continue guessing? (y/n): ").lower()
            if continue_guessing == 'n':
                print("Thanks for playing!")
                break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")